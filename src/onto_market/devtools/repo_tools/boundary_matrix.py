"""Domain boundary coupling matrix.

Groups every module in the import graph by its *domain* (the second component
of the ``onto_market.<domain>.*`` path) and builds an NxN coupling table that
shows how many directed import edges cross from domain A into domain B.

A dense off-diagonal cell means those two domains are tightly coupled, which
is useful context before a refactor or packaging cleanup.

Uses :func:`import_graph.build_graph` as its sole data source so that parsing
happens exactly once per invocation.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

import networkx as nx

from ._paths import resolve_output_path, resolve_repo_root
from .import_graph import PACKAGE_NAME, build_graph

# Canonical domain order for matrix display — lower index = more foundational.
DOMAIN_ORDER = [
    "config",
    "utils",
    "core",
    "polymarket_agents",
    "connectors",
    "memory",
    "ontology",
    "swarm",
    "trading",
    "agents",
    "context",
    "devtools",
]


def _domain(module: str) -> str:
    """Extract the top-level domain label from a fully-qualified module name."""
    parts = module.split(".")
    if parts[0] == PACKAGE_NAME:
        return parts[1] if len(parts) >= 2 else "_root"
    return parts[0]


def _all_domains(g: nx.DiGraph) -> list[str]:
    """Return domains present in *g*, sorted by DOMAIN_ORDER then alphabetically."""
    present = {_domain(n) for n in g.nodes()}
    ordered = [d for d in DOMAIN_ORDER if d in present]
    extras = sorted(present - set(DOMAIN_ORDER))
    return ordered + extras


@dataclass
class BoundaryMatrixSnapshot:
    root: Path
    domains: list[str] = field(default_factory=list)
    matrix: dict[str, dict[str, int]] = field(default_factory=dict)
    top_couplings: list[tuple[str, str, int]] = field(default_factory=list)
    boundaries_checked: int = 0


def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:
    """Derive the boundary matrix from a pre-built import graph."""
    domains = _all_domains(g)

    matrix: dict[str, dict[str, int]] = {d: defaultdict(int) for d in domains}  # type: ignore[arg-type]

    edge_count = 0
    for src, dst in g.edges():
        sd, dd = _domain(src), _domain(dst)
        if sd != dd:
            matrix.setdefault(sd, defaultdict(int))[dd] += 1  # type: ignore[arg-type]
            edge_count += 1

    plain_matrix = {sd: dict(counts) for sd, counts in matrix.items()}

    top: list[tuple[str, str, int]] = []
    for sd, row in plain_matrix.items():
        for dd, count in row.items():
            if count:
                top.append((sd, dd, count))
    top.sort(key=lambda t: t[2], reverse=True)

    return BoundaryMatrixSnapshot(
        root=root,
        domains=domains,
        matrix=plain_matrix,
        top_couplings=top[:20],
        boundaries_checked=edge_count,
    )


def analyze(root: str | Path | None = None) -> BoundaryMatrixSnapshot:
    repo_root = resolve_repo_root(root)
    g = build_graph(repo_root)
    return analyze_from_graph(g, repo_root)


def render_markdown(snapshot: BoundaryMatrixSnapshot) -> str:
    lines: list[str] = []
    lines.append("# Boundary Matrix Report\n")
    lines.append(f"- Repo root: `{snapshot.root}`")
    lines.append(f"- Cross-boundary import edges: **{snapshot.boundaries_checked}**\n")

    lines.append("## Top cross-domain couplings")
    lines.append("| From domain | To domain | Edge count |")
    lines.append("|-------------|-----------|-----------|")
    for src, dst, count in snapshot.top_couplings:
        lines.append(f"| `{src}` | `{dst}` | {count} |")
    lines.append("")

    domains = snapshot.domains
    if domains:
        lines.append("## Full coupling matrix (rows import from columns)")
        header = "| Domain | " + " | ".join(f"`{d}`" for d in domains) + " |"
        sep = "|--------|" + "|".join("---" for _ in domains) + "|"
        lines.append(header)
        lines.append(sep)
        for sd in domains:
            row_vals = [str(snapshot.matrix.get(sd, {}).get(dd, 0)) for dd in domains]
            lines.append(f"| `{sd}` | " + " | ".join(row_vals) + " |")
        lines.append("")

    return "\n".join(lines)


def write_report(
    snapshot: BoundaryMatrixSnapshot,
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "boundary_matrix.json"
    md_path = output_dir / "boundary_matrix.md"

    payload = {
        "root": str(snapshot.root),
        "domains": snapshot.domains,
        "matrix": snapshot.matrix,
        "top_couplings": snapshot.top_couplings,
        "boundaries_checked": snapshot.boundaries_checked,
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(snapshot), encoding="utf-8")
    return json_path, md_path


def run(
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    snapshot = analyze(root=root)
    return write_report(snapshot, root=root, reports_dir=reports_dir)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Show cross-domain import coupling for onto_market"
    )
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
