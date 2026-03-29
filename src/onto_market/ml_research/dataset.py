"""Fetch resolved Polymarket markets and build train/val splits.

Ground truth comes from the Gamma API: closed markets with
``umaResolutionStatus == "resolved"`` and binary ``outcomePrices``
(exactly ``["1","0"]`` or ``["0","1"]``).
"""
from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from onto_market.config import config
from onto_market.connectors.gamma import GammaConnector
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)

_DEFAULT_DB = config.DATABASE_PATH

_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS resolved_markets (
    market_id   TEXT PRIMARY KEY,
    question    TEXT,
    category    TEXT,
    tags        TEXT,       -- JSON list
    volume      REAL,
    liquidity   REAL,
    implied_prob_at_close REAL,
    resolved_yes INTEGER,  -- 1 = YES won, 0 = NO won
    end_date    TEXT,
    closed_time TEXT,
    fetched_at  TEXT
)
"""


@contextmanager
def _conn(db_path: str):
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()


def _bootstrap(db_path: str) -> None:
    with _conn(db_path) as con:
        con.execute(_CREATE_TABLE)


def _parse_json_field(value: Any, default: Any = None) -> Any:
    if value is None:
        return default
    if isinstance(value, str):
        try:
            return json.loads(value)
        except (json.JSONDecodeError, ValueError):
            return default
    return value


def _is_binary_resolved(raw: dict) -> bool:
    """Return True if this market has a clean binary resolution."""
    status = raw.get("umaResolutionStatus", "")
    if status != "resolved":
        return False
    prices = _parse_json_field(raw.get("outcomePrices"), [])
    if not isinstance(prices, list) or len(prices) != 2:
        return False
    try:
        floats = sorted([float(p) for p in prices])
    except (ValueError, TypeError):
        return False
    return floats == [0.0, 1.0]


def _extract_row(raw: dict) -> dict:
    """Convert a raw Gamma market dict into a resolved_markets row."""
    prices = _parse_json_field(raw.get("outcomePrices"), ["0.5", "0.5"])
    resolved_yes = int(float(prices[0]) == 1.0)

    tags_raw = _parse_json_field(raw.get("tags"), [])
    tag_labels: list[str] = []
    if isinstance(tags_raw, list):
        for t in tags_raw:
            tag_labels.append(t.get("label", str(t)) if isinstance(t, dict) else str(t))

    category = raw.get("category", "")
    if not category and tag_labels:
        category = tag_labels[0]

    volume = float(raw.get("volumeNum", 0) or raw.get("volume", 0) or 0)
    liquidity = float(raw.get("liquidityNum", 0) or raw.get("liquidity", 0) or 0)

    best_bid = _parse_json_field(raw.get("bestBid"))
    if best_bid is not None:
        implied = float(best_bid)
    else:
        implied = float(prices[0]) if prices else 0.5

    return {
        "market_id": str(raw["id"]),
        "question": raw.get("question", ""),
        "category": category,
        "tags": json.dumps(tag_labels),
        "volume": volume,
        "liquidity": liquidity,
        "implied_prob_at_close": implied,
        "resolved_yes": resolved_yes,
        "end_date": raw.get("endDate", ""),
        "closed_time": raw.get("closedTime", ""),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def fetch_resolved(
    max_markets: int = 2000,
    db_path: str = _DEFAULT_DB,
) -> int:
    """Download resolved markets from Gamma and upsert into SQLite.

    Returns the number of new/updated rows.
    """
    _bootstrap(db_path)
    gamma = GammaConnector()
    inserted = 0
    offset = 0
    page_size = 100

    while inserted < max_markets:
        batch = gamma.get_markets(
            limit=page_size,
            offset=offset,
            active=False,
            closed=True,
            order="volumeNum",
            ascending=False,
        )
        if not batch:
            break

        rows = [_extract_row(m) for m in batch if _is_binary_resolved(m)]

        if rows:
            with _conn(db_path) as con:
                con.executemany(
                    """INSERT OR REPLACE INTO resolved_markets
                       (market_id, question, category, tags, volume, liquidity,
                        implied_prob_at_close, resolved_yes, end_date, closed_time,
                        fetched_at)
                       VALUES (:market_id, :question, :category, :tags, :volume,
                               :liquidity, :implied_prob_at_close, :resolved_yes,
                               :end_date, :closed_time, :fetched_at)""",
                    rows,
                )
            inserted += len(rows)
            logger.info("fetch_resolved: stored %d resolved markets (total %d)", len(rows), inserted)

        offset += len(batch)
        if len(batch) < page_size:
            break

    logger.info("fetch_resolved: finished — %d resolved markets in DB", inserted)
    return inserted


def load_resolved(
    db_path: str = _DEFAULT_DB,
) -> list[dict]:
    """Load all resolved markets from the local SQLite store."""
    _bootstrap(db_path)
    with _conn(db_path) as con:
        cursor = con.execute(
            "SELECT * FROM resolved_markets ORDER BY closed_time ASC"
        )
        return [dict(row) for row in cursor.fetchall()]


def time_split(
    rows: list[dict],
    train_frac: float = 0.7,
) -> tuple[list[dict], list[dict]]:
    """Split rows temporally — older fraction for train, rest for validation.

    Rows must already be sorted by closed_time (``load_resolved`` does this).
    """
    if not rows:
        return [], []
    n = max(1, int(len(rows) * train_frac))
    return rows[:n], rows[n:]
