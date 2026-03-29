"""
MiroFish-inspired LLM client — thin wrapper around the multi-LLM router.
Use this in agents/subagents for consistent call patterns.

Supports an explicit ``provider`` / ``base_url`` override so callers can
target a specific backend (e.g. a local Ollama instance) without changing
the global ``LLM_PROVIDER`` setting.
"""
import json
import re

from onto_market.core.llm_router import llm_completion, llm_json


class LLMClient:
    def __init__(
        self,
        model: str | None = None,
        temperature: float = 0.7,
        provider: str | None = None,
        base_url: str | None = None,
    ):
        self.model = model
        self.temperature = temperature
        self.provider = provider
        self.base_url = base_url

    def _extra_kwargs(self) -> dict:
        kw: dict = {}
        if self.provider:
            kw["provider"] = self.provider
        if self.base_url:
            kw["base_url"] = self.base_url
        return kw

    def chat(self, messages: list[dict], temperature: float | None = None) -> str:
        return llm_completion(
            messages,
            temperature=temperature if temperature is not None else self.temperature,
            model=self.model,
            **self._extra_kwargs(),
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

    @classmethod
    def local(cls, model: str | None = None, base_url: str | None = None) -> "LLMClient":
        """Create a client targeting a local Ollama instance (CPU/RAM).

        Use this to keep the GPU free for training while the researcher
        LLM runs on system RAM::

            researcher = LLMClient.local()            # gpt-oss:20b default
            researcher = LLMClient.local("qwen2:7b")  # different model
        """
        from onto_market.config import config as cfg
        return cls(
            model=model or cfg.LOCAL_MODEL,
            provider="local",
            base_url=base_url or cfg.OLLAMA_BASE_URL,
        )
