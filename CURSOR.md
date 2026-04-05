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
cp .env.example .env        # fill in XAI_API_KEY at minimum
make refresh                 # seed local DB from Gamma API
python -m onto_market.main "Will Bitcoin hit $100k?"
make dryrun                  # topology + tests + mypy
```

## What Works Today

- Full end-to-end planning pipeline (query → BET/WATCH/PASS + edge, EV, Kelly fraction)
- Ontology knowledge accumulation across runs (514 nodes, 886 edges)
- Thread-safe ontology persistence (locked + atomic writes)
- Swarm consensus with convergence detection
- Multi-LLM routing (Grok, OpenAI, Gemini, Claude, local Ollama)
- ML research pipeline (sklearn + PyTorch training, versioned artifacts)
- SQLite memory persistence (markets, research, analytics)
- Gamma API market discovery + Polymarket CLOB order building
- Web research (Tavily) + news headlines (NewsAPI)
- Ontology explorer dashboard
- Comprehensive test suite (~180 tests) + mypy type checking
- Repo cartography devtools (import graph, dead weight, symbol xref, etc.)

## What Doesn't Work Yet (Phase 2)

- **Zep Cloud** graph memory — stub exists (`src/onto_market/memory/zep_reader.py`), returns empty
- **Domain registry** — pluggable crypto/NBA agents, not implemented
- **Vue 3 dashboard** — not started

## Where to Focus Next

1. **Backtest swarm** — run planning_agent on 30-day resolved markets (swarm ON vs OFF), compute Brier delta
2. **Separate analysis/execution** — decouple module-level singletons in planning_agent
3. **PageRank on ontology** — surface high-influence entities, prune low-degree nodes
4. **Swarm value validation** — prove ≥2% Brier improvement over LLM-only baseline

## See Also

- `CLAUDE.md` — Claude Code guidance (architecture, env vars, commands)
- `GEMINI.md` — Gemini CLI guidance
- `REPO_MAP.md` — auto-generated annotated directory tree (`make repo-map`)
- `.cursor/rules.md` — full Cursor context (what's real, what's stub, bottlenecks)
