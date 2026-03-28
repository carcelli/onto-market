# Repository Guidelines

## Project Structure & Module Organization
This repo is an active Python project with a mixed root-plus-`src/` layout. Runtime code currently lives across top-level packages such as `agents/`, `core/`, `config/`, and `ontology/`, plus `src/` packages such as `src/connectors/`, `src/memory/`, `src/swarm/`, and `src/trading/`.

Keep new reusable developer tooling under `src/onto_market/devtools/`, specifically `src/onto_market/devtools/repo_tools/` for repo-cartography and architecture checks. Keep `scripts/` limited to thin wrappers or launch points. Put tests in `tests/` or alongside source files as `*.test.*`. Store local-only editor or assistant settings under `.claude/`; do not make runtime code depend on them.

## Build, Test, and Development Commands
The repo has a Python package manifest, a `Makefile`, and a pytest suite. Prefer these entry points:

- `pip install -e ".[dev]"` to install the project in editable mode with test dependencies
- `pytest` or `make test` for automated tests
- `make lint` for static checks
- `make repo-census` / `repo-census` for repo census reports
- `make repo-map` / `repo-map` for `REPO_MAP.md`
- `make ontology-audit` / `audit-ontology` for ontology health checks

## Coding Style & Naming Conventions
Use clear, small modules and avoid adding project logic at the repository root. Follow the formatter and linter for the language you introduce; if none exists yet, add one with the feature.

Prefer:

- `kebab-case` for Markdown and config filenames
- `PascalCase` for UI components
- `camelCase` for functions and variables
- `UPPER_SNAKE_CASE` for environment variable names

Use consistent indentation within each language, and keep JSON and Markdown cleanly formatted.

## Testing Guidelines
Every new feature should include tests. Name test files `*.test.<ext>` or `*.spec.<ext>`, and keep them near the code they cover or under `tests/` with matching paths.

Before opening a PR, run the project’s documented test and lint commands locally and note any gaps if tooling is still being introduced.

## Commit & Pull Request Guidelines
Git history is not available in this workspace, so no repository-specific commit pattern can be inferred yet. Use short, imperative commit subjects such as `Add auth service scaffold` or `Document local setup`.

PRs should include a concise summary, linked issues when relevant, testing notes, and screenshots for UI changes. Call out new environment variables and any manual setup steps.

## Security & Configuration Tips
Keep secrets in `.env` and never commit real credentials. If you add new configuration, provide a safe example file and document required keys in `README.md`.
