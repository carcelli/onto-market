"""
Planning Agent — full analysis pipeline with swarm + trading.

Flow:
  research_node
      → ontology_node   (extract triples, query prior knowledge)
      → stats_node
      → probability_node  (LLM estimate using ontology context)
      → swarm_node        (OASIS-style swarm consensus)
      → decision_node     (BET / WATCH / PASS)
      → trade_node        (dry-run order if BET)

Decision thresholds: MIN_EDGE=3%, MIN_VOLUME=$5k, MIN_KELLY=1%
"""
import json
import sys

from langchain_core.messages import HumanMessage
from langgraph.graph import END, StateGraph

from agents.ontology_agent import ontology_node
from agents.state import PlanningState
from config import config
from core.graph import register_graph
from src.connectors.gamma import GammaConnector
from src.connectors.news import NewsConnector
from src.connectors.search import SearchConnector
from src.memory.manager import MemoryManager
from src.polymarket_agents.utils.analytics import score_market
from src.swarm.oracle import SocialSentimentOracle
from src.utils.llm_client import LLMClient
from src.utils.logger import get_logger

logger = get_logger(__name__)
memory = MemoryManager(config.DATABASE_PATH)
gamma = GammaConnector()
search = SearchConnector()
news = NewsConnector()
llm = LLMClient()

_STOPWORDS = frozenset({
    "a", "an", "the", "is", "it", "be", "of", "in", "at", "to", "by",
    "will", "end", "for", "on", "or", "and", "not", "has", "have", "had",
    "this", "that", "with", "from", "are", "was", "were", "been", "does",
})


# ── helpers ────────────────────────────────────────────────────────────────

def _normalize_market(m: dict) -> dict:
    """Ensure consistent keys whether m came from DB or Gamma Market objects."""
    prices = m.get("outcome_prices")
    if isinstance(prices, str):
        try:
            prices = json.loads(prices)
        except (json.JSONDecodeError, ValueError):
            prices = None
    implied = float(prices[0]) if prices else m.get("implied_prob", 0.5)

    token_ids = m.get("clob_token_ids", [])
    if isinstance(token_ids, str):
        try:
            token_ids = json.loads(token_ids) if token_ids else []
        except (json.JSONDecodeError, ValueError):
            token_ids = []

    return {**m, "implied_prob": implied, "clob_token_ids": token_ids}


def _market_from_obj(m) -> dict:
    """Convert a Gamma Market object to a normalized dict."""
    return {
        "id": m.id,
        "question": m.question,
        "implied_prob": m.implied_probability,
        "volume": m.volume,
        "category": m.category,
        "clob_token_ids": m.clob_token_ids,
    }


def _score_market_match(query_tokens: set[str], question: str, volume: float) -> float:
    """Score how well a market question matches the query tokens.

    Overlap dominates; volume is a tiebreaker only.
    """
    q_lower = question.lower()
    overlap = sum(1 for t in query_tokens if t in q_lower)
    return overlap * 10_000 + volume / 1e6


# ── nodes ──────────────────────────────────────────────────────────────────

def research_node(state: PlanningState) -> dict:
    query = state["query"]
    logger.info("research_node: '%s'", query)

    db_markets = [_normalize_market(m) for m in memory.search_markets(query)]

    live_markets: list[dict] = []
    try:
        searched = gamma.search_markets(query, limit=10)
        live_markets = [_market_from_obj(m) for m in searched]
        logger.info("research_node: Gamma search returned %d markets", len(live_markets))
    except Exception as exc:
        logger.warning("research_node: Gamma search failed (%s), falling back to top-volume", exc)

    if not live_markets:
        live_markets = [_market_from_obj(m) for m in gamma.iter_markets(max_markets=10)]

    research_context = ""
    try:
        research_context = search.search_text(query, max_results=3)
    except Exception:
        try:
            research_context = news.headlines_text(query, page_size=5)
        except Exception:
            pass

    if not research_context:
        try:
            research_context = llm.chat(
                [llm.system("Summarize current facts relevant to this prediction market question. Be concise."),
                 llm.user(query)],
                temperature=0.3,
            )
            logger.info("research_node: used Grok native search for context (%d chars)", len(research_context))
        except Exception as exc:
            logger.warning("research_node: Grok search fallback failed: %s", exc)

    return {"market_data": db_markets + live_markets, "research_context": research_context}


