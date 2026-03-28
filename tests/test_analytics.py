"""Unit tests for edge/kelly/EV analytics."""
import pytest
from onto_market.polymarket_agents.utils.analytics import (
    calculate_edge,
    expected_value,
    kelly_fraction,
    score_market,
)


def test_edge_positive():
    assert calculate_edge(0.60, 0.50) == pytest.approx(0.10, abs=1e-6)


def test_edge_negative():
    assert calculate_edge(0.40, 0.55) < 0


def test_expected_value():
    ev = expected_value(0.60, 0.50)
    assert ev == pytest.approx(0.20, abs=1e-4)


def test_kelly_zero_when_no_edge():
    assert kelly_fraction(0.0, 0.5) == 0.0


def test_score_market_bet():
    result = score_market(0.65, 0.50, volume=10_000)
    assert result["action"] == "BET"
    assert result["edge"] > 0.03


def test_score_market_pass():
    result = score_market(0.48, 0.50, volume=10_000)
    assert result["action"] == "PASS"


def test_score_market_watch_low_volume():
    # Positive edge but under MIN_VOLUME
    result = score_market(0.60, 0.50, volume=100)
    assert result["action"] in ("WATCH", "PASS")  # volume too low for BET
