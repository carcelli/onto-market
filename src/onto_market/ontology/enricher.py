"""
Multi-source ontology enrichment — turn every data signal into graph triples.

Instead of a single LLM extraction bottleneck, the enricher offers four
*cheap* (no-LLM) extraction paths and one *rich* (LLM) path:

Cheap (heuristic):
    from_market_metadata   — tags, categories, cross-market correlations
    from_ml_features       — feature importance → "X influences outcome"
    from_resolved_outcome  — ground truth confirms/refutes existing edges
    from_market_pair       — shared tags/events → correlates_with edges

Rich (LLM):
    from_text              — enhanced triple extraction with entity decomposition

The planning agent's ontology_node uses the rich path once per query.
Everything else hooks in via cheap paths, so the graph densifies on every
data refresh, training run, and market resolution — with zero LLM cost.
"""
from __future__ import annotations

import math
import re
import time
from collections import Counter
from itertools import combinations
from typing import Any

from onto_market.ontology.graph import OntologyGraph, Triple, PREDICATES
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)

_STOPWORDS = frozenset({
    "the", "a", "an", "is", "are", "was", "were", "will", "be", "been",
    "have", "has", "had", "do", "does", "did", "can", "could", "should",
    "would", "may", "might", "shall", "this", "that", "these", "those",
    "what", "which", "who", "whom", "how", "when", "where", "why",
    "and", "or", "but", "not", "no", "yes", "if", "then", "than",
    "of", "in", "on", "at", "to", "for", "with", "by", "from", "as",
    "into", "about", "between", "through", "before", "after", "above",
    "below", "over", "under", "it", "its", "they", "their", "them",
    "he", "she", "his", "her", "we", "our", "us", "you", "your",
    "my", "me", "i", "so", "up", "down", "out", "off", "more", "most",
    "very", "just", "also", "any", "each", "all", "some", "many",
})


def _normalize(text: str) -> str:
    """Lowercase, strip, collapse whitespace."""
    return re.sub(r"\s+", " ", text.lower().strip())


def _noun_phrase(text: str, max_words: int = 5) -> str:
    """Extract a short noun phrase — strip stopwords from edges."""
    words = _normalize(text).split()
    while words and words[0] in _STOPWORDS:
        words = words[1:]
    while words and words[-1] in _STOPWORDS:
        words = words[:-1]
    return " ".join(words[:max_words]) if words else text.lower().strip()


def _extract_entities_from_question(question: str) -> list[str]:
    """Pull candidate entity phrases from a market question string.

    Uses simple heuristics: quoted strings, capitalized phrases, known
    patterns like dollar amounts, percentages, dates.
    """
    entities: list[str] = []

    # Quoted strings
    for m in re.finditer(r'"([^"]{2,40})"', question):
        entities.append(_noun_phrase(m.group(1)))
    for m in re.finditer(r"'([^']{2,40})'", question):
        entities.append(_noun_phrase(m.group(1)))

    # Dollar amounts / percentages / numerical milestones
    for m in re.finditer(r"\$[\d,.]+[kmbt]?", question, re.IGNORECASE):
        entities.append(m.group(0).lower())
    for m in re.finditer(r"\d+(?:\.\d+)?%", question):
        entities.append(m.group(0))

    # Capitalized multi-word phrases (proper nouns)
    for m in re.finditer(r"(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)", question):
        entities.append(_noun_phrase(m.group(0)))

    # Known entity patterns: "X by <date>", "X before <date>"
    for m in re.finditer(r"([\w\s]+?)\s+(?:by|before|after)\s+([\w\s,]+\d{4})", question, re.IGNORECASE):
        entities.append(_noun_phrase(m.group(1)))
        entities.append(_noun_phrase(m.group(2)))

    # Single capitalized words that aren't at sentence start (likely proper nouns)
    words = question.split()
    for i, w in enumerate(words):
        if i > 0 and w[0:1].isupper() and w.lower() not in _STOPWORDS and len(w) > 2:
            entities.append(w.lower())

    return list(dict.fromkeys(e for e in entities if len(e) > 1))


# ── Cheap enrichment: market metadata ─────────────────────────────────────


