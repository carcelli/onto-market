from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence

from ._paths import resolve_output_path, resolve_repo_root

SKIP_DIRS = {
    "__pycache__",
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    "node_modules",
    "*.egg-info",
    ".venv",
    "venv",
}
SKIP_SUFFIXES = {".pyc", ".pyo", ".DS_Store", ".log"}
SKIP_NAMES = {"package-lock.json", ".gitignore"}

ANNOTATIONS: dict[str, str] = {
    "src/onto_market/agents/planning_agent.py": "✅ Full 7-node pipeline (research→ontology→stats→probability→swarm→decision→trade)",
    "src/onto_market/agents/memory_agent.py": "✅ DB-first pipeline (memory→enrichment→reasoning→decide)",
    "src/onto_market/agents/ontology_agent.py": "✅ Extracts semantic triples → OntologyGraph",
    "src/onto_market/agents/state.py": "✅ AgentState / MemoryAgentState / PlanningState TypedDicts",
    "src/onto_market/config/config.py": "✅ Env vars, decision thresholds, swarm params",
    "src/onto_market/core/llm_router.py": "✅ LiteLLM multi-provider (Grok / GPT / Gemini / Claude)",
    "src/onto_market/core/graph.py": "✅ register_graph() decorator",
    "src/onto_market/core/agent_base.py": "⚠ Vestigial — BaseAgent defined but unused",
    "src/onto_market/core/state.py": "⚠ Vestigial — duplicates agents/state.py",
    "src/onto_market/ontology/graph.py": "✅ OntologyGraph (NetworkX DiGraph, JSON-persisted) ⚠ NOT thread-safe",
    "src/onto_market/connectors/gamma.py": "✅ Gamma Markets API — paginated, search",
    "src/onto_market/connectors/search.py": "✅ Tavily web search",
    "src/onto_market/connectors/news.py": "✅ NewsAPI headlines",
    "src/onto_market/connectors/polymarket.py": "✅ Polymarket CLOB order builder",
    "src/onto_market/memory/manager.py": "✅ SQLite MemoryManager (upsert, search, analytics)",
    "src/onto_market/memory/zep_reader.py": "⏳ Phase 2 stub — Zep Cloud, not wired",
    "src/onto_market/swarm/oracle.py": "✅ SocialSentimentOracle — 5000 agents, small-world net",
    "src/onto_market/swarm/archetypes.py": "✅ 6 archetypes: BULL / BEAR / ANALYST / CONTRARIAN / NOISE_TRADER / INSIDER",
    "src/onto_market/swarm/dynamics.py": "✅ build_network() + run_dynamics() (Watts-Strogatz)",
    "src/onto_market/trading/executor.py": "✅ SAFE_MODE executor (dry-run default)",
    "src/onto_market/trading/trader.py": "✅ discover→filter→map→superforecast→execute pipeline",
    "src/onto_market/utils/llm_client.py": "✅ LLMClient wrapping the router",
    "src/onto_market/utils/retry.py": "✅ retry_with_backoff (tenacity)",
    "src/onto_market/utils/logger.py": "✅ get_logger() — structured + rotating file",
    "src/onto_market/polymarket_agents/utils/analytics.py": "✅ score_market, kelly_fraction, calculate_edge, EV",
    "src/onto_market/polymarket_agents/utils/objects.py": "✅ Market, ResearchNote dataclasses",
    "src/onto_market/polymarket_agents/utils/database.py": "✅ Database SQLite wrapper",
    "src/onto_market/devtools/repo_tools/census.py": "✅ Importable repo census logic",
    "src/onto_market/devtools/repo_tools/repo_map.py": "✅ Importable repo map generator",
    "src/onto_market/devtools/repo_tools/ontology_audit.py": "✅ Importable ontology health check",
    "src/onto_market/devtools/repo_tools/import_graph.py": "✅ AST-based module dependency graph (NetworkX DiGraph) — base engine for all graph tools",
    "src/onto_market/devtools/repo_tools/boundary_matrix.py": "✅ Domain coupling matrix — cross-boundary edge counts derived from import graph",
    "src/onto_market/devtools/repo_tools/cycle_detector.py": "✅ Import cycle detector — SCCs + simple cycles via NetworkX",
    "src/onto_market/devtools/repo_tools/architecture_drift.py": "✅ Architecture drift auditor — policy-rule violations against allowed layer dependencies",
    "tests/test_analytics.py": "✅ Edge / Kelly / EV unit tests",
    "tests/test_memory.py": "✅ MemoryManager unit tests",
    "tests/test_swarm.py": "✅ SocialSentimentOracle tests",
    "tests/test_trading.py": "✅ Trading executor tests",
    "tests/test_planning_agent.py": "✅ Planning agent integration tests",
    "tests/test_integration.py": "✅ End-to-end smoke tests",
    "tests/conftest.py": "✅ sample_market, db_path fixtures",
    "tests/test_repo_tools.py": "✅ Repo-cartography package tests",
    "scripts/refresh_markets.py": "✅ Seed data/memory.db from Gamma API",
    "scripts/repo_census.py": "✅ Compatibility shim for repo census",
    "scripts/generate_repo_map.py": "✅ Compatibility shim for repo map generation",
    "scripts/audit_ontology.py": "✅ Compatibility shim for ontology audit",
    "scripts/cli.py": "✅ Typer CLI entry point",
    "main.py": "✅ CLI entry point",
    "pyproject.toml": "⚠ Packaging drift — root + src layout still mixed; repo tools now live under src/onto_market/",
    "langgraph.json": "✅ LangGraph graph registry",
    "Makefile": "✅ make test | dryrun | repo-map | ontology-audit",
    "data/memory.db": "✅ Live SQLite — markets + analytics",
    "data/ontology.json": "✅ Live ontology graph — grows each planning_agent run",
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


def _skip(path: Path) -> bool:
    if path.name in SKIP_NAMES:
        return True
    if path.suffix in SKIP_SUFFIXES:
        return True
    for pattern in SKIP_DIRS:
        if "*" in pattern:
            if path.match(pattern):
                return True
        elif path.name == pattern:
            return True
    return False


def _walk(directory: Path, prefix: str = "", rel_base: Path | None = None) -> list[str]:
    if rel_base is None:
        rel_base = directory

    entries = sorted(directory.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))
    lines: list[str] = []
    visible = [entry for entry in entries if not _skip(entry)]

    for index, entry in enumerate(visible):
        is_last = index == len(visible) - 1
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "

        rel = entry.relative_to(rel_base)
        annotation = ANNOTATIONS.get(str(rel), "")
        suffix = f"   # {annotation}" if annotation else ""
        lines.append(f"{prefix}{connector}{entry.name}{suffix}")

        if entry.is_dir():
            lines.extend(_walk(entry, prefix + extension, rel_base))

    return lines


