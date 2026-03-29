"""Fetch resolved Polymarket markets and build train/val splits.

Ground truth comes from the Gamma API: closed markets with
``umaResolutionStatus == "resolved"`` and binary ``outcomePrices``
(exactly ``["1","0"]`` or ``["0","1"]``).

Active markets are snapshotted separately for live inference — they have
no ground-truth label so they never enter the training set.
"""
from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
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
    recent_days: int | None = None,
) -> int:
    """Download resolved markets from Gamma and upsert into SQLite.

    Args:
        recent_days: If set, only fetch markets that ended within the last
            N days. Keeps training data fresh and relevant.

    Returns the number of new/updated rows.
    """
    _bootstrap(db_path)
    gamma = GammaConnector()
    inserted = 0
    offset = 0
    page_size = 100

    end_date_min: str | None = None
    if recent_days is not None and recent_days > 0:
        cutoff = datetime.now(timezone.utc) - timedelta(days=recent_days)
        end_date_min = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")
        logger.info("fetch_resolved: filtering to markets ending after %s", end_date_min)

    while inserted < max_markets:
        batch = gamma.get_markets(
            limit=page_size,
            offset=offset,
            active=False,
            closed=True,
            order="volumeNum",
            ascending=False,
            end_date_min=end_date_min,
        )
        if not batch:
            break

        rows = [_extract_row(m) for m in batch if _is_binary_resolved(m)]

        # Client-side date guard in case API doesn't filter perfectly
        if recent_days is not None:
            cutoff_str = (datetime.now(timezone.utc) - timedelta(days=recent_days)).isoformat()
            rows = [
                r for r in rows
                if (r.get("closed_time") or r.get("end_date", "")) >= cutoff_str
            ]

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
    max_age_days: int | None = None,
) -> list[dict]:
    """Load resolved markets from the local SQLite store.

    Args:
        max_age_days: If set, only return markets whose ``closed_time``
            falls within the last N days.  Keeps the training set focused
            on recent market dynamics.
    """
    _bootstrap(db_path)
    with _conn(db_path) as con:
        if max_age_days is not None and max_age_days > 0:
            cutoff = (datetime.now(timezone.utc) - timedelta(days=max_age_days)).isoformat()
            cursor = con.execute(
                "SELECT * FROM resolved_markets "
                "WHERE closed_time >= ? "
                "ORDER BY closed_time ASC",
                (cutoff,),
            )
        else:
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


_ACTIVE_TABLE = """
CREATE TABLE IF NOT EXISTS active_market_snapshots (
    market_id       TEXT PRIMARY KEY,
    question        TEXT,
    category        TEXT,
    tags            TEXT,       -- JSON list
    volume          REAL,
    liquidity       REAL,
    implied_prob    REAL,       -- current mid price
    end_date        TEXT,
    snapshotted_at  TEXT
)
"""


def _extract_active_row(raw: dict) -> dict:
    """Convert a raw Gamma active-market dict into a snapshot row."""
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

    prices = _parse_json_field(raw.get("outcomePrices"), ["0.5", "0.5"])
    implied = float(prices[0]) if prices else 0.5

    return {
        "market_id": str(raw["id"]),
        "question": raw.get("question", ""),
        "category": category,
        "tags": json.dumps(tag_labels),
        "volume": volume,
        "liquidity": liquidity,
        "implied_prob": implied,
        "end_date": raw.get("endDate", ""),
        "snapshotted_at": datetime.now(timezone.utc).isoformat(),
    }


def fetch_active_snapshot(
    max_markets: int = 500,
    db_path: str = _DEFAULT_DB,
    min_volume: float = 1000.0,
) -> int:
    """Snapshot current active markets from Gamma into SQLite.

    These are used for live inference / scoring — never for training
    (no ground-truth label exists yet).

    Returns the number of markets stored.
    """
    with _conn(db_path) as con:
        con.execute(_ACTIVE_TABLE)

    gamma = GammaConnector()
    stored = 0
    offset = 0
    page_size = 100

    while stored < max_markets:
        batch = gamma.get_markets(
            limit=page_size,
            offset=offset,
            active=True,
            closed=False,
            order="volumeNum",
            ascending=False,
        )
        if not batch:
            break

        rows = []
        for m in batch:
            prices = _parse_json_field(m.get("outcomePrices"), [])
            if not isinstance(prices, list) or len(prices) != 2:
                continue
            vol = float(m.get("volumeNum", 0) or m.get("volume", 0) or 0)
            if vol < min_volume:
                continue
            rows.append(_extract_active_row(m))

        if rows:
            with _conn(db_path) as con:
                con.executemany(
                    """INSERT OR REPLACE INTO active_market_snapshots
                       (market_id, question, category, tags, volume, liquidity,
                        implied_prob, end_date, snapshotted_at)
                       VALUES (:market_id, :question, :category, :tags, :volume,
                               :liquidity, :implied_prob, :end_date, :snapshotted_at)""",
                    rows,
                )
            stored += len(rows)
            logger.info("fetch_active: stored %d active markets (total %d)", len(rows), stored)

        offset += len(batch)
        if len(batch) < page_size:
            break

    logger.info("fetch_active: finished — %d active markets snapshotted", stored)
    return stored


def load_active(db_path: str = _DEFAULT_DB) -> list[dict]:
    """Load the latest active-market snapshot for inference."""
    with _conn(db_path) as con:
        con.execute(_ACTIVE_TABLE)
        cursor = con.execute(
            "SELECT * FROM active_market_snapshots ORDER BY volume DESC"
        )
        return [dict(row) for row in cursor.fetchall()]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch and inspect Polymarket data")
    parser.add_argument("--fetch", action="store_true", help="Download resolved markets from Gamma API")
    parser.add_argument("--fetch-active", action="store_true", help="Snapshot active markets for inference")
    parser.add_argument("--max-markets", type=int, default=2000)
    parser.add_argument(
        "--recent-days", type=int, default=None,
        help="Only fetch/show markets resolved within the last N days",
    )
    args = parser.parse_args()

    if args.fetch:
        print("Fetching resolved markets from Gamma API...")
        count = fetch_resolved(max_markets=args.max_markets, recent_days=args.recent_days)
        print(f"Stored {count} resolved markets")

    if args.fetch_active:
        print("Snapshotting active markets from Gamma API...")
        count = fetch_active_snapshot(max_markets=args.max_markets)
        print(f"Stored {count} active market snapshots")

    rows = load_resolved(max_age_days=args.recent_days)
    total_rows = load_resolved()
    print(f"\nResolved markets in DB: {len(total_rows)} total, {len(rows)} within filter")
    if rows:
        categories: dict[str, int] = {}
        for r in rows:
            cat = r.get("category", "unknown")
            categories[cat] = categories.get(cat, 0) + 1
        print(f"Top categories: {dict(sorted(categories.items(), key=lambda x: -x[1])[:10])}")
        yes_count = sum(1 for r in rows if r.get("resolved_yes"))
        print(f"Resolved YES: {yes_count}/{len(rows)} ({100*yes_count/len(rows):.1f}%)")
        oldest_closed = min((r.get("closed_time", "") for r in rows if r.get("closed_time")), default="N/A")
        newest_closed = max((r.get("closed_time", "") for r in rows if r.get("closed_time")), default="N/A")
        print(f"Date range: {oldest_closed} → {newest_closed}")
    else:
        print("No resolved markets found. Run with --fetch to download from Gamma API.")

    active = load_active()
    print(f"\nActive market snapshots: {len(active)}")
    if active:
        print(f"Top by volume: {active[0].get('question', '')[:80]}  (${active[0].get('volume', 0):,.0f})")
