# Config Surface

Env vars: **25** | Config file loads: **2**

## Environment Variables

| Variable | Files |
|----------|-------|
| `ANTHROPIC_API_KEY` | `src/onto_market/config/config.py` |
| `CHAIN_ID` | `src/onto_market/config/config.py` |
| `CLOB_API_KEY` | `src/onto_market/config/config.py` |
| `CLOB_API_URL` | `src/onto_market/config/config.py`, `src/onto_market/context.py` |
| `CLOB_PASSPHRASE` | `src/onto_market/config/config.py` |
| `CLOB_SECRET` | `src/onto_market/config/config.py` |
| `DATABASE_PATH` | `src/onto_market/config/config.py`, `src/onto_market/context.py` |
| `GOOGLE_API_KEY` | `src/onto_market/config/config.py` |
| `GROK_MODEL` | `src/onto_market/config/config.py` |
| `LLM_PROVIDER` | `src/onto_market/config/config.py` |
| `MIN_EDGE` | `src/onto_market/config/config.py` |
| `MIN_KELLY` | `src/onto_market/config/config.py` |
| `MIN_VOLUME` | `src/onto_market/config/config.py` |
| `NEWSAPI_API_KEY` | `src/onto_market/config/config.py`, `src/onto_market/connectors/news.py` |
| `OPENAI_API_KEY` | `src/onto_market/config/config.py` |
| `POLYGON_PRIVATE_KEY` | `src/onto_market/config/config.py` |
| `POLYGON_RPC_URL` | `src/onto_market/config/config.py` |
| `SAFE_MODE` | `src/onto_market/config/config.py`, `src/onto_market/context.py` |
| `SWARM_ANALYST_FRACTION` | `src/onto_market/config/config.py` |
| `SWARM_CONVERGENCE_THRESHOLD` | `src/onto_market/config/config.py` |
| `SWARM_ROUNDS` | `src/onto_market/config/config.py` |
| `SWARM_SIZE` | `src/onto_market/config/config.py` |
| `TAVILY_API_KEY` | `src/onto_market/config/config.py`, `src/onto_market/connectors/search.py` |
| `XAI_API_KEY` | `src/onto_market/config/config.py`, `src/onto_market/core/llm_router.py` |
| `ZEP_API_KEY` | `src/onto_market/config/config.py` |

## Config File Loads

| Pattern | Kind | File | Line |
|---------|------|------|-----:|
| `*.json` | json_load | `src/devtools/repo_tools/_common.py` | 106 |
| `*.json` | json_load | `src/devtools/repo_tools/symbol_xref.py` | 27 |
| `*.json` | json_load | `src/onto_market/agents/planning_agent.py` | 55 |
| `*.json` | json_load | `src/onto_market/agents/planning_agent.py` | 63 |
| `*.json` | json_load | `src/onto_market/agents/planning_agent.py` | 331 |
| `*.json` | json_load | `src/onto_market/core/llm_router.py` | 115 |
| `*.json` | json_load | `src/onto_market/devtools/repo_tools/ontology_audit.py` | 32 |
| `*.json` | json_load | `src/onto_market/devtools/repo_tools/repo_map.py` | 184 |
| `*.json` | json_load | `src/onto_market/devtools/repo_tools/symbol_xref.py` | 28 |
| `*.json` | json_load | `src/onto_market/ontology/graph.py` | 191 |
| `*.json` | json_load | `tests/test_repo_tools.py` | 49 |
| `*.json` | json_load | `tests/test_repo_tools.py` | 158 |
| `*.json` | json_load | `tests/test_repo_tools.py` | 282 |
| `.env` | dotenv_load | `src/onto_market/config/config.py` | 4 |