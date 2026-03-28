# Architecture Drift Report

- Repo root: `/home/orson-dev/projects/onto-market`
- Modules scanned: **52**
- Edges checked: **84**
- Violations: **3**

**⚠ 3 violation(s) found. Each represents an import that crosses a forbidden layer boundary.**

## Violations
| # | From module | To module | Reason |
|---|-------------|-----------|--------|
| 1 | `onto_market.connectors.gamma` | `onto_market.polymarket_agents.utils.objects` | 'connectors' is not permitted to import from 'polymarket_agents' under the current layering policy |
| 2 | `onto_market.main` | `onto_market.ontology.graph` | 'main' is not permitted to import from 'ontology' under the current layering policy |
| 3 | `onto_market.utils.llm_client` | `onto_market.core.llm_router` | 'utils' is not permitted to import from 'core' under the current layering policy |

## Layer policy (allowed imports)
| Domain | May import from |
|--------|----------------|
| `agents` | `config`, `connectors`, `core`, `memory`, `ontology`, `polymarket_agents`, `swarm`, `trading`, `utils` |
| `config` | _(nothing)_ |
| `connectors` | `config`, `core`, `utils` |
| `context` | `config`, `connectors`, `core`, `memory`, `utils` |
| `core` | `config`, `utils` |
| `devtools` | `agents`, `config`, `connectors`, `context`, `core`, `memory`, `ontology`, `polymarket_agents`, `swarm`, `trading`, `utils` |
| `main` | `agents`, `config`, `core`, `utils` |
| `memory` | `config`, `core`, `polymarket_agents`, `utils` |
| `ontology` | `config`, `core`, `utils` |
| `polymarket_agents` | `config`, `core`, `utils` |
| `swarm` | `config`, `core`, `utils` |
| `trading` | `config`, `connectors`, `core`, `memory`, `polymarket_agents`, `utils` |
| `utils` | `config` |