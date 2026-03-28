"""
MiroFish-inspired LLM client — thin wrapper around the multi-LLM router.
Use this in agents/subagents for consistent call patterns.
"""
import json
import re

from onto_market.core.llm_router import llm_completion, llm_json


class LLMClient:
    def __init__(self, model: str | None = None, temperature: float = 0.7):
        self.model = model
        self.temperature = temperature

    def chat(self, messages: list[dict], temperature: float | None = None) -> str:
        return llm_completion(
            messages,
            temperature=temperature if temperature is not None else self.temperature,
            model=self.model,
        )

    def chat_json(self, messages: list[dict], temperature: float | None = None) -> dict:
        return llm_json(
            messages,
            temperature=temperature if temperature is not None else 0.2,
            model=self.model,
        )

    def strip_think_tags(self, text: str) -> str:
        """Remove <think>...</think> blocks (Grok/DeepSeek reasoning traces)."""
        return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

    def system(self, content: str) -> dict:
        return {"role": "system", "content": content}

    def user(self, content: str) -> dict:
        return {"role": "user", "content": content}
