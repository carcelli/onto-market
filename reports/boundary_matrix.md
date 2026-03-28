# Boundary Matrix Report

- Repo root: `/home/orson-dev/projects/onto-market`
- Cross-boundary import edges: **61**

## Top cross-domain couplings
| From domain | To domain | Edge count |
|-------------|-----------|-----------|
| `connectors` | `utils` | 8 |
| `agents` | `utils` | 6 |
| `agents` | `connectors` | 5 |
| `trading` | `connectors` | 4 |
| `trading` | `utils` | 4 |
| `agents` | `config` | 4 |
| `core` | `config` | 2 |
| `connectors` | `config` | 2 |
| `memory` | `polymarket_agents` | 2 |
| `memory` | `config` | 2 |
| `swarm` | `utils` | 2 |
| `swarm` | `config` | 2 |
| `agents` | `memory` | 2 |
| `agents` | `core` | 2 |
| `context` | `connectors` | 2 |
| `utils` | `core` | 1 |
| `connectors` | `polymarket_agents` | 1 |
| `trading` | `polymarket_agents` | 1 |
| `agents` | `ontology` | 1 |
| `agents` | `polymarket_agents` | 1 |

## Full coupling matrix (rows import from columns)
| Domain | `config` | `utils` | `core` | `polymarket_agents` | `connectors` | `memory` | `ontology` | `swarm` | `trading` | `agents` | `context` | `devtools` | `_root` | `main` |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `config` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `utils` | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `core` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `polymarket_agents` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `connectors` | 2 | 8 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `memory` | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `ontology` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `swarm` | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `trading` | 0 | 4 | 0 | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `agents` | 4 | 6 | 2 | 1 | 5 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `context` | 0 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `devtools` | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_root` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `main` | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
