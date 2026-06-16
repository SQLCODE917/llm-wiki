"""Explicit application state: filesystem layout and runtime settings."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

DEFAULT_CONTEXT_TOKENS = 16384
DEFAULT_OLLAMA_ENDPOINT = "http://localhost:11434"
DEFAULT_OLLAMA_MODEL = "qwen3-coder:30b"
DEFAULT_4090_MODEL = "qwen3-coder:30b"
DEFAULT_RUNTIME = "ollama-default"
DEFAULT_STRICT_EVIDENCE = "off"
# Per-read cap on plain raw source text. PDFs use the chunked map/integrate path.
SOURCE_READ_BUDGET_CHARS = 24_000

type RuntimeName = Literal["ollama-default", "local-4090"]
type BackendKind = Literal["ollama"]
type LifecycleMode = Literal["connect"]
type StrictEvidenceMode = Literal["off", "warn", "fail"]

VALID_RUNTIMES: tuple[RuntimeName, ...] = ("ollama-default", "local-4090")
VALID_STRICT_EVIDENCE_MODES: tuple[StrictEvidenceMode, ...] = ("off", "warn", "fail")


class ConfigError(Exception):
    """Raised when the environment cannot satisfy an explicit requirement."""


@dataclass(frozen=True)
class WikiPaths:
    """The three layers of the wiki on disk, rooted at the project directory."""

    root: Path

    @property
    def raw_dir(self) -> Path:
        return self.root / "raw"

    @property
    def wiki_dir(self) -> Path:
        return self.root / "wiki"

    @property
    def schema_path(self) -> Path:
        return self.root / "SCHEMA.md"

    @property
    def index_path(self) -> Path:
        return self.wiki_dir / "index.md"

    @property
    def log_path(self) -> Path:
        return self.wiki_dir / "log.md"

    @property
    def candidates_path(self) -> Path:
        return self.wiki_dir / "wiki-candidates.json"

    @property
    def graph_path(self) -> Path:
        return self.wiki_dir / "wiki-graph.json"

    @property
    def runs_dir(self) -> Path:
        return self.root / "harness" / "runs"

    @property
    def cache_dir(self) -> Path:
        """Derived extraction artifacts (disposable; not a wiki layer)."""
        return self.root / "harness" / "cache"

    @property
    def ingest_profiles_dir(self) -> Path:
        """Curator-editable ingest strategy profiles."""
        return self.root / "profiles" / "ingest"

    def validate(self) -> None:
        for path in (self.raw_dir, self.wiki_dir, self.schema_path, self.index_path, self.log_path):
            if not path.exists():
                raise ConfigError(
                    f"Wiki layer missing: {path}. Run from the project root "
                    "(or pass --root) - see SCHEMA.md for the expected layout."
                )

    def validate_status(self) -> None:
        """Validate only the layers required for read-only curator status."""
        for path in (self.raw_dir, self.wiki_dir):
            if not path.exists():
                raise ConfigError(
                    f"Wiki layer missing: {path}. Run from the project root "
                    "(or pass --root) - see SCHEMA.md for the expected layout."
                )


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ConfigError(f"{name} must be an integer, got {raw!r}.") from exc


def _runtime_name(value: str) -> RuntimeName:
    if value in VALID_RUNTIMES:
        return value
    valid = ", ".join(VALID_RUNTIMES)
    raise ConfigError(f"Unknown runtime {value!r}. Valid runtimes: {valid}.")


def _strict_evidence_mode(value: str) -> StrictEvidenceMode:
    if value in VALID_STRICT_EVIDENCE_MODES:
        return value
    valid = ", ".join(VALID_STRICT_EVIDENCE_MODES)
    raise ConfigError(f"Unknown strict evidence mode {value!r}. Valid modes: {valid}.")


@dataclass(frozen=True)
class RuntimeProfile:
    """Structured local runtime settings; no shell fragments."""

    name: RuntimeName
    provider: BackendKind
    model: str
    context_tokens: int
    endpoint: str
    lifecycle: LifecycleMode = "connect"


@dataclass(frozen=True)
class BackendConfig:
    """Forge-compatible backend startup configuration."""

    runtime_name: RuntimeName
    backend_kind: BackendKind
    model: str
    context_tokens: int
    endpoint: str
    lifecycle: LifecycleMode = "connect"

    def summary(self) -> str:
        return (
            f"{self.runtime_name} "
            f"provider={self.backend_kind} model={self.model} ctx={self.context_tokens}"
        )


def resolve_runtime_profile(runtime_name: str | None = None) -> RuntimeProfile:
    """Resolve CLI/env/default runtime precedence into a structured profile."""
    selected = _runtime_name(runtime_name or os.environ.get("LLMWIKI_RUNTIME") or DEFAULT_RUNTIME)
    endpoint = os.environ.get("LLMWIKI_OLLAMA_URL", DEFAULT_OLLAMA_ENDPOINT)
    if selected == "local-4090":
        return RuntimeProfile(
            name=selected,
            provider="ollama",
            model=os.environ.get("LLMWIKI_4090_MODEL", DEFAULT_4090_MODEL),
            context_tokens=_env_int(
                "LLMWIKI_4090_CTX",
                _env_int("LLMWIKI_CTX", DEFAULT_CONTEXT_TOKENS),
            ),
            endpoint=endpoint,
        )
    return RuntimeProfile(
        name=selected,
        provider="ollama",
        model=os.environ.get("LLMWIKI_OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL),
        context_tokens=_env_int("LLMWIKI_CTX", DEFAULT_CONTEXT_TOKENS),
        endpoint=endpoint,
    )


def load_backend_config(runtime_name: str | None = None) -> BackendConfig:
    """Resolve runtime settings for the forge backend."""
    profile = resolve_runtime_profile(runtime_name)
    return BackendConfig(
        runtime_name=profile.name,
        backend_kind=profile.provider,
        model=profile.model,
        context_tokens=profile.context_tokens,
        endpoint=profile.endpoint,
        lifecycle=profile.lifecycle,
    )


def resolve_strict_evidence_mode(mode: str | None = None) -> StrictEvidenceMode:
    """Resolve CLI/env/default strict-evidence precedence."""

    selected = mode or os.environ.get("LLMWIKI_STRICT_EVIDENCE") or DEFAULT_STRICT_EVIDENCE
    return _strict_evidence_mode(selected)
