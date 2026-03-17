"""Tests for the trading pipeline and Polymarket connector."""
import pytest
from unittest.mock import MagicMock, patch

from src.connectors.polymarket import PolymarketConnector
from src.trading.executor import TradeExecutor
from src.trading.trader import Trader


class TestPolymarketConnector:
    def test_safe_mode_default(self):
        with patch.dict("os.environ", {"SAFE_MODE": "true"}, clear=False):
            connector = PolymarketConnector(safe_mode=True)
            assert connector.safe_mode is True

    def test_safe_mode_explicit(self):
        connector = PolymarketConnector(safe_mode=True)
        assert connector.safe_mode is True

    def test_build_order_dry_run(self):
        connector = PolymarketConnector(safe_mode=True)
        result = connector.build_order(
            token_id="test_token_123",
            price=0.65,
            size=10.0,
            side="BUY",
        )
        assert result["dry_run"] is True
        assert result["token_id"] == "test_token_123"
        assert result["price"] == 0.65
        assert result["size"] == 10.0
        assert result["side"] == "BUY"

    def test_build_order_has_timestamp(self):
        connector = PolymarketConnector(safe_mode=True)
        result = connector.build_order(
            token_id="abc",
            price=0.5,
            size=5.0,
        )
        assert "timestamp" in result

    def test_execute_market_order_dry_run(self):
        connector = PolymarketConnector(safe_mode=True)
        result = connector.execute_market_order(
            token_id="test_token_456",
            amount=25.0,
        )
        assert result["dry_run"] is True
        assert result["token_id"] == "test_token_456"
        assert result["amount"] == 25.0

    def test_no_wallet_graceful(self):
        """Connector should init without crashing when no wallet key is set."""
        connector = PolymarketConnector(safe_mode=True)
        assert connector.wallet_address is None

    def test_map_market(self):
        raw = {
            "id": 12345,
            "question": "Will BTC hit $100k?",
            "endDate": "2025-12-31",
            "description": "Test",
            "active": True,
            "funded": True,
            "rewardsMinSize": "10",
            "rewardsMaxSpread": "0.5",
            "spread": "0.02",
            "outcomes": '["Yes", "No"]',
            "outcomePrices": '["0.65", "0.35"]',
            "clobTokenIds": '["abc", "def"]',
        }
        result = PolymarketConnector._map_market(raw)
        assert result["id"] == 12345
        assert result["question"] == "Will BTC hit $100k?"
        assert result["active"] is True

    def test_map_event(self):
        raw = {
            "id": 99,
            "ticker": "BTC-100K",
            "slug": "btc-100k",
            "title": "Bitcoin $100k",
            "description": "Test event",
            "active": True,
            "closed": False,
            "archived": False,
            "new": True,
            "featured": False,
            "restricted": False,
            "endDate": "2025-12-31",
            "markets": [{"id": 1}, {"id": 2}],
        }
        result = PolymarketConnector._map_event(raw)
        assert result["id"] == 99
        assert result["title"] == "Bitcoin $100k"
        assert result["markets"] == "1,2"


class TestTradeExecutor:
    def test_superforecast_returns_dict(self):
        mock_llm = MagicMock()
        mock_llm.chat_json.return_value = {
            "probability": 0.72,
            "side": "YES",
            "rationale": "Strong momentum",
        }
        mock_llm.system.return_value = {"role": "system", "content": "test"}
        mock_llm.user.return_value = {"role": "user", "content": "test"}

        executor = TradeExecutor(llm=mock_llm)
        result = executor.superforecast(
            question="Will BTC hit $100k?",
            description="Bitcoin price prediction",
            outcomes=["YES", "NO"],
        )
        assert result["probability"] == 0.72
        assert result["side"] == "YES"

    def test_superforecast_clamps_probability(self):
        mock_llm = MagicMock()
        mock_llm.chat_json.return_value = {"probability": 1.5, "side": "YES", "rationale": ""}
        mock_llm.system.return_value = {"role": "system", "content": ""}
        mock_llm.user.return_value = {"role": "user", "content": ""}

        executor = TradeExecutor(llm=mock_llm)
        result = executor.superforecast("Q", "D", ["YES", "NO"])
        assert result["probability"] <= 0.99

    def test_size_trade_half_kelly(self):
        mock_poly = MagicMock()
        mock_poly.get_usdc_balance.return_value = 1000.0

        executor = TradeExecutor(polymarket=mock_poly)
        size = executor.size_trade(edge=0.05, kelly_fraction=0.10)
        assert size == 50.0  # half-kelly: 0.10/2 * 1000

    def test_size_trade_max_cap(self):
        mock_poly = MagicMock()
        mock_poly.get_usdc_balance.return_value = 10000.0

        executor = TradeExecutor(polymarket=mock_poly)
        size = executor.size_trade(edge=0.10, kelly_fraction=0.50, max_position_pct=0.05)
        assert size == 500.0  # capped at 5% of 10000

    def test_filter_events_fallback(self):
        """When LLM fails, filter_events should return top N."""
        mock_llm = MagicMock()
        mock_llm.chat_json.side_effect = Exception("API error")
        mock_llm.system.return_value = {"role": "system", "content": ""}
        mock_llm.user.return_value = {"role": "user", "content": ""}

        executor = TradeExecutor(llm=mock_llm)
        events = [{"id": i, "title": f"Event {i}"} for i in range(20)]
        result = executor.filter_events(events, max_keep=5)
        assert len(result) == 5


class TestTrader:
    def test_one_best_trade_no_events(self):
        mock_poly = MagicMock()
        mock_poly.get_tradeable_events.return_value = []

        trader = Trader(polymarket=mock_poly)
        result = trader.one_best_trade()
        assert result["action"] == "PASS"

    def test_one_best_trade_no_markets(self):
        mock_poly = MagicMock()
        mock_poly.get_tradeable_events.return_value = [
            {"id": 1, "title": "Test", "markets": ""}
        ]

        mock_llm = MagicMock()
        mock_llm.chat_json.return_value = {"selected_ids": [1], "rationale": ""}
        mock_llm.system.return_value = {"role": "system", "content": ""}
        mock_llm.user.return_value = {"role": "user", "content": ""}

        mock_gamma = MagicMock()
        mock_gamma.get_markets.return_value = []

        trader = Trader(llm=mock_llm, gamma=mock_gamma, polymarket=mock_poly)
        result = trader.one_best_trade()
        assert result["action"] == "PASS"

    def test_events_to_markets_uses_get_market_by_id(self):
        mock_gamma = MagicMock()
        mock_gamma.get_market_by_id.return_value = {
            "id": "42",
            "question": "Will BTC hit $100k?",
            "outcomes": '["YES","NO"]',
            "outcome_prices": '[0.6,0.4]',
            "volume": 10000.0,
            "description": "",
            "clob_token_ids": '["tok1","tok2"]',
        }
        trader = Trader(gamma=mock_gamma)
        markets = trader._events_to_markets([{"id": 1, "title": "BTC", "markets": "42"}])
        mock_gamma.get_market_by_id.assert_called_once_with("42")
        assert len(markets) == 1
