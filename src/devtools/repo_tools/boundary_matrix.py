"""Collapse the import graph to domain-level relations.

Reads reports/import_graph.json (run import_graph first).
Outputs:
  reports/boundary_matrix.json  — machine-readable domain-pair counts
  reports/boundary_matrix.md    — human-readable Markdown table
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, load_import_graph_json

# Ordered from most foundational to most app-specific.
# A dependency pointing "upward" (foundation → app) is a smell.
DOMAINS: list[str] = [
    "config",
    "ontology",
    "core",
    "src.utils",
    "src.polymarket_agents",
    "src.connectors",
    "src.memory",
    "src.swarm",
    "src.trading",
    "agents",
    "tests",
    "scripts",
]

# Tiers for documentation (lower index = more foundational)
TIER: dict[str, int] = {d: i for i, d in enumerate(DOMAINS)}


def domain_of(module: str) -> str:
    for domain in DOMAINS:
        if module == domain or module.startswith(domain + "."):
            return domain
    # Fall back to top-level prefix
    return module.split(".")[0]


def build_matrix(data: dict) -> Counter[tuple[str, str]]:
    pairs: Counter[tuple[str, str]] = Counter()
    for edge in data["edges"]:
        src = domain_of(edge["source"])
        dst = domain_of(edge["target"])
        if src != dst:
            pairs[(src, dst)] += 1
    return pairs


def _upward_flag(src: str, dst: str) -> str:
    """Return '⚠' if a foundational layer imports an app-layer module."""
    src_tier = TIER.get(src, 99)
    dst_tier = TIER.get(dst, 99)
    return " ⚠" if src_tier > dst_tier else ""


def write_json(pairs: Counter[tuple[str, str]], out_dir: Path = OUTPUT_DIR) -> Path:
    data = [
        {"source": src, "target": dst, "edge_count": count}
        for (src, dst), count in sorted(pairs.items(), key=lambda x: (-x[1], x[0]))
    ]
    path = out_dir / "boundary_matrix.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def write_md(pairs: Counter[tuple[str, str]], out_dir: Path = OUTPUT_DIR) -> Path:
    lines = [
        "# Boundary Matrix",
        "",
        "> A ⚠ flag means a foundational layer depends on an app-layer — architectural smell.",
        "",
        "| Source | Target | Edges |",
        "|--------|--------|------:|",
    ]
    for (src, dst), count in sorted(pairs.items(), key=lambda x: (-x[1], x[0])):
        flag = _upward_flag(src, dst)
        lines.append(f"| `{src}` | `{dst}` | {count}{flag} |")

    path = out_dir / "boundary_matrix.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    data = load_import_graph_json()
    pairs = build_matrix(data)

    json_path = write_json(pairs)
    md_path = write_md(pairs)

    print(f"Domain pairs: {len(pairs)}")
    smells = sum(
        1 for (src, dst) in pairs if TIER.get(src, 99) > TIER.get(dst, 99)
    )
    if smells:
        print(f"Boundary smells (upward deps): {smells} — see boundary_matrix.md")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
