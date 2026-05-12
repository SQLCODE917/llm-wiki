"""Tests for wiki_llm.prompts module."""
import pytest
from pathlib import Path
import tempfile

from wiki_llm.prompts import (
    load_system_prompt,
    load_prompt_template,
    get_available_prompts,
    PROMPT_FILES,
)


class TestLoadSystemPrompt:
    """Tests for load_system_prompt()."""

    def test_loads_agents_md_fallback(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            worktree = Path(tmpdir)
            (worktree / "AGENTS.md").write_text("# Test Agent Rules")

            prompt = load_system_prompt("full", worktree)
            assert "Test Agent Rules" in prompt
            assert "Working directory:" in prompt

    def test_unknown_style_uses_agents(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            worktree = Path(tmpdir)
            (worktree / "AGENTS.md").write_text("# Agent Content")

            prompt = load_system_prompt("unknown_style", worktree)
            assert "Agent Content" in prompt


class TestPromptFiles:
    """Tests for PROMPT_FILES constant."""

    def test_expected_styles(self):
        assert "synthesis" in PROMPT_FILES
        assert "extract" in PROMPT_FILES
        assert "judge" in PROMPT_FILES
        assert "query" in PROMPT_FILES


class TestGetAvailablePrompts:
    """Tests for get_available_prompts()."""

    def test_returns_list(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            worktree = Path(tmpdir)
            prompts_dir = worktree / "tools" / "prompts"
            prompts_dir.mkdir(parents=True)
            (prompts_dir / "test-prompt.md").write_text("# Test")

            prompts = get_available_prompts(worktree)
            assert "test-prompt" in prompts

    def test_handles_missing_dir(self):
        # When worktree has no prompts dir, it falls back to cwd tools/prompts
        # This test just verifies the function doesn't crash
        with tempfile.TemporaryDirectory() as tmpdir:
            worktree = Path(tmpdir)
            prompts = get_available_prompts(worktree)
            # May return prompts from real dir if it exists
            assert isinstance(prompts, list)
