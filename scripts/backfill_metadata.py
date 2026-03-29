"""Backfill tags and categories for markets with empty metadata.

Iterates through resolved_markets and markets tables, fetches per-market
metadata from the Gamma API, and updates rows in-place.  Idempotent — skips
rows that already have non-empty tags.

Usage:
    python scripts/backfill_metadata.py
    python scripts/backfill_metadata.py --limit 500 --sleep 0.15
    make backfill-metadata
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from pathlib import Path

_SRC = Path(__file__).resolve().parent.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from onto_market.config import config
from onto_market.connectors.gamma import GammaConnector, _json_field
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)

_DB = config.DATABASE_PATH


def _parse_tags(raw: dict) -> list[str]:
    """Extract tag labels from a raw Gamma market dict."""
    tags_raw = _json_field(raw.get("tags"), [])
    labels: list[str] = []
    if isinstance(tags_raw, list):
        for t in tags_raw:
            label = t.get("label", str(t)) if isinstance(t, dict) else str(t)
            if label:
                labels.append(label)
    return labels


def _parse_category(raw: dict, tags: list[str]) -> str:
    category = raw.get("category", "")
    if not category and tags:
        category = tags[0]
    return category


def _needs_backfill(tags_val: str | None, cat_val: str | None) -> bool:
    """Return True if this row's tags/category need backfill."""
    tags_empty = not tags_val or tags_val in ("", "[]", "null")
    cat_empty = not cat_val or cat_val == ""
    return tags_empty and cat_empty


def backfill(
    db_path: str = _DB,
    limit: int | None = None,
    sleep_sec: float = 0.1,
) -> dict[str, int]:
    gamma = GammaConnector()
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    stats = {"resolved_checked": 0, "resolved_updated": 0,
             "active_checked": 0, "active_updated": 0, "api_errors": 0}

    # ── Resolved markets ──────────────────────────────────────────────
    try:
        rows = con.execute(
            "SELECT market_id, tags, category FROM resolved_markets"
        ).fetchall()
    except sqlite3.OperationalError:
        rows = []

    need = [dict(r) for r in rows if _needs_backfill(r["tags"], r["category"] if "category" in r.keys() else None)]
    if limit:
        need = need[:limit]
    total = len(need)
    print(f"  Resolved markets needing backfill: {total}")

    for i, row in enumerate(need):
        mid = row["market_id"]
        try:
            raw = gamma.get_market_by_id(mid)
        except Exception as exc:
            logger.debug("backfill: API error for %s: %s", mid, exc)
            stats["api_errors"] += 1
            continue

        if not raw:
            stats["api_errors"] += 1
            continue

        tags = _parse_tags(raw)
        category = _parse_category(raw, tags)
        stats["resolved_checked"] += 1

        if tags or category:
            con.execute(
                "UPDATE resolved_markets SET tags = ?, category = ? WHERE market_id = ?",
                (json.dumps(tags), category, mid),
            )
            stats["resolved_updated"] += 1

        if (i + 1) % 50 == 0:
            con.commit()
            print(f"    resolved: {i + 1}/{total} checked, {stats['resolved_updated']} updated")

        time.sleep(sleep_sec)

    con.commit()

    # ── Active markets ────────────────────────────────────────────────
    try:
        rows = con.execute(
            "SELECT id, tags, category FROM markets"
        ).fetchall()
    except sqlite3.OperationalError:
        rows = []

    need_active = []
    for r in rows:
        d = dict(r)
        if _needs_backfill(d.get("tags"), d.get("category")):
            need_active.append(d)
    if limit:
        need_active = need_active[:limit]
    total_active = len(need_active)
    print(f"  Active markets needing backfill: {total_active}")

    for i, row in enumerate(need_active):
        mid = row["id"]
        try:
            raw = gamma.get_market_by_id(mid)
        except Exception as exc:
            logger.debug("backfill: API error for %s: %s", mid, exc)
            stats["api_errors"] += 1
            continue

        if not raw:
            stats["api_errors"] += 1
            continue

        tags = _parse_tags(raw)
        category = _parse_category(raw, tags)
        description = raw.get("description", "")
        stats["active_checked"] += 1

        if tags or category:
            con.execute(
                "UPDATE markets SET tags = ?, category = ?, description = COALESCE(NULLIF(description, ''), ?) WHERE id = ?",
                (json.dumps(tags), category, description, mid),
            )
            stats["active_updated"] += 1

        if (i + 1) % 50 == 0:
            con.commit()
            print(f"    active: {i + 1}/{total_active} checked, {stats['active_updated']} updated")

        time.sleep(sleep_sec)

    con.commit()
    con.close()
    gamma.close()
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill market tags/categories from Gamma API")
    parser.add_argument("--limit", type=int, default=None, help="Max markets to backfill per table")
    parser.add_argument("--sleep", type=float, default=0.1, help="Seconds between API calls (default: 0.1)")
    parser.add_argument("--db-path", type=str, default=_DB, help="SQLite database path")
    args = parser.parse_args()

    print("  Backfilling market metadata from Gamma API…")
    stats = backfill(db_path=args.db_path, limit=args.limit, sleep_sec=args.sleep)

    print(f"\n  Backfill complete:")
    print(f"    Resolved: {stats['resolved_updated']}/{stats['resolved_checked']} updated")
    print(f"    Active:   {stats['active_updated']}/{stats['active_checked']} updated")
    if stats["api_errors"]:
        print(f"    API errors: {stats['api_errors']}")


if __name__ == "__main__":
    main()
