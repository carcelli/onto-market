"""
Planning Agent — full analysis pipeline.

Flow: research_node → stats_node → probability_node → decision_node
Decision thresholds: MIN_EDGE=3%, MIN_VOLUME=$5k, MIN_KELLY=1%
Output: BET / WATCH / PASS
"""
import sys

from langchain_core.messages import HumanMessage
from langgraph.graph import END, StateGraph

from agents.state import PlanningState
from config import config
from src.connectors.gamma import GammaConnector
from src.connectors.news import NewsConnector
from src.connectors.search import SearchConnector
from src.memory.manager import MemoryManager
from src.polymarket_agents.utils.analytics import score_market
from src.utils.llm_client import LLMClient
from src.utils.logger import get_logger

logger = get_logger(__name__)
memory = MemoryManager(config.DATABASE_PATH)
gamma = GammaConnector()
search = SearchConnector()
news = NewsConnector()
llm = LLMClient()


# ── nodes ──────────────────────────────────────────────────────────────────

def research_node(state: PlanningState) -> dict:
    query = state["query"]
    logger.info("research_node: '%s'", query)

    # DB first
    db_markets = memory.search_markets(query)

    # Enrich with live Gamma if sparse
    live_markets = []
    if len(db_markets) < 3:
        try:
            live_markets = [
                {
                    "id": m.id,
                    "question": m.question,
                    "implied_prob": m.implied_probability,
                    "volume": m.volume,
                    "category": m.category,
                }
                for m in gamma.iter_markets(max_markets=10)
            ]
        except Exception as exc:
            logger.warning("research_node: Gamma error: %s", exc)

    # Web context
    research_context = ""
    try:
        research_context = search.search_text(query, max_results=3)
    except Exception:
        try:
            research_context = news.headlines_text(query, page_size=5)
        except Exception:
            pass

    all_markets = db_markets + live_markets
    return {"market_data": all_markets, "research_context": research_context}


def stats_node(state: PlanningState) -> dict:
    markets = state["market_data"]
    if not markets:
        logger.info("stats_node: no market data")
        return {"implied_probability": 0.5}

    # Use first matching market's implied prob
    implied = markets[0].get("implied_prob", 0.5)
    logger.info("stats_node: implied_prob=%.3f from %d markets", implied, len(markets))
    return {"implied_probability": implied}


def probability_node(state: PlanningState) -> dict:
    implied = state["implied_probability"]
    query = state["query"]
    context = state["research_context"][:1500]  # trim for token budget
    markets_summary = "\n".join(
        f"- {m.get('question', '?')} → {m.get('implied_prob', 0.5):.1%} (vol=${m.get('volume', 0):,.0f})"
        for m in state["market_data"][:5]
    )

    messages = [
        llm.system(
            "You are a quantitative Polymarket analyst. Given the query, market data, "
            "and research context, estimate the TRUE probability of the event. "
            "Respond with a JSON object: {\"estimated_prob\": <float 0-1>, \"rationale\": <str>}"
        ),
        llm.user(
            f"Query: {query}\n\n"
            f"Implied market probability: {implied:.1%}\n\n"
            f"Markets:\n{markets_summary}\n\n"
            f"Research context:\n{context}"
        ),
    ]

    logger.info("probability_node: asking LLM for true probability estimate")
    result = llm.chat_json(messages, temperature=0.2)
    estimated = float(result.get("estimated_prob", implied))
    logger.info("probability_node: estimated_prob=%.3f (implied=%.3f)", estimated, implied)
    return {"estimated_probability": estimated}


def decision_node(state: PlanningState) -> dict:
    implied = state["implied_probability"]
    estimated = state["estimated_probability"]
    volume = state["market_data"][0].get("volume", 0) if state["market_data"] else 0

    scorecard = score_market(
        true_prob=estimated,
        implied_prob=implied,
        volume=volume,
        min_edge=config.MIN_EDGE,
        min_volume=config.MIN_VOLUME,
        min_kelly=config.MIN_KELLY,
    )

    market_id = state["market_data"][0].get("id", "") if state["market_data"] else ""
    side = "YES" if estimated > 0.5 else "NO"

    recommendation = {
        "action": scorecard["action"],
        "market_id": market_id,
        "side": side,
        **scorecard,
    }

    logger.info(
        "decision_node: %s | edge=%.1f%% | EV=%.3f | kelly=%.1f%%",
        scorecard["action"],
        scorecard["edge"] * 100,
        scorecard["expected_value"],
        scorecard["kelly_fraction"] * 100,
    )

    # Persist to DB
    if market_id:
        memory.store_analytics(
            market_id=market_id,
            estimated_prob=estimated,
            edge=scorecard["edge"],
            action=scorecard["action"],
        )

    return {
        "edge": scorecard["edge"],
        "expected_value": scorecard["expected_value"],
        "kelly_fraction": scorecard["kelly_fraction"],
        "recommendation": recommendation,
    }


# ── graph ──────────────────────────────────────────────────────────────────

from core.graph import register_graph

# ... (rest of imports)

@register_graph("planning_agent")
def create_planning_agent():
    g = StateGraph(PlanningState)
    g.add_node("research", research_node)
    g.add_node("stats", stats_node)
    g.add_node("probability", probability_node)
    g.add_node("decision", decision_node)

    g.set_entry_point("research")
    g.add_edge("research", "stats")
    g.add_edge("stats", "probability")
    g.add_edge("probability", "decision")
    g.add_edge("decision", END)

    return g.compile()


# ── CLI entry point ────────────────────────────────────────────────────────

if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) or "Will Bitcoin hit $100k by end of 2025?"
    agent = create_planning_agent()
    result = agent.invoke(
        {"query": query, "messages": [HumanMessage(content=query)]},
        config={"recursion_limit": 10},
    )
    rec = result.get("recommendation", {})
    print(f"\n=== Recommendation: {rec.get('action')} ===")
    print(f"  Side:   {rec.get('side')}")
    print(f"  Edge:   {rec.get('edge', 0):.1%}")
    print(f"  EV:     {rec.get('expected_value', 0):.3f}")
    print(f"  Kelly:  {rec.get('kelly_fraction', 0):.1%}")
