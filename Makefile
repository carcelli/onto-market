# onto-market Makefile
# Usage: make <target>
# Assumes the `onto-market` conda environment is active.
# Run `conda activate onto-market` first, then use `make`.

SHELL        := /bin/bash
PYTHON       := python
PIP          := pip
ENV_NAME     := onto-market
DB_PATH      := data/memory.db
TEST_DIR     := tests
MAX_MARKETS  ?= 500
PYTHONPATH   := src:.

.DEFAULT_GOAL := help

# ── Colors ────────────────────────────────────────────────────────────────────
CYAN  := \033[1;36m
RESET := \033[0m
GREEN := \033[1;32m
YELLOW:= \033[1;33m
RED   := \033[1;31m

# ── Helpers ───────────────────────────────────────────────────────────────────
define log
	@printf "$(CYAN)▶ $(1)$(RESET)\n"
endef

# ── Targets ───────────────────────────────────────────────────────────────────

.PHONY: help
help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  $(CYAN)%-18s$(RESET) %s\n", $$1, $$2}'

# ── Setup ─────────────────────────────────────────────────────────────────────

.PHONY: setup
setup: _check-env install data refresh  ## Full first-time setup (install + seed DB)
	$(call log,Setup complete — run: python main.py \"Will Bitcoin hit \$$100k?\")

.PHONY: install
install: _check-env  ## pip install -e .[dev]
	$(call log,Installing package in editable mode with dev extras)
	$(PIP) install -e ".[dev]" --quiet

.PHONY: data
data:  ## Create data/ directory if missing
	@mkdir -p data
	$(call log,data/ directory ready)

.PHONY: refresh
refresh: data  ## Seed/refresh local market DB from Gamma API
	$(call log,Seeding $(DB_PATH) — fetching up to $(MAX_MARKETS) markets)
	$(PYTHON) scripts/refresh_markets.py --max-events $(MAX_MARKETS)

# ── Development ───────────────────────────────────────────────────────────────

.PHONY: run
run:  ## Run the CLI (QUERY="..." make run)
	$(PYTHON) -m onto_market.main "$(QUERY)"

.PHONY: memory
memory:  ## Run memory_agent (QUERY="..." make memory)
	$(PYTHON) -m onto_market.agents.memory_agent "$(QUERY)"

.PHONY: plan
plan:  ## Run planning_agent (QUERY="..." make plan)
	$(PYTHON) -m onto_market.agents.planning_agent "$(QUERY)"

# ── Quality gates ─────────────────────────────────────────────────────────────

.PHONY: test
test:  ## Run full test suite
	$(call log,Running test suite)
	$(PYTHON) -m pytest $(TEST_DIR)/ -x -q

.PHONY: test-v
test-v:  ## Verbose test run with coverage summary
	$(PYTHON) -m pytest $(TEST_DIR)/ -v --tb=short

.PHONY: lint
lint:  ## mypy type-check
	$(call log,Running mypy)
	$(PYTHON) -m mypy src/onto_market/ --ignore-missing-imports

.PHONY: dryrun
dryrun: test lint  ## Gate: run before every prod push (tests + lint)
	@printf "$(GREEN)✔ dryrun passed — safe to push$(RESET)\n"

# ── Analysis ─────────────────────────────────────────────────────────────────

.PHONY: repo-census
repo-census:  ## Generate reports/repo_census.{json,md}
	$(call log,Generating repo census reports)
	$(PYTHON) scripts/repo_census.py
	@printf "$(GREEN)✔ repo census updated$(RESET)\n"

.PHONY: repo-map
repo-map:  ## Generate REPO_MAP.md from directory tree
	$(call log,Generating REPO_MAP.md)
	$(PYTHON) scripts/generate_repo_map.py
	@printf "$(GREEN)✔ REPO_MAP.md updated$(RESET)\n"

.PHONY: ontology-audit
ontology-audit:  ## Analyze ontology graph (PageRank, components, centrality)
	$(call log,Running ontology audit)
	$(PYTHON) scripts/audit_ontology.py

.PHONY: ontology-prune
ontology-prune:  ## Audit + prune low-confidence ontology edges (destructive)
	$(call log,Auditing and pruning ontology graph)
	$(PYTHON) scripts/audit_ontology.py --prune

# ── Repo Cartography ──────────────────────────────────────────────────────────

.PHONY: cartography
cartography:  ## Run full cartography pipeline (all 11 tools → reports/)
	$(call log,Running full repo cartography pipeline)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.cartography
	@printf "$(GREEN)✔ Cartography complete — see reports/$(RESET)\n"

.PHONY: import-graph
import-graph:  ## Build AST import graph (JSON + Mermaid + DOT)
	$(call log,Building import graph)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.import_graph
	@printf "$(GREEN)✔ import graph updated$(RESET)\n"

.PHONY: boundary-matrix
boundary-matrix:  ## Collapse import graph to domain-level coupling matrix
	$(call log,Computing boundary matrix)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.boundary_matrix
	@printf "$(GREEN)✔ boundary matrix updated$(RESET)\n"

.PHONY: entrypoint-map
entrypoint-map:  ## Discover all real execution entrypoints
	$(call log,Mapping entrypoints)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.entrypoint_map
	@printf "$(GREEN)✔ entrypoint map updated$(RESET)\n"

.PHONY: symbol-index
symbol-index:  ## Index all classes, functions, dataclasses, enums
	$(call log,Indexing symbols)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.symbol_index
	@printf "$(GREEN)✔ symbol index updated$(RESET)\n"

.PHONY: symbol-xref
symbol-xref:  ## Cross-reference symbol usages (requires symbol-index to run first)
	$(call log,Cross-referencing symbols)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.symbol_xref
	@printf "$(GREEN)✔ symbol xref updated$(RESET)\n"

.PHONY: test-map
test-map:  ## Map source modules to tests, show coverage gaps
	$(call log,Mapping test coverage)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.test_map
	@printf "$(GREEN)✔ test map updated$(RESET)\n"

.PHONY: config-surface
config-surface:  ## Surface all env vars and config file loads
	$(call log,Scanning config surface)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.config_surface
	@printf "$(GREEN)✔ config surface updated$(RESET)\n"

.PHONY: cycle-check
cycle-check:  ## Detect circular imports (strongly connected components)
	$(call log,Detecting import cycles)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.cycle_detector
	@printf "$(GREEN)✔ cycle check done$(RESET)\n"

.PHONY: dead-weight
dead-weight:  ## Flag unreachable files and stale copies
	$(call log,Finding dead weight)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.dead_weight
	@printf "$(GREEN)✔ dead weight report updated$(RESET)\n"

.PHONY: arch-drift
arch-drift:  ## Check architecture boundary rules, emit violations
	$(call log,Auditing architecture drift)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m onto_market.devtools.repo_tools.architecture_drift
	@printf "$(GREEN)✔ architecture drift audit done$(RESET)\n"

.PHONY: repo-health
repo-health: cartography  ## Alias for cartography (full pipeline)
	@printf "$(GREEN)✔ full repo health check done$(RESET)\n"

.PHONY: dashboard
dashboard:  ## Launch the Streamlit repo ontology dashboard
	$(call log,Launching dashboard at http://localhost:8501)
	$(PYTHON) -m streamlit run reports/streamlit_app.py

# ── ML Research ──────────────────────────────────────────────────────────

.PHONY: fetch-resolved
fetch-resolved:  ## Download resolved markets from Gamma → SQLite
	$(call log,Fetching resolved markets)
	$(PYTHON) scripts/fetch_resolved.py
	@printf "$(GREEN)✔ resolved markets fetched$(RESET)\n"

.PHONY: ml-train
ml-train:  ## Single training run → save artifact
	$(call log,Training ML forecaster)
	$(PYTHON) scripts/ml_train.py
	@printf "$(GREEN)✔ training complete$(RESET)\n"

.PHONY: ml-research
ml-research:  ## Start the autoresearch experiment loop
	$(call log,Starting autoresearch loop)
	$(PYTHON) scripts/ml_research.py
	@printf "$(GREEN)✔ autoresearch complete$(RESET)\n"

.PHONY: ml-train-torch
ml-train-torch:  ## Single PyTorch training run → save artifact
	$(call log,Training PyTorch forecaster)
	$(PYTHON) scripts/ml_train_torch.py
	@printf "$(GREEN)✔ torch training complete$(RESET)\n"

.PHONY: ml-research-torch
ml-research-torch:  ## Start the autoresearch loop (PyTorch mode, local LLM)
	$(call log,Starting autoresearch loop — torch mode)
	$(PYTHON) scripts/ml_research.py --mode torch --researcher local
	@printf "$(GREEN)✔ torch autoresearch complete$(RESET)\n"

.PHONY: ml-research-local
ml-research-local:  ## Autoresearch: local LLM on CPU, training on GPU
	$(call log,Starting autoresearch — researcher=local (Ollama on CPU/RAM))
	$(PYTHON) scripts/ml_research.py --mode sklearn --researcher local
	@printf "$(GREEN)✔ local autoresearch complete$(RESET)\n"

.PHONY: ml-research-local-torch
ml-research-local-torch:  ## Autoresearch (torch): local LLM on CPU, training on GPU
	$(call log,Starting autoresearch — torch mode + researcher=local)
	$(PYTHON) scripts/ml_research.py --mode torch --researcher local
	@printf "$(GREEN)✔ local torch autoresearch complete$(RESET)\n"

.PHONY: ml-status
ml-status:  ## Print latest ML artifact metadata + Brier score
	@$(PYTHON) scripts/ml_status.py

# ── Maintenance ───────────────────────────────────────────────────────────────

.PHONY: clean
clean:  ## Remove caches, egg-info, pyc files
	$(call log,Cleaning build artifacts)
	@find . -type d -name "__pycache__" -not -path "./.venv/*" -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -not -path "./.venv/*" -delete 2>/dev/null || true
	@rm -rf *.egg-info onto_market.egg-info .pytest_cache .mypy_cache

.PHONY: clean-db
clean-db:  ## Delete local market database (destructive!)
	@printf "$(RED)Deleting $(DB_PATH)...$(RESET)\n"
	@rm -f $(DB_PATH)

.PHONY: reset
reset: clean clean-db setup  ## Nuclear reset: clean + wipe DB + full setup

# ── Guard ─────────────────────────────────────────────────────────────────────

.PHONY: _check-env
_check-env:
	@if [ "$$(conda info --envs 2>/dev/null | grep '^\*' | awk '{print $$1}')" != "$(ENV_NAME)" ] && \
	    [ "$$(basename $${CONDA_DEFAULT_ENV:-})" != "$(ENV_NAME)" ]; then \
		printf "$(YELLOW)⚠  Warning: active conda env is not '$(ENV_NAME)'.\n"; \
		printf "   Run: conda activate $(ENV_NAME)$(RESET)\n"; \
	fi
