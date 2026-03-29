"""Batch-enrich the ontology from all available data sources.

Runs the cheap (no-LLM) enrichment paths:
  1. Active market metadata (tags, categories, entities)
  2. Cross-market correlations (shared events/tags)
  3. ML artifact feature importance (if artifacts exist)
  4. Resolved market outcomes (confirm/refute existing edges)
  5. Entity decomposition (split hub nodes)

Usage:
    python scripts/enrich_ontology.py
    make enrich-ontology
"""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from onto_market.ontology.graph import OntologyGraph
from onto_market.ontology.enricher import (
    enrich_from_all_sources,
    from_resolved_outcome,
)
from onto_market.ml_research.artifacts import get_latest, get_metadata, list_versions
from onto_market.config import config
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)

_DB = config.DATABASE_PATH


def _load_active_markets(db_path: str) -> list[dict]:
    """Load active markets from the markets table."""
    db = Path(db_path)
    if not db.exists():
        return []
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            "SELECT * FROM markets WHERE active = 1 ORDER BY volume DESC LIMIT 200"
        ).fetchall()
        markets = []
        for r in rows:
            m = dict(r)
            if isinstance(m.get("tags"), str):
                try:
                    m["tags"] = json.loads(m["tags"])
                except (json.JSONDecodeError, ValueError):
                    m["tags"] = []
            markets.append(m)
        return markets
    except Exception as exc:
        logger.warning("Could not load active markets: %s", exc)
        return []
    finally:
        con.close()


def _load_resolved_markets(db_path: str, limit: int = 2500) -> list[dict]:
    """Load resolved markets with parsed tags."""
    db = Path(db_path)
    if not db.exists():
        return []
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            "SELECT * FROM resolved_markets ORDER BY volume DESC LIMIT ?",
            (limit,),
        ).fetchall()
        markets = []
        for r in rows:
            m = dict(r)
            if isinstance(m.get("tags"), str):
                try:
                    m["tags"] = json.loads(m["tags"])
                except (json.JSONDecodeError, ValueError):
                    m["tags"] = []
            else:
                m["tags"] = []
            markets.append(m)
        return markets
    except Exception as exc:
        logger.warning("Could not load resolved markets: %s", exc)
        return []
    finally:
        con.close()


def _load_ml_metadata() -> dict | None:
    """Load the latest ML artifact metadata."""
    reg = list_versions("data/ml_artifacts")
    promoted = reg.get("promoted", 0)
    if promoted > 0:
        return get_metadata(promoted, "data/ml_artifacts")
    latest = reg.get("latest", 0)
    if latest > 0:
        return get_metadata(latest, "data/ml_artifacts")
    return None


def main() -> None:
    onto = OntologyGraph()
    before_nodes = onto.g.number_of_nodes()
    before_edges = onto.g.number_of_edges()

    print(f"  Ontology before: {before_nodes} nodes, {before_edges} edges")

    # Gather all data sources
    active = _load_active_markets(_DB)
    resolved = _load_resolved_markets(_DB)
    ml_meta = _load_ml_metadata()

    # Resolved markets with tags feed both metadata extraction AND outcome enrichment
    resolved_with_tags = [m for m in resolved if m.get("tags")]
    resolved_no_tags = len(resolved) - len(resolved_with_tags)

    print(f"  Data sources: {len(active)} active markets, "
          f"{len(resolved)} resolved markets ({len(resolved_with_tags)} with tags), "
          f"ML metadata: {'yes' if ml_meta else 'no'}")

    # Combine all markets for metadata/pair extraction
    all_markets = active + resolved
    summary = enrich_from_all_sources(
        onto,
        markets=all_markets if all_markets else None,
        ml_metadata=ml_meta,
        decompose=True,
        persist=False,
    )

    # Resolved outcomes: ground truth reinforcement of existing edges
    res_count = 0
    for mkt in resolved:
        triples = from_resolved_outcome(mkt, onto, source="resolution")
        if triples:
            onto.add_triples(triples, persist=False)
            res_count += len(triples)
    summary["resolved_outcomes"] = res_count

    # Single persist at the end
    onto._save()

    after_nodes = onto.g.number_of_nodes()
    after_edges = onto.g.number_of_edges()

    print(f"\n  Enrichment summary:")
    for src, count in sorted(summary.items()):
        if src != "total":
            print(f"    {src}: {count} triples")
    print(f"    {'─' * 30}")
    print(f"    total: {summary.get('total', 0) + res_count} triples")
    print(f"\n  Ontology after: {after_nodes} nodes (+{after_nodes - before_nodes}), "
          f"{after_edges} edges (+{after_edges - before_edges})")


if __name__ == "__main__":
    main()
