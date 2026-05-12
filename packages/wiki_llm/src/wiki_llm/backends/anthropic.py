"""Anthropic API backend for model inference.

Usage:
    from wiki_llm.backends import AnthropicBackend, ModelConfig
    
    backend = AnthropicBackend()
    response = backend.run(prompt, config)
"""
from __future__ import annotations

import os

from wiki_llm.backends.base import ModelBackend
from wiki_llm.backends.bedrock import log_context_stats
from wiki_llm.backends.types import ModelConfig, ModelResponse


class AnthropicBackend(ModelBackend):
    """Backend using Anthropic API for Claude models."""

    def __init__(
        self,
        model: str = "claude-sonnet-4-20250514",
        api_key_env: str = "ANTHROPIC_API_KEY",
        max_tokens: int = 8192,
        temperature: float = 0.1,
        **kwargs,
    ):
        self.model = model
        self.api_key_env = api_key_env
        self.max_tokens = max_tokens
        self.temperature = temperature
        self._client = None

    @property
    def client(self):
        """Lazy-load Anthropic client."""
        if self._client is None:
            try:
                import anthropic
                api_key = os.environ.get(self.api_key_env)
                if not api_key:
                    raise ValueError(
                        f"Environment variable {self.api_key_env} not set")
                self._client = anthropic.Anthropic(api_key=api_key)
            except ImportError:
                raise ImportError(
                    "anthropic is required for Anthropic backend. Install with: pip install anthropic")
        return self._client

    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (anthropic)")

        system_prompt = self._build_system_prompt(config)

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=system_prompt,
                messages=[{"role": "user", "content": prompt}],
            )

            output_text = response.content[0].text if response.content else ""
            stop_reason = response.stop_reason
            usage = {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
            }

            log_paths = self._save_logs(config, prompt, output_text, {
                "backend": "anthropic",
                "model": self.model,
                "stop_reason": stop_reason,
                "usage": usage,
            })

            truncated = stop_reason == "max_tokens"

            return ModelResponse(
                success=stop_reason == "end_turn" and not truncated,
                output=output_text,
                log_paths=log_paths,
                stop_reason=stop_reason,
                usage=usage,
                truncated=truncated,
            )

        except Exception as e:
            error_msg = str(e)
            log_paths = self._save_logs(config, prompt, "", {
                "backend": "anthropic",
                "model": self.model,
                "error": error_msg,
            })
            return ModelResponse(
                success=False,
                output="",
                log_paths=log_paths,
                error=error_msg,
            )
