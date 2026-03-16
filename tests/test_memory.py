"""Unit tests for MemoryManager."""
from src.memory.manager import MemoryManager
from src.polymarket_agents.utils.objects import Market


def test_upsert_and_search(db_path, sample_market):
    mem = MemoryManager(db_path)
    mem.upsert_market(sample_market)
    results = mem.search_markets("Bitcoin")
    assert any(r["id"] == "test-001" for r in results)


def test_store_and_get_research(db_path):
    mem = MemoryManager(db_path)
    mem.store_research("test-001", "BTC bullish sentiment from on-chain data", "internal")
    rows = mem.get_research("test-001")
    assert len(rows) == 1
    assert "bullish" in rows[0]["content"]


def test_store_analytics(db_path):
    mem = MemoryManager(db_path)
    mem.store_analytics("test-001", 0.65, 0.15, "BET", "Strong edge detected")
    row = mem.db.execute_one("SELECT * FROM analytics WHERE market_id = 'test-001'")
    assert row is not None
    assert row["action"] == "BET"
