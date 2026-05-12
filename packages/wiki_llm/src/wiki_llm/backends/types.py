"""Configuration and response types for model backends.

Usage:
    from wiki_llm.backends import ModelConfig, ModelResponse
    
    config = ModelConfig(worktree=Path("/tmp/work"), prefix="phase2")
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ModelConfig:
    """Configuration passed to model backends."""
    worktree: Path
    prefix: str
    timeout: int = 600
    task_description: str = ""
    validation_command: str = ""
    # Debug file handling
    save_debug_files: bool = False  # Set True or WIKI_DEBUG=1 to save
    debug_dir: Path | None = None  # Defaults to .tmp/model-runs/
    # System prompt style: "full" = AGENTS.md, "synthesis" = slim synthesis prompt
    system_prompt_style: str = "full"
    # Codex-specific
    codex_bin: str = "codex"
    codex_profile: str = "local-4090"
    codex_model: str | None = None

    def get_debug_dir(self) -> Path:
        """Get the directory for debug files, creating if needed."""
        if self.debug_dir:
            d = self.debug_dir
        else:
            d = self.worktree / ".tmp" / "model-runs"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def should_save_debug(self) -> bool:
        """Check if debug files should be saved."""
        return self.save_debug_files or os.environ.get("WIKI_DEBUG", "") == "1"


@dataclass
class ModelResponse:
    """Response from a model backend."""
    success: bool
    output: str
    log_paths: list[Path] = field(default_factory=list)
    stop_reason: str | None = None
    usage: dict[str, Any] | None = None
    error: str | None = None
    truncated: bool = False

    def is_complete(self) -> bool:
        """Check if the response appears complete (not truncated).

        Returns False if:
        - Stop reason indicates truncation (length, max_tokens)
        - Output is suspiciously short
        - Response is explicitly marked as truncated
        """
        if self.truncated:
            return False

        if self.stop_reason in ("length", "max_tokens"):
            return False

        # Very short outputs are suspicious unless there's an error
        if len(self.output) < 100 and not self.error:
            return False

        return True
