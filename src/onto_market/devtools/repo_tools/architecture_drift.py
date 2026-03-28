"""Architecture drift auditor.

Compares the actual import graph against a set of *allowed dependency rules*
and reports every edge that violates the intended layering.

## Intended layer order (lower = more foundational; higher may import lower)

    config            ← leaf; imports nothing inside the package
    utils             ← config only
    core              ← config, utils
    polymarket_agents ← config, utils, core
    connectors        ← config, utils, core
    memory            ← config, utils, core, polymarket_agents
    ontology          ← config, utils, core
    swarm             ← config, utils, core
    trading           ← config, utils, core, connectors, memory, polymarket_agents
    agents            ← everything above
    context           ← config, utils, core, connectors, memory
    devtools          ← everything (meta / observability layer)

Any import from a *lower* layer into a *higher* layer (e.g. ``config`` →
``agents``, or ``connectors`` → ``swarm``) is a **violation**.

The rules can be extended without touching any other module.
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

PACKAGE_NAME = "onto_market"

# ---------------------------------------------------------------------------
# Policy definition
# ---------------------------------------------------------------------------

#: Map of domain → set of domains it is ALLOWED to import from.
#: Any intra-package edge not listed here is a violation.
ALLOWED_IMPORTS: dict[str, frozenset[str]] = {
    "config": frozenset(),
    "utils": frozenset({"config"}),
    "core": frozenset({"config", "utils"}),
    "polymarket_agents": frozenset({"config", "utils", "core"}),
    "connectors": frozenset({"config", "utils", "core"}),
    "memory": frozenset({"config", "utils", "core", "polymarket_agents"}),
    "ontology": frozenset({"config", "utils", "core"}),
    "swarm": frozenset({"config", "utils", "core"}),
    "trading": frozenset(
        {"config", "utils", "core", "connectors", "memory", "polymarket_agents"}
    ),
    "agents": frozenset(
        {
            "config",
            "utils",
            "core",
            "connectors",
            "memory",
            "ontology",
            "swarm",
            "trading",
            "polymarket_agents",
        }
    ),
    "context": frozenset({"config", "utils", "core", "connectors", "memory"}),
    # main is the CLI entry point — may invoke agents, ontology, and config
    "main": frozenset({"config", "utils", "core", "agents", "ontology"}),
    # devtools / tests may inspect anything — no intra-package restrictions
    "devtools": frozenset(
        {
            "config",
            "utils",
            "core",
            "connectors",
            "memory",
            "ontology",
            "swarm",
            "trading",
            "polymarket_agents",
            "agents",
            "context",
        }
    ),
}


def _domain(module: str) -> str:
    parts = module.split(".")
    if parts[0] == PACKAGE_NAME:
        return parts[1] if len(parts) >= 2 else "_root"
    return parts[0]


# ---------------------------------------------------------------------------
# Violation dataclass + analysis
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Violation:
    src_module: str
    dst_module: str
    src_domain: str
    dst_domain: str
    reason: str


@dataclass
class ArchitectureDriftSnapshot:
    root: Path
    modules_scanned: int = 0
    edges_checked: int = 0
    violations_found: int = 0
    violations: list[Violation] = field(default_factory=list)
    # domains present in the graph but not in ALLOWED_IMPORTS (unknown layer)
    unknown_domains: list[str] = field(default_factory=list)


def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:
    """Check every edge in *g* against the layer policy."""
    violations: list[Violation] = []
    unknown: set[str] = set()

    for src, dst in g.edges():
        sd = _domain(src)
        dd = _domain(dst)

        if sd == dd:
            continue  # intra-domain edges are always fine

        allowed_for_src = ALLOWED_IMPORTS.get(sd)
        if allowed_for_src is None:
            unknown.add(sd)
            continue  # skip uncatalogued domains

        if dd not in allowed_for_src:
            violations.append(
                Violation(
                    src_module=src,
                    dst_module=dst,
                    src_domain=sd,
                    dst_domain=dd,
                    reason=(
                        f"'{sd}' is not permitted to import from '{dd}' "
                        f"under the current layering policy"
                    ),
                )
            )

    # Sort: severity-first (same domain pairs together), then alphabetically
    violations.sort(key=lambda v: (v.src_domain, v.dst_domain, v.src_module))

    return ArchitectureDriftSnapshot(
        root=root,
        modules_scanned=g.number_of_nodes(),
        edges_checked=g.number_of_edges(),
        violations_found=len(violations),
        violations=violations,
        unknown_domains=sorted(unknown),
    )


def analyze(root: str | Path | None = None) -> ArchitectureDriftSnapshot:
    repo_root = resolve_repo_root(root)
    g = build_graph(repo_root)
    return analyze_from_graph(g, repo_root)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def _verdict(snapshot: ArchitectureDriftSnapshot) -> str:
    if snapshot.violations_found == 0:
        return "✅ No architecture violations — import graph conforms to the layer policy."
    return (
        f"⚠ {snapshot.violations_found} violation(s) found. "
        "Each represents an import that crosses a forbidden layer boundary."
    )


def render_markdown(snapshot: ArchitectureDriftSnapshot) -> str:
    lines: list[str] = []
    lines.append("# Architecture Drift Report\n")
    lines.append(f"- Repo root: `{snapshot.root}`")
    lines.append(f"- Modules scanned: **{snapshot.modules_scanned}**")
    lines.append(f"- Edges checked: **{snapshot.edges_checked}**")
    lines.append(f"- Violations: **{snapshot.violations_found}**\n")
    lines.append(f"**{_verdict(snapshot)}**\n")

    if snapshot.unknown_domains:
        lines.append("## Unknown domains (not in policy)")
        for d in snapshot.unknown_domains:
            lines.append(f"- `{d}` — add to `ALLOWED_IMPORTS` in `architecture_drift.py`")
        lines.append("")

    if snapshot.violations:
        lines.append("## Violations")
        lines.append("| # | From module | To module | Reason |")
        lines.append("|---|-------------|-----------|--------|")
        for i, v in enumerate(snapshot.violations, 1):
            lines.append(
                f"| {i} | `{v.src_module}` | `{v.dst_module}` | {v.reason} |"
            )
        lines.append("")

    lines.append("## Layer policy (allowed imports)")
    lines.append("| Domain | May import from |")
    lines.append("|--------|----------------|")
    for domain, allowed in sorted(ALLOWED_IMPORTS.items()):
        allowed_str = ", ".join(f"`{a}`" for a in sorted(allowed)) or "_(nothing)_"
        lines.append(f"| `{domain}` | {allowed_str} |")

    return "\n".join(lines)


def write_report(
    snapshot: ArchitectureDriftSnapshot,
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "architecture_drift.json"
    md_path = output_dir / "architecture_drift.md"

    payload = {
        "root": str(snapshot.root),
        "modules_scanned": snapshot.modules_scanned,
        "edges_checked": snapshot.edges_checked,
        "violations_found": snapshot.violations_found,
        "violations": [
            {
                "src_module": v.src_module,
                "dst_module": v.dst_module,
                "src_domain": v.src_domain,
                "dst_domain": v.dst_domain,
                "reason": v.reason,
            }
            for v in snapshot.violations
        ],
        "unknown_domains": snapshot.unknown_domains,
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
        description="Audit the onto_market import graph for architecture violations"
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
