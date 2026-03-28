#!/usr/bin/env python3
"""
generate_repo_map.py — Dynamic annotated repo tree for onto-market.

Produces REPO_MAP.md with:
  - Live file tree (respects .gitignore patterns)
  - Per-module status annotations (real vs Phase 2 stub)
  - Mermaid architecture diagram of the planning_agent pipeline
  - Logical layer groupings
  - Module verdicts table
  - Ontology graph stats (nodes, edges, top entities)
  - Top leverage points

Usage:
    python scripts/generate_repo_map.py        # writes REPO_MAP.md
    python scripts/generate_repo_map.py --dry   # print to stdout only
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ── Skip patterns ──────────────────────────────────────────────────────────

SKIP_DIRS = {
    "__pycache__", ".git", ".mypy_cache", ".pytest_cache",
    "node_modules", "*.egg-info", ".venv", "venv",
}
SKIP_SUFFIXES = {".pyc", ".pyo", ".DS_Store", ".log"}
SKIP_NAMES = {"package-lock.json", ".gitignore"}

# ── Module annotations ──────────────────────────────────────────────────────

ANNOTATIONS: dict[str, str] = {
    # agents
    "agents/planning_agent.py":         "✅ Full 7-node pipeline (research→ontology→stats→probability→swarm→decision→trade)",
    "agents/memory_agent.py":           "✅ DB-first pipeline (memory→enrichment→reasoning→decide)",
    "agents/ontology_agent.py":         "✅ Extracts semantic triples → OntologyGraph",
    "agents/state.py":                  "✅ AgentState / MemoryAgentState / PlanningState TypedDicts",

    # config
    "config/config.py":                 "✅ Env vars, decision thresholds, swarm params",

    # core
    "core/llm_router.py":               "✅ LiteLLM multi-provider (Grok / GPT / Gemini / Claude)",
    "core/graph.py":                    "✅ register_graph() decorator",
    "core/agent_base.py":               "⚠ Vestigial — BaseAgent defined but unused",
    "core/state.py":                    "⚠ Vestigial — duplicates agents/state.py",

    # ontology
    "ontology/graph.py":                "✅ OntologyGraph (NetworkX DiGraph, JSON-persisted) ⚠ NOT thread-safe",

    # src/connectors
    "src/connectors/gamma.py":          "✅ Gamma Markets API — paginated, search",
    "src/connectors/search.py":         "✅ Tavily web search",
    "src/connectors/news.py":           "✅ NewsAPI headlines",
    "src/connectors/polymarket.py":     "✅ Polymarket CLOB order builder",

    # src/memory
    "src/memory/manager.py":            "✅ SQLite MemoryManager (upsert, search, analytics)",
    "src/memory/zep_reader.py":         "⏳ Phase 2 stub — Zep Cloud, not wired",

    # src/swarm
    "src/swarm/oracle.py":              "✅ SocialSentimentOracle — 5000 agents, small-world net",
    "src/swarm/archetypes.py":          "✅ 6 archetypes: BULL / BEAR / ANALYST / CONTRARIAN / NOISE_TRADER / INSIDER",
    "src/swarm/dynamics.py":            "✅ build_network() + run_dynamics() (Watts-Strogatz)",

    # src/trading
    "src/trading/executor.py":          "✅ SAFE_MODE executor (dry-run default)",
    "src/trading/trader.py":            "✅ discover→filter→map→superforecast→execute pipeline",

    # src/utils
    "src/utils/llm_client.py":          "✅ LLMClient wrapping the router",
    "src/utils/retry.py":               "✅ retry_with_backoff (tenacity)",
    "src/utils/logger.py":              "✅ get_logger() — structured + rotating file",

    # src/polymarket_agents
    "src/polymarket_agents/utils/analytics.py": "✅ score_market, kelly_fraction, calculate_edge, EV",
    "src/polymarket_agents/utils/objects.py":   "✅ Market, ResearchNote dataclasses",
    "src/polymarket_agents/utils/database.py":  "✅ Database SQLite wrapper",

    # tests
    "tests/test_analytics.py":          "✅ Edge / Kelly / EV unit tests",
    "tests/test_memory.py":             "✅ MemoryManager unit tests",
    "tests/test_swarm.py":              "✅ SocialSentimentOracle tests",
    "tests/test_trading.py":            "✅ Trading executor tests",
    "tests/test_planning_agent.py":     "✅ Planning agent integration tests",
    "tests/test_integration.py":        "✅ End-to-end smoke tests",
    "tests/conftest.py":                "✅ sample_market, db_path fixtures",

    # scripts
    "scripts/refresh_markets.py":       "✅ Seed data/memory.db from Gamma API",
    "scripts/generate_repo_map.py":     "✅ This script — auto-generates REPO_MAP.md",
    "scripts/audit_ontology.py":        "✅ Ontology health check (PageRank + confidence dist)",
    "scripts/cli.py":                   "✅ Typer CLI entry point",

    # root
    "main.py":                          "✅ CLI entry point",
    "pyproject.toml":                   "⚠ Packaging drift — dual layout (root + src/); unify into src/",
    "langgraph.json":                   "✅ LangGraph graph registry",
    "Makefile":                         "✅ make test | dryrun | repo-map | ontology-audit",
    "data/memory.db":                   "✅ Live SQLite — markets + analytics",
    "data/ontology.json":               "✅ Live ontology graph — grows each planning_agent run",
}

MERMAID_DIAGRAM = """\
```mermaid
graph TD
    subgraph Entry["Entry Points"]
        MAIN["main.py"]
        CLI["scripts/cli.py"]
    end

    subgraph Agents["LangGraph Agents"]
        PA["planning_agent<br/>7-node pipeline"]
        MA["memory_agent<br/>4-node pipeline"]
        OA["ontology_agent<br/>triple extraction"]
    end

    subgraph Core["Core Services"]
        LLM["llm_router<br/>Grok / OpenAI / Gemini / Claude"]
        OG["OntologyGraph<br/>NetworkX DiGraph"]
        SO["SocialSentimentOracle<br/>5000 agents, 6 archetypes"]
    end

    subgraph Connectors["External Connectors"]
        GAMMA["GammaConnector<br/>market discovery"]
        POLY["PolymarketConnector<br/>CLOB orders"]
        TAVILY["SearchConnector<br/>Tavily"]
        NEWS["NewsConnector<br/>NewsAPI"]
    end

    subgraph Storage["Persistence"]
        DB[("memory.db<br/>SQLite")]
        ONT[("ontology.json<br/>NetworkX JSON")]
    end

    MAIN --> PA
    CLI --> PA
    CLI --> MA
    CLI --> SO

    PA --> OA
    PA --> LLM
    PA --> SO
    PA --> GAMMA
    PA --> TAVILY
    PA --> NEWS

    MA --> LLM
    MA --> GAMMA

    OA --> OG
    OA --> LLM

    PA --> POLY
    PA --> DB
    MA --> DB
    OG --> ONT

    style OG fill:#f9f,stroke:#333
    style SO fill:#bbf,stroke:#333
    style PA fill:#bfb,stroke:#333
```"""


# ── Tree walking ─────────────────────────────────────────────────────────

def _skip(path: Path) -> bool:
    if path.name in SKIP_NAMES:
        return True
    if path.suffix in SKIP_SUFFIXES:
        return True
    for pat in SKIP_DIRS:
        if "*" in pat:
            if path.match(pat):
                return True
        elif path.name == pat:
            return True
    return False


def _walk(directory: Path, prefix: str = "", rel_base: Path | None = None) -> list[str]:
    if rel_base is None:
        rel_base = directory

    entries = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    lines: list[str] = []

    visible = [e for e in entries if not _skip(e)]
    for i, entry in enumerate(visible):
        is_last = i == len(visible) - 1
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "

        rel = entry.relative_to(rel_base)
        rel_str = str(rel)

        annotation = ANNOTATIONS.get(rel_str, "")
        ann_suffix = f"   # {annotation}" if annotation else ""

        lines.append(f"{prefix}{connector}{entry.name}{ann_suffix}")

        if entry.is_dir():
            lines.extend(_walk(entry, prefix + extension, rel_base))

    return lines


# ── Data collection ──────────────────────────────────────────────────────

def _ontology_stats() -> dict:
    ontology_path = ROOT / "data" / "ontology.json"
    if not ontology_path.exists():
        return {"nodes": 0, "edges": 0, "top_entities": []}
    try:
        data = json.loads(ontology_path.read_text(encoding="utf-8"))
        nodes = data.get("nodes", [])
        edges = data.get("links", data.get("edges", []))
        return {
            "nodes": len(nodes),
            "edges": len(edges),
            "top_entities": [n.get("id", "?") for n in nodes[:8]],
        }
    except Exception as exc:
        return {"nodes": -1, "edges": -1, "error": str(exc)}


def _db_stats() -> dict:
    db_path = ROOT / "data" / "memory.db"
    if not db_path.exists():
        return {"size_kb": 0, "exists": False}
    size_kb = db_path.stat().st_size // 1024
    return {"size_kb": size_kb, "exists": True}


# ── Section renderers ────────────────────────────────────────────────────

def _render_layers() -> str:
    layers = [
        ("Layer 1: Entry Points", [
            ("`main.py`", "CLI entry point — parses query, invokes planning_agent"),
            ("`scripts/cli.py`", "Typer CLI — analyze, scan, trade, swarm commands"),
            ("`scripts/refresh_markets.py`", "Seed markets.db from Gamma API"),
        ]),
        ("Layer 2: Agent Orchestration", [
            ("`agents/planning_agent.py`", "Full 7-node LangGraph pipeline"),
            ("`agents/memory_agent.py`", "DB-first 4-node pipeline"),
            ("`agents/ontology_agent.py`", "Triple extraction + graph query"),
            ("`agents/state.py`", "TypedDict state definitions"),
        ]),
        ("Layer 3: Domain Logic", [
            ("`ontology/graph.py`", "OntologyGraph — knowledge accumulation engine"),
            ("`src/swarm/oracle.py`", "SocialSentimentOracle — swarm consensus"),
            ("`src/swarm/archetypes.py`", "6 agent archetypes with configurable biases"),
            ("`src/swarm/dynamics.py`", "Watts-Strogatz network + influence propagation"),
            ("`src/polymarket_agents/utils/analytics.py`", "Edge, Kelly, EV calculations"),
            ("`src/trading/executor.py`", "Trade sizing and execution"),
            ("`src/trading/trader.py`", "Trading pipeline orchestration"),
        ]),
        ("Layer 4: Connectors & I/O", [
            ("`src/connectors/gamma.py`", "Polymarket Gamma API client"),
            ("`src/connectors/polymarket.py`", "Polymarket CLOB trading client"),
            ("`src/connectors/search.py`", "Tavily web search"),
            ("`src/connectors/news.py`", "NewsAPI headlines"),
            ("`src/memory/manager.py`", "SQLite memory persistence"),
        ]),
        ("Layer 5: Utilities & Infrastructure", [
            ("`core/llm_router.py`", "Multi-LLM routing via LiteLLM"),
            ("`config/config.py`", "Configuration management"),
            ("`src/context.py`", "AppContext dependency injection"),
            ("`src/utils/llm_client.py`", "LLMClient wrapper"),
            ("`src/utils/retry.py`", "Retry logic (tenacity)"),
            ("`src/utils/logger.py`", "Structured logging"),
        ]),
    ]

    lines: list[str] = []
    for layer_name, modules in layers:
        lines.append(f"### {layer_name}\n")
        lines.append("| Module | Description |")
        lines.append("|--------|-------------|")
        for module, desc in modules:
            lines.append(f"| {module} | {desc} |")
        lines.append("")

    return "\n".join(lines)


def _render_verdicts() -> str:
    """Module verdicts table grouped by status."""
    phase1 = []
    phase2 = []
    vestigial = []
    tests = []

    for path, ann in sorted(ANNOTATIONS.items()):
        if ann.startswith("⏳"):
            phase2.append((path, ann))
        elif ann.startswith("⚠"):
            vestigial.append((path, ann))
        elif path.startswith("tests/"):
            tests.append((path, ann))
        else:
            phase1.append((path, ann))

    lines = [
        "| Module | Status | Verdict |",
        "|--------|--------|---------|",
    ]
    for path, ann in phase1:
        lines.append(f"| `{path}` | Phase 1 | {ann} |")
    for path, ann in phase2:
        lines.append(f"| `{path}` | Phase 2 | {ann} |")
    for path, ann in vestigial:
        lines.append(f"| `{path}` | Vestigial | {ann} |")
    for path, ann in tests:
        lines.append(f"| `{path}` | Tests | {ann} |")

    return "\n".join(lines)


# ── Main generator ───────────────────────────────────────────────────────

def generate(dry_run: bool = False) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    tree_lines = _walk(ROOT, rel_base=ROOT)
    onto = _ontology_stats()
    db = _db_stats()

    body = f"""\
