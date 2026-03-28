"""
Integration tests for the end-to-end trading pipeline.

These tests exercise the full order flow paths including:
- SAFE_MODE=false live-order path (no CLOB client → RuntimeError)
- _events_to_markets event_id fallback when per-ID lookup returns nothing
- LLM provider routing (grok/openai/gemini/claude dispatch)
- Full one_best_trade() with SAFE_MODE=false through mocked dependencies
"""
import pytest
from unittest.mock import MagicMock, patch, call

from onto_market.connectors.polymarket import PolymarketConnector
from onto_market.trading.trader import Trader
from onto_market.core.llm_router import llm_completion, llm_json, _LITELLM_MODELS


# ── SAFE_MODE=false order path ─────────────────────────────────────────────

class TestLiveOrderPath:
    def test_build_order_live_raises_without_clob_client(self):
        """SAFE_MODE=false should raise RuntimeError when CLOB client is absent."""
        connector = PolymarketConnector(safe_mode=False)
        assert connector.client is None
        with pytest.raises(RuntimeError, match="CLOB client not initialized"):
            connector.build_order(
                token_id="some_token",
                price=0.6,
                size=10.0,
                side="BUY",
            )

    def test_market_order_live_raises_without_clob_client(self):
        connector = PolymarketConnector(safe_mode=False)
        with pytest.raises(RuntimeError, match="CLOB client not initialized"):
            connector.execute_market_order(token_id="some_token", amount=50.0)

    def test_get_orderbook_raises_without_clob_client(self):
        connector = PolymarketConnector(safe_mode=False)
        with pytest.raises(RuntimeError, match="CLOB client not initialized"):
            connector.get_orderbook("some_token")

    def test_get_usdc_balance_raises_without_web3(self):
        connector = PolymarketConnector(safe_mode=False)
        with pytest.raises(RuntimeError, match="Web3 not initialized"):
            connector.get_usdc_balance()

    def test_full_trade_pipeline_live_mode(self):
        """Full one_best_trade() in live mode should call build_order with dry_run=False path."""
        mock_poly = MagicMock()
        mock_poly.safe_mode = False
        mock_poly.get_tradeable_events.return_value = [
            {"id": 7, "title": "BTC $100k", "markets": "42"}
        ]
        mock_poly.build_order.return_value = {
            "token_id": "tok1",
            "price": 0.6,
            "size": 5.0,
            "side": "BUY",
            "dry_run": False,
        }
        mock_poly.get_usdc_balance.return_value = 200.0

        mock_gamma = MagicMock()
        mock_gamma.get_market_by_id.return_value = {
            "id": "42",
            "question": "Will BTC hit $100k?",
            "description": "Bitcoin prediction",
            "outcomes": ["YES", "NO"],
            "outcome_prices": [0.6, 0.4],
            "volume": 50000.0,
            "clob_token_ids": ["tok1", "tok2"],
        }

        mock_llm = MagicMock()
        mock_llm.chat_json.side_effect = [
            {"selected_ids": [7], "rationale": "high volume"},  # filter_events
            {"probability": 0.72, "side": "YES", "rationale": "strong momentum"},  # superforecast
        ]
        mock_llm.system.return_value = {"role": "system", "content": ""}
        mock_llm.user.return_value = {"role": "user", "content": ""}

        trader = Trader(llm=mock_llm, gamma=mock_gamma, polymarket=mock_poly)
        result = trader.one_best_trade()

        assert result["action"] == "BET"
        mock_poly.build_order.assert_called_once()
        _, kwargs = mock_poly.build_order.call_args
        assert kwargs["token_id"] == "tok1"
        assert kwargs["side"] == "BUY"
        assert result["execution"]["dry_run"] is False


# ── event_id fallback ──────────────────────────────────────────────────────

