"""
Multi-LLM router.

Default provider: Grok/xAI — uses the OpenAI-compatible Responses API with
native agent tools (web_search, x_search).

Alternate providers (openai, gemini, claude) are routed through LiteLLM so
callers never need to change anything other than the LLM_PROVIDER env var.

  LLM_PROVIDER=grok    → xai/grok-4           (default)
  LLM_PROVIDER=openai  → openai/gpt-4o-mini
  LLM_PROVIDER=gemini  → gemini/gemini-1.5-pro
  LLM_PROVIDER=claude  → anthropic/claude-3-5-sonnet-20241022
"""
import json
import os
from typing import Any

import litellm
from openai import OpenAI

from onto_market.config import config

# Suppress noisy litellm success logs
litellm.suppress_debug_info = True

_LITELLM_MODELS: dict[str, str] = {
    "openai": "openai/gpt-4o-mini",
    "gemini": "gemini/gemini-1.5-pro",
    "claude": "anthropic/claude-3-5-sonnet-20241022",
}


def get_xai_client() -> OpenAI:
    """Return an OpenAI-compatible client pointed at the xAI endpoint."""
    return OpenAI(
        api_key=os.getenv("XAI_API_KEY"),
        base_url="https://api.x.ai/v1",
    )


def _litellm_completion(
    messages: list[dict[str, str]],
    temperature: float,
    model: str,
) -> str:
    """Call litellm for non-xAI providers."""
    response = litellm.completion(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content or ""


def llm_completion(
    messages: list[dict[str, str]],
    temperature: float = 0.7,
    model: str | None = None,
    tools: list[dict] | None = None,
    use_tools: bool = True,
    **kwargs: Any,
) -> str:
    """Route a chat completion to the configured LLM provider.

    For Grok the xAI Responses API is used with native web/x search tools.
    For all other providers LiteLLM handles the call.
    """
    provider = config.LLM_PROVIDER

    if provider == "grok":
        client = get_xai_client()
        target_model = model or config.GROK_MODEL
        active_tools = tools if tools is not None else (
            [{"type": "web_search"}, {"type": "x_search"}] if use_tools else []
        )
        response = client.responses.create(
            model=target_model,
            input=messages,
            tools=active_tools,
            temperature=temperature,
            **kwargs,
        )
        if hasattr(response, "output_text"):
            return response.output_text
        return response.choices[0].message.content or ""

    # Non-xAI provider via LiteLLM
    litellm_model = model or _LITELLM_MODELS.get(provider)
    if not litellm_model:
        raise ValueError(
            f"Unknown LLM_PROVIDER '{provider}'. "
            f"Valid options: grok, {', '.join(_LITELLM_MODELS)}"
        )
    return _litellm_completion(messages, temperature, litellm_model)


def llm_json(
    messages: list[dict[str, str]],
    temperature: float = 0.2,
    model: str | None = None,
) -> dict:
    """Route a completion that expects a JSON response.

    Tools are disabled so the model returns clean text rather than invoking
    web search, which would produce non-JSON output.
    """
    raw = llm_completion(
        messages, temperature=temperature, model=model, use_tools=False
    )
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}
