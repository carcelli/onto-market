"""Import cycle detector.

Finds all directed cycles in the module import graph produced by
:func:`import_graph.build_graph`.

A cycle ``A → B → C → A`` means those three modules are mutually dependent
and cannot be imported in isolation.  In practice even a two-module cycle
(``A ↔ B``) complicates refactoring and can mask subtle import-time errors.

Results are grouped first by strongly-connected components (fast) and then
enumerated as individual simple cycles (precise but potentially slow on very
large graphs — safe up to ~200-node graphs which is well above this repo's
footprint).
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

import networkx as nx

from ._paths import resolve_output_path, resolve_repo_root
from .import_graph import build_graph


@dataclass
class CycleSnapshot:
    root: Path
    modules_scanned: int = 0
    cycles_found: int = 0
    # Strongly-connected components with more than one node
    scc_groups: list[list[str]] = field(default_factory=list)
    # Every individual simple cycle (list of module names forming the loop)
    simple_cycles: list[list[str]] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Core analysis
# ---------------------------------------------------------------------------


def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:
    """Detect cycles in a pre-built import graph."""
    # SCCs with >1 node indicate mutual dependencies
    sccs = [
        sorted(component)
        for component in nx.strongly_connected_components(g)
        if len(component) > 1
    ]
    sccs.sort(key=len, reverse=True)

    # Simple cycles — exact enumeration
    simple = [sorted(cycle) for cycle in nx.simple_cycles(g)]
    simple.sort(key=len)

    return CycleSnapshot(
        root=root,
        modules_scanned=g.number_of_nodes(),
        cycles_found=len(simple),
        scc_groups=sccs,
        simple_cycles=simple,
    )


def analyze(root: str | Path | None = None) -> CycleSnapshot:
    repo_root = resolve_repo_root(root)
    g = build_graph(repo_root)
    return analyze_from_graph(g, repo_root)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def _verdict(snapshot: CycleSnapshot) -> str:
    if snapshot.cycles_found == 0:
        return "✅ No import cycles detected — dependency graph is a DAG."
    return (
        f"⚠ {snapshot.cycles_found} cycle(s) found across "
        f"{len(snapshot.scc_groups)} strongly-connected component(s). "
        "Resolve before adding concurrent agents."
    )


def render_markdown(snapshot: CycleSnapshot) -> str:
    lines: list[str] = []
    lines.append("# Cycle Detector Report\n")
    lines.append(f"- Repo root: `{snapshot.root}`")
    lines.append(f"- Modules scanned: **{snapshot.modules_scanned}**")
    lines.append(f"- Simple cycles found: **{snapshot.cycles_found}**")
    lines.append(f"- Strongly-connected components (>1 node): **{len(snapshot.scc_groups)}**\n")
    lines.append(f"**{_verdict(snapshot)}**\n")

    if snapshot.scc_groups:
        lines.append("## Strongly-connected components")
        for i, group in enumerate(snapshot.scc_groups, 1):
            lines.append(f"\n### SCC {i} ({len(group)} modules)")
            for mod in group:
                lines.append(f"- `{mod}`")
        lines.append("")

    if snapshot.simple_cycles:
        lines.append("## All simple cycles")
        for i, cycle in enumerate(snapshot.simple_cycles, 1):
            chain = " → ".join(f"`{m}`" for m in cycle) + f" → `{cycle[0]}`"
            lines.append(f"{i}. {chain}")
        lines.append("")

    return "\n".join(lines)


def write_report(
    snapshot: CycleSnapshot,
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "cycles.json"
    md_path = output_dir / "cycles.md"

    payload = {
        "root": str(snapshot.root),
        "modules_scanned": snapshot.modules_scanned,
        "cycles_found": snapshot.cycles_found,
        "scc_groups": snapshot.scc_groups,
        "simple_cycles": snapshot.simple_cycles,
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


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Detect import cycles in the onto_market package"
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
