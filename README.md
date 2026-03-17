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

## Quick Start (in your existing environment)

```bash
conda activate market-dev

git clone https://github.com/carcelli/onto-market.git
cd onto-market

# Install Python dependencies (Polymarket Agents + Grok integration)
pip install -r requirements.txt

# MiroFish (Node + Python backend) – one-time setup
cp .env.example .env
# Edit .env with:
#   XAI_API_KEY=your_new_key
#   POLYGON_WALLET_PRIVATE_KEY=...
#   LLM_BASE_URL=https://api.x.ai/v1
#   LLM_MODEL_NAME=grok-4

npm run setup:all          # (if you want the MiroFish UI)
npm run dev                # or docker compose up -d