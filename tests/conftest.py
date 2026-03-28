"""Pytest fixtures shared across the test suite."""
import pytest

from onto_market.polymarket_agents.utils.objects import Market


@pytest.fixture
def sample_market() -> Market:
    return Market(
        id="test-001",
        question="Will Bitcoin exceed $100k by end of 2025?",
        category="crypto",
        outcome_prices=[0.42, 0.58],
        volume=250_000,
        liquidity=50_000,
        active=True,
    )


@pytest.fixture
def db_path(tmp_path) -> str:
    return str(tmp_path / "test_memory.db")
