"""Model backends for wiki LLM interactions.

This module provides a unified interface for different LLM backends:
- codex: Local models via OpenAI Codex CLI
- bedrock: AWS Bedrock managed inference
- openai: OpenAI API (GPT-4o, etc.)
- anthropic: Anthropic API (Claude)

Usage:
    from wiki_llm.backends import get_backend, ModelConfig
    
    backend = get_backend("bedrock")  # or from WIKI_MODEL_BACKEND env var
    config = ModelConfig(worktree=Path("/tmp/work"), prefix="phase2")
    response = backend.run(prompt, config)
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from wiki_llm.backends.types import ModelConfig, ModelResponse
from wiki_llm.backends.base import ModelBackend
from wiki_llm.backends.codex import CodexBackend
from wiki_llm.backends.bedrock import BedrockBackend
from wiki_llm.backends.openai import OpenAIBackend
from wiki_llm.backends.anthropic import AnthropicBackend


def load_backend_config(name: str) -> dict[str, Any]:
    """Load backend config from wiki_model_defaults.json."""
    # Check multiple locations
    search_paths = [
        Path("tools/wiki_model_defaults.json"),
        Path(__file__).parent.parent.parent.parent.parent.parent /
        "tools" / "wiki_model_defaults.json",
    ]

    for defaults_path in search_paths:
        if defaults_path.exists():
            defaults = json.loads(defaults_path.read_text())
            return defaults.get("backends", {}).get(name, {})
    return {}


def get_backend(name: str | None = None) -> ModelBackend:
    """Get a model backend by name or from environment.

    Backend selection priority:
    1. Explicit name parameter
    2. WIKI_MODEL_BACKEND environment variable
    3. Default from wiki_model_defaults.json
    4. Fallback to "codex"

    Args:
        name: Backend name (codex, bedrock, openai, anthropic)

    Returns:
        Configured ModelBackend instance
    """
    if name is None:
        name = os.environ.get("WIKI_MODEL_BACKEND")

    if name is None:
        # Check for defaults file
        search_paths = [
            Path("tools/wiki_model_defaults.json"),
            Path(__file__).parent.parent.parent.parent.parent.parent /
            "tools" / "wiki_model_defaults.json",
        ]
        for defaults_path in search_paths:
            if defaults_path.exists():
                defaults = json.loads(defaults_path.read_text())
                name = defaults.get("backend", "codex")
                break
        else:
            name = "codex"

    config = load_backend_config(name)

    # Remove 'type' key if present (it's for documentation, not constructor)
    config.pop("type", None)

    backends = {
        "codex": CodexBackend,
        "bedrock": BedrockBackend,
        "openai": OpenAIBackend,
        "anthropic": AnthropicBackend,
    }

    if name not in backends:
        available = ", ".join(backends.keys())
        raise ValueError(f"Unknown backend: {name}. Available: {available}")

    return backends[name](**config)


__all__ = [
    # Types
    "ModelConfig",
    "ModelResponse",
    "ModelBackend",
    # Backends
    "CodexBackend",
    "BedrockBackend",
    "OpenAIBackend",
    "AnthropicBackend",
    # Factory
    "get_backend",
    "load_backend_config",
]
