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
├── agents/             # LangGraph agent definitions (planning, memory)
├── config/             # Configuration management (Pydantic-style)
├── core/               # Core agent base classes and LLM routing
├── scripts/            # Database seeding and maintenance scripts
├── src/
│   ├── polymarket_agents/ # Domain logic (crypto, nba), ML models, analytics
│   ├── connectors/     # API wrappers (Gamma, News, Search, Polymarket)
│   ├── memory/         # Memory managers (SQLite, Zep)
│   └── utils/          # Shared utilities (logging, LLM client)
├── tests/              # Pytest suite
├── main.py             # CLI entry point
└── langgraph.json      # LangGraph Cloud / Studio configuration
```

## Setup and Commands

### Environment Setup
Always use a Python 3.12 environment.
```bash
pip install -e ".[dev]"
```

### Running the System
```bash
# General query via main entry point
python main.py "Will Bitcoin hit $100k by end of 2025?"

# Run specific LangGraph agents directly
python -m agents.planning_agent "Who will win the 2024 NBA Finals?"
python -m agents.memory_agent "Find crypto-related markets"
```

### Development & Maintenance
```bash
# Run tests
python -m pytest tests/

# Refresh market data from Gamma API
python scripts/python/refresh_markets.py --max-events 500

# Type checking
mypy .
```

## Development Conventions

### State Management
Agents use `TypedDict` for state, often annotated with `add_messages` from `langgraph.graph.message`. See `agents/state.py`.

### Multi-LLM Routing
Use `core/llm_router.py` or `src/utils/llm_client.py` to interact with models. The system defaults to `grok` (via LiteLLM `xai/grok-beta`) but is easily switchable via the `LLM_PROVIDER` environment variable.

### Decision Thresholds
Standard trading parameters are defined in `config/config.py`:
- `MIN_EDGE`: 3.0%
- `MIN_VOLUME`: $5,000
- `MIN_KELLY`: 1.0%

### Domain Plugins
New domains (e.g., "politics") should be registered in the domain registry to automatically provide specialized scanning and reasoning tools to the agents.

## Required Environment Variables
See `config/config.py` for full details.
- `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY`, `XAI_API_KEY` (as needed)
- `POLYGON_PRIVATE_KEY`: For live trading
- `CLOB_API_KEY`, `CLOB_SECRET`, `CLOB_PASSPHRASE`: Polymarket CLOB access
- `TAVILY_API_KEY`: For web research nodes
- `ZEP_API_KEY`: For graph memory
