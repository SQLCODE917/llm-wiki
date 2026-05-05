#!/usr/bin/env python3
"""Model backend abstraction for llm-wiki.

Supports multiple backends:
- codex: Local models via OpenAI Codex CLI
- bedrock: AWS Bedrock managed inference
- openai: OpenAI API (GPT-4o, etc.)
- anthropic: Anthropic API (Claude)

Usage:
    from wiki_model_backend import get_backend, ModelConfig
    
    backend = get_backend("bedrock")  # or from WIKI_MODEL_BACKEND env var
    config = ModelConfig(worktree=Path("/tmp/work"), prefix="phase2")
    response = backend.run(prompt, config)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from wiki_common import log_context_stats


@dataclass
class ModelConfig:
    """Configuration passed to model backends."""
    worktree: Path
    prefix: str
    timeout: int = 600
    task_description: str = ""
    validation_command: str = ""
    # Codex-specific
    codex_bin: str = "codex"
    codex_profile: str = "local-4090"
    codex_model: str | None = None


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


class ModelBackend(ABC):
    """Abstract base class for model backends."""
    
    @abstractmethod
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        """Run the model with the given prompt and return a response."""
        pass
    
    def _build_system_prompt(self, config: ModelConfig) -> str:
        """Build system prompt from AGENTS.md."""
        agents_path = config.worktree / "AGENTS.md"
        if not agents_path.exists():
            agents_path = Path("AGENTS.md")
        
        agents_md = agents_path.read_text() if agents_path.exists() else ""
        
        return f"""You are a wiki maintenance agent. Follow these rules exactly:

{agents_md}

Working directory: {config.worktree}

