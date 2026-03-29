# Test Map

Source modules: **43** | Covered: **23** | Gaps: **20** | Coverage: **53%**

## Coverage Gaps (untested modules)

- `onto_market.agents.memory_agent`
- `onto_market.agents.ontology_agent`
- `onto_market.agents.state`
- `onto_market.connectors.news`
- `onto_market.connectors.search`
- `onto_market.context`
- `onto_market.core.agent_base`
- `onto_market.core.graph`
- `onto_market.core.state`
- `onto_market.memory.zep_reader`
- `onto_market.ontology`
- `onto_market.ontology.graph`
- `onto_market.polymarket_agents.utils.database`
- `onto_market.utils`
- `onto_market.utils.file_parser`
- `onto_market.utils.llm_client`
- `onto_market.utils.logger`
- `onto_market.utils.retry`
- `reports.streamlit_app`
- `tests`

## Full Coverage Table

| Module | Covered | Test Files |
|--------|:-------:|------------|
| `devtools` | yes | `src/devtools/repo_tools/test_map.py` |
| `onto_market` | yes | `scripts/repo_tools/test_map.py`, `tests/test_analytics.py`, `tests/test_integration.py`, `tests/test_memory.py`, `tests/test_planning_agent.py`, `tests/test_repo_tools.py`, `tests/test_swarm.py`, `tests/test_trading.py` |
| `onto_market.agents` | yes | `tests/test_planning_agent.py` |
| `onto_market.agents.memory_agent` | **NO** | _none_ |
| `onto_market.agents.ontology_agent` | **NO** | _none_ |
| `onto_market.agents.planning_agent` | yes | `tests/test_planning_agent.py` |
| `onto_market.agents.state` | **NO** | _none_ |
| `onto_market.connectors` | yes | `tests/test_integration.py`, `tests/test_planning_agent.py`, `tests/test_trading.py` |
| `onto_market.connectors.gamma` | yes | `tests/test_planning_agent.py` |
| `onto_market.connectors.news` | **NO** | _none_ |
| `onto_market.connectors.polymarket` | yes | `tests/test_integration.py`, `tests/test_trading.py` |
| `onto_market.connectors.search` | **NO** | _none_ |
| `onto_market.context` | **NO** | _none_ |
| `onto_market.core` | yes | `tests/test_integration.py` |
| `onto_market.core.agent_base` | **NO** | _none_ |
| `onto_market.core.graph` | **NO** | _none_ |
| `onto_market.core.llm_router` | yes | `tests/test_integration.py` |
| `onto_market.core.state` | **NO** | _none_ |
| `onto_market.devtools` | yes | `scripts/repo_tools/test_map.py`, `tests/test_repo_tools.py` |
| `onto_market.memory` | yes | `tests/test_memory.py` |
| `onto_market.memory.manager` | yes | `tests/test_memory.py` |
| `onto_market.memory.zep_reader` | **NO** | _none_ |
| `onto_market.ontology` | **NO** | _none_ |
| `onto_market.ontology.graph` | **NO** | _none_ |
| `onto_market.polymarket_agents` | yes | `tests/test_analytics.py`, `tests/test_memory.py` |
| `onto_market.polymarket_agents.utils` | yes | `tests/test_analytics.py`, `tests/test_memory.py` |
| `onto_market.polymarket_agents.utils.analytics` | yes | `tests/test_analytics.py` |
| `onto_market.polymarket_agents.utils.database` | **NO** | _none_ |
| `onto_market.polymarket_agents.utils.objects` | yes | `tests/test_memory.py` |
| `onto_market.swarm` | yes | `tests/test_swarm.py` |
| `onto_market.swarm.archetypes` | yes | `tests/test_swarm.py` |
| `onto_market.swarm.dynamics` | yes | `tests/test_swarm.py` |
| `onto_market.swarm.oracle` | yes | `tests/test_swarm.py` |
| `onto_market.trading` | yes | `tests/test_integration.py`, `tests/test_trading.py` |
| `onto_market.trading.executor` | yes | `tests/test_trading.py` |
| `onto_market.trading.trader` | yes | `tests/test_integration.py`, `tests/test_trading.py` |
| `onto_market.utils` | **NO** | _none_ |
| `onto_market.utils.file_parser` | **NO** | _none_ |
| `onto_market.utils.llm_client` | **NO** | _none_ |
| `onto_market.utils.logger` | **NO** | _none_ |
| `onto_market.utils.retry` | **NO** | _none_ |
| `reports.streamlit_app` | **NO** | _none_ |
| `tests` | **NO** | _none_ |