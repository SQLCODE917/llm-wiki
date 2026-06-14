"""CLI argument contract and explicit config resolution."""

from pathlib import Path

import pytest

from llmwiki.cli import _build_parser
from llmwiki.config import ConfigError, WikiPaths, load_backend_config


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

    def test_op_is_required(self) -> None:
        with pytest.raises(SystemExit):
            _build_parser().parse_args([])


class TestBackendConfig:
    def test_env_override_wins(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        gguf = tmp_path / "model.gguf"
        gguf.write_bytes(b"GGUF")
        monkeypatch.setenv("LLMWIKI_GGUF", str(gguf))
        monkeypatch.setenv("LLMWIKI_PORT", "9001")
        monkeypatch.setenv("LLMWIKI_CTX", "8192")
        config = load_backend_config()
        assert config.gguf_path == gguf
        assert config.port == 9001
        assert config.context_tokens == 8192

    def test_missing_model_fails_loudly(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("LLMWIKI_GGUF", str(tmp_path / "absent.gguf"))
        with pytest.raises(ConfigError, match="GGUF not found"):
            load_backend_config()


class TestWikiPathsValidation:
    def test_complete_tree_validates(self, paths: WikiPaths) -> None:
        paths.validate()

    def test_missing_layer_raises(self, tmp_path: Path) -> None:
        with pytest.raises(ConfigError, match="Wiki layer missing"):
            WikiPaths(root=tmp_path).validate()
