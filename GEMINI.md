# GEMINI.md

This file provides foundational context and instructional mandates for Gemini CLI when working in the `onto-market` repository.

## Project Overview

`onto-market` is a sophisticated multi-agent trading system for Polymarket prediction markets. It leverages **LangGraph** for orchestration, **LiteLLM** for multi-model support (Grok, Gemini, Claude, OpenAI), and incorporates swarm intelligence via social sentiment oracles.

### Key Features

- **LangGraph Multi-Agent Orchestration:** Complex reasoning pipelines for market analysis and trade execution.
- **Social Sentiment Oracle:** MiroFish-inspired trader crowd simulation to produce sentiment signals.
- **Hybrid Memory:** SQLite for short-term state and **Zep Cloud** for long-term graph-based market narrative memory.
- **Domain-Driven Architecture:** Pluggable registry for market domains (e.g., Crypto, NBA).
- **Quantitative Edge Detection:** ML-driven edge, EV, and Kelly criterion calculations.

## Core Technologies

- **Language:** Python 3.12+
- **Orchestration:** [LangGraph](https://github.com/langchain-ai/langgraph)
- **LLM Abstraction:** [LiteLLM](https://github.com/BerriAI/litellm)
- **Blockchain:** [Web3.py](https://github.com/ethereum/web3.py), [py-clob-client](https://github.com/polymarket/python-clob-client)
- **Data/Analytics:** Pandas, Rich, Pydantic
- **Memory:** Zep Cloud, SQLite

## Directory Structure

```text
.
├── src/onto_market/        # Single canonical package
│   ├── agents/             # LangGraph agents (planning, memory, ontology)
│   ├── config/             # Configuration management (env-driven)
│   ├── connectors/         # API wrappers (Gamma, News, Search, Polymarket)
│   ├── core/               # LLM routing, graph registry, agent base
│   ├── dashboard/          # Ontology explorer (HTML + serve)
│   ├── devtools/           # Repo cartography & health tools
│   ├── memory/             # Memory managers (SQLite, Zep stub)
│   ├── ml_research/        # ML training pipeline (sklearn + PyTorch)
│   ├── ontology/           # OntologyGraph (NetworkX DiGraph, JSON-persisted)
│   ├── polymarket_agents/  # Analytics (score_market, kelly, edge, EV)
│   ├── swarm/              # Social Sentiment Oracle (5000 agents)
│   ├── trading/            # SAFE_MODE executor, position sizing
│   └── utils/              # LLM client, retry, structured logger
├── scripts/                # Thin CLI wrappers and data scripts
├── tests/                  # Pytest suite (~180 test functions)
├── data/                   # SQLite DB + ontology JSON + ML artifacts
└── langgraph.json          # LangGraph graph registry
```

## Setup and Commands

### Environment Setup

Always use the `onto-market` conda environment with Python 3.12+.
```bash
conda activate onto-market
pip install -e ".[dev]"
cp .env.example .env   # Fill in at minimum: XAI_API_KEY
```

### Running the System

```bash
# General query via main entry point
python -m onto_market.main "Will Bitcoin hit $100k by end of 2025?"

# Run specific LangGraph agents directly
python -m onto_market.agents.planning_agent "Who will win the 2024 NBA Finals?"
python -m onto_market.agents.memory_agent "Find crypto-related markets"
```

### Development & Maintenance

```bash
# Full gate (topology + tests + mypy)
make dryrun

# Run tests
make test

# Type checking
make lint

# Refresh market data from Gamma API
make refresh
```

## Development Conventions

### State Management

Agents use `TypedDict` for state, annotated with `add_messages` from `langgraph.graph.message`. See `src/onto_market/agents/state.py`.

### Multi-LLM Routing

Use `src/onto_market/core/llm_router.py` or `src/onto_market/utils/llm_client.py` to interact with models. The system defaults to `grok` (xAI Responses API with native web/x search tools) but is switchable via the `LLM_PROVIDER` environment variable.

### Decision Thresholds

Standard trading parameters are defined in `src/onto_market/config/config.py`:
- `MIN_EDGE`: 3.0%
- `MIN_VOLUME`: $5,000
- `MIN_KELLY`: 1.0%

### Domain Plugins

New domains (e.g., "politics") should be registered in the domain registry to automatically provide specialized scanning and reasoning tools to the agents (Phase 2).

## Required Environment Variables

See `.env.example` for the full list with defaults.
- `XAI_API_KEY`: Grok/xAI (default LLM provider)
- `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY` (as needed)
- `POLYGON_PRIVATE_KEY`: For live trading
- `CLOB_API_KEY`, `CLOB_SECRET`, `CLOB_PASSPHRASE`: Polymarket CLOB access
- `TAVILY_API_KEY`: For web research nodes
- `ZEP_API_KEY`: For graph memory (Phase 2)
