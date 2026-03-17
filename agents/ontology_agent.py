"""
Ontology Agent - LangGraph node that sits between research and stats.

Responsibilities
----------------
1. Extract semantic triples from the research context via LLM.
2. Ingest those triples into the shared OntologyGraph (persisted to disk).
3. Query the graph for what is already known about the current query.
4. Return `ontology_context` — a ranked list of prior facts — which the
   probability_node uses to sharpen its estimate.

The LLM call is optional: if no key is configured the node still returns
whatever the graph already contains from previous runs.
"""
from ontology.graph import OntologyGraph, Triple
from src.utils.llm_client import LLMClient
from src.utils.logger import get_logger

logger = get_logger(__name__)
llm = LLMClient()

# Shared singleton — all agents in the process share one graph
onto = OntologyGraph()

_EXTRACT_SYSTEM = """\
You are a knowledge-graph builder for a prediction market research system.

Given a market query and research text, extract the most useful semantic
triples that help forecast the market outcome.

Rules:
- Subject and object must be SHORT noun phrases (2-5 words, lowercase).
- Predicate must be one of: influences, related_to, contradicts, predicts,
  caused_by, involves, supports, opposes, correlates_with
- Only include triples with confidence >= 0.5.
- Return at most 12 triples.

Respond ONLY with valid JSON:
{"triples": [{"subject": "...", "predicate": "...", "object": "...", "confidence": 0.0-1.0}]}
"""


def _extract_triples(text: str, query: str, source: str) -> list[Triple]:
    """Call the LLM to extract triples. Returns [] on any failure."""
    if not text.strip():
        return []
    try:
        result = llm.chat_json(
            [
                llm.system(_EXTRACT_SYSTEM),
                llm.user(f"Market query: {query}\n\nResearch text:\n{text[:2500]}"),
            ],
            temperature=0.1,
        )
    except Exception as exc:
        logger.debug("ontology triple extraction skipped: %s", exc)
        return []

    triples: list[Triple] = []
    for raw in result.get("triples", []):
        try:
            triples.append(
                Triple(
                    subject=str(raw["subject"]).lower().strip(),
                    predicate=str(raw["predicate"]).lower().strip(),
                    obj=str(raw["object"]).lower().strip(),
                    confidence=float(raw.get("confidence", 0.7)),
                    source=source,
                )
            )
        except (KeyError, ValueError, TypeError):
            continue

    return triples


def ontology_node(state: dict) -> dict:
    """
    LangGraph node.  Accepts any state dict that contains:
      - query: str
      - research_context: str  (from research_node)
      - market_data: list[dict]

    Returns:
      - ontology_context: str  (structured prior knowledge for probability_node)
    """
    query = state.get("query", "")
    research_context = state.get("research_context", "")
    market_data = state.get("market_data", [])

    # Build combined text: web/news research + market question titles
    market_text = "\n".join(
        m.get("question", "") for m in market_data[:5] if m.get("question")
    )
    combined = f"{research_context}\n\n{market_text}".strip()

    # --- Step 1: extract new triples and ingest --------------------------------
    triples = _extract_triples(combined, query=query, source="planning_agent")
    if triples:
        onto.add_triples(triples, persist=True)
        logger.info(
            "ontology_node: ingested %d triples  (graph now %d nodes, %d edges)",
            len(triples),
            onto.g.number_of_nodes(),
            onto.g.number_of_edges(),
        )
    else:
        logger.info("ontology_node: no new triples (LLM unavailable or no context)")

    # --- Step 2: query graph for prior knowledge on this query ----------------
    ontology_context = onto.context_for(query)
    if ontology_context:
        lines = ontology_context.count("\n") + 1
        logger.info("ontology_node: returning %d prior facts from graph", lines)
    else:
        logger.info("ontology_node: graph has no prior knowledge for this query yet")

    return {"ontology_context": ontology_context}
