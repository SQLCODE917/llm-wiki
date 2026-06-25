"""CLI argument contract and explicit config resolution."""

from pathlib import Path
from typing import Any

import pytest

from llmwiki.cli import _build_parser, _default_text_recognizer, _run
from llmwiki.config import (
    ConfigError,
    WikiPaths,
    load_backend_config,
    resolve_runtime_profile,
    resolve_strict_evidence_mode,
)
from llmwiki.domain.contradictions import DEFAULT_MAX_PAIRS
from llmwiki.domain.semantic_lint import DEFAULT_MAX_ITEMS
from llmwiki.pdf.recognizer import NullRecognizer


class TestParser:
    def test_ingest_args(self) -> None:
        args = _build_parser().parse_args(["ingest", "article.md"])
        assert (args.op, args.source) == ("ingest", "article.md")

    def test_ingest_profile_args(self) -> None:
        args = _build_parser().parse_args(
            ["ingest", "book.pdf", "--profile", "rulebook", "--profile", "table-heavy"]
        )
        assert args.profile == ["rulebook", "table-heavy"]

    def test_ingest_pdf_extractor_arg(self) -> None:
        args = _build_parser().parse_args(["ingest", "book.pdf", "--pdf-extractor", "pymupdf"])
        assert args.pdf_extractor == "pymupdf"

    def test_ingest_confidence_pdf_extractor_arg(self) -> None:
        args = _build_parser().parse_args(
            ["ingest-confidence", "book.pdf", "--pdf-extractor", "pymupdf"]
        )
        assert args.pdf_extractor == "pymupdf"

    def test_query_args(self) -> None:
        args = _build_parser().parse_args(["query", "what happened?"])
        assert (args.op, args.question) == ("query", "what happened?")

    def test_lint_args_and_root_override(self, tmp_path: Path) -> None:
        args = _build_parser().parse_args(["--root", str(tmp_path), "lint"])
        assert args.op == "lint"
        assert args.root == tmp_path

    def test_curator_status_args(self) -> None:
        args = _build_parser().parse_args(["curator-status", "--strict-evidence", "warn"])
        assert args.op == "curator-status"
        assert args.strict_evidence == "warn"

    def test_maintenance_args(self) -> None:
        args = _build_parser().parse_args(["maintenance", "--strict-evidence", "fail"])
        assert args.op == "maintenance"
        assert args.strict_evidence == "fail"

    def test_candidates_list_args(self) -> None:
        args = _build_parser().parse_args(["candidates"])
        assert args.op == "candidates"
        assert args.candidate_op is None

    def test_candidates_reject_args(self) -> None:
        args = _build_parser().parse_args(
            ["candidates", "reject", "iterable", "--reason", "covered elsewhere"]
        )
        assert args.op == "candidates"
        assert args.candidate_op == "reject"
        assert args.slug == "iterable"
        assert args.reason == "covered elsewhere"

    def test_contradictions_args(self) -> None:
        args = _build_parser().parse_args(["contradictions", "--max-pairs", "7"])
        assert args.op == "contradictions"
        assert args.max_pairs == 7

    def test_contradictions_default_pair_cap(self) -> None:
        args = _build_parser().parse_args(["contradictions"])
        assert args.max_pairs == DEFAULT_MAX_PAIRS

    def test_semantic_lint_args(self) -> None:
        args = _build_parser().parse_args(["semantic-lint", "--max-items", "3"])
        assert args.op == "semantic-lint"
        assert args.max_items == 3

    def test_semantic_lint_default_item_cap(self) -> None:
        args = _build_parser().parse_args(["semantic-lint"])
        assert args.max_items == DEFAULT_MAX_ITEMS

    def test_graph_args(self) -> None:
        args = _build_parser().parse_args(["graph", "--check"])
        assert args.op == "graph"
        assert args.check

    def test_profiles_args(self) -> None:
        args = _build_parser().parse_args(["profiles"])
        assert args.op == "profiles"

    def test_strict_evidence_arg(self) -> None:
        args = _build_parser().parse_args(["lint", "--strict-evidence", "warn"])
        assert args.strict_evidence == "warn"

    def test_runtime_arg(self) -> None:
        args = _build_parser().parse_args(["--runtime", "local-4090", "query", "what happened?"])
        assert args.runtime == "local-4090"

    def test_op_is_required(self) -> None:
        with pytest.raises(SystemExit):
            _build_parser().parse_args([])


