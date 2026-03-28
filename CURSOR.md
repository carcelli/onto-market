# CURSOR.md

## What is onto-market?

A Polymarket prediction market trading system (v0.1.0) that combines LangGraph multi-agent orchestration, a NetworkX ontology knowledge graph that accumulates across runs, and an OASIS-style heterogeneous swarm simulation (5000 agents, 6 archetypes) to find and trade mispriced prediction markets. Query in, BET/WATCH/PASS out.

## Architecture at a Glance

**Planning Agent Pipeline (7 nodes):**
```
research → ontology → stats → probability → swarm → decision → trade
```

**Memory Agent Pipeline (4 nodes):**
```
memory → enrichment → reasoning → decide
```

**Key subsystems:**
- **Ontology** — NetworkX DiGraph persisted to JSON; triples extracted by LLM each run, queried for prior knowledge
- **Swarm** — 5000 heterogeneous agents on Watts-Strogatz network; 6 archetypes with distinct biases; only 3% call LLM
- **Multi-LLM** — Grok/xAI default, switchable to OpenAI/Gemini/Claude via `LLM_PROVIDER`
- **Trading** — Kelly criterion sizing, edge/EV scoring, SAFE_MODE dry-run by default

## Getting Started

```bash
conda activate onto-market
pip install -e ".[dev]"
python scripts/refresh_markets.py --max-events 500
python main.py "Will Bitcoin hit $100k?"
make test
```

## What Works Today

- Full end-to-end planning pipeline (query → BET/WATCH/PASS + edge, EV, Kelly fraction)
- Ontology knowledge accumulation across runs
- Swarm consensus with convergence detection
- Multi-LLM routing (Grok, OpenAI, Gemini, Claude)
- SQLite memory persistence (markets, research, analytics)
- Gamma API market discovery + Polymarket CLOB order building
- Web research (Tavily) + news headlines (NewsAPI)
- Comprehensive test suite (analytics, memory, swarm, trading, planning)

## What Doesn't Work Yet (Phase 2)

- **Zep Cloud** graph memory — stub exists (`src/memory/zep_reader.py`), returns empty
- **Domain registry** — pluggable crypto/NBA agents, not implemented
- **Vue 3 dashboard** — not started

## Where to Focus Next

1. **Unify packaging** — delete stale `requirements.txt`, fix pyproject.toml package discovery
2. **Separate analysis/execution** — decouple module-level singletons in planning_agent
3. **Strengthen ontology** — file locking for thread safety, typed entity categories, PageRank audits
4. **Backtest swarm** — historical resolution data, calibration tracking (Brier score)

## See Also

- `CLAUDE.md` — Claude Code guidance (architecture, env vars, commands)
- `GEMINI.md` — Gemini CLI guidance
- `REPO_MAP.md` — auto-generated annotated directory tree (`make repo-map`)
- `.cursor/rules.md` — full Cursor context (what's real, what's stub, bottlenecks)
