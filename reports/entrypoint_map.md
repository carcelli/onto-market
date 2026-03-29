# Entrypoint Map

Total entrypoints: **77**

| Kind | File | Line | Detail |
|------|------|-----:|--------|
| `__main__` | `scripts/audit_ontology.py` | 7 | `` |
| `__main__` | `scripts/cli.py` | 175 | `` |
| `__main__` | `scripts/generate_repo_map.py` | 7 | `` |
| `__main__` | `scripts/import_graph.py` | 75 | `` |
| `__main__` | `scripts/refresh_markets.py` | 36 | `` |
| `__main__` | `scripts/repo_census.py` | 7 | `` |
| `__main__` | `scripts/repo_tools/architecture_drift.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/boundary_matrix.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/cartography.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/config_surface.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/cycle_detector.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/dead_weight.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/entrypoint_map.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/import_graph.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/symbol_index.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/symbol_xref.py` | 11 | `` |
| `__main__` | `scripts/repo_tools/test_map.py` | 11 | `` |
| `__main__` | `src/devtools/repo_tools/architecture_drift.py` | 188 | `` |
| `__main__` | `src/devtools/repo_tools/boundary_matrix.py` | 109 | `` |
| `__main__` | `src/devtools/repo_tools/cartography.py` | 95 | `` |
| `__main__` | `src/devtools/repo_tools/census.py` | 177 | `` |
| `__main__` | `src/devtools/repo_tools/config_surface.py` | 196 | `` |
| `__main__` | `src/devtools/repo_tools/cycle_detector.py` | 155 | `` |
| `__main__` | `src/devtools/repo_tools/dead_weight.py` | 211 | `` |
| `__main__` | `src/devtools/repo_tools/entrypoint_map.py` | 230 | `` |
| `__main__` | `src/devtools/repo_tools/import_graph.py` | 99 | `` |
| `__main__` | `src/devtools/repo_tools/symbol_index.py` | 172 | `` |
| `__main__` | `src/devtools/repo_tools/symbol_xref.py` | 160 | `` |
| `__main__` | `src/devtools/repo_tools/test_map.py` | 169 | `` |
| `__main__` | `src/onto_market/agents/memory_agent.py` | 124 | `` |
| `__main__` | `src/onto_market/agents/planning_agent.py` | 400 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/architecture_drift.py` | 290 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 184 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/cartography.py` | 113 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/census.py` | 230 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/config_surface.py` | 167 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/cycle_detector.py` | 171 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/dead_weight.py` | 176 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 199 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/import_graph.py` | 284 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/ontology_audit.py` | 295 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/repo_map.py` | 430 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/symbol_index.py` | 156 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/symbol_xref.py` | 137 | `` |
| `__main__` | `src/onto_market/devtools/repo_tools/test_map.py` | 139 | `` |
| `__main__` | `src/onto_market/main.py` | 90 | `` |
| `console-script` | `pyproject.toml` | 40 | `onto-market = onto_market.main:main` |
| `console-script` | `pyproject.toml` | 41 | `repo-census = onto_market.devtools.repo_tools.census:main` |
| `console-script` | `pyproject.toml` | 42 | `repo-import-graph = onto_market.devtools.repo_tools.import_graph:main` |
| `console-script` | `pyproject.toml` | 43 | `repo-boundary = onto_market.devtools.repo_tools.boundary_matrix:main` |
| `console-script` | `pyproject.toml` | 44 | `repo-entrypoints = onto_market.devtools.repo_tools.entrypoint_map:main` |
| `console-script` | `pyproject.toml` | 45 | `repo-symbols = onto_market.devtools.repo_tools.symbol_index:main` |
| `console-script` | `pyproject.toml` | 46 | `repo-xref = onto_market.devtools.repo_tools.symbol_xref:main` |
| `console-script` | `pyproject.toml` | 47 | `repo-test-map = onto_market.devtools.repo_tools.test_map:main` |
| `console-script` | `pyproject.toml` | 48 | `repo-config = onto_market.devtools.repo_tools.config_surface:main` |
| `console-script` | `pyproject.toml` | 49 | `repo-cycles = onto_market.devtools.repo_tools.cycle_detector:main` |
| `console-script` | `pyproject.toml` | 50 | `repo-dead-weight = onto_market.devtools.repo_tools.dead_weight:main` |
| `console-script` | `pyproject.toml` | 51 | `repo-arch-drift = onto_market.devtools.repo_tools.architecture_drift:main` |
| `console-script` | `pyproject.toml` | 52 | `repo-cartography = onto_market.devtools.repo_tools.cartography:main` |
| `langgraph` | `src/onto_market/agents/memory_agent.py` | 107 | `StateGraph` |
| `langgraph` | `src/onto_market/agents/memory_agent.py` | 108 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/memory_agent.py` | 109 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/memory_agent.py` | 110 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/memory_agent.py` | 111 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 377 | `StateGraph` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 378 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 379 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 380 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 381 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 382 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 383 | `.add_node()` |
| `langgraph` | `src/onto_market/agents/planning_agent.py` | 384 | `.add_node()` |
| `langgraph` | `src/onto_market/core/agent_base.py` | 26 | `StateGraph` |
| `langgraph` | `src/onto_market/ontology/graph.py` | 76 | `.add_node()` |
| `langgraph` | `tests/test_repo_tools.py` | 327 | `.add_node()` |
| `langgraph` | `tests/test_repo_tools.py` | 328 | `.add_node()` |
| `typer/click` | `scripts/cli.py` | 15 | `typer.Typer` |