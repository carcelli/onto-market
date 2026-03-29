#!/usr/bin/env python
"""Seed/refresh the local market database from the Gamma API.

Fetches active markets (for agent queries & inference) and optionally
resolved markets (for ML training).  Use ``--include-resolved`` to pull
both in one pass.
"""
import argparse

from rich.console import Console
from rich.progress import track

from onto_market.config import config
from onto_market.connectors.gamma import GammaConnector
from onto_market.memory.manager import MemoryManager
from onto_market.utils.logger import get_logger

console = Console()
logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Refresh Polymarket markets from Gamma API")
    parser.add_argument("--max-events", type=int, default=500)
    parser.add_argument("--category", default=None)
    parser.add_argument(
        "--include-resolved", action="store_true",
        help="Also fetch recently resolved markets into resolved_markets table for ML training",
    )
    parser.add_argument(
        "--recent-days", type=int, default=90,
        help="When fetching resolved markets, only include those closed within the last N days (default: 90)",
    )
    args = parser.parse_args()

    # ── Active markets (for agents & inference) ──
    console.print(f"[bold cyan]Fetching up to {args.max_events} active markets from Gamma API...[/]")

    gamma = GammaConnector()
    memory = MemoryManager(config.DATABASE_PATH)

    markets = gamma.iter_markets(max_markets=args.max_events, category=args.category)

    for market in track(markets, description="Storing active markets..."):
        memory.upsert_market(market)

    console.print(f"[bold green]Done — {len(markets)} active markets stored to {config.DATABASE_PATH}[/]")

    # ── Resolved markets (for ML training) ──
    if args.include_resolved:
        from onto_market.ml_research.dataset import fetch_active_snapshot, fetch_resolved

        console.print(
            f"[bold cyan]Fetching resolved markets (last {args.recent_days} days) "
            f"for ML training...[/]"
        )
        resolved_count = fetch_resolved(
            max_markets=args.max_events,
            recent_days=args.recent_days,
        )
        console.print(f"[bold green]Done — {resolved_count} resolved markets stored[/]")

        console.print("[bold cyan]Snapshotting active markets for inference...[/]")
        active_count = fetch_active_snapshot(max_markets=args.max_events)
        console.print(f"[bold green]Done — {active_count} active market snapshots stored[/]")


if __name__ == "__main__":
    main()