def stats_node(state: PlanningState) -> dict:
    markets = state["market_data"]
    if not markets:
        logger.info("stats_node: no market data")
        return {"implied_probability": 0.5, "selected_market": {}}

    query_tokens = {
        t.lower() for t in state["query"].split()
        if len(t) > 2 and t.lower() not in _STOPWORDS
    }

    best_market = markets[0]
    best_score = -1.0
    for m in markets:
        question = m.get("question", "")
        volume = float(m.get("volume", 0) or 0)
        score = _score_market_match(query_tokens, question, volume)
        if score > best_score:
            best_score = score
            best_market = m

    implied = float(best_market.get("implied_prob", 0.5))
    if implied < 0.005 or implied > 0.995:
        logger.warning(
            "stats_node: implied_prob=%.4f is extreme — likely wrong market match",
            implied,
        )

    logger.info(
        "stats_node: implied_prob=%.3f from '%s' (score=%.0f, best of %d markets)",
        implied, best_market.get("question", "?")[:50], best_score, len(markets),
    )
    return {"implied_probability": implied, "selected_market": best_market}


def probability_node(state: PlanningState) -> dict:
    implied = state["implied_probability"]
    query = state["query"]
    context = state.get("research_context", "")[:1500]
    ontology_context = state.get("ontology_context", "")
    selected = state.get("selected_market", {})
    selected_q = selected.get("question", query)

    markets_summary = "\n".join(
        f"- {m.get('question', '?')} -> {m.get('implied_prob', 0.5):.1%} "
        f"(vol=${m.get('volume', 0):,.0f})"
        for m in state["market_data"][:5]
    )

    onto_section = (
        f"\n\nOntology prior knowledge (structured facts from previous analyses):\n"
        f"{ontology_context}"
        if ontology_context
        else ""
    )

    messages = [
        llm.system(
            "You are a quantitative Polymarket analyst. Given the query, the selected "
            "market question, market data, research context, and any structured ontology "
            "facts, estimate the TRUE probability of the event resolving YES.\n\n"
            "IMPORTANT: Your estimate must be between 0.01 and 0.99 — never return "
            "exactly 0 or 1. The ontology facts are curated from prior research runs — "
            "treat high-confidence ones as reliable signals.\n\n"
            'Respond ONLY with valid JSON: {"estimated_prob": <float 0.01-0.99>, "rationale": <str>}'
        ),
        llm.user(
            f"Query: {query}\n\n"
            f"Selected market: {selected_q}\n"
            f"Implied market probability: {implied:.1%}\n\n"
            f"Markets:\n{markets_summary}\n\n"
            f"Research context:\n{context}"
            f"{onto_section}"
        ),
    ]

    logger.info("probability_node: calling LLM (%s)", config.GROK_MODEL)
    result = llm.chat_json(messages, temperature=0.2)
    raw = float(result.get("estimated_prob", implied))
    estimated = max(0.01, min(0.99, raw))
    if raw != estimated:
        logger.warning("probability_node: clamped %.3f -> %.3f", raw, estimated)
    logger.info("probability_node: estimated=%.3f  implied=%.3f", estimated, implied)
    return {"estimated_probability": estimated}


def swarm_node(state: PlanningState) -> dict:
    """Run Social Sentiment Oracle to get swarm consensus on the estimated probability."""
    estimated = state["estimated_probability"]
    query = state["query"]
    context = state.get("research_context", "")

    logger.info("swarm_node: running oracle (swarm_size=%d)", config.SWARM_SIZE)

    try:
        oracle = SocialSentimentOracle()
        result = oracle.estimate(
            query=query,
            base_prob=estimated,
            context=context,
            llm_client=llm,
        )

        logger.info(
            "swarm_node: consensus=%.3f confidence=%.3f dissent=%.1f%%",
            result.consensus_prob, result.confidence, result.dissent_ratio * 100,
        )

        return {
            "swarm_consensus": result.consensus_prob,
            "swarm_confidence": result.confidence,
            "swarm_dissent": result.dissent_ratio,
        }
    except Exception as exc:
        logger.warning("swarm_node: oracle failed, using LLM estimate: %s", exc)
        return {
            "swarm_consensus": estimated,
            "swarm_confidence": 0.0,
            "swarm_dissent": 0.0,
        }


def decision_node(state: PlanningState) -> dict:
    implied = state["implied_probability"]
    estimated = state["estimated_probability"]
    swarm_consensus = state.get("swarm_consensus", estimated)
    swarm_confidence = state.get("swarm_confidence", 0.0)
    selected = state.get("selected_market", {})
    volume = float(selected.get("volume", 0) or 0)

    blend_weight = min(0.5, swarm_confidence * 0.6)
    final_prob = (1 - blend_weight) * estimated + blend_weight * swarm_consensus

    scorecard = score_market(
        true_prob=final_prob,
        implied_prob=implied,
        volume=volume,
        min_edge=config.MIN_EDGE,
        min_volume=config.MIN_VOLUME,
        min_kelly=config.MIN_KELLY,
    )

    market_id = selected.get("id", "")
    side = "YES" if final_prob > 0.5 else "NO"

    recommendation = {
        "action": scorecard["action"],
        "market_id": market_id,
        "market_question": selected.get("question", ""),
        "side": side,
        "swarm_consensus": swarm_consensus,
        "swarm_confidence": swarm_confidence,
        **scorecard,
    }

    logger.info(
        "decision_node: %s | edge=%.1f%% | EV=%.3f | kelly=%.1f%% | "
        "swarm=%.3f (conf=%.2f) | market='%s'",
        scorecard["action"],
        scorecard["edge"] * 100,
        scorecard["expected_value"],
        scorecard["kelly_fraction"] * 100,
        swarm_consensus,
        swarm_confidence,
        selected.get("question", "?")[:40],
    )

    if market_id:
        memory.store_analytics(
            market_id=market_id,
            estimated_prob=final_prob,
            edge=scorecard["edge"],
            action=scorecard["action"],
        )

    return {
        "edge": scorecard["edge"],
        "expected_value": scorecard["expected_value"],
        "kelly_fraction": scorecard["kelly_fraction"],
        "recommendation": recommendation,
    }


