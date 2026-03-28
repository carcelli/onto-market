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
	$(PYTHON) main.py "$(QUERY)"

.PHONY: memory
memory:  ## Run memory_agent (QUERY="..." make memory)
	$(PYTHON) -m agents.memory_agent "$(QUERY)"

.PHONY: plan
plan:  ## Run planning_agent (QUERY="..." make plan)
	$(PYTHON) -m agents.planning_agent "$(QUERY)"

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
	$(PYTHON) -m mypy agents/ src/ core/ config/ main.py --ignore-missing-imports

.PHONY: dryrun
dryrun: test lint  ## Gate: run before every prod push (tests + lint)
	@printf "$(GREEN)✔ dryrun passed — safe to push$(RESET)\n"

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
