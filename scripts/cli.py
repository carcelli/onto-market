"""
onto-market CLI — Typer-based command-line interface.

Commands:
    analyze   Run full planning agent pipeline on a query
    scan      Discover and list markets from Gamma API
    trade     Run the trading pipeline (dry-run by default)
    swarm     Run the Social Sentiment Oracle standalone
"""
import sys
from pathlib import Path

# Ensure project root is on sys.path for local imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer(
    name="onto-market",
    help="Swarm Intelligence x Polymarket Agents x Ontology",
    no_args_is_help=True,
)


@app.command()
def analyze(
    query: str = typer.Argument(..., help="Market question to analyze"),
):
    """Run the full planning agent pipeline: research -> ontology -> stats -> probability -> swarm -> decision -> trade."""
    from langchain_core.messages import HumanMessage
    from agents.planning_agent import create_planning_agent

    console.print(f"\n[bold cyan]Analyzing:[/] {query}\n")

    agent = create_planning_agent()
    result = agent.invoke(
        {"query": query, "messages": [HumanMessage(content=query)], "ontology_context": ""},
        config={"recursion_limit": 15},
    )

    rec = result.get("recommendation", {})
    action = rec.get("action", "UNKNOWN")
    colour = {"BET": "green", "WATCH": "yellow", "PASS": "red"}.get(action, "white")

    console.print(f"[bold {colour}]{'─' * 50}[/]")
    console.print(f"[bold {colour}]  {action}[/]")
    console.print(f"[bold {colour}]{'─' * 50}[/]")
    console.print(f"  Side:            [bold]{rec.get('side', '-')}[/]")
    console.print(f"  Edge:            {rec.get('edge', 0):.1%}")
    console.print(f"  EV:              {rec.get('expected_value', 0):.3f}")
    console.print(f"  Kelly:           {rec.get('kelly_fraction', 0):.1%}")
    console.print(f"  Swarm consensus: {rec.get('swarm_consensus', 0):.3f}")
    console.print(f"  Swarm confidence:{rec.get('swarm_confidence', 0):.2f}")
    console.print(f"  Market:          {rec.get('market_id', '-')}")

    trade = result.get("trade_result", {})
    if trade and not trade.get("skipped"):
        dry = "DRY RUN" if trade.get("dry_run") else "LIVE"
        console.print(f"\n  [bold]Trade:[/] [{dry}] {trade.get('side', 'BUY')} @ {trade.get('price', '?')}")

    console.print()


@app.command()
def scan(
    category: str = typer.Option(None, "--category", "-c", help="Filter by category (e.g. crypto, politics)"),
    limit: int = typer.Option(20, "--limit", "-n", help="Max markets to display"),
):
    """Discover and list active markets from Gamma API."""
    from src.connectors.gamma import GammaConnector

    console.print(f"\n[bold cyan]Scanning markets[/]", end="")
    if category:
        console.print(f" [dim](category={category})[/]")
    else:
        console.print()

    gamma = GammaConnector()
    markets = gamma.iter_markets(max_markets=limit, category=category)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=8)
    table.add_column("Question", width=50)
    table.add_column("Implied", justify="right", width=8)
    table.add_column("Volume", justify="right", width=12)
    table.add_column("Category", width=12)

    for m in markets:
        table.add_row(
            str(m.id)[:8],
            m.question[:48],
            f"{m.implied_probability:.1%}",
            f"${m.volume:,.0f}",
            m.category[:12] if m.category else "-",
        )

    console.print(table)
    console.print(f"\n[dim]{len(markets)} markets shown[/]\n")


@app.command()
def trade(
    query: str = typer.Argument(None, help="Optional query to focus trading on"),
    live: bool = typer.Option(False, "--live", help="Execute live trades (disables SAFE_MODE)"),
):
    """Run the trading pipeline. Dry-run by default unless --live is passed."""
    from src.trading.trader import Trader
    from src.connectors.polymarket import PolymarketConnector

    if live:
        console.print("[bold red]WARNING: Live trading mode enabled![/]\n")

    polymarket = PolymarketConnector(safe_mode=not live)
    trader = Trader(polymarket=polymarket)

    console.print("[bold cyan]Running trading pipeline...[/]\n")
    result = trader.one_best_trade()

    action = result.get("action", "PASS")
    colour = {"BET": "green", "WATCH": "yellow", "PASS": "red"}.get(action, "white")

    console.print(f"[bold {colour}]{action}[/]")
    if action == "BET":
        console.print(f"  Market:    {result.get('market_question', '-')}")
        console.print(f"  Side:      {result.get('side', '-')}")
        console.print(f"  Edge:      {result.get('edge', 0):.1%}")
        console.print(f"  EV:        {result.get('expected_value', 0):.3f}")
        console.print(f"  Size:      ${result.get('size_usd', 0):.2f}")
        dry = result.get("execution", {}).get("dry_run", True)
        console.print(f"  Execution: {'DRY RUN' if dry else 'LIVE'}")
    else:
        console.print(f"  Reason: {result.get('reason', '-')}")

    console.print()


@app.command()
def swarm(
    query: str = typer.Argument(..., help="Market question"),
    base_prob: float = typer.Option(0.5, "--base-prob", "-p", help="Base probability (0-1)"),
    swarm_size: int = typer.Option(None, "--size", "-s", help="Override swarm size"),
    rounds: int = typer.Option(None, "--rounds", "-r", help="Override max rounds"),
):
    """Run the Social Sentiment Oracle standalone."""
    from src.swarm.oracle import SocialSentimentOracle
    from src.utils.llm_client import LLMClient

    size = swarm_size or None
    max_rounds = rounds or None

    console.print(f"\n[bold cyan]Social Sentiment Oracle[/]")
    console.print(f"  Query:     {query}")
    console.print(f"  Base prob: {base_prob:.3f}")

    oracle = SocialSentimentOracle(
        swarm_size=size,
        max_rounds=max_rounds,
    )
    llm = LLMClient()

    result = oracle.estimate(
        query=query,
        base_prob=base_prob,
        llm_client=llm,
    )

    console.print(f"\n[bold]Results:[/]")
    console.print(f"  Consensus:  [bold]{result.consensus_prob:.3f}[/]")
    console.print(f"  Confidence: {result.confidence:.3f}")
    console.print(f"  Dissent:    {result.dissent_ratio:.1%}")
    console.print(f"  Rounds:     {result.rounds_executed}")
    console.print(f"  Mean:       {result.mean_estimate:.3f}")
    console.print(f"  Std:        {result.std_estimate:.4f}")
    console.print(f"  Swarm size: {result.swarm_size}")
    console.print()


if __name__ == "__main__":
    app()