def trade_node(state: PlanningState) -> dict:
    """Build a LIVE order when the decision is BET."""
    rec = state.get("recommendation", {})
    if rec.get("action") != "BET":
        logger.info("trade_node: skipping (action=%s)", rec.get("action", "NONE"))
        return {"trade_result": {"skipped": True, "reason": rec.get("action", "NO_REC")}}

    selected = state.get("selected_market", {})
    if not selected:
        return {"trade_result": {"skipped": True, "reason": "no_selected_market"}}

    token_ids = selected.get("clob_token_ids", [])
    if isinstance(token_ids, str):
        try:
            token_ids = json.loads(token_ids) if token_ids else []
        except (json.JSONDecodeError, ValueError):
            token_ids = []

    side = rec.get("side", "YES")
    token_id = token_ids[0] if side == "YES" and token_ids else (
        token_ids[1] if side == "NO" and len(token_ids) > 1 else None
    )

    if not token_id:
        return {"trade_result": {"skipped": True, "reason": "no_token_id"}}

    try:
        from src.connectors.polymarket import PolymarketConnector

        kelly = state.get("kelly_fraction", 0.0)
        implied = state.get("implied_probability", 0.5)

        connector = PolymarketConnector()
        try:
            balance = connector.get_usdc_balance()
        except Exception:
            logger.warning("trade_node: could not fetch USDC balance, using notional $100")
            balance = 100.0
        half_kelly = kelly / 2.0
        size = max(1.0, round(balance * min(half_kelly, 0.05), 2))
        result = connector.build_order(
            token_id=token_id,
            price=implied,
            size=size,
            side="BUY",
        )

        dry = "LIVE" if not result.get("dry_run") else "DRY RUN"
        logger.info("trade_node: %s order built for '%s'", dry, selected.get("question", "?")[:40])
        return {"trade_result": result}

    except Exception as exc:
        logger.warning("trade_node: order failed: %s", exc)
        return {"trade_result": {"error": str(exc)}}


# ── graph ──────────────────────────────────────────────────────────────────

@register_graph("planning_agent")
def create_planning_agent():
    g = StateGraph(PlanningState)
    g.add_node("research", research_node)
    g.add_node("ontology", ontology_node)
    g.add_node("stats", stats_node)
    g.add_node("probability", probability_node)
    g.add_node("swarm", swarm_node)
    g.add_node("decision", decision_node)
    g.add_node("trade", trade_node)

    g.set_entry_point("research")
    g.add_edge("research", "ontology")
    g.add_edge("ontology", "stats")
    g.add_edge("stats", "probability")
    g.add_edge("probability", "swarm")
    g.add_edge("swarm", "decision")
    g.add_edge("decision", "trade")
    g.add_edge("trade", END)

    return g.compile()


# ── CLI entry point ────────────────────────────────────────────────────────

if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) or "Will Bitcoin hit $100k by end of 2025?"
    agent = create_planning_agent()
    result = agent.invoke(
        {"query": query, "messages": [HumanMessage(content=query)]},
        config={"recursion_limit": 15},
    )
    rec = result.get("recommendation", {})
    print(f"\n=== Recommendation: {rec.get('action')} ===")
    print(f"  Side:   {rec.get('side')}")
    print(f"  Edge:   {rec.get('edge', 0):.1%}")
    print(f"  EV:     {rec.get('expected_value', 0):.3f}")
    print(f"  Kelly:  {rec.get('kelly_fraction', 0):.1%}")
    print(f"  Swarm:  {rec.get('swarm_consensus', 0):.3f} (conf={rec.get('swarm_confidence', 0):.2f})")

    trade = result.get("trade_result", {})
    if trade and not trade.get("skipped"):
        dry = "DRY RUN" if trade.get("dry_run") else "LIVE"
        print(f"  Trade:  [{dry}] {trade.get('side', '')} @ {trade.get('price', '')}")
