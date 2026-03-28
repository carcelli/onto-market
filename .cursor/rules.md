# onto-market Cursor Rules

## Project Identity

onto-market is a Polymarket prediction market trading system (v0.1.0 advanced prototype) that combines LangGraph multi-agent orchestration, ontology-graph accumulation via NetworkX, and OASIS-style heterogeneous swarm simulation to find mispriced prediction markets. Query in, BET/WATCH/PASS out.

## Current State (v0.1.0)

- **Maturity:** functional advanced prototype — runs end-to-end but not production-hardened
- **Python:** `>=3.11` (pyproject.toml is canonical; GEMINI.md incorrectly says 3.12+)
- **Environment:** conda `onto-market`, install via `pip install -e ".[dev]"`
- **Build:** pyproject.toml + setuptools; `requirements.txt` exists but is stale (drift risk)
- **No CI/CD, no Docker, no deployment manifest**
- **SAFE_MODE=true by default** (dry-run trading; live orders require `--live` flag)
- **Single developer, ~15 commits**

## What Is Real (Phase 1)

### Agents (LangGraph)
- `agents/planning_agent.py` — 7-node pipeline: research → ontology → stats → probability → swarm → decision → trade
- `agents/memory_agent.py` — 4-node DB-first pipeline: memory → enrichment → reasoning → decide
- `agents/ontology_agent.py` — LLM triple extraction from research context + graph query node
- `agents/state.py` — canonical state definitions (AgentState, MemoryAgentState, PlanningState as TypedDicts)

### Ontology
- `ontology/graph.py` — `OntologyGraph` (NetworkX DiGraph), `Triple` dataclass, closed predicate vocabulary (9 relations), JSON persistence at `data/ontology.json`, `context_for()` token-overlap retrieval, `prune()`, `stats()`
- Graph **accumulates across runs** — each planning_agent invocation extracts and ingests new triples

### Swarm
- `src/swarm/oracle.py` — `SocialSentimentOracle`: N agents (default 5000), convergence-based dynamics, confidence-weighted median aggregation
- `src/swarm/archetypes.py` — 6 archetypes: BULL (25%), BEAR (25%), ANALYST (3%, calls LLM), CONTRARIAN (12%, inverts influence), NOISE_TRADER (25%), INSIDER (10%)
- `src/swarm/dynamics.py` — Watts-Strogatz small-world network (k=6, p=0.1), influence propagation, convergence check (std < 0.02)

### Core
- `core/llm_router.py` — Multi-LLM via LiteLLM; Grok/xAI uses Responses API with native web+x search; openai/gemini/claude via LiteLLM completion
- `config/config.py` — `Config` class, all settings from env vars
- `src/context.py` — `AppContext` lazy singleton dependency injection

### Connectors
- `src/connectors/gamma.py` — GammaConnector: paginated market fetch, search, market-by-id
- `src/connectors/polymarket.py` — PolymarketConnector: Web3 wallet, CLOB client, order building, SAFE_MODE gate
- `src/connectors/search.py` — SearchConnector (Tavily web search)
- `src/connectors/news.py` — NewsConnector (NewsAPI headlines)

### Memory & Analytics
- `src/memory/manager.py` — MemoryManager: SQLite CRUD for markets, research, analytics tables
- `src/polymarket_agents/utils/analytics.py` — `score_market()`, `kelly_fraction()`, `calculate_edge()`, `expected_value()`
- `src/polymarket_agents/utils/objects.py` — `Market`, `ResearchNote` dataclasses
- `src/polymarket_agents/utils/database.py` — `Database` SQLite wrapper

### Trading
- `src/trading/executor.py` — TradeExecutor: LLM-powered event filtering, superforecasting, half-Kelly sizing
- `src/trading/trader.py` — Trader: discover → filter → map → superforecast → execute pipeline

### Utilities
- `src/utils/llm_client.py` — LLMClient wrapper (chat, chat_json, system/user helpers)
- `src/utils/retry.py` — `@retry_with_backoff` (tenacity), `RetryableAPIClient`
- `src/utils/logger.py` — `get_logger()`: console + rotating file handler

### Tests
- `tests/test_analytics.py` — edge, Kelly, EV unit tests
- `tests/test_memory.py` — MemoryManager CRUD tests
- `tests/test_swarm.py` — archetypes, dynamics, oracle tests
- `tests/test_trading.py` — trade execution tests
- `tests/test_planning_agent.py` — normalization, scoring, Gamma helpers
- `tests/test_integration.py` — full pipeline integration

