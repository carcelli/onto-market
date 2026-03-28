"""Enforce architecture rules and detect boundary violations.

Reads reports/import_graph.json (run import_graph first).

Rules (tailored to onto-market's actual layering):
  Foundation (no upward deps allowed):
    config       — may import: nothing internal
    ontology     — may import: config
    core         — may import: config, ontology
    src.utils    — may import: config, core
    src.polymarket_agents — may import: config, src.utils

  Mid-tier (connector/data layer):
    src.connectors — may import: config, core, src.utils, src.polymarket_agents
    src.memory     — may import: config, core, src.utils, src.polymarket_agents
    src.swarm      — may import: config, core, src.utils, src.polymarket_agents
    src.trading    — may import: config, core, src.utils, src.polymarket_agents,
                                src.connectors

  App layer (can import anything except tests/scripts):
    agents         — may import: all non-test, non-scripts layers
    ontology (agent-side uses) — already covered

  Meta:
    tests          — may import: anything
    scripts        — may import: anything
    devtools       — may import: anything

Violations are edges that cross a forbidden boundary.

Outputs:
  reports/architecture_drift.json  — list of violations
  reports/architecture_drift.md    — violations table + rule summary
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, load_import_graph_json
from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of

# Allowed upstream dependencies per domain.
# An edge src->dst is a VIOLATION if dst is NOT in ALLOWED[src] (and dst is internal).
# None = "may import anything" (no restrictions)
ALLOWED: dict[str, set[str] | None] = {
    "config":                frozenset(),
    "ontology":              frozenset({"config"}),
    "core":                  frozenset({"config", "ontology"}),
    "src.utils":             frozenset({"config", "core", "ontology"}),
    "src.polymarket_agents": frozenset({"config", "src.utils"}),
    "src.connectors":        frozenset({"config", "core", "src.utils", "src.polymarket_agents"}),
    "src.memory":            frozenset({"config", "core", "src.utils", "src.polymarket_agents", "ontology"}),
    "src.swarm":             frozenset({"config", "core", "src.utils", "src.polymarket_agents"}),
    "src.trading":           frozenset({"config", "core", "src.utils", "src.polymarket_agents", "src.connectors"}),
    "agents":                None,   # app layer: unrestricted
    "tests":                 None,
    "scripts":               None,
    "devtools":              None,
}

# Domains we recognize as internal (anything else = third-party, skip)
INTERNAL_DOMAINS: frozenset[str] = frozenset(DOMAINS)


@dataclass
class Violation:
    src_domain: str
    dst_domain: str
    src_module: str
    dst_module: str
    rule: str


def find_violations(data: dict) -> list[Violation]:
    violations: list[Violation] = []

    for edge in data["edges"]:
        src_mod = edge["source"]
        dst_mod = edge["target"]

        src_domain = domain_of(src_mod)
        dst_domain = domain_of(dst_mod)

        if src_domain == dst_domain:
            continue
        if dst_domain not in INTERNAL_DOMAINS:
            continue

        allowed = ALLOWED.get(src_domain)
        if allowed is None:
            continue  # Unrestricted domain

        if dst_domain not in allowed:
            rule = f"`{src_domain}` must not import `{dst_domain}`"
            violations.append(
                Violation(src_domain, dst_domain, src_mod, dst_mod, rule)
            )

    return sorted(violations, key=lambda v: (v.src_domain, v.dst_domain, v.src_module))


def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:
    data = [
        {
            "src_domain": v.src_domain,
            "dst_domain": v.dst_domain,
            "src_module": v.src_module,
            "dst_module": v.dst_module,
            "rule": v.rule,
        }
        for v in violations
    ]
    path = out_dir / "architecture_drift.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:
    lines = [
        "# Architecture Drift Report",
        "",
    ]
    if not violations:
        lines += [
            "> No architecture violations detected. All domain boundaries respected.",
            "",
        ]
    else:
        lines += [
            f"> **{len(violations)} violation(s)** detected across "
            f"{len({v.src_domain for v in violations})} source domain(s).",
            "",
            "| Source Domain | Target Domain | Source Module | Target Module |",
            "|---------------|---------------|---------------|---------------|",
        ]
        for v in violations:
            lines.append(
                f"| `{v.src_domain}` | `{v.dst_domain}` | `{v.src_module}` | `{v.dst_module}` |"
            )
        lines.append("")

    lines += [
        "## Architecture Rules",
        "",
        "Layers ordered from most foundational (top) to most app-specific (bottom).",
        "An arrow means 'may import'.",
        "",
        "| Layer | May Import |",
        "|-------|------------|",
    ]
    for domain, allowed in ALLOWED.items():
        if allowed is None:
            allowed_str = "_anything_"
        elif not allowed:
            allowed_str = "_nothing internal_"
        else:
            allowed_str = ", ".join(f"`{d}`" for d in sorted(allowed))
        lines.append(f"| `{domain}` | {allowed_str} |")

    path = out_dir / "architecture_drift.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    data = load_import_graph_json()
    violations = find_violations(data)
    json_path = write_json(violations)
    md_path = write_md(violations)

    if violations:
        print(f"Violations: {len(violations)}")
        by_src: dict[str, int] = {}
        for v in violations:
            by_src[v.src_domain] = by_src.get(v.src_domain, 0) + 1
        for domain, count in sorted(by_src.items()):
            print(f"  {domain}: {count}")
    else:
        print("No architecture violations — all boundaries clean.")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
