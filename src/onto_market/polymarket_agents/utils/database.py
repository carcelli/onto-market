"""SQLite helper — thin wrapper for the memory manager and connectors."""
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any


class Database:
    def __init__(self, path: str = "data/memory.db"):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        self._bootstrap()

    def _bootstrap(self) -> None:
        with self.conn() as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS markets (
                    id TEXT PRIMARY KEY,
                    question TEXT,
                    description TEXT,
                    category TEXT,
                    outcome_prices TEXT,
                    clob_token_ids TEXT,
                    volume REAL,
                    liquidity REAL,
                    active INTEGER,
                    end_date TEXT,
                    last_updated TEXT,
                    tags TEXT
                )
            """)
            # Migrate existing DBs that lack the tags column
            try:
                db.execute("ALTER TABLE markets ADD COLUMN tags TEXT")
            except sqlite3.OperationalError:
                pass  # column already exists
            db.execute("""
                CREATE TABLE IF NOT EXISTS research (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    market_id TEXT,
                    content TEXT,
                    source TEXT,
                    timestamp TEXT
                )
            """)
            db.execute("""
                CREATE TABLE IF NOT EXISTS analytics (
                    market_id TEXT PRIMARY KEY,
                    estimated_prob REAL,
                    edge REAL,
                    action TEXT,
                    analyst_notes TEXT,
                    timestamp TEXT
                )
            """)

    @contextmanager
    def conn(self):
        con = sqlite3.connect(self.path)
        con.row_factory = sqlite3.Row
        try:
            yield con
            con.commit()
        finally:
            con.close()

    def execute(self, sql: str, params: tuple = ()) -> list[dict]:
        with self.conn() as db:
            cursor = db.execute(sql, params)
            return [dict(row) for row in cursor.fetchall()]

    def execute_one(self, sql: str, params: tuple = ()) -> dict | None:
        rows = self.execute(sql, params)
        return rows[0] if rows else None