### Scripts & Entry Points
- `main.py` — CLI entry point (`onto-market <query>`)
- `scripts/cli.py` — Typer CLI with analyze/scan/trade/swarm commands
- `scripts/refresh_markets.py` — seed markets.db from Gamma API

## What Is Phase 2 (Stubs / Missing)

- `src/memory/zep_reader.py` — `ZepEntityReader` is a stub: `get_facts()` returns `[]`, `store_fact()` is a no-op
- **Domain registry** (`domains/registry.py`) — mentioned in docs, does not exist
- **Vue 3 dashboard** — does not exist
- `core/agent_base.py` — `BaseAgent`/`AgentProtocol` defined but unused (agents use functional StateGraph)
- `core/state.py` — duplicates `agents/state.py` (vestigial)

## Differentiators

1. **Ontology accumulation** — the knowledge graph persists across runs. Each planning_agent invocation extracts triples from research and ingests them. Subsequent queries benefit from prior knowledge via `context_for()`. This compounds over time.
2. **Heterogeneous swarm simulation** — unlike single-LLM-estimate systems, onto-market spawns thousands of agents with distinct biases (6 archetypes) on a Watts-Strogatz network and runs OASIS-style influence dynamics to produce consensus more robust than any single estimate. Only 3% of agents call the LLM (ANALYST archetype); the rest use fast heuristic perturbations.

## Immediate Bottlenecks

1. **Packaging drift** — `requirements.txt` contains only `litellm` while `pyproject.toml` has the real dependency list. `setuptools.packages.find` uses `where = ["src", "."]` which is fragile.
2. **Analysis/execution coupled** — `planning_agent.py` instantiates module-level singletons (MemoryManager, GammaConnector, etc.) at import time. Importing triggers DB creation and HTTP session init. Testing and dry analysis require a live Gamma connection.
3. **JSON ontology not thread-safe** — `OntologyGraph._save()` writes the entire graph to a single JSON file. Concurrent writes (two planning_agent runs) will corrupt data. No file locking.
4. **Phase 2 stubs add false complexity** — ZepEntityReader, BaseAgent, and duplicate state.py are imported but do nothing.

## Leverage Order

1. **Unify packaging** — delete `requirements.txt`, fix `pyproject.toml` packages.find, reconcile Python version claims
2. **Separate analysis from execution** — use AppContext consistently, make singletons lazy, allow dry analysis without network
3. **Strengthen ontology** — add file locking to `_save/_load`, consider SQLite backend, add typed entity categories, run PageRank audits
4. **Backtest swarm** — add historical market resolution data, replay swarm predictions, track calibration (Brier score)

## Development Environment

```bash
conda activate onto-market
pip install -e ".[dev]"
make test          # pytest tests/ -x -q
make lint          # mypy type check
make dryrun        # tests + lint gate
make repo-map       # regenerate REPO_MAP.md
make ontology-audit # analyze ontology graph
```

Default LLM: `LLM_PROVIDER=grok` (xAI). Set `XAI_API_KEY`. Switch with `LLM_PROVIDER=openai|gemini|claude`.

Decision thresholds: `MIN_EDGE=3%`, `MIN_VOLUME=$5k`, `MIN_KELLY=1%`.

## Code Conventions

- **State:** TypedDicts in `agents/state.py`
- **LangGraph nodes:** plain functions `(state: dict) -> dict` returning partial state updates
- **Connectors:** class-based, all HTTP methods decorated with `@retry_with_backoff`
- **Logging:** `get_logger(__name__)` everywhere (console + rotating file)
- **JSON from LLM:** use `llm.chat_json()` which strips markdown fences and parses
- **Config:** class-level attributes on `Config` in `config/config.py`, all from env vars with defaults
- **CLI output:** Rich tables and panels (consistent across main.py, cli.py, refresh_markets.py)

## Key Files

| File | Purpose |
|------|---------|
| `agents/planning_agent.py` | Central 7-node LangGraph pipeline |
| `ontology/graph.py` | OntologyGraph — knowledge accumulation engine |
| `src/swarm/oracle.py` | SocialSentimentOracle — swarm consensus |
| `core/llm_router.py` | Multi-LLM routing (Grok/OpenAI/Gemini/Claude) |
| `config/config.py` | All configuration and env var loading |
| `src/connectors/gamma.py` | Polymarket market discovery |
| `src/memory/manager.py` | SQLite memory persistence |
| `src/polymarket_agents/utils/analytics.py` | Edge, Kelly, EV calculations |
| `src/trading/executor.py` | Trade sizing and execution |
| `agents/state.py` | Canonical TypedDict state definitions |

For the full annotated directory tree, see `REPO_MAP.md` (generate with `make repo-map`).