def from_market_metadata(
    markets: list[dict[str, Any]],
    source: str = "market_metadata",
) -> list[Triple]:
    """Extract triples from market tags, categories, and question text.

    No LLM call — purely structural extraction.  Each market yields:
      - <entity> involves <tag>       for each tag
      - <entity> related_to <category>
      - question-entity relationships (predicts, involves)
    """
    triples: list[Triple] = []
    now = time.time()

    for mkt in markets:
        question = mkt.get("question", "")
        if not question:
            continue

        q_entity = _noun_phrase(question, max_words=6)
        tags = mkt.get("tags", [])
        category = mkt.get("category", "")
        description = mkt.get("description", "")

        # Tags → involves edges
        if isinstance(tags, list):
            for tag in tags:
                tag_str = tag if isinstance(tag, str) else str(tag)
                tag_norm = _noun_phrase(tag_str)
                if tag_norm and tag_norm != q_entity:
                    triples.append(Triple(
                        subject=q_entity,
                        predicate="involves",
                        obj=tag_norm,
                        confidence=0.7,
                        source=source,
                        timestamp=now,
                    ))

        # Category → related_to edge
        if category:
            cat_norm = _noun_phrase(category)
            if cat_norm and cat_norm != q_entity:
                triples.append(Triple(
                    subject=q_entity,
                    predicate="related_to",
                    obj=cat_norm,
                    confidence=0.6,
                    source=source,
                    timestamp=now,
                ))

        # Question entity extraction → sub-entity relationships
        entities = _extract_entities_from_question(question)
        for ent in entities[:8]:
            if ent != q_entity and len(ent) > 2:
                triples.append(Triple(
                    subject=q_entity,
                    predicate="involves",
                    obj=ent,
                    confidence=0.65,
                    source=source,
                    timestamp=now,
                ))

    logger.info("enricher.from_market_metadata: extracted %d triples from %d markets",
                len(triples), len(markets))
    return triples


# ── Cheap enrichment: cross-market correlations ───────────────────────────


def from_market_pairs(
    markets: list[dict[str, Any]],
    source: str = "market_pairs",
    min_shared_tags: int = 1,
) -> list[Triple]:
    """Detect correlates_with edges between markets sharing tags/events.

    Markets in the same event or sharing tags get a correlation edge, with
    confidence proportional to overlap.
    """
    triples: list[Triple] = []
    now = time.time()

    # Group by event
    event_groups: dict[str, list[str]] = {}
    for mkt in markets:
        eid = mkt.get("event_id", "")
        q = _noun_phrase(mkt.get("question", ""), max_words=6)
        if eid and q:
            event_groups.setdefault(eid, []).append(q)

    for eid, entities in event_groups.items():
        for a, b in combinations(set(entities), 2):
            triples.append(Triple(
                subject=a, predicate="correlates_with", obj=b,
                confidence=0.8, source=source, timestamp=now,
            ))

    # Tag overlap between pairs (sample at most 200 pairs)
    tagged = [(mkt, set(mkt.get("tags", []) if isinstance(mkt.get("tags"), list) else []))
              for mkt in markets if mkt.get("tags")]
    for i, (m1, t1) in enumerate(tagged[:20]):
        for m2, t2 in tagged[i + 1:20]:
            shared = t1 & t2
            if len(shared) >= min_shared_tags:
                q1 = _noun_phrase(m1.get("question", ""), max_words=6)
                q2 = _noun_phrase(m2.get("question", ""), max_words=6)
                if q1 and q2 and q1 != q2:
                    conf = min(0.9, 0.5 + 0.1 * len(shared))
                    triples.append(Triple(
                        subject=q1, predicate="correlates_with", obj=q2,
                        confidence=conf, source=source, timestamp=now,
                    ))

    logger.info("enricher.from_market_pairs: extracted %d correlation triples", len(triples))
    return triples


# ── Cheap enrichment: ML feature importance ───────────────────────────────


_FEATURE_SEMANTICS: dict[str, tuple[str, str]] = {
    "implied_prob":   ("market implied probability", "predicts"),
    "log_volume":     ("trading volume",             "influences"),
    "log_liquidity":  ("market liquidity",           "influences"),
    "days_to_end":    ("time to resolution",         "influences"),
    "tag_count":      ("topic diversity",            "correlates_with"),
    "category_enc":   ("market category",            "related_to"),
}


