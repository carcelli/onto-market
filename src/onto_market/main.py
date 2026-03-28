"""
onto-market entry point.

Demonstrates one full planning cycle:
  research -> ontology (triple extraction + graph query) -> stats
           -> probability -> decision

After the run, prints the ontology graph stats so you can see it accumulate
knowledge across repeated queries.
"""
import sys

from rich.console import Console
from rich.table import Table

from onto_market.utils.logger import get_logger

console = Console()
logger = get_logger("onto-market")


def main():
    logger.info("onto-market starting")
    console.print(
        "\n[bold cyan]onto-market[/]  "
        "Swarm Intelligence x Polymarket Agents x Ontology\n"
    )

    if len(sys.argv) < 2:
        console.print("[dim]Usage:[/]  onto-market <query>")
        console.print("[dim]Example:[/] onto-market 'Will Bitcoin hit $100k?'\n")
        sys.exit(0)

    query = " ".join(sys.argv[1:])
    logger.info("query: %s", query)

    from onto_market.agents.planning_agent import create_planning_agent
    from langchain_core.messages import HumanMessage

    agent = create_planning_agent()
    result = agent.invoke(
        {
            "query": query,
            "messages": [HumanMessage(content=query)],
            "ontology_context": "",   # seed empty; ontology_node populates it
        },
        config={"recursion_limit": 15},
    )

    # ── recommendation ──────────────────────────────────────────────────────
    rec = result.get("recommendation", {})
    action = rec.get("action", "UNKNOWN")
    colour = {"BET": "green", "WATCH": "yellow", "PASS": "red"}.get(action, "white")

    console.print(f"[bold {colour}]{'─'*40}[/]")
    console.print(f"[bold {colour}]  {action}[/]")
    console.print(f"[bold {colour}]{'─'*40}[/]")
    console.print(f"  Side:   [bold]{rec.get('side', '-')}[/]")
    console.print(f"  Edge:   {rec.get('edge', 0):.1%}")
    console.print(f"  EV:     {rec.get('expected_value', 0):.3f}")
    console.print(f"  Kelly:  {rec.get('kelly_fraction', 0):.1%}")
    console.print(f"  Market: {rec.get('market_id', '-')}")

    # ── ontology context used ───────────────────────────────────────────────
    onto_ctx = result.get("ontology_context", "")
    if onto_ctx:
        console.print("\n[bold]Ontology context used:[/]")
        for line in onto_ctx.splitlines()[:8]:
            console.print(f"  [dim]{line}[/]")

    # ── ontology graph stats ────────────────────────────────────────────────
    from onto_market.ontology.graph import OntologyGraph
    onto = OntologyGraph()          # loads same persisted graph
    stats = onto.stats()

    console.print(f"\n[bold]Ontology graph[/]  "
                  f"({stats['nodes']} nodes, {stats['edges']} edges)")

    if stats["top_entities"]:
        table = Table(show_header=True, header_style="bold magenta", box=None)
        table.add_column("Entity", style="cyan", no_wrap=True)
        table.add_column("Degree", justify="right")
        for entity, degree in stats["top_entities"][:8]:
            table.add_row(entity, str(degree))
        console.print(table)

    console.print()


if __name__ == "__main__":
    main()
