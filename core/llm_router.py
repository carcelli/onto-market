"""
xAI Native Multi-LLM router.
Supports Grok (xAI) with native Agent Tools (web_search, x_search).
"""
import json
import os
from typing import Any

from openai import OpenAI
from dotenv import load_dotenv

from config import config

load_dotenv()


def get_client() -> OpenAI:
    """Get the xAI client configured with the correct base URL."""
    return OpenAI(
        api_key=os.getenv("XAI_API_KEY"),
        base_url="https://api.x.ai/v1"
    )


def llm_completion(
    messages: list[dict[str, str]],
    temperature: float = 0.7,
    model: str | None = None,
    tools: list[dict] | None = None,
    **kwargs: Any,
) -> str:
    """Route a chat completion to the configured LLM provider (default Grok)."""
    client = get_client()
    target_model = model or os.getenv("GROK_MODEL", "grok-4")

    # Use the new Responses API for native search tools
    response = client.responses.create(
        model=target_model,
        input=messages,
        tools=tools or [{"type": "web_search"}, {"type": "x_search"}],
        temperature=temperature,
        **kwargs
    )
    
    # Extract text from the new response format or fallback to standard choices
    if hasattr(response, "output_text"):
        return response.output_text
    
    return response.choices[0].message.content or ""


def llm_json(
    messages: list[dict[str, str]],
    temperature: float = 0.2,
    model: str | None = None,
) -> dict:
    """Route a completion that expects a JSON response."""
    raw = llm_completion(messages, temperature=temperature, model=model)
    # Strip markdown fences if present
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}
