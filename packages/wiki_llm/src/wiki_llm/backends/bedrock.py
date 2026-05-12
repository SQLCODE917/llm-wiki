"""AWS Bedrock backend for model inference.

Usage:
    from wiki_llm.backends import BedrockBackend, ModelConfig
    
    backend = BedrockBackend()
    response = backend.run(prompt, config)
"""
from __future__ import annotations

import os

from wiki_llm.backends.base import ModelBackend
from wiki_llm.backends.types import ModelConfig, ModelResponse


def log_context_stats(text: str, label: str = "context") -> None:
    """Log context statistics (approximate tokens)."""
    # Rough approximation: 1 token ≈ 4 chars for English
    chars = len(text)
    approx_tokens = chars // 4
    print(f"  {label}: ~{approx_tokens} tokens ({chars} chars)")


class BedrockBackend(ModelBackend):
    """Backend using AWS Bedrock for managed model inference."""

    def __init__(
        self,
        model_id: str = "qwen.qwen3-coder-30b-a3b-v1:0",
        region: str | None = None,
        max_tokens: int = 16384,
        temperature: float = 0.1,
        **kwargs,
    ):
        self.model_id = model_id
        self.region = region or os.environ.get("AWS_REGION", "us-east-1")
        self.max_tokens = max_tokens
        self.temperature = temperature
        self._client = None

    @property
    def client(self):
        """Lazy-load boto3 client."""
        if self._client is None:
            try:
                import boto3
                self._client = boto3.client(
                    "bedrock-runtime", region_name=self.region)
            except ImportError:
                raise ImportError(
                    "boto3 is required for Bedrock backend. Install with: pip install boto3")
        return self._client

    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} user prompt")

        system_prompt = self._build_system_prompt(config)
        log_context_stats(
            system_prompt, label=f"{config.prefix} system prompt")

        try:
            response = self.client.converse(
                modelId=self.model_id,
                messages=[{"role": "user", "content": [{"text": prompt}]}],
                inferenceConfig={
                    "maxTokens": self.max_tokens,
                    "temperature": self.temperature,
                },
                system=[{"text": system_prompt}],
            )

            output_text = response["output"]["message"]["content"][0]["text"]
            stop_reason = response["stopReason"]
            usage = response.get("usage", {})

            # Log actual token usage from API response
            input_tokens = usage.get("inputTokens", "?")
            output_tokens = usage.get("outputTokens", "?")
            total_tokens = usage.get("totalTokens", "?")
            print(
                f"  Bedrock API usage: input={input_tokens}, output={output_tokens}, total={total_tokens}")
            print(f"  Stop reason: {stop_reason}")
            if stop_reason in ("max_tokens", "length"):
                print(
                    f"  WARNING: Output was truncated (max_tokens={self.max_tokens})")

            log_paths = self._save_logs(config, prompt, output_text, {
                "backend": "bedrock",
                "model_id": self.model_id,
                "region": self.region,
                "stop_reason": stop_reason,
                "usage": usage,
            })

            truncated = stop_reason in ("max_tokens", "length")

            return ModelResponse(
                success=stop_reason in (
                    "end_turn", "stop_sequence") and not truncated,
                output=output_text,
                log_paths=log_paths,
                stop_reason=stop_reason,
                usage=usage,
                truncated=truncated,
            )

        except Exception as e:
            error_msg = str(e)
            log_paths = self._save_logs(config, prompt, "", {
                "backend": "bedrock",
                "model_id": self.model_id,
                "error": error_msg,
            })
            return ModelResponse(
                success=False,
                output="",
                log_paths=log_paths,
                error=error_msg,
            )
