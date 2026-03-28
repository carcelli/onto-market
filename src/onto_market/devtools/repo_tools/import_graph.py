"""Intra-package import graph builder for onto_market.

Walks every .py file in the package, parses each with :mod:`ast` to extract
import statements, resolves relative imports to their absolute equivalents, and
returns a :class:`networkx.DiGraph` whose nodes are fully-qualified module names
and whose edges represent "A imports B".

All other repo-cartography tools (boundary_matrix, cycle_detector,
architecture_drift) call :func:`build_graph` here rather than re-parsing.
"""

from __future__ import annotations

import argparse
import ast
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

import networkx as nx

from ._paths import resolve_output_path, resolve_repo_root

PACKAGE_NAME = "onto_market"

_SKIP_DIRS: frozenset[str] = frozenset(
    {
        "__pycache__",
        ".git",
        ".mypy_cache",
        ".pytest_cache",
        "node_modules",
        ".venv",
        "venv",
        "dist",
        "build",
        ".ruff_cache",
    }
)


def _should_skip(path: Path) -> bool:
    return any(part in _SKIP_DIRS for part in path.parts)


def _find_package_dir(repo_root: Path) -> Path:
    candidate = repo_root / "src" / PACKAGE_NAME
    if candidate.is_dir():
        return candidate
    for init in repo_root.rglob(f"{PACKAGE_NAME}/__init__.py"):
        if not _should_skip(init):
            return init.parent
    raise RuntimeError(
        f"Cannot locate the '{PACKAGE_NAME}' package directory under {repo_root}"
    )


