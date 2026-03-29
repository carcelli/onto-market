"""
Ontology Agent - LangGraph node that sits between research and stats.

Responsibilities
----------------
1. Extract semantic triples from the research context via LLM (rich path).
2. Extract structural triples from market metadata cheaply (no LLM cost).
3. Ingest both into the shared OntologyGraph (persisted to disk).
4. Decompose hub entities when they accumulate enough edges.
5. Query the graph for what is already known about the current query.
6. Return `ontology_context` — a ranked list of prior facts — which the
   probability_node uses to sharpen its estimate.

Data flow: every planning_agent run now feeds the ontology from TWO paths:
  - LLM extraction (up to 20 triples from research text + descriptions)
  - Structural extraction (tags, categories, entity co-occurrence — zero LLM cost)
"""
from onto_market.ontology.graph import OntologyGraph, Triple
from onto_market.ontology.enricher import (
    from_market_metadata,
    from_market_pairs,
    decompose_hub_entities,
)
from onto_market.utils.llm_client import LLMClient
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)
llm = LLMClient()

# Shared singleton — all agents in the process share one graph
onto = OntologyGraph()

_EXTRACT_SYSTEM = """\
You are a knowledge-graph builder for a prediction market research system.

Given a market query and research text, extract the most useful semantic
triples that help forecast the market outcome.  Be granular — decompose
broad concepts into specific sub-entities when the text supports it.

Rules:
- Subject and object must be SHORT noun phrases (2-5 words, lowercase).
- Predicate must be one of: influences, related_to, contradicts, predicts,
  caused_by, involves, supports, opposes, correlates_with
- Only include triples with confidence >= 0.5.
- Return up to 20 triples — prefer more fine-grained triples over fewer
  coarse ones (e.g. "fed rate cut" over just "fed policy").
- Include cross-entity relationships when the text implies them.

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
                llm.user(f"Market query: {query}\n\nResearch text:\n{text[:4000]}"),
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

    # ── Step 1a: LLM extraction (rich path) ───────────────────────────────
    # Include descriptions from market data for richer context
    market_lines: list[str] = []
    for m in market_data[:10]:
        q = m.get("question", "")
        desc = m.get("description", "")
        if q:
            market_lines.append(q)
        if desc and len(desc) > 20:
            market_lines.append(desc[:300])

    combined = f"{research_context}\n\n" + "\n".join(market_lines)
    combined = combined.strip()

    llm_triples = _extract_triples(combined, query=query, source="planning_agent")
    if llm_triples:
        onto.add_triples(llm_triples, persist=False)
        logger.info("ontology_node: LLM extracted %d triples", len(llm_triples))

    # ── Step 1b: structural extraction (cheap path, no LLM) ──────────────
    struct_triples = from_market_metadata(market_data, source="market_metadata")
    pair_triples = from_market_pairs(market_data, source="market_pairs")
    cheap_triples = struct_triples + pair_triples

    if cheap_triples:
        onto.add_triples(cheap_triples, persist=False)
        logger.info("ontology_node: structural extraction added %d triples "
                     "(metadata=%d, pairs=%d)",
                     len(cheap_triples), len(struct_triples), len(pair_triples))

    # ── Step 1c: decompose hub entities if they've grown ──────────────────
    decomp_triples = decompose_hub_entities(onto, min_degree=5)
    if decomp_triples:
        onto.add_triples(decomp_triples, persist=False)
        logger.info("ontology_node: decomposed hubs → %d new triples", len(decomp_triples))

    # Persist once after all enrichment
    total = len(llm_triples) + len(cheap_triples) + len(decomp_triples)
    if total > 0:
        onto._save()
        logger.info(
            "ontology_node: persisted %d total new triples  "
            "(graph now %d nodes, %d edges)",
            total, onto.g.number_of_nodes(), onto.g.number_of_edges(),
        )

    # ── Step 2: query graph for prior knowledge on this query ─────────────
    ontology_context = onto.context_for(query)
    if ontology_context:
        lines = ontology_context.count("\n") + 1
        logger.info("ontology_node: returning %d prior facts from graph", lines)
    else:
        logger.info("ontology_node: graph has no prior knowledge for this query yet")

    return {"ontology_context": ontology_context}
