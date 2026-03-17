# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`onto-market` is a Polymarket prediction market trading system built with:
- **LangGraph** multi-agent orchestration (memory_agent + planning_agent)
- **Multi-LLM** via LiteLLM (Grok/xAI default; OpenAI, Gemini, Claude supported)
- **MiroFish-inspired** utils: LLMClient, retry_with_backoff, structured logger
- **Domain-driven pluggable** scanner/agent pattern (crypto + NBA planned for Phase 2)
- **Social Sentiment Oracle** subagent (OASIS-style swarm sim, Phase 2)
- **Zep Cloud** knowledge graph memory (Phase 2 stub in place)

Reference implementation: `/home/orson-dev/projects/polymarket_langchain/`

## Python Environment

**Always use the `onto-market` conda environment.**

```bash
conda activate onto-market
pip install -e ".[dev]"
```

## Commands

```bash
# Seed local DB from Gamma API
python scripts/refresh_markets.py --max-events 500

# Run agents
python -m agents.memory_agent "Find crypto markets"
python -m agents.planning_agent "Will Bitcoin hit $100k?"

# CLI entry point
python main.py "Will Bitcoin hit $100k?"

# Tests (all must pass)
python -m pytest tests/ -x -q

# Single test
python -m pytest tests/test_analytics.py -x -q
```

## Architecture

### Directory layout

```
├── agents/                    # LangGraph agents
│   ├── state.py               # AgentState, MemoryAgentState, PlanningState TypedDicts
│   ├── memory_agent.py        # DB-first agent: memory→enrichment→reasoning→decide
│   └── planning_agent.py      # Full pipeline: research→stats→probability→decision
├── config/
│   └── config.py              # Config class (env vars, LLM models, thresholds)
├── core/
│   └── llm_router.py          # LiteLLM multi-LLM router (llm_completion, llm_json)
├── src/
│   ├── utils/                 # MiroFish-inspired utils
│   │   ├── llm_client.py      # LLMClient wrapping the router
│   │   ├── retry.py           # retry_with_backoff (tenacity), RetryableAPIClient
│   │   └── logger.py          # get_logger() — console + rotating file
│   ├── connectors/            # External API clients
│   │   ├── gamma.py           # Gamma Markets API (market discovery, paginated)
│   │   ├── search.py          # Tavily web search
│   │   └── news.py            # NewsAPI headlines
│   ├── memory/
│   │   ├── manager.py         # SQLite: upsert_market, search_markets, store_analytics
│   │   └── zep_reader.py      # Zep Cloud stub (Phase 2)
│   └── polymarket_agents/
│       └── utils/
│           ├── objects.py     # Market, ResearchNote dataclasses
│           ├── analytics.py   # score_market, kelly_fraction, calculate_edge, expected_value
│           └── database.py    # Database SQLite wrapper
├── scripts/
│   └── refresh_markets.py     # Seed markets.db from Gamma API
├── tests/
│   ├── conftest.py            # sample_market, db_path fixtures
│   ├── test_analytics.py      # Edge/Kelly/EV unit tests
│   └── test_memory.py         # MemoryManager unit tests
├── langgraph.json             # LangGraph graph registry
├── main.py                    # CLI entry point
└── pyproject.toml
```

### LangGraph agents

**memory_agent** — DB-first, Gamma enrichment on demand:
```
memory_node → enrichment_node → reasoning_node → decide_node
```
Enriches from Gamma only when query contains live/current/today keywords or DB has no results.

**planning_agent** — full analysis pipeline:
```
research_node → stats_node → probability_node → decision_node
```
Decision thresholds (from `config`): `MIN_EDGE=3%`, `MIN_VOLUME=$5k`, `MIN_KELLY=1%`.
Output: **BET** / **WATCH** / **PASS** + edge, EV, Kelly fraction.

### Multi-LLM routing

Set `LLM_PROVIDER` in `.env` to switch models:
- `grok` → `xai/grok-beta` (default)
- `openai` → `openai/gpt-4o-mini`
- `gemini` → `gemini/gemini-1.5-pro`
- `claude` → `anthropic/claude-3-5-sonnet-20241022`

### Adding a new connector or agent

- New connectors go in `src/connectors/`; wrap all HTTP calls with `@retry_with_backoff`
- New agents go in `agents/`; add state to `agents/state.py` if needed
- Register new graphs in `langgraph.json`

## Key Environment Variables

- `LLM_PROVIDER` — `grok` | `openai` | `gemini` | `claude`
- `XAI_API_KEY` — Grok/xAI (default LLM)
- `OPENAI_API_KEY` — OpenAI
- `GOOGLE_API_KEY` — Gemini
- `ANTHROPIC_API_KEY` — Claude
- `DATABASE_PATH` — SQLite path (default: `data/memory.db`)
- `TAVILY_API_KEY` — web search (optional)
- `NEWSAPI_API_KEY` — news headlines (optional)
- `POLYGON_PRIVATE_KEY` — live order execution (optional)
- `ZEP_API_KEY` — Zep Cloud graph memory (Phase 2, optional)
- `SWARM_SIZE` — Social Sentiment Oracle crowd size (default: 5000)
- `MIN_EDGE` / `MIN_VOLUME` / `MIN_KELLY` — decision thresholds

## Phase 2 (deferred)

- Full OASIS/MiroFish swarm simulation → Social Sentiment Oracle subagent
- Wire `ZepEntityReader` in `src/memory/zep_reader.py`
- Domain registry (`domains/registry.py`) with crypto + NBA pluggable agents
- Vue 3 trading dashboard
