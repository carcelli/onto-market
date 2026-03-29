#!/usr/bin/env python
"""Fetch resolved Polymarket markets from Gamma → SQLite."""
import argparse

from rich.console import Console

from onto_market.config import config
from onto_market.ml_research.dataset import fetch_resolved

console = Console()


def main():
    parser = argparse.ArgumentParser(description="Fetch resolved markets from Gamma API")
    parser.add_argument("--max-markets", type=int, default=2000)
    parser.add_argument("--db-path", type=str, default=config.DATABASE_PATH)
    args = parser.parse_args()

    console.print(f"[bold cyan]Fetching up to {args.max_markets} resolved markets...[/]")
    count = fetch_resolved(max_markets=args.max_markets, db_path=args.db_path)
    console.print(f"[bold green]Done — {count} resolved markets stored to {args.db_path}[/]")


if __name__ == "__main__":
    main()
