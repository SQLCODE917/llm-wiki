"""OpenAI Codex CLI backend for local model inference.

Usage:
    from wiki_llm.backends import CodexBackend, ModelConfig
    
    backend = CodexBackend()
    response = backend.run(prompt, config)
"""
from __future__ import annotations

import subprocess

from wiki_llm.backends.base import ModelBackend
from wiki_llm.backends.bedrock import log_context_stats
from wiki_llm.backends.types import ModelConfig, ModelResponse


class CodexBackend(ModelBackend):
    """Backend using OpenAI Codex CLI for local model inference."""

    def __init__(self, bin: str = "codex", default_profile: str = "local-4090", **kwargs):
        self.bin = bin
        self.default_profile = default_profile

    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (codex)")

        # Use debug_dir for temp files
        debug_dir = config.get_debug_dir()
        stdout_path = debug_dir / f"{config.prefix}-stdout.log"
        stderr_path = debug_dir / f"{config.prefix}-stderr.log"
        last_message_path = debug_dir / f"{config.prefix}-last-message.md"
        prompt_path = debug_dir / f"{config.prefix}-prompt.md"
        prompt_path.write_text(prompt)

        profile = config.codex_profile or self.default_profile
        command = [
            config.codex_bin or self.bin,
            "exec",
            "--profile", profile,
            "--cd", str(config.worktree),
            "--dangerously-bypass-approvals-and-sandbox",
            "--skip-git-repo-check",
            "--ephemeral",
            "--output-last-message", str(last_message_path),
        ]
        if config.codex_model:
            command.extend(["--model", config.codex_model])
        command.append("-")

        log_paths = [prompt_path, stdout_path, stderr_path, last_message_path]

        with stdout_path.open("w") as stdout, stderr_path.open("w") as stderr:
            try:
                completed = subprocess.run(
                    command,
                    cwd=config.worktree,
                    input=prompt,
                    text=True,
                    stdout=stdout,
                    stderr=stderr,
                    timeout=config.timeout,
                )
                output = last_message_path.read_text() if last_message_path.exists() else ""
                return ModelResponse(
                    success=completed.returncode == 0,
                    output=output,
                    log_paths=log_paths,
                    stop_reason="complete" if completed.returncode == 0 else "error",
                )
            except subprocess.TimeoutExpired:
                stderr.write(f"\nTIMEOUT after {config.timeout} seconds\n")
                return ModelResponse(
                    success=False,
                    output="",
                    log_paths=log_paths,
                    error=f"Timeout after {config.timeout} seconds",
                )
            except Exception as e:
                return ModelResponse(
                    success=False,
                    output="",
                    log_paths=log_paths,
                    error=str(e),
                )
