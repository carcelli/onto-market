# Repository Guidelines

## Project Structure & Module Organization
This repository is currently a minimal scaffold. The committed root files are [`README.md`](/home/orson-dev/projects/onto-market/README.md), [`.env`](/home/orson-dev/projects/onto-market/.env), and [`.claude/settings.local.json`](/home/orson-dev/projects/onto-market/.claude/settings.local.json).

Keep the root directory sparse. When application code is added, place runtime modules in `src/`, shared assets in `assets/`, and tests in `tests/` or alongside source files as `*.test.*`. Store local-only editor or assistant settings under `.claude/`; do not make runtime code depend on them.

## Build, Test, and Development Commands
No package manifest, Makefile, or test runner is committed yet, so there is no standard build or test command today.

When introducing tooling, expose predictable entry points and document them in both this file and `README.md`, for example:

- `npm run dev` or `pnpm dev` for local development
- `npm test` or `pnpm test` for automated tests
- `npm run lint` for formatting and static checks

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
