# Dead Weight Report

Flagged files: **36**

> `zero_inbound` = nothing imports this module (may be a legitimate entrypoint)
> `versioned_copy` = filename contains `_v2`, `_old`, `_backup`, etc.
> `empty_module` = no classes, functions, or assignments

## Zero Inbound Imports (20)

| File | Module | All Flags |
|------|--------|-----------|
| `reports/streamlit_app.py` | `reports.streamlit_app` | zero_inbound |
| `src/devtools/__init__.py` | `devtools` | zero_inbound, empty_module |
| `src/onto_market/__init__.py` | `onto_market` | zero_inbound |
| `src/onto_market/agents/__init__.py` | `onto_market.agents` | zero_inbound |
| `src/onto_market/agents/memory_agent.py` | `onto_market.agents.memory_agent` | zero_inbound |
| `src/onto_market/connectors/__init__.py` | `onto_market.connectors` | zero_inbound |
| `src/onto_market/context.py` | `onto_market.context` | zero_inbound |
| `src/onto_market/core/__init__.py` | `onto_market.core` | zero_inbound |
| `src/onto_market/core/agent_base.py` | `onto_market.core.agent_base` | zero_inbound |
| `src/onto_market/devtools/__init__.py` | `onto_market.devtools` | zero_inbound, empty_module |
| `src/onto_market/memory/__init__.py` | `onto_market.memory` | zero_inbound |
| `src/onto_market/memory/zep_reader.py` | `onto_market.memory.zep_reader` | zero_inbound |
| `src/onto_market/ontology/__init__.py` | `onto_market.ontology` | zero_inbound |
| `src/onto_market/polymarket_agents/__init__.py` | `onto_market.polymarket_agents` | zero_inbound |
| `src/onto_market/polymarket_agents/utils/__init__.py` | `onto_market.polymarket_agents.utils` | zero_inbound |
| `src/onto_market/swarm/__init__.py` | `onto_market.swarm` | zero_inbound |
| `src/onto_market/trading/__init__.py` | `onto_market.trading` | zero_inbound |
| `src/onto_market/utils/__init__.py` | `onto_market.utils` | zero_inbound |
| `src/onto_market/utils/file_parser.py` | `onto_market.utils.file_parser` | zero_inbound |
| `tests/__init__.py` | `tests` | zero_inbound, empty_module |

## Versioned Copies (0)

_None._

## Empty Modules (19)

| File | Module | All Flags |
|------|--------|-----------|
| `scripts/audit_ontology.py` | `scripts.audit_ontology` | empty_module |
| `scripts/generate_repo_map.py` | `scripts.generate_repo_map` | empty_module |
| `scripts/repo_census.py` | `scripts.repo_census` | empty_module |
| `scripts/repo_tools/__init__.py` | `scripts.repo_tools` | empty_module |
| `scripts/repo_tools/architecture_drift.py` | `scripts.repo_tools.architecture_drift` | empty_module |
| `scripts/repo_tools/boundary_matrix.py` | `scripts.repo_tools.boundary_matrix` | empty_module |
| `scripts/repo_tools/cartography.py` | `scripts.repo_tools.cartography` | empty_module |
| `scripts/repo_tools/config_surface.py` | `scripts.repo_tools.config_surface` | empty_module |
| `scripts/repo_tools/cycle_detector.py` | `scripts.repo_tools.cycle_detector` | empty_module |
| `scripts/repo_tools/dead_weight.py` | `scripts.repo_tools.dead_weight` | empty_module |
| `scripts/repo_tools/entrypoint_map.py` | `scripts.repo_tools.entrypoint_map` | empty_module |
| `scripts/repo_tools/import_graph.py` | `scripts.repo_tools.import_graph` | empty_module |
| `scripts/repo_tools/symbol_index.py` | `scripts.repo_tools.symbol_index` | empty_module |
| `scripts/repo_tools/symbol_xref.py` | `scripts.repo_tools.symbol_xref` | empty_module |
| `scripts/repo_tools/test_map.py` | `scripts.repo_tools.test_map` | empty_module |
| `src/devtools/repo_tools/__init__.py` | `devtools.repo_tools` | empty_module |
| `src/devtools/__init__.py` | `devtools` | zero_inbound, empty_module |
| `src/onto_market/devtools/__init__.py` | `onto_market.devtools` | zero_inbound, empty_module |
| `tests/__init__.py` | `tests` | zero_inbound, empty_module |