class TestBackendConfig:
    def test_default_runtime_is_ollama(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("LLMWIKI_RUNTIME", raising=False)
        monkeypatch.delenv("LLMWIKI_OLLAMA_MODEL", raising=False)
        monkeypatch.delenv("LLMWIKI_OLLAMA_URL", raising=False)
        monkeypatch.delenv("LLMWIKI_OLLAMA_TIMEOUT", raising=False)
        monkeypatch.delenv("LLMWIKI_CTX", raising=False)
        config = load_backend_config()
        assert config.runtime_name == "ollama-default"
        assert config.backend_kind == "ollama"
        assert config.model == "qwen3-coder:30b"
        assert config.endpoint == "http://localhost:11434"
        assert config.context_tokens == 16384
        assert config.timeout_seconds == 900

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

    def test_ollama_timeout_override(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_OLLAMA_TIMEOUT", "1200")
        config = load_backend_config()
        assert config.timeout_seconds == 1200

    def test_invalid_runtime_fails_loudly(self) -> None:
        with pytest.raises(ConfigError, match="Valid runtimes"):
            resolve_runtime_profile("nope")

    def test_invalid_context_fails_loudly(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_CTX", "many")
        with pytest.raises(ConfigError, match="LLMWIKI_CTX must be an integer"):
            load_backend_config()


class TestStrictEvidenceConfig:
    def test_default_strict_evidence_is_off(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("LLMWIKI_STRICT_EVIDENCE", raising=False)
        assert resolve_strict_evidence_mode() == "off"

    def test_env_strict_evidence(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_STRICT_EVIDENCE", "warn")
        assert resolve_strict_evidence_mode() == "warn"

    def test_cli_strict_evidence_overrides_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_STRICT_EVIDENCE", "fail")
        assert resolve_strict_evidence_mode("warn") == "warn"

    def test_invalid_strict_evidence_fails_loudly(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLMWIKI_STRICT_EVIDENCE", "strictest")
        with pytest.raises(ConfigError, match="Valid modes"):
            resolve_strict_evidence_mode()


class TestWikiPathsValidation:
    def test_complete_tree_validates(self, paths: WikiPaths) -> None:
        paths.validate()

    def test_missing_layer_raises(self, tmp_path: Path) -> None:
        with pytest.raises(ConfigError, match="Wiki layer missing"):
            WikiPaths(root=tmp_path).validate()


class TestProfileCli:
    async def test_profiles_lists_without_backend(self, paths: WikiPaths) -> None:
        profile_dir = paths.ingest_profiles_dir
        profile_dir.mkdir(parents=True)
        (profile_dir / "rulebook.toml").write_text(
            """
id = "rulebook"
enabled = true
description = "Rules."
priority = 100

[namespace]
mode = "source-slug"

[overlays]
ingest = "Use {source_namespace}."
""".strip(),
            encoding="utf-8",
        )
        args = _build_parser().parse_args(["--root", str(paths.root), "profiles"])

        result = await _run(args)

        assert result.op == "profiles"
        assert "rulebook [enabled" in result.output

    async def test_unknown_profile_fails_before_backend(
        self, monkeypatch: pytest.MonkeyPatch, paths: WikiPaths
    ) -> None:
        called = False

        async def fake_start_backend(config: object) -> object:
            nonlocal called
            called = True
            raise AssertionError("backend should not start")

        monkeypatch.setattr("llmwiki.cli.start_backend", fake_start_backend)
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "ingest", "book.pdf", "--profile", "missing"]
        )

        with pytest.raises(ConfigError, match="Unknown ingest profile"):
            await _run(args)
        assert not called

    async def test_disabled_profile_fails_before_backend(
        self, monkeypatch: pytest.MonkeyPatch, paths: WikiPaths
    ) -> None:
        profile_dir = paths.ingest_profiles_dir
        profile_dir.mkdir(parents=True)
        (profile_dir / "draft.toml").write_text(
            """
id = "draft"
enabled = false
description = "Disabled."
priority = 100

[namespace]
mode = "source-slug"

[overlays]
ingest = "Use {source_namespace}."
""".strip(),
            encoding="utf-8",
        )
        called = False

        async def fake_start_backend(config: object) -> object:
            nonlocal called
            called = True
            raise AssertionError("backend should not start")

        monkeypatch.setattr("llmwiki.cli.start_backend", fake_start_backend)
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "ingest", "book.pdf", "--profile", "draft"]
        )

        with pytest.raises(ConfigError, match="disabled"):
            await _run(args)
        assert not called


class TestPdfRecognizerSelection:
    def test_missing_vision_uses_null_recognizer(self, monkeypatch: pytest.MonkeyPatch) -> None:
        real_import = __import__

        def fake_import(name: str, *args: Any, **kwargs: Any) -> Any:
            if name in {"Foundation", "Vision"}:
                raise ImportError(name)
            return real_import(name, *args, **kwargs)

        monkeypatch.setattr("builtins.__import__", fake_import)

        assert isinstance(_default_text_recognizer(), NullRecognizer)