def _ontology_stats(root: Path) -> dict[str, Any]:
    ontology_path = root / "data" / "ontology.json"
    if not ontology_path.exists():
        return {"nodes": 0, "edges": 0, "top_entities": []}
    try:
        data = json.loads(ontology_path.read_text(encoding="utf-8"))
        nodes = data.get("nodes", [])
        edges = data.get("links", data.get("edges", []))
        return {
            "nodes": len(nodes),
            "edges": len(edges),
            "top_entities": [node.get("id", "?") for node in nodes[:8]],
        }
    except Exception as exc:
        return {"nodes": -1, "edges": -1, "error": str(exc)}


def _db_stats(root: Path) -> dict[str, Any]:
    db_path = root / "data" / "memory.db"
    if not db_path.exists():
        return {"size_kb": 0, "exists": False}
    return {"size_kb": db_path.stat().st_size // 1024, "exists": True}


def _render_layers() -> str:
    layers = [
        (
            "Layer 1: Entry Points",
            [
                ("`main.py`", "CLI entry point — parses query, invokes planning_agent"),
                ("`scripts/cli.py`", "Typer CLI — analyze, scan, trade, swarm commands"),
                ("`scripts/refresh_markets.py`", "Seed markets.db from Gamma API"),
                ("`scripts/repo_census.py`", "Compatibility wrapper for repo census"),
            ],
        ),
        (
            "Layer 2: Agent Orchestration",
            [
                ("`agents/planning_agent.py`", "Full 7-node LangGraph pipeline"),
                ("`agents/memory_agent.py`", "DB-first 4-node pipeline"),
                ("`agents/ontology_agent.py`", "Triple extraction + graph query"),
                ("`agents/state.py`", "TypedDict state definitions"),
            ],
        ),
        (
            "Layer 3: Domain Logic",
            [
                ("`ontology/graph.py`", "OntologyGraph — knowledge accumulation engine"),
                ("`src/swarm/oracle.py`", "SocialSentimentOracle — swarm consensus"),
                ("`src/swarm/archetypes.py`", "6 agent archetypes with configurable biases"),
                ("`src/swarm/dynamics.py`", "Watts-Strogatz network + influence propagation"),
                ("`src/polymarket_agents/utils/analytics.py`", "Edge, Kelly, EV calculations"),
                ("`src/trading/executor.py`", "Trade sizing and execution"),
                ("`src/trading/trader.py`", "Trading pipeline orchestration"),
            ],
        ),
        (
            "Layer 4: Connectors & I/O",
            [
                ("`src/connectors/gamma.py`", "Polymarket Gamma API client"),
                ("`src/connectors/polymarket.py`", "Polymarket CLOB trading client"),
                ("`src/connectors/search.py`", "Tavily web search"),
                ("`src/connectors/news.py`", "NewsAPI headlines"),
                ("`src/memory/manager.py`", "SQLite memory persistence"),
            ],
        ),
        (
            "Layer 5: Devtools",
            [
                ("`src/onto_market/devtools/repo_tools/census.py`", "Repo census report builder"),
                ("`src/onto_market/devtools/repo_tools/repo_map.py`", "Annotated repository map generator"),
                ("`src/onto_market/devtools/repo_tools/ontology_audit.py`", "Ontology graph health check"),
                ("`src/onto_market/devtools/repo_tools/import_graph.py`", "AST import graph engine — base for boundary_matrix, cycle_detector, architecture_drift"),
            ],
        ),
        (
            "Layer 6: Utilities & Infrastructure",
            [
                ("`core/llm_router.py`", "Multi-LLM routing via LiteLLM"),
                ("`config/config.py`", "Configuration management"),
                ("`src/context.py`", "AppContext dependency injection"),
                ("`src/utils/llm_client.py`", "LLMClient wrapper"),
                ("`src/utils/retry.py`", "Retry logic (tenacity)"),
                ("`src/utils/logger.py`", "Structured logging"),
            ],
        ),
    ]

    lines: list[str] = []
    for layer_name, modules in layers:
        lines.append(f"### {layer_name}\n")
        lines.append("| Module | Description |")
        lines.append("|--------|-------------|")
        for module, description in modules:
            lines.append(f"| {module} | {description} |")
        lines.append("")

    return "\n".join(lines)


def _render_verdicts() -> str:
    phase1: list[tuple[str, str]] = []
    phase2: list[tuple[str, str]] = []
    vestigial: list[tuple[str, str]] = []
    tests: list[tuple[str, str]] = []

    for path, annotation in sorted(ANNOTATIONS.items()):
        if annotation.startswith("⏳"):
            phase2.append((path, annotation))
        elif annotation.startswith("⚠"):
            vestigial.append((path, annotation))
        elif path.startswith("tests/"):
            tests.append((path, annotation))
        else:
            phase1.append((path, annotation))

    lines = [
        "| Module | Status | Verdict |",
        "|--------|--------|---------|",
    ]
    for path, annotation in phase1:
        lines.append(f"| `{path}` | Phase 1 | {annotation} |")
    for path, annotation in phase2:
        lines.append(f"| `{path}` | Phase 2 | {annotation} |")
    for path, annotation in vestigial:
        lines.append(f"| `{path}` | Vestigial | {annotation} |")
    for path, annotation in tests:
        lines.append(f"| `{path}` | Tests | {annotation} |")

    return "\n".join(lines)


def generate(
    root: str | Path | None = None,
    dry_run: bool = False,
    output_path: str | Path | None = None,
) -> str:
    repo_root = resolve_repo_root(root)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    tree_lines = _walk(repo_root, rel_base=repo_root)
    ontology = _ontology_stats(repo_root)
    database = _db_stats(repo_root)

    body = f"""\
# onto-market Repository Map

_Auto-generated by `repo-map` on {now}._
_Regenerate: `make repo-map` or `repo-map`_

---

## Project State

| Dimension | Value |
|-----------|-------|
| Maturity | Advanced prototype / mature MVP — v0.1.0 |
| Pipeline | `planning_agent`: research → ontology → stats → probability → swarm → decision → trade |
| Differentiator | Ontology accumulation + heterogeneous swarm simulation |
| Top debt | Packaging drift (root + src mix), ontology not thread-safe |
| Devtools boundary | Repo tools live in `src/onto_market/devtools/repo_tools/`; `scripts/` stays thin |
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
| Nodes | {ontology['nodes']} |
| Edges | {ontology['edges']} |
| Top entities | {', '.join(str(e) for e in ontology.get('top_entities', [])) or '(empty)'} |
| Path | `data/ontology.json` |
| Thread-safe | Yes — `threading.Lock` + atomic write |

> Grows every `planning_agent` run via `ontology_node` → `ontology/graph.py`.

---

## Live Memory DB

| Metric | Value |
|--------|-------|
| Exists | {'Yes' if database['exists'] else 'No'} |
| Size | {database['size_kb']} KB |
| Path | `data/memory.db` |

---

## Top Leverage Points

1. **Continue unifying packaging** — move more runtime packages behind clean import boundaries and retire path bootstraps
2. **Thread-safe ontology** — add file locking to `OntologyGraph._save()` and `add_triples()`
3. **Backtest swarm** — run on resolved Polymarket data; compute Brier Score delta (swarm ON vs OFF)
4. **Separate side effects** — move `memory.store_analytics()` from `decision_node` to `trade_node`
5. **Implement repo boundary tools** — fill in `import_graph.py`, `boundary_matrix.py`, `cycle_detector.py`, and `architecture_drift.py`

---

_Run `make ontology-audit` or `audit-ontology` for PageRank + confidence distribution analysis._
"""

    if dry_run:
        print(body)
        return body

    destination = resolve_output_path(repo_root, output_path, "REPO_MAP.md")
    destination.write_text(body, encoding="utf-8")
    print(f"Wrote {destination} ({len(body):,} bytes)")
    return body


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate REPO_MAP.md for onto-market")
    parser.add_argument("--root", type=Path, default=None, help="Repository root to analyze")
    parser.add_argument("--dry", action="store_true", help="Print to stdout without writing a file")
    parser.add_argument("--output", type=Path, default=None, help="Output path for the repo map")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    generate(root=args.root, dry_run=args.dry, output_path=args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
