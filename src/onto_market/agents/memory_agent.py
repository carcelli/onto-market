"""
Memory Agent — DB-first, Gamma API enrichment on demand.

Flow:  memory_node → enrichment_node → reasoning_node → decide_node
"""
import sys
from typing import Any

from langchain_core.messages import HumanMessage
from langgraph.graph import END, StateGraph

from onto_market.agents.state import MemoryAgentState
from onto_market.config import config
from onto_market.connectors.gamma import GammaConnector
from onto_market.memory.manager import MemoryManager
from onto_market.utils.llm_client import LLMClient
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)
memory = MemoryManager(config.DATABASE_PATH)
gamma = GammaConnector()
llm = LLMClient()

_LIVE_KEYWORDS = {"live", "current", "today", "now", "latest", "recent"}


# ── nodes ──────────────────────────────────────────────────────────────────

def memory_node(state: MemoryAgentState) -> dict:
    query = state["query"]
    logger.info("memory_node: querying local DB for '%s'", query)
    rows = memory.search_markets(query)
    return {"memory_context": rows}


def enrichment_node(state: MemoryAgentState) -> dict:
    query = state["query"].lower()
    needs_live = any(kw in query for kw in _LIVE_KEYWORDS) or not state["memory_context"]

    if not needs_live:
        logger.info("enrichment_node: skipping (DB had results, no live keyword)")
        return {"live_data": []}

    logger.info("enrichment_node: fetching live data from Gamma")
    try:
        markets = gamma.iter_markets(max_markets=20)
        live_data = [
            {
                "id": m.id,
                "question": m.question,
                "implied_prob": m.implied_probability,
                "volume": m.volume,
                "category": m.category,
            }
            for m in markets
        ]
    except Exception as exc:
        logger.warning("enrichment_node: Gamma fetch failed: %s", exc)
        live_data = []

    return {"live_data": live_data}


def reasoning_node(state: MemoryAgentState) -> dict:
    all_markets = state["memory_context"] + state["live_data"]
    context_text = "\n".join(
        f"- {m.get('question', m.get('id', '?'))} (vol=${m.get('volume', 0):,.0f})"
        for m in all_markets[:15]
    )

    messages = [
        llm.system(
            "You are a Polymarket research analyst. Analyse the markets below and "
            "produce a concise summary of opportunities relevant to the user query."
        ),
        llm.user(f"Query: {state['query']}\n\nMarkets:\n{context_text}"),
    ]

    logger.info("reasoning_node: calling LLM (%s)", config.GROK_MODEL)
    analysis = llm.strip_think_tags(llm.chat(messages, temperature=0.3))
    return {"analysis": analysis}


def decide_node(state: MemoryAgentState) -> dict:
    all_markets = state["memory_context"] + state["live_data"]
    high_volume = [m for m in all_markets if m.get("volume", 0) >= config.MIN_VOLUME]

    decision: dict[str, Any] = {}
    if not high_volume:
        decision = {"action": "ANALYZE_ONLY", "reason": "No markets meet volume threshold"}
    else:
        decision = {
            "action": "WATCH",
            "markets": high_volume[:5],
            "reason": f"Found {len(high_volume)} markets above ${config.MIN_VOLUME:,.0f} volume",
        }

    logger.info("decide_node: %s", decision["action"])
    return {"decision": decision}


# ── graph ──────────────────────────────────────────────────────────────────

from onto_market.core.graph import register_graph


@register_graph("memory_agent")
def create_memory_agent():
    g = StateGraph(MemoryAgentState)
    g.add_node("memory", memory_node)
    g.add_node("enrichment", enrichment_node)
    g.add_node("reasoning", reasoning_node)
    g.add_node("decide", decide_node)

    g.set_entry_point("memory")
    g.add_edge("memory", "enrichment")
    g.add_edge("enrichment", "reasoning")
    g.add_edge("reasoning", "decide")
    g.add_edge("decide", END)

    return g.compile()


# ── CLI entry point ────────────────────────────────────────────────────────

if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) or "Find crypto markets"
    agent = create_memory_agent()
    result = agent.invoke(
        {"query": query, "messages": [HumanMessage(content=query)]},
        config={"recursion_limit": 10},
    )
    print("\n=== Analysis ===")
    print(result.get("analysis", "(no analysis)"))
    print("\n=== Decision ===")
    print(result.get("decision"))
