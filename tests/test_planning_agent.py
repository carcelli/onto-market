"""Tests for planning_agent helpers: normalize, scoring, and node logic."""
import json
import pytest
from unittest.mock import MagicMock, patch

from onto_market.agents.planning_agent import (
    _normalize_market,
    _market_from_obj,
    _score_market_match,
    _STOPWORDS,
)


class TestNormalizeMarket:
    def test_db_row_with_json_strings(self):
        row = {
            "id": "123",
            "question": "Will BTC hit $100k?",
            "outcome_prices": '["0.65","0.35"]',
            "clob_token_ids": '["tok1","tok2"]',
            "volume": 50000,
        }
        result = _normalize_market(row)
        assert result["implied_prob"] == pytest.approx(0.65)
        assert result["clob_token_ids"] == ["tok1", "tok2"]
        assert result["volume"] == 50000

    def test_live_market_already_has_implied(self):
        row = {
            "id": "456",
            "question": "Will ETH flip BTC?",
            "implied_prob": 0.3,
            "clob_token_ids": ["a", "b"],
        }
        result = _normalize_market(row)
        assert result["implied_prob"] == pytest.approx(0.3)
        assert result["clob_token_ids"] == ["a", "b"]

    def test_missing_prices_defaults_to_half(self):
        row = {"id": "789", "question": "Test"}
        result = _normalize_market(row)
        assert result["implied_prob"] == pytest.approx(0.5)
        assert result["clob_token_ids"] == []

    def test_malformed_json_string_falls_back(self):
        row = {
            "id": "bad",
            "question": "Bad data",
            "outcome_prices": "not_json",
            "clob_token_ids": "not_json_either",
        }
        result = _normalize_market(row)
        assert result["implied_prob"] == pytest.approx(0.5)
        assert result["clob_token_ids"] == []

    def test_empty_string_token_ids(self):
        row = {"id": "e", "question": "Empty", "clob_token_ids": ""}
        result = _normalize_market(row)
        assert result["clob_token_ids"] == []


class TestMarketFromObj:
    def test_converts_market_object(self):
        m = MagicMock()
        m.id = "42"
        m.question = "Will it rain?"
        m.implied_probability = 0.7
        m.volume = 100_000.0
        m.category = "weather"
        m.clob_token_ids = ["tok_yes", "tok_no"]

        result = _market_from_obj(m)
        assert result["id"] == "42"
        assert result["question"] == "Will it rain?"
        assert result["implied_prob"] == 0.7
        assert result["volume"] == 100_000.0
        assert result["clob_token_ids"] == ["tok_yes", "tok_no"]


class TestScoreMarketMatch:
    def test_full_overlap_beats_volume(self):
        tokens = {"bitcoin", "100k"}
        high_vol_wrong = _score_market_match(tokens, "Fed rate decision", 10_000_000)
        low_vol_right = _score_market_match(tokens, "Bitcoin price 100k", 1_000)
        assert low_vol_right > high_vol_wrong

    def test_zero_overlap_gets_volume_only(self):
        tokens = {"bitcoin", "100k"}
        score = _score_market_match(tokens, "Ethereum merge date", 5_000_000)
        assert score == pytest.approx(5_000_000 / 1e6)

    def test_case_insensitive(self):
        tokens = {"bitcoin"}
        score = _score_market_match(tokens, "BITCOIN Price Prediction", 0)
        assert score == 10_000

    def test_empty_tokens(self):
        score = _score_market_match(set(), "Any market", 1_000)
        assert score == pytest.approx(1_000 / 1e6)


class TestStopwords:
    def test_common_words_filtered(self):
        assert "will" in _STOPWORDS
        assert "the" in _STOPWORDS
        assert "by" in _STOPWORDS
        assert "end" in _STOPWORDS
        assert "of" in _STOPWORDS

    def test_meaningful_tokens_not_filtered(self):
        assert "btc" not in _STOPWORDS
        assert "fed" not in _STOPWORDS
        assert "nba" not in _STOPWORDS
        assert "hit" not in _STOPWORDS


class TestSearchMarketsIntegration:
    """Integration-style tests mocking the Gamma connector."""

    def test_gamma_search_returns_market_objects(self):
        from onto_market.connectors.gamma import GammaConnector, _parse_market

        raw_response = {
            "events": [
                {
                    "markets": [
                        {
                            "id": "101",
                            "question": "Will Bitcoin hit $100k?",
                            "outcomePrices": '["0.72","0.28"]',
                            "outcomes": '["YES","NO"]',
                            "clobTokenIds": '["cid1","cid2"]',
                            "volumeNum": 500000,
                            "liquidityNum": 100000,
                            "active": True,
                        }
                    ]
                }
            ]
        }

        gc = GammaConnector()
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = raw_response
        mock_resp.raise_for_status = MagicMock()

        with patch.object(gc.session, "get", return_value=mock_resp):
            markets = gc.search_markets("bitcoin 100k", limit=5)
            assert len(markets) == 1
            assert markets[0].question == "Will Bitcoin hit $100k?"
            assert markets[0].outcome_prices[0] == pytest.approx(0.72)
            assert markets[0].clob_token_ids == ["cid1", "cid2"]

    def test_gamma_search_empty_results(self):
        from onto_market.connectors.gamma import GammaConnector

        gc = GammaConnector()
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"events": []}
        mock_resp.raise_for_status = MagicMock()

        with patch.object(gc.session, "get", return_value=mock_resp):
            markets = gc.search_markets("nonexistent query xyz", limit=5)
            assert len(markets) == 0
