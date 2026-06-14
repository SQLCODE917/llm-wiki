"""CLI argument contract and explicit config resolution."""

from pathlib import Path

import pytest

from llmwiki.cli import _build_parser
from llmwiki.config import (
    ConfigError,
    WikiPaths,
    load_backend_config,
    resolve_runtime_profile,
)


class TestParser:
    def test_ingest_args(self) -> None:
        args = _build_parser().parse_args(["ingest", "article.md"])
        assert (args.op, args.source) == ("ingest", "article.md")

    def test_query_args(self) -> None:
        args = _build_parser().parse_args(["query", "what happened?"])
        assert (args.op, args.question) == ("query", "what happened?")

    def test_lint_args_and_root_override(self, tmp_path: Path) -> None:
        args = _build_parser().parse_args(["--root", str(tmp_path), "lint"])
        assert args.op == "lint"
        assert args.root == tmp_path

    def test_runtime_arg(self) -> None:
        args = _build_parser().parse_args(
            ["--runtime", "local-4090", "query", "what happened?"]
        )
        assert args.runtime == "local-4090"

    def test_op_is_required(self) -> None:
        with pytest.raises(SystemExit):
            _build_parser().parse_args([])


class TestBackendConfig:
    def test_default_runtime_is_ollama(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("LLMWIKI_RUNTIME", raising=False)
        monkeypatch.delenv("LLMWIKI_OLLAMA_MODEL", raising=False)
        monkeypatch.delenv("LLMWIKI_OLLAMA_URL", raising=False)
        monkeypatch.delenv("LLMWIKI_CTX", raising=False)
        config = load_backend_config()
        assert config.runtime_name == "ollama-default"
        assert config.backend_kind == "ollama"
        assert config.model == "qwen3-coder:30b"
        assert config.endpoint == "http://localhost:11434"
        assert config.context_tokens == 16384

    def test_env_runtime_selects_local_4090(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_RUNTIME", "local-4090")
        monkeypatch.setenv("LLMWIKI_CTX", "8192")
        monkeypatch.setenv("LLMWIKI_4090_MODEL", "qwen3-coder:30b")
        config = load_backend_config()
        assert config.runtime_name == "local-4090"
        assert config.backend_kind == "ollama"
        assert config.model == "qwen3-coder:30b"
        assert config.context_tokens == 8192

    def test_cli_runtime_overrides_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_RUNTIME", "local-4090")
        monkeypatch.setenv("LLMWIKI_OLLAMA_MODEL", "gpt-oss:20b")
        config = load_backend_config("ollama-default")
        assert config.runtime_name == "ollama-default"
        assert config.model == "gpt-oss:20b"

    def test_profile_specific_context_wins(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_RUNTIME", "local-4090")
        monkeypatch.setenv("LLMWIKI_CTX", "8192")
        monkeypatch.setenv("LLMWIKI_4090_CTX", "32768")
        config = load_backend_config()
        assert config.context_tokens == 32768

    def test_ollama_endpoint_override(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_OLLAMA_URL", "http://127.0.0.1:11434")
        config = load_backend_config()
        assert config.endpoint == "http://127.0.0.1:11434"

    def test_invalid_runtime_fails_loudly(self) -> None:
        with pytest.raises(ConfigError, match="Valid runtimes"):
            resolve_runtime_profile("nope")

    def test_invalid_context_fails_loudly(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_CTX", "many")
        with pytest.raises(ConfigError, match="LLMWIKI_CTX must be an integer"):
            load_backend_config()


class TestWikiPathsValidation:
    def test_complete_tree_validates(self, paths: WikiPaths) -> None:
        paths.validate()

    def test_missing_layer_raises(self, tmp_path: Path) -> None:
        with pytest.raises(ConfigError, match="Wiki layer missing"):
            WikiPaths(root=tmp_path).validate()
