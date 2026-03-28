#!/usr/bin/env python
"""Seed/refresh the local market database from the Gamma API."""
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
    args = parser.parse_args()

    console.print(f"[bold cyan]Fetching up to {args.max_events} markets from Gamma API...[/]")

    gamma = GammaConnector()
    memory = MemoryManager(config.DATABASE_PATH)

    markets = gamma.iter_markets(max_markets=args.max_events, category=args.category)

    for market in track(markets, description="Storing markets..."):
        memory.upsert_market(market)

    console.print(f"[bold green]Done — {len(markets)} markets stored to {config.DATABASE_PATH}[/]")


if __name__ == "__main__":
    main()
