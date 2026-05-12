"""Abstract base class for model backends.

All backend implementations inherit from ModelBackend and implement
the run() method.
"""
from __future__ import annotations

import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from wiki_llm.backends.types import ModelConfig, ModelResponse


class ModelBackend(ABC):
    """Abstract base class for model backends."""

    @abstractmethod
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        """Run the model with the given prompt and return a response."""
        pass

    def _build_system_prompt(self, config: ModelConfig) -> str:
        """Build system prompt based on config.system_prompt_style.

        Supported styles:
        - "full": Complete AGENTS.md (~7K tokens)
        - "synthesis": Wiki page synthesis (~800 tokens)
        - "synthesis-json": JSON schema output for synthesis (~500 tokens)
        - "extract": Claim extraction (~500 tokens)
        - "query": Query answering (~400 tokens)
        - "judge": Claim judging (~400 tokens)
        """
        from wiki_llm.prompts import load_system_prompt
        return load_system_prompt(config.system_prompt_style, config.worktree)

    def _load_agents_md(self, config: ModelConfig) -> str:
        """Load AGENTS.md content."""
        agents_path = config.worktree / "AGENTS.md"
        if not agents_path.exists():
            agents_path = Path("AGENTS.md")

        if agents_path.exists():
            return agents_path.read_text()
        return "You are a wiki maintenance agent."

    def _save_logs(
        self,
        config: ModelConfig,
        prompt: str,
        output: str,
        metadata: dict[str, Any],
    ) -> list[Path]:
        """Save prompt, output, and metadata for debugging (only if enabled)."""
        if not config.should_save_debug():
            return []

        debug_dir = config.get_debug_dir()
        prefix = config.prefix

        prompt_path = debug_dir / f"{prefix}-prompt.md"
        output_path = debug_dir / f"{prefix}-output.md"
        meta_path = debug_dir / f"{prefix}-meta.json"

        prompt_path.write_text(prompt)
        output_path.write_text(output)
        meta_path.write_text(json.dumps(metadata, indent=2, default=str))

        return [prompt_path, output_path, meta_path]