Output file contents in fenced code blocks with the file path as the language tag.
Example:
```wiki/concepts/example.md
---
title: Example
type: concept
---
# Example
Content here.
```"""
    
    def _save_logs(
        self,
        config: ModelConfig,
        prompt: str,
        output: str,
        metadata: dict[str, Any],
    ) -> list[Path]:
        """Save prompt, output, and metadata for debugging."""
        prefix = config.prefix
        worktree = config.worktree
        
        prompt_path = worktree / f"{prefix}-prompt.md"
        output_path = worktree / f"{prefix}-output.md"
        meta_path = worktree / f"{prefix}-meta.json"
        
        prompt_path.write_text(prompt)
        output_path.write_text(output)
        meta_path.write_text(json.dumps(metadata, indent=2, default=str))
        
        return [prompt_path, output_path, meta_path]


class CodexBackend(ModelBackend):
    """Backend using OpenAI Codex CLI for local model inference."""
    
    def __init__(self, bin: str = "codex", default_profile: str = "local-4090", **kwargs):
        self.bin = bin
        self.default_profile = default_profile
    
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (codex)")
        
        stdout_path = config.worktree / f"{config.prefix}-stdout.log"
        stderr_path = config.worktree / f"{config.prefix}-stderr.log"
        last_message_path = config.worktree / f"{config.prefix}-last-message.md"
        prompt_path = config.worktree / f"{config.prefix}-prompt.md"
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


class BedrockBackend(ModelBackend):
    """Backend using AWS Bedrock for managed model inference."""
    
    def __init__(
        self,
        model_id: str = "qwen.qwen3-coder-30b-a3b-v1:0",
        region: str | None = None,
        max_tokens: int = 8192,
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
                self._client = boto3.client("bedrock-runtime", region_name=self.region)
            except ImportError:
                raise ImportError("boto3 is required for Bedrock backend. Install with: pip install boto3")
        return self._client
    
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (bedrock)")
        
        system_prompt = self._build_system_prompt(config)
        
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
            
            log_paths = self._save_logs(config, prompt, output_text, {
                "backend": "bedrock",
                "model_id": self.model_id,
                "region": self.region,
                "stop_reason": stop_reason,
                "usage": usage,
            })
            
            truncated = stop_reason in ("max_tokens", "length")
            
            return ModelResponse(
                success=stop_reason in ("end_turn", "stop_sequence") and not truncated,
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
                    raise ValueError(f"Environment variable {self.api_key_env} not set")
                self._client = openai.OpenAI(api_key=api_key)
            except ImportError:
                raise ImportError("openai is required for OpenAI backend. Install with: pip install openai")
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
                    raise ValueError(f"Environment variable {self.api_key_env} not set")
                self._client = anthropic.Anthropic(api_key=api_key)
            except ImportError:
                raise ImportError("anthropic is required for Anthropic backend. Install with: pip install anthropic")
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


# --- Output Parsing Utilities ---


def parse_model_output(output: str, expected_files: list[str] | None = None) -> dict[str, str]:
    """Parse model output into file contents.
    
    Expected format:
    ```wiki/path/to/file.md
    file contents here
    ```
    
    Args:
        output: Raw model output text
        expected_files: Optional list of expected file paths (for validation)
    
    Returns:
        Dictionary mapping file paths to their contents
    """
    files: dict[str, str] = {}
    current_file: str | None = None
    current_content: list[str] = []
    
    for line in output.split("\n"):
        # Start of a fenced code block with a path
        if line.startswith("```") and len(line) > 3 and not line.startswith("```\n"):
            # Save previous file if any
            if current_file:
                files[current_file] = "\n".join(current_content)
            
            path = line[3:].strip()
            # Check if it looks like a file path
            if path.endswith(".md") or path.endswith(".json") or path.endswith(".py"):
                current_file = path
                current_content = []
            elif expected_files and path in expected_files:
                current_file = path
                current_content = []
            else:
                current_file = None
                current_content = []
        
        # End of fenced code block
        elif line == "```" and current_file:
            files[current_file] = "\n".join(current_content)
            current_file = None
            current_content = []
        
        # Content within a file block
        elif current_file is not None:
            current_content.append(line)
    
    return files


def check_response_completeness(response: ModelResponse) -> bool:
    """Check if a response appears complete (not truncated).
    
    Returns False if:
    - Stop reason indicates truncation (length, max_tokens)
    - Output is suspiciously short
    - Response is explicitly marked as truncated
    """
    if response.truncated:
        return False
    
    if response.stop_reason in ("length", "max_tokens"):
        return False
    
    # Very short outputs are suspicious unless there's an error
    if len(response.output) < 100 and not response.error:
        return False
    
    return True


def validate_file_paths(files: dict[str, str], worktree: Path) -> list[str]:
    """Validate that all file paths are within the worktree.
    
    Returns list of invalid paths (empty if all valid).
    """
    invalid = []
    worktree_resolved = worktree.resolve()
    
    for path in files.keys():
        try:
            full_path = (worktree / path).resolve()
            if not str(full_path).startswith(str(worktree_resolved)):
                invalid.append(path)
        except Exception:
            invalid.append(path)
    
    return invalid


def write_parsed_files(files: dict[str, str], worktree: Path, dry_run: bool = False) -> list[Path]:
    """Write parsed files to the worktree.
    
    Args:
        files: Dictionary mapping paths to contents
        worktree: Root directory for file writes
        dry_run: If True, only print what would be written
    
    Returns:
        List of paths that were written (or would be written)
    """
    written = []
    
    for path, content in files.items():
        full_path = worktree / path
        
        if dry_run:
            print(f"Would write: {full_path} ({len(content)} chars)")
        else:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content)
            print(f"Wrote: {full_path} ({len(content)} chars)")
        
        written.append(full_path)
    
    return written


# --- Backend Factory ---


def load_backend_config(name: str) -> dict[str, Any]:
    """Load backend config from wiki_model_defaults.json."""
    defaults_path = Path(__file__).parent / "wiki_model_defaults.json"
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
        defaults_path = Path(__file__).parent / "wiki_model_defaults.json"
        if defaults_path.exists():
            defaults = json.loads(defaults_path.read_text())
            name = defaults.get("backend", "codex")
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


# --- CLI for testing ---


def main():
    """Simple CLI for testing backends."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test model backends")
    parser.add_argument("--backend", "-b", help="Backend name")
    parser.add_argument("--list", "-l", action="store_true", help="List available backends")
    parser.add_argument("--test", "-t", action="store_true", help="Test backend connectivity")
    args = parser.parse_args()
    
    if args.list:
        print("Available backends:")
        print("  codex     - Local models via Codex CLI")
        print("  bedrock   - AWS Bedrock managed inference")
        print("  openai    - OpenAI API (GPT-4o, etc.)")
        print("  anthropic - Anthropic API (Claude)")
        return 0
    
    backend = get_backend(args.backend)
    print(f"Backend: {backend.__class__.__name__}")
    
    if hasattr(backend, "model_id"):
        print(f"  Model ID: {backend.model_id}")
    if hasattr(backend, "model"):
        print(f"  Model: {backend.model}")
    if hasattr(backend, "region"):
        print(f"  Region: {backend.region}")
    
    if args.test:
        print("\nTesting connectivity...")
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            worktree = Path(tmpdir)
            # Create minimal AGENTS.md for testing
            (worktree / "AGENTS.md").write_text("# Test\nYou are a test agent.")
            
            config = ModelConfig(worktree=worktree, prefix="test")
            response = backend.run("Say 'hello' and nothing else.", config)
            
            if response.success:
                print(f"  Success: {response.output[:100]}")
            else:
                print(f"  Failed: {response.error}")
    
    return 0


if __name__ == "__main__":
    exit(main())