# onto-market Repository Map

_Auto-generated by `scripts/generate_repo_map.py` on {now}._
_Regenerate: `make repo-map`_

---

## Project State

| Dimension | Value |
|-----------|-------|
| Maturity | Advanced prototype / mature MVP — v0.1.0 |
| Pipeline | `planning_agent`: research → ontology → stats → probability → swarm → decision → trade |
| Differentiator | Ontology accumulation + heterogeneous swarm simulation |
| Top debt | Packaging drift (root + src/ mix), ontology not thread-safe |
| Phase 2 stubs | Zep Cloud, domain registry, Vue dashboard |

---

## Architecture Diagram

{MERMAID_DIAGRAM}

---

## Annotated File Tree

```
onto-market/
{chr(10).join(tree_lines)}
```

---

## Logical Layers

{_render_layers()}
---

## Module Verdicts

{_render_verdicts()}

---

## Live Ontology State

| Metric | Value |
|--------|-------|
| Nodes | {onto['nodes']} |
| Edges | {onto['edges']} |
| Top entities | {', '.join(onto.get('top_entities', [])) or '(empty)'} |
| Path | `data/ontology.json` |
| Thread-safe | No — add file locking before concurrent agents |

> Grows every `planning_agent` run via `ontology_node` → `ontology/graph.py`.

