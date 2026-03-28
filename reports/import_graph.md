# Import Graph Report

- Repo root: `/home/orson-dev/projects/onto-market`
- Modules scanned: **52**
- Import edges: **84**
- Isolated modules (no imports): **12**
- Cycles detected: **0**

## Top importers (highest out-degree)
| Module | Imports |
|--------|---------|
| `onto_market.agents.planning_agent` | 14 |
| `onto_market.agents.memory_agent` | 8 |
| `onto_market.trading.trader` | 6 |
| `onto_market.swarm.oracle` | 5 |
| `onto_market.connectors.polymarket` | 4 |
| `onto_market.context` | 4 |
| `onto_market.trading.executor` | 4 |
| `onto_market.agents.ontology_agent` | 3 |
| `onto_market.connectors.gamma` | 3 |
| `onto_market.main` | 3 |
| `onto_market.connectors.news` | 2 |
| `onto_market.connectors.search` | 2 |

## Most imported (highest in-degree)
| Module | Imported by |
|--------|------------|
| `onto_market.utils.logger` | 12 |
| `onto_market.config.config` | 7 |
| `onto_market.devtools.repo_tools._paths` | 7 |
| `onto_market.config` | 6 |
| `onto_market.utils.llm_client` | 6 |
| `onto_market.connectors.gamma` | 5 |
| `onto_market.connectors.polymarket` | 4 |
| `onto_market.utils.retry` | 4 |
| `onto_market.devtools.repo_tools.import_graph` | 3 |
| `onto_market.memory.manager` | 3 |
| `onto_market.ontology.graph` | 3 |
| `onto_market.swarm.archetypes` | 3 |

## Adjacency list

### `onto_market.agents.memory_agent`
- `onto_market.agents.state`
- `onto_market.config`
- `onto_market.config.config`
- `onto_market.connectors.gamma`
- `onto_market.core.graph`
- `onto_market.memory.manager`
- `onto_market.utils.llm_client`
- `onto_market.utils.logger`

### `onto_market.agents.ontology_agent`
- `onto_market.ontology.graph`
- `onto_market.utils.llm_client`
- `onto_market.utils.logger`

### `onto_market.agents.planning_agent`
- `onto_market.agents.ontology_agent`
- `onto_market.agents.state`
- `onto_market.config`
- `onto_market.config.config`
- `onto_market.connectors.gamma`
- `onto_market.connectors.news`
- `onto_market.connectors.polymarket`
- `onto_market.connectors.search`
- `onto_market.core.graph`
- `onto_market.memory.manager`
- `onto_market.polymarket_agents.utils.analytics`
- `onto_market.swarm.oracle`
- `onto_market.utils.llm_client`
- `onto_market.utils.logger`

### `onto_market.config`
- `onto_market.config.config`

### `onto_market.connectors.gamma`
- `onto_market.polymarket_agents.utils.objects`
- `onto_market.utils.logger`
- `onto_market.utils.retry`

### `onto_market.connectors.news`
- `onto_market.utils.logger`
- `onto_market.utils.retry`

### `onto_market.connectors.polymarket`
- `onto_market.config`
- `onto_market.config.config`
- `onto_market.utils.logger`
- `onto_market.utils.retry`

### `onto_market.connectors.search`
- `onto_market.utils.logger`
- `onto_market.utils.retry`

### `onto_market.context`
- `onto_market.connectors.gamma`
- `onto_market.connectors.polymarket`
- `onto_market.memory.manager`
- `onto_market.utils.llm_client`

### `onto_market.core.agent_base`
- `onto_market.core.state`

### `onto_market.core.llm_router`
- `onto_market.config`
- `onto_market.config.config`

### `onto_market.devtools.repo_tools.architecture_drift`
- `onto_market.devtools.repo_tools._paths`
- `onto_market.devtools.repo_tools.import_graph`

### `onto_market.devtools.repo_tools.boundary_matrix`
- `onto_market.devtools.repo_tools._paths`
- `onto_market.devtools.repo_tools.import_graph`

### `onto_market.devtools.repo_tools.census`
- `onto_market.devtools.repo_tools._paths`

### `onto_market.devtools.repo_tools.cycle_detector`
- `onto_market.devtools.repo_tools._paths`
- `onto_market.devtools.repo_tools.import_graph`

### `onto_market.devtools.repo_tools.import_graph`
- `onto_market.devtools.repo_tools._paths`

### `onto_market.devtools.repo_tools.ontology_audit`
- `onto_market.devtools.repo_tools._paths`
- `onto_market.ontology.graph`

### `onto_market.devtools.repo_tools.repo_map`
- `onto_market.devtools.repo_tools._paths`

### `onto_market.main`
- `onto_market.agents.planning_agent`
- `onto_market.ontology.graph`
- `onto_market.utils.logger`

### `onto_market.memory.manager`
- `onto_market.polymarket_agents.utils.database`
- `onto_market.polymarket_agents.utils.objects`

### `onto_market.memory.zep_reader`
- `onto_market.config`
- `onto_market.config.config`

### `onto_market.swarm`
- `onto_market.swarm.archetypes`
- `onto_market.swarm.oracle`

### `onto_market.swarm.dynamics`
- `onto_market.swarm.archetypes`
- `onto_market.utils.logger`

### `onto_market.swarm.oracle`
- `onto_market.config`
- `onto_market.config.config`
- `onto_market.swarm.archetypes`
- `onto_market.swarm.dynamics`
- `onto_market.utils.logger`

### `onto_market.trading`
- `onto_market.trading.executor`
- `onto_market.trading.trader`

### `onto_market.trading.executor`
- `onto_market.connectors.gamma`
- `onto_market.connectors.polymarket`
- `onto_market.utils.llm_client`
- `onto_market.utils.logger`

### `onto_market.trading.trader`
- `onto_market.connectors.gamma`
- `onto_market.connectors.polymarket`
- `onto_market.polymarket_agents.utils.analytics`
- `onto_market.trading.executor`
- `onto_market.utils.llm_client`
- `onto_market.utils.logger`

### `onto_market.utils.llm_client`
- `onto_market.core.llm_router`