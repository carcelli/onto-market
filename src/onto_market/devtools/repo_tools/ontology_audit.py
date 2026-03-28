from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Sequence

from ._paths import resolve_repo_root

DEFAULT_PATH = resolve_repo_root() / "data" / "ontology.json"


def _load_nx():
    try:
        import networkx as nx

        return nx
    except ImportError:
        print("❌ networkx not installed. Run: pip install networkx", file=sys.stderr)
        raise SystemExit(1) from None


def _load_graph(nx, path: Path):
    if not path.exists():
        print(f"Ontology file not found: {path}")
        print("Run: python main.py 'any query' to generate it.")
        raise SystemExit(0)

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        edges_key = "links" if "links" in data else "edges"
        graph = nx.node_link_graph(data, directed=True, multigraph=False, edges=edges_key)
        print(f"Loaded ontology from {path}")
        return graph
    except Exception as exc:
        print(f"Failed to load ontology: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


def _load_ontology_graph_class(root: Path):
    from onto_market.ontology.graph import OntologyGraph

    return OntologyGraph


def _section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


def audit(
    path: Path = DEFAULT_PATH,
    min_confidence: float = 0.3,
    stale_days: int = 14,
    prune: bool = False,
    top_n: int = 10,
) -> None:
    nx = _load_nx()
    graph = _load_graph(nx, path)
    root = resolve_repo_root(path.parent.parent)

    _section("1. BASIC STATS")
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    density = nx.density(graph)
    components = nx.number_weakly_connected_components(graph)
    isolates = list(nx.isolates(graph))

    print(f"  Nodes         : {num_nodes}")
    print(f"  Edges         : {num_edges}")
    print(f"  Density       : {density:.4f}")
    print(f"  Components    : {components}")
    print(f"  Isolate nodes : {len(isolates)}")
    if isolates:
        print(f"  Isolates      : {', '.join(isolates[:8])}")

    _section("2. PAGERANK — High-Influence Entities")
    if num_nodes < 2:
        print("  Not enough nodes for PageRank")
    else:
        try:
            pagerank = nx.pagerank(graph, weight="confidence")
        except Exception:
            try:
                pagerank = nx.pagerank(graph, weight="confidence", backend="networkx")
            except Exception:
                pagerank = {node: 1.0 / num_nodes for node in graph.nodes()}
                print("  (scipy unavailable — showing uniform PageRank)")

        ranked = sorted(pagerank.items(), key=lambda item: -item[1])[:top_n]
        print(f"  {'Entity':<35} {'PageRank':>10}  {'Degree':>8}")
        print(f"  {'─' * 35} {'─' * 10}  {'─' * 8}")
        for entity, score in ranked:
            print(f"  {entity:<35} {score:>10.4f}  {graph.degree(entity):>8}")

    _section("2b. BETWEENNESS CENTRALITY — Bridge Entities")
    if num_nodes < 3:
        print("  Not enough nodes for betweenness centrality")
    else:
        betweenness = nx.betweenness_centrality(graph)
        ranked = sorted(betweenness.items(), key=lambda item: -item[1])[:top_n]
        print(f"  {'Entity':<35} {'Betweenness':>12}  {'Degree':>8}")
        print(f"  {'─' * 35} {'─' * 12}  {'─' * 8}")
        for entity, score in ranked:
            print(f"  {entity:<35} {score:>12.4f}  {graph.degree(entity):>8}")

    _section("2c. DEGREE DISTRIBUTION")
    degrees = [degree for _, degree in graph.degree()]
    if degrees:
        in_degrees = [degree for _, degree in graph.in_degree()]
        out_degrees = [degree for _, degree in graph.out_degree()]
        mean_degree = sum(degrees) / len(degrees)
        sorted_degrees = sorted(degrees)
        median_degree = sorted_degrees[len(sorted_degrees) // 2]

        print(f"  Mean degree   : {mean_degree:.2f}")
        print(f"  Median degree : {median_degree}")
        print(f"  Max degree    : {max(degrees)}")
        print(f"  Max in-degree : {max(in_degrees)}")
        print(f"  Max out-degree: {max(out_degrees)}")

        sinks = [
            (node, graph.in_degree(node), graph.out_degree(node))
            for node in graph.nodes()
            if graph.in_degree(node) > 0 and graph.out_degree(node) == 0
        ]
        if sinks:
            print(f"\n  Terminal sinks (referenced but not connected outward): {len(sinks)}")
            for node, in_degree, out_degree in sorted(sinks, key=lambda item: -item[1])[:5]:
                print(f"    {node:<35}  in={in_degree}  out={out_degree}")

        roots = [
            (node, graph.in_degree(node), graph.out_degree(node))
            for node in graph.nodes()
            if graph.out_degree(node) > 0 and graph.in_degree(node) == 0
        ]
        if roots:
            print(f"\n  Root causes (influence others but not explained): {len(roots)}")
            for node, in_degree, out_degree in sorted(roots, key=lambda item: -item[2])[:5]:
                print(f"    {node:<35}  in={in_degree}  out={out_degree}")
    else:
        print("  No nodes found")

    _section("3. CONFIDENCE DISTRIBUTION")
    confidences = [edge.get("confidence", 0.0) for _, _, edge in graph.edges(data=True)]
    if not confidences:
        print("  ⚠ No edges found")
    else:
        buckets = {"[0.0–0.3)": 0, "[0.3–0.5)": 0, "[0.5–0.7)": 0, "[0.7–1.0]": 0}
        for confidence in confidences:
            if confidence < 0.3:
                buckets["[0.0–0.3)"] += 1
            elif confidence < 0.5:
                buckets["[0.3–0.5)"] += 1
            elif confidence < 0.7:
                buckets["[0.5–0.7)"] += 1
            else:
                buckets["[0.7–1.0]"] += 1

        total = len(confidences)
        mean_confidence = sum(confidences) / total
        low_confidence_pct = (buckets["[0.0–0.3)"] / total) * 100

        print(f"  Total edges  : {total}")
        print(f"  Mean conf    : {mean_confidence:.3f}")
        for bucket, count in buckets.items():
            bar = "█" * int(count / max(total, 1) * 30)
            print(f"  {bucket}  {count:>4}  {bar}")
        if low_confidence_pct > 20:
            print(f"\n  ⚠ {low_confidence_pct:.0f}% of edges have confidence < 0.3 — consider pruning")
        else:
            print(f"\n  ✅ Confidence distribution looks healthy (low-conf: {low_confidence_pct:.0f}%)")

    _section("4. PREDICATE VOCABULARY DISCIPLINE")
    valid_predicates = {
        "influences",
        "related_to",
        "contradicts",
        "predicts",
        "caused_by",
        "involves",
        "supports",
        "opposes",
        "correlates_with",
    }
    predicate_counts: dict[str, int] = {}
    for _, _, edge in graph.edges(data=True):
        predicate = edge.get("predicate", "unknown")
        predicate_counts[predicate] = predicate_counts.get(predicate, 0) + 1

    for predicate, count in sorted(predicate_counts.items(), key=lambda item: -item[1]):
        marker = "✅" if predicate in valid_predicates else "❌ OUT-OF-VOCAB"
        print(f"  {predicate:<20} {count:>4}  {marker}")

    out_of_vocab = [predicate for predicate in predicate_counts if predicate not in valid_predicates]
    if out_of_vocab:
        print(f"\n  ⚠ Out-of-vocab predicates: {out_of_vocab}")
        print("    → These will be normalized to 'related_to' on next add_triple()")
    else:
        print("\n  ✅ All predicates are within controlled vocabulary")

    _section(f"5. STALE NODES (not updated in {stale_days} days)")
    stale_cutoff = time.time() - stale_days * 86400
    stale_nodes: list[tuple[str, float]] = []
    for node, node_data in graph.nodes(data=True):
        last_seen = node_data.get("last_seen", node_data.get("first_seen", 0))
        if last_seen and last_seen < stale_cutoff:
            stale_nodes.append((node, last_seen))

    if not stale_nodes:
        print(f"  ✅ No stale nodes (all updated within {stale_days} days)")
    else:
        from datetime import datetime, timezone

        print(f"  ⚠ {len(stale_nodes)} stale node(s):")
        for node, timestamp in sorted(stale_nodes, key=lambda item: item[1])[:top_n]:
            age_days = (time.time() - timestamp) / 86400
            formatted = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y-%m-%d")
            print(f"  {node:<35}  last seen {formatted} ({age_days:.0f}d ago)")

    _section(f"6. PRUNING RECOMMENDATION (threshold={min_confidence})")
    to_prune = [
        (source, target, edge.get("confidence", 0))
        for source, target, edge in graph.edges(data=True)
        if edge.get("confidence", 0) < min_confidence
    ]
    print(f"  Edges to prune : {len(to_prune)} / {num_edges}")

    if to_prune and prune:
        ontology_graph_cls = _load_ontology_graph_class(root)
        ontology_graph = ontology_graph_cls(str(path))
        removed = ontology_graph.prune(min_confidence=min_confidence)
        ontology_graph._save()
        print(f"  ✅ Pruned {removed} edges and orphan nodes — graph saved")
    elif to_prune:
        print("  → Run with --prune to apply (removes edges + orphan nodes)")
    else:
        print(f"  ✅ No edges below confidence threshold {min_confidence}")

    _section("SUMMARY")
    issues: list[str] = []
    if isolates:
        issues.append(f"{len(isolates)} isolate nodes")
    if out_of_vocab:
        issues.append(f"{len(out_of_vocab)} out-of-vocab predicates")
    if confidences and (sum(1 for confidence in confidences if confidence < 0.3) / len(confidences)) > 0.2:
        issues.append(">20% low-confidence edges")
    if stale_nodes:
        issues.append(f"{len(stale_nodes)} stale nodes")

    if issues:
        print(f"  ⚠ Issues found: {' | '.join(issues)}")
        print("  → Recommended: audit-ontology --prune + review stale nodes")
    else:
        print("  ✅ Ontology graph is healthy")

    print()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="onto-market ontology audit")
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH, help=f"Path to ontology JSON (default: {DEFAULT_PATH})")
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.3,
        help="Confidence threshold for pruning (default: 0.3)",
    )
    parser.add_argument(
        "--stale-days",
        type=int,
        default=14,
        help="Days after which a node is considered stale (default: 14)",
    )
    parser.add_argument("--prune", action="store_true", help="Apply pruning to the live ontology.json")
    parser.add_argument("--top-n", type=int, default=10, help="How many top entities/edges to show (default: 10)")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    audit(
        path=args.path,
        min_confidence=args.min_confidence,
        stale_days=args.stale_days,
        prune=args.prune,
        top_n=args.top_n,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
