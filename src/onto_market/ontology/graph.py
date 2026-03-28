"""
Ontology knowledge graph for onto-market.

Stores semantic triples (subject, predicate, object) as a NetworkX directed
graph with confidence-weighted edges.  Persists to JSON — no external service
required.  Zep Cloud integration is a drop-in replacement in Phase 2.

Triple schema
-------------
  subject   : short noun phrase  ("bitcoin price", "fed interest rate")
  predicate : relation verb      ("influences", "predicts", "contradicts", ...)
  obj       : short noun phrase  ("btc market", "inflation")
  confidence: float 0-1
  source    : agent or connector that produced this fact
"""
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import networkx as nx

# Closed predicate vocabulary — keeps the graph queryable and consistent
PREDICATES = frozenset({
    "influences",
    "related_to",
    "contradicts",
    "predicts",
    "caused_by",
    "involves",
    "supports",
    "opposes",
    "correlates_with",
})


@dataclass
class Triple:
    subject: str
    predicate: str
    obj: str                    # "object" is a Python builtin
    confidence: float = 0.7
    source: str = ""
    timestamp: float = field(default_factory=time.time)

    def __post_init__(self) -> None:
        if self.predicate not in PREDICATES:
            self.predicate = "related_to"
        self.confidence = max(0.0, min(1.0, self.confidence))


class OntologyGraph:
    """
    Semantic knowledge graph.

    Nodes  — entities (noun phrases): stored with degree-weighted confidence.
    Edges  — directed relations: subject -[predicate]-> object.

    Multiple triples between the same pair merge: max confidence wins, all
    predicates are recorded so the edge is labelled with the strongest one.
    """

    def __init__(self, persist_path: str = "data/ontology.json"):
        self.g: nx.DiGraph = nx.DiGraph()
        self.persist_path = Path(persist_path)
        self._load()

    # ── write ──────────────────────────────────────────────────────────────

    def add_triple(self, triple: Triple) -> None:
        """Upsert a triple into the graph."""
        # Ensure both nodes exist
        for node in (triple.subject, triple.obj):
            if node not in self.g:
                self.g.add_node(node, sources=[], first_seen=triple.timestamp)
            sources: list = self.g.nodes[node].get("sources", [])
            if triple.source and triple.source not in sources:
                sources.append(triple.source)
            self.g.nodes[node]["sources"] = sources
            self.g.nodes[node]["last_seen"] = triple.timestamp

        # Upsert edge
        if self.g.has_edge(triple.subject, triple.obj):
            edge = self.g[triple.subject][triple.obj]
            edge["confidence"] = max(edge["confidence"], triple.confidence)
            predicates: set = set(edge.get("predicates", [edge["predicate"]]))
            predicates.add(triple.predicate)
            edge["predicates"] = sorted(predicates)
            # Dominant predicate = highest-confidence one recorded first
            edge["predicate"] = edge["predicates"][0]
        else:
            self.g.add_edge(
                triple.subject,
                triple.obj,
                predicate=triple.predicate,
                predicates=[triple.predicate],
                confidence=triple.confidence,
                source=triple.source,
                timestamp=triple.timestamp,
            )

    def add_triples(self, triples: list[Triple], persist: bool = True) -> None:
        for t in triples:
            self.add_triple(t)
        if persist:
            self._save()

    def prune(self, min_confidence: float = 0.3) -> int:
        """Remove low-confidence edges; return count removed."""
        to_remove = [
            (u, v)
            for u, v, d in self.g.edges(data=True)
            if d.get("confidence", 0) < min_confidence
        ]
        self.g.remove_edges_from(to_remove)
        # Remove orphan nodes
        isolates = list(nx.isolates(self.g))
        self.g.remove_nodes_from(isolates)
        self._save()
        return len(to_remove)

    # ── read ──────────────────────────────────────────────────────────────

    def context_for(self, query: str, top_n: int = 15) -> str:
        """
        Return a formatted string of known facts most relevant to `query`.
        Matches on token overlap — no embedding needed.
        """
        tokens = {t.lower() for t in query.split() if len(t) > 3}
        if not tokens:
            return ""

        # Find seed nodes whose name overlaps with query tokens
        seeds = [
            n for n in self.g.nodes
            if any(tok in n.lower() for tok in tokens)
        ]
        if not seeds:
            return ""

        facts: list[tuple[float, str]] = []
        for seed in seeds[:6]:
            for _, tgt, d in self.g.out_edges(seed, data=True):
                pred = d.get("predicate", "related_to")
                conf = d.get("confidence", 0.5)
                facts.append((conf, f"{seed} {pred} {tgt}  [conf={conf:.2f}]"))

            for src, _, d in self.g.in_edges(seed, data=True):
                pred = d.get("predicate", "related_to")
                conf = d.get("confidence", 0.5)
                facts.append((conf, f"{src} {pred} {seed}  [conf={conf:.2f}]"))

        seen: set[str] = set()
        lines: list[str] = []
        for _, fact in sorted(facts, key=lambda x: -x[0]):
            if fact not in seen:
                seen.add(fact)
                lines.append(fact)
            if len(lines) >= top_n:
                break

        return "\n".join(lines)

    def get_entity(self, name: str) -> dict[str, Any] | None:
        """Return node metadata dict or None."""
        if name not in self.g:
            return None
        return dict(self.g.nodes[name])

    def stats(self) -> dict:
        degrees = sorted(self.g.degree(), key=lambda x: -x[1])
        return {
            "nodes": self.g.number_of_nodes(),
            "edges": self.g.number_of_edges(),
            "top_entities": [(n, d) for n, d in degrees[:10]],
        }

    # ── persistence ────────────────────────────────────────────────────────

    def _save(self) -> None:
        self.persist_path.parent.mkdir(parents=True, exist_ok=True)
        # node_link_data is the canonical nx JSON format
        data = nx.node_link_data(self.g, edges="links")
        self.persist_path.write_text(json.dumps(data, default=str), encoding="utf-8")

    def _load(self) -> None:
        if not self.persist_path.exists():
            return
        try:
            data = json.loads(self.persist_path.read_text(encoding="utf-8"))
            self.g = nx.node_link_graph(data, directed=True, multigraph=False, edges="links")
        except Exception:
            self.g = nx.DiGraph()  # corrupt file → start fresh