def from_ml_features(
    metadata: dict[str, Any],
    source: str = "ml_training",
) -> list[Triple]:
    """Convert ML artifact metadata into ontology triples.

    Maps feature importance (from model metadata) into semantic triples:
      - "<feature_concept> influences resolution_outcome" with confidence
        proportional to normalized feature importance.
      - Bag-of-words features → "<word> involves market_prediction"
    """
    triples: list[Triple] = []
    now = time.time()

    feature_names: list[str] = metadata.get("feature_names", [])
    importances: list[float] | None = metadata.get("feature_importances")
    brier: float | None = metadata.get("brier")

    # Model performance → meta-triple
    if brier is not None:
        model_class = metadata.get("model_class", "ml model")
        conf = max(0.5, 1.0 - brier)  # lower brier = higher confidence
        triples.append(Triple(
            subject=model_class.lower(),
            predicate="predicts",
            obj="market outcome",
            confidence=round(conf, 2),
            source=source,
            timestamp=now,
        ))

    if not feature_names:
        return triples

    # If we have explicit importances, use them; otherwise derive from names
    if importances and len(importances) == len(feature_names):
        imp_max = max(abs(v) for v in importances) or 1.0
        for name, imp in zip(feature_names, importances):
            norm_imp = abs(imp) / imp_max
            if norm_imp < 0.05:
                continue
            _add_feature_triple(triples, name, norm_imp, source, now)
    else:
        for name in feature_names:
            _add_feature_triple(triples, name, 0.5, source, now)

    logger.info("enricher.from_ml_features: extracted %d triples from ML metadata", len(triples))
    return triples


def _add_feature_triple(
    triples: list[Triple], name: str, importance: float,
    source: str, now: float,
) -> None:
    """Map a single feature name to a semantic triple."""
    if name.startswith("bow_"):
        word = name[4:]
        if word not in _STOPWORDS and len(word) > 2:
            triples.append(Triple(
                subject=word,
                predicate="involves",
                obj="market prediction",
                confidence=round(0.5 + importance * 0.3, 2),
                source=source,
                timestamp=now,
            ))
        return

    semantic = _FEATURE_SEMANTICS.get(name)
    if semantic:
        concept, predicate = semantic
        triples.append(Triple(
            subject=concept,
            predicate=predicate,
            obj="resolution outcome",
            confidence=round(0.5 + importance * 0.4, 2),
            source=source,
            timestamp=now,
        ))


# ── Cheap enrichment: resolved market outcomes ────────────────────────────


def from_resolved_outcome(
    market: dict[str, Any],
    onto: OntologyGraph,
    source: str = "resolution",
) -> list[Triple]:
    """Generate triples from a resolved market, strengthening or weakening
    existing graph edges based on ground truth.

    If the market resolved YES and the graph had a `predicts` edge pointing
    at something related, that edge's confidence gets a boost.  If it
    resolved NO, a `contradicts` edge is added (or existing `supports`
    edges are weakened).
    """
    triples: list[Triple] = []
    now = time.time()

    question = market.get("question", "")
    resolved_yes = bool(market.get("resolved_yes", market.get("outcome") == "YES"))
    q_entity = _noun_phrase(question, max_words=6)

    if not q_entity:
        return triples

    # Ground truth triple
    outcome_label = "confirmed outcome" if resolved_yes else "rejected outcome"
    triples.append(Triple(
        subject=q_entity,
        predicate="supports" if resolved_yes else "contradicts",
        obj=outcome_label,
        confidence=0.95,
        source=source,
        timestamp=now,
    ))

    # Reinforce or weaken existing edges that touch this entity
    for _, tgt, data in onto.g.out_edges(q_entity, data=True):
        pred = data.get("predicate", "related_to")
        old_conf = data.get("confidence", 0.5)
        if resolved_yes and pred in ("predicts", "supports"):
            boost = min(1.0, old_conf + 0.1)
            triples.append(Triple(
                subject=q_entity, predicate=pred, obj=tgt,
                confidence=boost, source=source, timestamp=now,
            ))
        elif not resolved_yes and pred in ("predicts", "supports"):
            weakened = max(0.1, old_conf - 0.15)
            triples.append(Triple(
                subject=q_entity, predicate="contradicts", obj=tgt,
                confidence=weakened, source=source, timestamp=now,
            ))

    for src, _, data in onto.g.in_edges(q_entity, data=True):
        pred = data.get("predicate", "related_to")
        old_conf = data.get("confidence", 0.5)
        if resolved_yes and pred in ("predicts", "supports", "influences"):
            boost = min(1.0, old_conf + 0.1)
            triples.append(Triple(
                subject=src, predicate=pred, obj=q_entity,
                confidence=boost, source=source, timestamp=now,
            ))

    logger.info("enricher.from_resolved_outcome: %s → %d triples (resolved_yes=%s)",
                q_entity[:30], len(triples), resolved_yes)
    return triples


