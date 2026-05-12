"""OpenAI API backend for model inference.

Usage:
    from wiki_llm.backends import OpenAIBackend, ModelConfig
    
    backend = OpenAIBackend()
    response = backend.run(prompt, config)
"""
from __future__ import annotations

import os

from wiki_llm.backends.base import ModelBackend
from wiki_llm.backends.bedrock import log_context_stats
from wiki_llm.backends.types import ModelConfig, ModelResponse


class OpenAIBackend(ModelBackend):
    """Backend using OpenAI API for GPT models."""

    def __init__(
        self,
        model: str = "gpt-4o",
        api_key_env: str = "OPENAI_API_KEY",
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
        """Lazy-load OpenAI client."""
        if self._client is None:
            try:
                import openai
                api_key = os.environ.get(self.api_key_env)
                if not api_key:
                    raise ValueError(
                        f"Environment variable {self.api_key_env} not set")
                self._client = openai.OpenAI(api_key=api_key)
            except ImportError:
                raise ImportError(
                    "openai is required for OpenAI backend. Install with: pip install openai")
        return self._client

    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (openai)")

        system_prompt = self._build_system_prompt(config)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature,
            )

            output_text = response.choices[0].message.content or ""
            finish_reason = response.choices[0].finish_reason
            usage = {
                "input_tokens": response.usage.prompt_tokens,
                "output_tokens": response.usage.completion_tokens,
            }

            log_paths = self._save_logs(config, prompt, output_text, {
                "backend": "openai",
                "model": self.model,
                "finish_reason": finish_reason,
                "usage": usage,
            })

            truncated = finish_reason == "length"

            return ModelResponse(
                success=finish_reason == "stop" and not truncated,
                output=output_text,
                log_paths=log_paths,
                stop_reason=finish_reason,
                usage=usage,
                truncated=truncated,
            )

        except Exception as e:
            error_msg = str(e)
            log_paths = self._save_logs(config, prompt, "", {
                "backend": "openai",
                "model": self.model,
                "error": error_msg,
            })
            return ModelResponse(
                success=False,
                output="",
                log_paths=log_paths,
                error=error_msg,
            )