---

## Live Memory DB

| Metric | Value |
|--------|-------|
| Exists | {'Yes' if db['exists'] else 'No'} |
| Size | {db['size_kb']} KB |
| Path | `data/memory.db` |

---

## Top Leverage Points

1. **Unify packaging** — move root packages (`agents/`, `config/`, `core/`, `ontology/`) into `src/`; fix `pyproject.toml`
2. **Thread-safe ontology** — add file locking to `OntologyGraph._save()` and `add_triples()`
3. **Backtest swarm** — run on resolved Polymarket data; compute Brier Score delta (swarm ON vs OFF)
4. **Separate side effects** — move `memory.store_analytics()` from `decision_node` to `trade_node`
5. **PageRank audit** — `make ontology-audit` to surface high-influence entities; prune low-degree noise

---

_Run `make ontology-audit` for PageRank + confidence distribution analysis._
"""
    if dry_run:
        print(body)
    else:
        out = ROOT / "REPO_MAP.md"
        out.write_text(body, encoding="utf-8")
        print(f"Wrote REPO_MAP.md ({len(body):,} bytes)")
    return body


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate REPO_MAP.md for onto-market")
    parser.add_argument("--dry", action="store_true", help="Print to stdout, don't write file")
    args = parser.parse_args()
    generate(dry_run=args.dry)
    sys.exit(0)
