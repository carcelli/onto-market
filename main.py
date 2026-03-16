"""onto-market entry point."""
import sys

from rich.console import Console

from src.utils.logger import get_logger

console = Console()
logger = get_logger("onto-market")


def main():
    logger.info("onto-market starting")
    console.print("[bold cyan]onto-market[/] — Swarm Intelligence × Polymarket Agents")

    if len(sys.argv) < 2:
        console.print("Usage: onto-market <query>")
        console.print("  onto-market 'Will Bitcoin hit $100k?'")
        sys.exit(0)

    query = " ".join(sys.argv[1:])
    logger.info("Running planning agent for: %s", query)

    from agents.planning_agent import create_planning_agent
    from langchain_core.messages import HumanMessage

    agent = create_planning_agent()
    result = agent.invoke(
        {"query": query, "messages": [HumanMessage(content=query)]},
        config={"recursion_limit": 15},
    )

    rec = result.get("recommendation", {})
    action = rec.get("action", "UNKNOWN")
    colour = {"BET": "green", "WATCH": "yellow", "PASS": "red"}.get(action, "white")

    console.print(f"\n[bold {colour}]── {action} ──[/]")
    console.print(f"  Side:  {rec.get('side', '-')}")
    console.print(f"  Edge:  {rec.get('edge', 0):.1%}")
    console.print(f"  EV:    {rec.get('expected_value', 0):.3f}")
    console.print(f"  Kelly: {rec.get('kelly_fraction', 0):.1%}")


if __name__ == "__main__":
    main()
