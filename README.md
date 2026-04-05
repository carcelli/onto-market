# Onto-Market

**Swarm Intelligence × Polymarket Agents × Grok**  
*Ontology-powered prediction engine that simulates thousands of digital humans before every trade*

---

## Overview

Onto-Market takes Polymarket trading to the next level.

Instead of relying on a single LLM guess or basic market data, it:

1. Uses **MiroFish** to spawn **thousands of AI agents** with real personalities, memories, and behaviors  
2. Lets them interact in a high-fidelity parallel digital world (swarm simulation)  
3. Extracts emergent predictions and confidence scores  
4. Feeds those insights into the official **Polymarket Agents** framework  
5. Executes autonomous, high-edge bets with Grok-powered reasoning

The result? A system that consistently finds mispriced probabilities by **pre-simulating the crowd itself** — the ultimate edge in prediction markets.

## Why This Combo Wins

- **MiroFish** (github.com/666ghj/MiroFish) → Massive multi-agent swarm simulation (29k+ stars, trending #1)  
- **Polymarket Agents** (github.com/Polymarket/agents) → Official framework for live trading, RAG, and execution  
- **Grok (xAI)** → Best-in-class reasoning engine (via your `XAI_API_KEY`)

Together they create “ontological” market intelligence: a structured, simulated understanding of reality before the market prices it.

## Features

- 🧬 **Thousand-Agent Swarm Simulations** – Predict crowd behavior before it happens  
- ⚡ **Autonomous Trading** – Place, manage, and exit positions on Polymarket 24/7  
- 🔄 **Live Re-Simulation Loop** – Update predictions in real-time as news drops  
- 📊 **Ontology Layer** – Semantic knowledge graphs for deeper event understanding  
- 📈 **Edge Scoring & Backtesting** – Confidence metrics + historical performance tracking  
- 🔌 **Pluggable Agents** – Easily add custom strategies or new data sources  

## Quick Start

```bash
conda activate onto-market

git clone https://github.com/carcelli/onto-market.git
cd onto-market

# Install in editable mode with dev extras
pip install -e ".[dev]"

# Configure environment
cp .env.example .env
# Edit .env with your keys (at minimum: XAI_API_KEY)

# Seed local market database
make refresh   # or: python scripts/refresh_markets.py --max-events 500

# Run the planning agent
python -m onto_market.main "Will Bitcoin hit $100k?"

# Verify everything works
make dryrun    # topology check + tests + mypy
```

## Developer Tooling

Repository-health and repo-cartography logic now lives under `src/onto_market/devtools/repo_tools/`. The files in `scripts/` are compatibility wrappers, not the primary implementation surface.

For local development, install the repo in editable mode so the console entry points are available:

```bash
pip install -e ".[dev]"
```

Useful commands:

- `repo-census` or `make repo-census` to write `reports/repo_census.json` and `reports/repo_census.md`
- `repo-map` or `make repo-map` to regenerate `REPO_MAP.md`
- `audit-ontology` or `make ontology-audit` to inspect ontology graph health

This keeps repo-specific tooling inside `onto-market` while preserving a clean extraction seam if it later needs to become its own package.