def _path_to_module(py_file: Path, package_dir: Path) -> str:
    """Convert an absolute .py path to a dotted module name.

    ``src/onto_market/agents/__init__.py`` -> ``onto_market.agents``
    ``src/onto_market/agents/state.py``    -> ``onto_market.agents.state``
    """
    rel = py_file.relative_to(package_dir.parent)
    parts = list(rel.with_suffix("").parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _resolve_relative(module: str | None, level: int, current: str) -> str | None:
    parts = current.split(".")
    anchor = parts[:-level] if level <= len(parts) else []
    if module:
        return ".".join(anchor + module.split("."))
    return ".".join(anchor) if anchor else None


def _extract_candidates(py_file: Path, current_module: str) -> list[str]:
    try:
        source = py_file.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(source, filename=str(py_file))
    except SyntaxError:
        return []

    pkg = PACKAGE_NAME
    results: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                if name == pkg or name.startswith(pkg + "."):
                    results.append(name)

        elif isinstance(node, ast.ImportFrom):
            if node.level == 0:
                mod = node.module or ""
                if mod == pkg or mod.startswith(pkg + "."):
                    results.append(mod)
                    for alias in node.names:
                        if alias.name != "*":
                            results.append(f"{mod}.{alias.name}")
            else:
                resolved = _resolve_relative(node.module, node.level, current_module)
                if resolved and (resolved == pkg or resolved.startswith(pkg + ".")):
                    results.append(resolved)
                    for alias in node.names:
                        if alias.name != "*":
                            results.append(f"{resolved}.{alias.name}")

    return results


# ---------------------------------------------------------------------------
# Public graph builder — single source of truth used by all downstream tools
# ---------------------------------------------------------------------------


def build_graph(root: str | Path | None = None) -> nx.DiGraph:
    """Parse every .py file under the package; return a module dependency DiGraph.

    Nodes  - fully-qualified module names (``onto_market.agents.state``)
    Edges  - (A, B) means module A imports module B
    """
    repo_root = resolve_repo_root(root)
    package_dir = _find_package_dir(repo_root)

    all_modules: dict[str, Path] = {}
    for py_file in sorted(package_dir.rglob("*.py")):
        if _should_skip(py_file):
            continue
        mod = _path_to_module(py_file, package_dir)
        all_modules[mod] = py_file

    g: nx.DiGraph = nx.DiGraph()
    g.add_nodes_from(all_modules.keys())

    for mod, py_file in all_modules.items():
        seen: set[str] = set()
        for target in _extract_candidates(py_file, mod):
            if target in all_modules and target != mod and target not in seen:
                g.add_edge(mod, target)
                seen.add(target)

    return g


# ---------------------------------------------------------------------------
# Snapshot + analysis
# ---------------------------------------------------------------------------


@dataclass
class ImportGraphSnapshot:
    root: Path
    modules_scanned: int = 0
    edges: int = 0
    cycles: int = 0
    isolated: int = 0
    top_importers: list[tuple[str, int]] = field(default_factory=list)
    top_imported: list[tuple[str, int]] = field(default_factory=list)
    adjacency: dict[str, list[str]] = field(default_factory=dict)


def analyze(root: str | Path | None = None) -> tuple[ImportGraphSnapshot, nx.DiGraph]:
    repo_root = resolve_repo_root(root)
    g = build_graph(repo_root)

    cycles = list(nx.simple_cycles(g))
    isolated = [n for n in g.nodes() if g.degree(n) == 0]
    out_deg = sorted(g.out_degree(), key=lambda x: x[1], reverse=True)
    in_deg = sorted(g.in_degree(), key=lambda x: x[1], reverse=True)

    snapshot = ImportGraphSnapshot(
        root=repo_root,
        modules_scanned=g.number_of_nodes(),
        edges=g.number_of_edges(),
        cycles=len(cycles),
        isolated=len(isolated),
        top_importers=[(m, d) for m, d in out_deg[:12] if d > 0],
        top_imported=[(m, d) for m, d in in_deg[:12] if d > 0],
        adjacency={n: sorted(g.successors(n)) for n in sorted(g.nodes())},
    )
    return snapshot, g


# ---------------------------------------------------------------------------
# Rendering + I/O
# ---------------------------------------------------------------------------


def render_markdown(snapshot: ImportGraphSnapshot) -> str:
    lines: list[str] = []
    lines.append("# Import Graph Report\n")
    lines.append(f"- Repo root: `{snapshot.root}`")
    lines.append(f"- Modules scanned: **{snapshot.modules_scanned}**")
    lines.append(f"- Import edges: **{snapshot.edges}**")
    lines.append(f"- Isolated modules (no imports): **{snapshot.isolated}**")
    lines.append(f"- Cycles detected: **{snapshot.cycles}**\n")

    lines.append("## Top importers (highest out-degree)")
    lines.append("| Module | Imports |")
    lines.append("|--------|---------|")
    for mod, deg in snapshot.top_importers:
        lines.append(f"| `{mod}` | {deg} |")
    lines.append("")

    lines.append("## Most imported (highest in-degree)")
    lines.append("| Module | Imported by |")
    lines.append("|--------|------------|")
    for mod, deg in snapshot.top_imported:
        lines.append(f"| `{mod}` | {deg} |")
    lines.append("")

    lines.append("## Adjacency list")
    for mod, deps in sorted(snapshot.adjacency.items()):
        if deps:
            lines.append(f"\n### `{mod}`")
            for dep in deps:
                lines.append(f"- `{dep}`")

    return "\n".join(lines)


def write_report(
    snapshot: ImportGraphSnapshot,
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "import_graph.json"
    md_path = output_dir / "import_graph.md"

    payload = {
        "root": str(snapshot.root),
        "modules_scanned": snapshot.modules_scanned,
        "edges": snapshot.edges,
        "cycles": snapshot.cycles,
        "isolated": snapshot.isolated,
        "top_importers": snapshot.top_importers,
        "top_imported": snapshot.top_imported,
        "adjacency": snapshot.adjacency,
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(snapshot), encoding="utf-8")
    return json_path, md_path


def run(
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    snapshot, _ = analyze(root=root)
    return write_report(snapshot, root=root, reports_dir=reports_dir)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze the onto_market module import graph"
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
