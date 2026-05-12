"""Tests for wiki_llm.backends module."""
import pytest
from pathlib import Path

from wiki_llm.backends import (
    ModelConfig,
    ModelResponse,
    get_backend,
)


class TestModelConfig:
    """Tests for ModelConfig."""

    def test_defaults(self):
        config = ModelConfig(worktree=Path("/tmp"), prefix="test")
        assert config.timeout == 600
        assert config.system_prompt_style == "full"

    def test_should_save_debug(self, monkeypatch):
        config = ModelConfig(worktree=Path("/tmp"), prefix="test")
        assert not config.should_save_debug()

        config.save_debug_files = True
        assert config.should_save_debug()

    def test_should_save_debug_env(self, monkeypatch):
        config = ModelConfig(worktree=Path("/tmp"), prefix="test")
        monkeypatch.setenv("WIKI_DEBUG", "1")
        assert config.should_save_debug()


class TestModelResponse:
    """Tests for ModelResponse."""

    def test_is_complete_success(self):
        response = ModelResponse(
            success=True,
            output="A" * 150,  # Must be at least 100 chars
            stop_reason="end_turn",
        )
        assert response.is_complete()

    def test_is_complete_truncated(self):
        response = ModelResponse(
            success=False,
            output="Output",
            truncated=True,
        )
        assert not response.is_complete()

    def test_is_complete_short_output(self):
        response = ModelResponse(
            success=True,
            output="x",  # Too short
            stop_reason="end_turn",
        )
        assert not response.is_complete()


class TestGetBackend:
    """Tests for get_backend()."""

    def test_unknown_backend_raises(self):
        with pytest.raises(ValueError, match="Unknown backend"):
            get_backend("nonexistent")

    def test_codex_backend(self):
        from wiki_llm.backends import CodexBackend
        backend = get_backend("codex")
        assert isinstance(backend, CodexBackend)

    def test_bedrock_backend(self):
        from wiki_llm.backends import BedrockBackend
        backend = get_backend("bedrock")
        assert isinstance(backend, BedrockBackend)
