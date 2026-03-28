#!/usr/bin/env python3
"""
audit_ontology.py — Ontology knowledge graph health check.

Runs the following analyses on data/ontology.json:
  1. Basic stats (nodes, edges, density, components)
  2. PageRank — surface high-influence entities
  3. Confidence distribution — flag low-confidence edges
  4. Predicate frequency — check vocabulary discipline
  5. Stale node detection — nodes not updated in N days
  6. Pruning recommendation — edges below threshold

Usage:
    python scripts/audit_ontology.py
    python scripts/audit_ontology.py --min-confidence 0.4 --stale-days 30
    python scripts/audit_ontology.py --prune  # writes pruned graph back to disk

Output: console report (rich table if installed, plain text fallback).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
DEFAULT_PATH = ROOT / "data" / "ontology.json"

# Add repo root to sys.path so we can import OntologyGraph if needed
sys.path.insert(0, str(ROOT))


def _load_nx():
    try:
        import networkx as nx
        return nx
    except ImportError:
        print("❌ networkx not installed. Run: pip install networkx", file=sys.stderr)
        sys.exit(1)


def _try_rich():
    try:
        from rich.console import Console
        from rich.table import Table
        return Console(), Table
    except ImportError:
        return None, None


def _load_graph(nx, path: Path):
    if not path.exists():
        print(f"Ontology file not found: {path}")
        print("Run: python main.py 'any query' to generate it.")
        sys.exit(0)

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        # Detect key name: OntologyGraph._save uses edges="links" but older
        # data may use "edges" (the networkx default).
        edges_key = "links" if "links" in data else "edges"
        g = nx.node_link_graph(data, directed=True, multigraph=False, edges=edges_key)
        print(f"Loaded ontology from {path}")
        return g, data
    except Exception as exc:
        print(f"Failed to load ontology: {exc}", file=sys.stderr)
        sys.exit(1)


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
    g, raw_data = _load_graph(nx, path)
    console, RichTable = _try_rich()

    # ── 1. Basic stats ──────────────────────────────────────────────────────
    _section("1. BASIC STATS")
    num_nodes = g.number_of_nodes()
    num_edges = g.number_of_edges()
    density = nx.density(g)
    components = nx.number_weakly_connected_components(g)
    isolates = list(nx.isolates(g))

    print(f"  Nodes         : {num_nodes}")
    print(f"  Edges         : {num_edges}")
    print(f"  Density       : {density:.4f}")
    print(f"  Components    : {components}")
    print(f"  Isolate nodes : {len(isolates)}")
    if isolates:
        print(f"  Isolates      : {', '.join(isolates[:8])}")

    # ── 2. PageRank ─────────────────────────────────────────────────────────
    _section("2. PAGERANK — High-Influence Entities")
    if num_nodes < 2:
        print("  Not enough nodes for PageRank")
    else:
        try:
            pr = nx.pagerank(g, weight="confidence")
        except Exception:
            # scipy not installed — fall back to power iteration
            try:
                pr = nx.pagerank(g, weight="confidence", backend="networkx")
            except Exception:
                pr = {n: 1.0 / num_nodes for n in g.nodes()}
                print("  (scipy unavailable — showing uniform PageRank)")
        ranked = sorted(pr.items(), key=lambda x: -x[1])[:top_n]
        print(f"  {'Entity':<35} {'PageRank':>10}  {'Degree':>8}")
        print(f"  {'─'*35} {'─'*10}  {'─'*8}")
        for entity, score in ranked:
            deg = g.degree(entity)
            print(f"  {entity:<35} {score:>10.4f}  {deg:>8}")

    # ── 2b. Betweenness centrality ─────────────────────────────────────────
    _section("2b. BETWEENNESS CENTRALITY — Bridge Entities")
    if num_nodes < 3:
        print("  Not enough nodes for betweenness centrality")
    else:
        bc = nx.betweenness_centrality(g)
        bc_ranked = sorted(bc.items(), key=lambda x: -x[1])[:top_n]
        print(f"  {'Entity':<35} {'Betweenness':>12}  {'Degree':>8}")
        print(f"  {'─'*35} {'─'*12}  {'─'*8}")
        for entity, score in bc_ranked:
            deg = g.degree(entity)
            print(f"  {entity:<35} {score:>12.4f}  {deg:>8}")

    # ── 2c. Degree distribution ──────────────────────────────────────────────
    _section("2c. DEGREE DISTRIBUTION")
    degrees = [d for _, d in g.degree()]
    if degrees:
        in_degrees = [d for _, d in g.in_degree()]
        out_degrees = [d for _, d in g.out_degree()]
        mean_deg = sum(degrees) / len(degrees)
        sorted_deg = sorted(degrees)
        median_deg = sorted_deg[len(sorted_deg) // 2]
        print(f"  Mean degree   : {mean_deg:.2f}")
        print(f"  Median degree : {median_deg}")
        print(f"  Max degree    : {max(degrees)}")
        print(f"  Max in-degree : {max(in_degrees)}")
        print(f"  Max out-degree: {max(out_degrees)}")

        # Terminal sinks (high in-degree, low out-degree)
        sinks = [(n, g.in_degree(n), g.out_degree(n)) for n in g.nodes()
                 if g.in_degree(n) > 0 and g.out_degree(n) == 0]
        if sinks:
            print(f"\n  Terminal sinks (referenced but not connected outward): {len(sinks)}")
            for n, ind, outd in sorted(sinks, key=lambda x: -x[1])[:5]:
                print(f"    {n:<35}  in={ind}  out={outd}")

        # Root causes (high out-degree, low in-degree)
        roots = [(n, g.in_degree(n), g.out_degree(n)) for n in g.nodes()
                 if g.out_degree(n) > 0 and g.in_degree(n) == 0]
        if roots:
            print(f"\n  Root causes (influence others but not explained): {len(roots)}")
            for n, ind, outd in sorted(roots, key=lambda x: -x[2])[:5]:
                print(f"    {n:<35}  in={ind}  out={outd}")
    else:
        print("  No nodes found")

    # ── 3. Confidence distribution ──────────────────────────────────────────
    _section("3. CONFIDENCE DISTRIBUTION")
    confidences = [d.get("confidence", 0.0) for _, _, d in g.edges(data=True)]
    if not confidences:
        print("  ⚠ No edges found")
    else:
        buckets = {"[0.0–0.3)": 0, "[0.3–0.5)": 0, "[0.5–0.7)": 0, "[0.7–1.0]": 0}
        for c in confidences:
            if c < 0.3:
                buckets["[0.0–0.3)"] += 1
            elif c < 0.5:
                buckets["[0.3–0.5)"] += 1
            elif c < 0.7:
                buckets["[0.5–0.7)"] += 1
            else:
                buckets["[0.7–1.0]"] += 1
        total = len(confidences)
        mean_conf = sum(confidences) / total
        low_pct = (buckets["[0.0–0.3)"] / total) * 100

        print(f"  Total edges  : {total}")
        print(f"  Mean conf    : {mean_conf:.3f}")
        for bucket, count in buckets.items():
            bar = "█" * int(count / max(total, 1) * 30)
            print(f"  {bucket}  {count:>4}  {bar}")
        if low_pct > 20:
            print(f"\n  ⚠ {low_pct:.0f}% of edges have confidence < 0.3 — consider pruning")
        else:
            print(f"\n  ✅ Confidence distribution looks healthy (low-conf: {low_pct:.0f}%)")

    # ── 4. Predicate vocabulary ──────────────────────────────────────────────
    _section("4. PREDICATE VOCABULARY DISCIPLINE")
    VALID_PREDICATES = {
        "influences", "related_to", "contradicts", "predicts",
        "caused_by", "involves", "supports", "opposes", "correlates_with",
    }
    pred_counts: dict[str, int] = {}
    for _, _, d in g.edges(data=True):
        p = d.get("predicate", "unknown")
        pred_counts[p] = pred_counts.get(p, 0) + 1

    for pred, count in sorted(pred_counts.items(), key=lambda x: -x[1]):
        valid_marker = "✅" if pred in VALID_PREDICATES else "❌ OUT-OF-VOCAB"
        print(f"  {pred:<20} {count:>4}  {valid_marker}")

    out_of_vocab = [p for p in pred_counts if p not in VALID_PREDICATES]
    if out_of_vocab:
        print(f"\n  ⚠ Out-of-vocab predicates: {out_of_vocab}")
        print("    → These will be normalized to 'related_to' on next add_triple()")
    else:
        print("\n  ✅ All predicates are within controlled vocabulary")

    # ── 5. Stale nodes ───────────────────────────────────────────────────────
    _section(f"5. STALE NODES (not updated in {stale_days} days)")
    stale_cutoff = time.time() - stale_days * 86400
    stale_nodes: list[tuple[str, float]] = []
    for node, data in g.nodes(data=True):
        last_seen = data.get("last_seen", data.get("first_seen", 0))
        if last_seen and last_seen < stale_cutoff:
            stale_nodes.append((node, last_seen))

    if not stale_nodes:
        print(f"  ✅ No stale nodes (all updated within {stale_days} days)")
    else:
        print(f"  ⚠ {len(stale_nodes)} stale node(s):")
        from datetime import datetime, timezone
        for node, ts in sorted(stale_nodes, key=lambda x: x[1])[:top_n]:
            age_days = (time.time() - ts) / 86400
            dt = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
            print(f"  {node:<35}  last seen {dt} ({age_days:.0f}d ago)")

    # ── 6. Pruning recommendation ────────────────────────────────────────────
    _section(f"6. PRUNING RECOMMENDATION (threshold={min_confidence})")
    to_prune = [
        (u, v, d.get("confidence", 0))
        for u, v, d in g.edges(data=True)
        if d.get("confidence", 0) < min_confidence
    ]
    print(f"  Edges to prune : {len(to_prune)} / {num_edges}")

    if to_prune and prune:
        from ontology.graph import OntologyGraph
        og = OntologyGraph(str(path))
        removed = og.prune(min_confidence=min_confidence)
        og._save()
        print(f"  ✅ Pruned {removed} edges and orphan nodes — graph saved")
    elif to_prune:
        print("  → Run with --prune to apply (removes edges + orphan nodes)")
    else:
        print(f"  ✅ No edges below confidence threshold {min_confidence}")

    # ── Summary ──────────────────────────────────────────────────────────────
    _section("SUMMARY")
    issues = []
    if len(isolates) > 0:
        issues.append(f"{len(isolates)} isolate nodes")
    if out_of_vocab:
        issues.append(f"{len(out_of_vocab)} out-of-vocab predicates")
    if confidences and (sum(1 for c in confidences if c < 0.3) / len(confidences)) > 0.2:
        issues.append(">20% low-confidence edges")
    if len(stale_nodes) > 0:
        issues.append(f"{len(stale_nodes)} stale nodes")

    if issues:
        print(f"  ⚠ Issues found: {' | '.join(issues)}")
        print("  → Recommended: python scripts/audit_ontology.py --prune + review stale nodes")
    else:
        print("  ✅ Ontology graph is healthy")

    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="onto-market ontology audit")
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH,
                        help=f"Path to ontology JSON (default: {DEFAULT_PATH.relative_to(ROOT)})")
    parser.add_argument("--min-confidence", type=float, default=0.3,
                        help="Confidence threshold for pruning (default: 0.3)")
    parser.add_argument("--stale-days", type=int, default=14,
                        help="Days after which a node is considered stale (default: 14)")
    parser.add_argument("--prune", action="store_true",
                        help="Apply pruning to the live ontology.json")
    parser.add_argument("--top-n", type=int, default=10,
                        help="How many top entities/edges to show (default: 10)")
    args = parser.parse_args()

    audit(
        path=args.path,
        min_confidence=args.min_confidence,
        stale_days=args.stale_days,
        prune=args.prune,
        top_n=args.top_n,
    )
