"""
Memory manager — SQLite short-term storage.
Zep Cloud (long-term graph memory) wired in Phase 2 via ZepEntityReader.
"""
import json
from datetime import datetime, timezone

from src.polymarket_agents.utils.database import Database
from src.polymarket_agents.utils.objects import Market


class MemoryManager:
    def __init__(self, db_path: str = "data/memory.db"):
        self.db = Database(db_path)

    # --- Markets ---

    def upsert_market(self, market: Market) -> None:
        self.db.execute(
            """
            INSERT OR REPLACE INTO markets
            (id, question, description, category, outcome_prices,
             clob_token_ids, volume, liquidity, active, end_date, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                market.id,
                market.question,
                market.description,
                market.category,
                json.dumps(market.outcome_prices),
                json.dumps(market.clob_token_ids),   # ← NEW
                market.volume,
                market.liquidity,
                int(market.active),
                market.end_date,
                market.last_updated.isoformat(),
                ),
            )

    def search_markets(self, query: str, category: str | None = None) -> list[dict]:
        if category:
            return self.db.execute(
                "SELECT * FROM markets WHERE category = ? AND active = 1 LIMIT 20",
                (category,),
            )
        return self.db.execute(
            "SELECT * FROM markets WHERE question LIKE ? AND active = 1 LIMIT 20",
            (f"%{query}%",),
        )

    # --- Research ---

    def store_research(self, market_id: str, content: str, source: str = "") -> None:
        self.db.execute(
            "INSERT INTO research (market_id, content, source, timestamp) VALUES (?, ?, ?, ?)",
            (market_id, content, source, datetime.now(timezone.utc).isoformat()),
        )

    def get_research(self, market_id: str) -> list[dict]:
        return self.db.execute(
            "SELECT * FROM research WHERE market_id = ? ORDER BY timestamp DESC LIMIT 5",
            (market_id,),
        )

    # --- Analytics ---

    def store_analytics(
        self,
        market_id: str,
        estimated_prob: float,
        edge: float,
        action: str,
        notes: str = "",
    ) -> None:
        self.db.execute(
            """
            INSERT OR REPLACE INTO analytics
              (market_id, estimated_prob, edge, action, analyst_notes, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (market_id, estimated_prob, edge, action, notes, datetime.now(timezone.utc).isoformat()),
        )
