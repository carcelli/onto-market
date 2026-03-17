import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # xAI (Native Agent Tools)
    XAI_API_KEY: str | None = os.getenv("XAI_API_KEY")
    GROK_MODEL: str = os.getenv("GROK_MODEL", "grok-4")

    # Multi-LLM support (fallback/secondary)
    GOOGLE_API_KEY: str | None = os.getenv("GOOGLE_API_KEY")
    ANTHROPIC_API_KEY: str | None = os.getenv("ANTHROPIC_API_KEY")
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")

    # Memory
    ZEP_API_KEY: str | None = os.getenv("ZEP_API_KEY")
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "data/memory.db")

    # Polymarket / Polygon
    POLYGON_PRIVATE_KEY: str | None = os.getenv("POLYGON_PRIVATE_KEY")
    POLYGON_RPC_URL: str = os.getenv("POLYGON_RPC_URL", "https://polygon-rpc.com")
    CLOB_API_KEY: str | None = os.getenv("CLOB_API_KEY")
    CLOB_SECRET: str | None = os.getenv("CLOB_SECRET")
    CLOB_PASS_PHRASE: str | None = os.getenv("CLOB_PASS_PHRASE")
    CLOB_API_URL: str = os.getenv("CLOB_API_URL", "https://clob.polymarket.com")
    CHAIN_ID: int = int(os.getenv("CHAIN_ID", "137"))

    # Trading safety
    SAFE_MODE: bool = os.getenv("SAFE_MODE", "true").lower() == "true"

    # Research APIs
    TAVILY_API_KEY: str | None = os.getenv("TAVILY_API_KEY")
    NEWSAPI_API_KEY: str | None = os.getenv("NEWSAPI_API_KEY")

    # Swarm simulation
    SWARM_SIZE: int = int(os.getenv("SWARM_SIZE", "5000"))
    SWARM_ROUNDS: int = int(os.getenv("SWARM_ROUNDS", "5"))
    SWARM_ANALYST_FRACTION: float = float(os.getenv("SWARM_ANALYST_FRACTION", "0.03"))
    SWARM_CONVERGENCE_THRESHOLD: float = float(os.getenv("SWARM_CONVERGENCE_THRESHOLD", "0.02"))

    # Agent thresholds
    MIN_EDGE: float = float(os.getenv("MIN_EDGE", "0.03"))       # 3%
    MIN_VOLUME: float = float(os.getenv("MIN_VOLUME", "5000"))   # $5k
    MIN_KELLY: float = float(os.getenv("MIN_KELLY", "0.01"))     # 1%


config = Config()
