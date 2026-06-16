from pathlib import Path

import pytest

from llmwiki.config import ConfigError
from llmwiki.domain.ingest_profiles import (
    IngestProfile,
    compose_prompt,
    load_ingest_profiles,
    render_profiles,
    select_ingest_profiles,
)
from llmwiki.store import WikiStore
from llmwiki.workflows import prompts
from llmwiki.workflows.definitions import build_ingest_workflow
from llmwiki.workflows.pdf_ingest import build_integrate_workflow, build_map_workflow


def _write_profile(
    directory: Path,
    stem: str,
    *,
    profile_id: str | None = None,
    enabled: bool = True,
    priority: int = 100,
    overlay: str = "Use {source_namespace} for {source_path}.",
) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{stem}.toml"
    path.write_text(
        f"""
id = "{profile_id or stem}"
enabled = {str(enabled).lower()}
description = "Test profile."
priority = {priority}

[namespace]
mode = "source-slug"

[overlays]
pdf_map = "{overlay}"
""".strip(),
        encoding="utf-8",
    )
    return path


class TestIngestProfiles:
    def test_loads_profiles_and_lists_disabled_status(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(directory, "rulebook")
        _write_profile(directory, "draft", enabled=False)

        profiles = load_ingest_profiles(directory)

        assert [profile.id for profile in profiles] == ["draft", "rulebook"]
        rendered = render_profiles(profiles)
        assert "draft [disabled" in rendered
        assert "rulebook [enabled" in rendered

    def test_filename_and_id_must_match(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(directory, "rulebook", profile_id="other")

        with pytest.raises(ConfigError, match="filename stem"):
            load_ingest_profiles(directory)

    def test_overlay_unknown_variable_fails(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(directory, "rulebook", overlay="Use {book_prefix}.")

        with pytest.raises(ConfigError, match="unknown variable"):
            load_ingest_profiles(directory)

    def test_selects_enabled_profiles_by_priority_then_cli_order(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(directory, "later", priority=200)
        _write_profile(directory, "first", priority=50)
        _write_profile(directory, "same-a", priority=100)
        _write_profile(directory, "same-b", priority=100)
        profiles = load_ingest_profiles(directory)

        selected = select_ingest_profiles(
            profiles,
            ["later", "same-b", "same-a", "first"],
        )

        assert [profile.id for profile in selected] == ["first", "same-b", "same-a", "later"]

    def test_unknown_and_disabled_profiles_fail(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(directory, "disabled", enabled=False)
        profiles = load_ingest_profiles(directory)

        with pytest.raises(ConfigError, match="Unknown ingest profile"):
            select_ingest_profiles(profiles, ["missing"])
        with pytest.raises(ConfigError, match="disabled"):
            select_ingest_profiles(profiles, ["disabled"])

    def test_compose_prompt_renders_source_derived_namespace(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(
            directory,
            "rulebook",
            overlay="Namespace {source_namespace}; slug {source_slug}; ids {profile_ids}.",
        )
        profiles = select_ingest_profiles(load_ingest_profiles(directory), ["rulebook"])

        prompt = compose_prompt(
            "Base prompt.",
            profiles,
            "pdf_map",
            "Sword World RPG - Complete Edition.pdf",
        )

        assert "Base prompt." in prompt
        assert "sword-world-rpg-complete-edition" in prompt
        assert "ids rulebook" in prompt

    def test_no_profile_prompt_is_unchanged(self) -> None:
        assert compose_prompt("Base prompt.", (), "ingest", "anything.md") == "Base prompt."


class TestProfiledWorkflows:
    def test_no_profile_ingest_template_is_unchanged(self, store: WikiStore) -> None:
        workflow = build_ingest_workflow(store, "2026-06-16")

        assert workflow.system_prompt_template == prompts.INGEST_TEMPLATE

    def test_pdf_map_and_integrate_receive_profile_overlays(self, store: WikiStore) -> None:
        profile = IngestProfile(
            id="rulebook",
            enabled=True,
            description="Rules.",
            priority=100,
            namespace_mode="source-slug",
            overlays={
                "pdf_map": "map {source_namespace}",
                "pdf_integrate": "integrate {source_namespace}",
            },
        )

        map_workflow = build_map_workflow(
            store,
            "2026-06-16",
            profiles=(profile,),
            source_path="Sword World RPG - Complete Edition.pdf",
        )
        integrate_workflow = build_integrate_workflow(
            store,
            "2026-06-16",
            profiles=(profile,),
            source_path="Sword World RPG - Complete Edition.pdf",
        )

        assert "map sword-world-rpg-complete-edition" in map_workflow.system_prompt_template
        assert (
            "integrate sword-world-rpg-complete-edition"
            in integrate_workflow.system_prompt_template
        )