class TestEventIdFallback:
    def test_fallback_triggered_when_per_id_returns_none(self):
        """When get_market_by_id returns None, should fall back to get_markets(event_id=...)."""
        fallback_market = {
            "id": "99",
            "question": "Will ETH flip BTC?",
            "description": "",
            "outcomes": ["YES", "NO"],
            "outcome_prices": [0.3, 0.7],
            "volume": 8000.0,
            "clob_token_ids": ["ethtok"],
        }

        mock_gamma = MagicMock()
        mock_gamma.get_market_by_id.return_value = None
        mock_gamma.get_markets.return_value = [fallback_market]

        trader = Trader(gamma=mock_gamma)
        events = [{"id": 5, "title": "ETH flip", "markets": "99"}]
        markets = trader._events_to_markets(events)

        mock_gamma.get_market_by_id.assert_called_once_with("99")
        mock_gamma.get_markets.assert_called_once_with(event_id=5, limit=50, active=True)
        assert len(markets) == 1
        assert markets[0]["id"] == "99"

    def test_no_fallback_when_per_id_succeeds(self):
        """Should NOT call get_markets when get_market_by_id succeeds."""
        mock_gamma = MagicMock()
        mock_gamma.get_market_by_id.return_value = {"id": "42", "question": "Q"}

        trader = Trader(gamma=mock_gamma)
        trader._events_to_markets([{"id": 1, "markets": "42"}])

        mock_gamma.get_markets.assert_not_called()

    def test_fallback_skipped_when_event_has_no_id(self):
        """No event_id on event dict → skip fallback gracefully."""
        mock_gamma = MagicMock()
        mock_gamma.get_market_by_id.return_value = None

        trader = Trader(gamma=mock_gamma)
        markets = trader._events_to_markets([{"title": "No ID event", "markets": "99"}])

        mock_gamma.get_markets.assert_not_called()
        assert markets == []

    def test_fallback_failure_is_logged_not_raised(self):
        """Fallback API error should not propagate — return empty list."""
        mock_gamma = MagicMock()
        mock_gamma.get_market_by_id.return_value = None
        mock_gamma.get_markets.side_effect = Exception("timeout")

        trader = Trader(gamma=mock_gamma)
        markets = trader._events_to_markets([{"id": 3, "markets": "55"}])
        assert markets == []


# ── LLM provider routing ───────────────────────────────────────────────────

class TestLLMProviderRouting:
    def test_grok_uses_xai_client(self):
        """LLM_PROVIDER=grok should use the xAI OpenAI-compatible client."""
        mock_response = MagicMock()
        mock_response.output_text = "grok says hello"

        mock_client = MagicMock()
        mock_client.responses.create.return_value = mock_response

        with patch("onto_market.core.llm_router.config") as mock_cfg, \
             patch("onto_market.core.llm_router.get_xai_client", return_value=mock_client):
            mock_cfg.LLM_PROVIDER = "grok"
            mock_cfg.GROK_MODEL = "grok-4"

            result = llm_completion([{"role": "user", "content": "hi"}])
            assert result == "grok says hello"
            mock_client.responses.create.assert_called_once()

    def test_grok_disables_tools_for_json(self):
        """llm_json calls should disable tools to get clean JSON back."""
        mock_response = MagicMock()
        mock_response.output_text = '{"key": "value"}'

        mock_client = MagicMock()
        mock_client.responses.create.return_value = mock_response

        with patch("onto_market.core.llm_router.config") as mock_cfg, \
             patch("onto_market.core.llm_router.get_xai_client", return_value=mock_client):
            mock_cfg.LLM_PROVIDER = "grok"
            mock_cfg.GROK_MODEL = "grok-4"

            result = llm_json([{"role": "user", "content": "return JSON"}])
            _, kwargs = mock_client.responses.create.call_args
            assert kwargs.get("tools") == []
            assert result == {"key": "value"}

    @pytest.mark.parametrize("provider,expected_model", [
        ("openai", "openai/gpt-4o-mini"),
        ("gemini", "gemini/gemini-1.5-pro"),
        ("claude", "anthropic/claude-3-5-sonnet-20241022"),
    ])
    def test_non_grok_providers_use_litellm(self, provider, expected_model):
        """Non-grok providers should route through litellm with the correct model string."""
        mock_choice = MagicMock()
        mock_choice.message.content = f"{provider} response"
        mock_litellm_resp = MagicMock()
        mock_litellm_resp.choices = [mock_choice]

        with patch("onto_market.core.llm_router.config") as mock_cfg, \
             patch("onto_market.core.llm_router.litellm") as mock_litellm:
            mock_cfg.LLM_PROVIDER = provider
            mock_litellm.completion.return_value = mock_litellm_resp

            result = llm_completion([{"role": "user", "content": "test"}])
            assert result == f"{provider} response"
            mock_litellm.completion.assert_called_once_with(
                model=expected_model,
                messages=[{"role": "user", "content": "test"}],
                temperature=0.7,
            )

    def test_unknown_provider_raises(self):
        with patch("onto_market.core.llm_router.config") as mock_cfg:
            mock_cfg.LLM_PROVIDER = "unknown_llm"
            with pytest.raises(ValueError, match="Unknown LLM_PROVIDER"):
                llm_completion([{"role": "user", "content": "test"}])

    def test_litellm_model_map_is_complete(self):
        """Ensure documented providers all have entries in _LITELLM_MODELS."""
        assert "openai" in _LITELLM_MODELS
        assert "gemini" in _LITELLM_MODELS
        assert "claude" in _LITELLM_MODELS