# ── Entity decomposition ──────────────────────────────────────────────────


def decompose_hub_entities(
    onto: OntologyGraph,
    min_degree: int = 5,
    source: str = "decomposition",
) -> list[Triple]:
    """When a node gets too connected, decompose it into sub-entities.

    Looks at the predicates on a hub's edges and creates sub-entities by
    grouping edges by predicate type:
      - bitcoin (degree 8) → "bitcoin price", "bitcoin regulation",
        "bitcoin market sentiment"

    This is a heuristic decomposition — the LLM-based enrichment in
    ontology_agent.py can refine these later.
    """
    triples: list[Triple] = []
    now = time.time()

    for node, degree in list(onto.g.degree()):
        if degree < min_degree:
            continue

        pred_groups: dict[str, list[str]] = {}
        for _, tgt, data in onto.g.out_edges(node, data=True):
            pred = data.get("predicate", "related_to")
            pred_groups.setdefault(pred, []).append(tgt)
        for src, _, data in onto.g.in_edges(node, data=True):
            pred = data.get("predicate", "related_to")
            pred_groups.setdefault(pred, []).append(src)

        _PRED_FACETS = {
            "influences":      "drivers",
            "predicts":        "forecast",
            "correlates_with": "correlations",
            "contradicts":     "risks",
            "opposes":         "opposition",
            "supports":        "support",
            "involves":        "context",
        }

        for pred, neighbors in pred_groups.items():
            if len(neighbors) < 2:
                continue
            facet = _PRED_FACETS.get(pred, pred)
            sub_entity = f"{node} {facet}"
            # Parent → sub-entity
            triples.append(Triple(
                subject=node, predicate="related_to", obj=sub_entity,
                confidence=0.8, source=source, timestamp=now,
            ))
            # Sub-entity → each neighbor
            for nb in neighbors[:6]:
                triples.append(Triple(
                    subject=sub_entity, predicate=pred, obj=nb,
                    confidence=0.7, source=source, timestamp=now,
                ))

    if triples:
        logger.info("enricher.decompose_hub_entities: decomposed %d hub nodes into %d triples",
                     sum(1 for n, d in onto.g.degree() if d >= min_degree), len(triples))
    return triples


# ── Batch enrichment orchestrator ─────────────────────────────────────────


def enrich_from_all_sources(
    onto: OntologyGraph,
    markets: list[dict[str, Any]] | None = None,
    ml_metadata: dict[str, Any] | None = None,
    resolved_markets: list[dict[str, Any]] | None = None,
    decompose: bool = True,
    persist: bool = True,
) -> dict[str, int]:
    """Run all cheap enrichment paths and ingest into the graph.

    Returns a summary dict with triple counts per source.
    """
    summary: dict[str, int] = {}
    all_triples: list[Triple] = []

    if markets:
        meta_triples = from_market_metadata(markets)
        pair_triples = from_market_pairs(markets)
        all_triples.extend(meta_triples)
        all_triples.extend(pair_triples)
        summary["market_metadata"] = len(meta_triples)
        summary["market_pairs"] = len(pair_triples)

    if ml_metadata:
        ml_triples = from_ml_features(ml_metadata)
        all_triples.extend(ml_triples)
        summary["ml_features"] = len(ml_triples)

    if resolved_markets:
        res_count = 0
        for mkt in resolved_markets:
            res_triples = from_resolved_outcome(mkt, onto)
            all_triples.extend(res_triples)
            res_count += len(res_triples)
        summary["resolved_outcomes"] = res_count

    if all_triples:
        onto.add_triples(all_triples, persist=persist)

    if decompose:
        decomp_triples = decompose_hub_entities(onto)
        if decomp_triples:
            onto.add_triples(decomp_triples, persist=persist)
            summary["decomposition"] = len(decomp_triples)

    total = sum(summary.values())
    logger.info("enricher.enrich_from_all_sources: ingested %d total triples — %s", total, summary)
    summary["total"] = total
    return summary
