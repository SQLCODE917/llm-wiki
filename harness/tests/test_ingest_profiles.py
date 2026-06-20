from pathlib import Path
from typing import Any

import pytest
from helpers import wiki_page

from llmwiki.config import ConfigError
from llmwiki.domain.ingest_profiles import (
    IngestProfile,
    compose_prompt,
    load_ingest_profiles,
    prevents_singular_plural_siblings,
    render_profiles,
    required_new_page_prefix,
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
    overlay: str = "Use {source_namespace} for {source_locator}.",
    prevent_siblings: bool = False,
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

[naming]
prevent_singular_plural_siblings = {str(prevent_siblings).lower()}

[overlays]
pdf_map = "{overlay}"
""".strip(),
        encoding="utf-8",
    )
    return path


def _plan_page(
    workflow: Any,
    name: str,
    *,
    category: str = "source",
    summary: str = "Planned page.",
    action: str = "create",
) -> str:
    plan_pages = workflow.tools["plan_pages"].callable
    return plan_pages(
        planned_pages=[
            {
                "metadata": {
                    "page_id": name,
                    "page_kind": category,
                    "summary": summary,
                    "sources": ["Sword World RPG - Complete Edition.pdf"],
                },
                "role": "planned test page",
                "action": action,
                "source_scope": "test scope",
                "confidence": "high",
                "rationale": "The test establishes an active ingest route plan.",
            }
        ],
        gaps=[],
    )


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

    def test_required_new_page_prefix_comes_from_profile_flag(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(directory, "loose")
        strict = _write_profile(directory, "strict")
        text = strict.read_text(encoding="utf-8")
        strict.write_text(
            text.replace(
                'mode = "source-slug"',
                'mode = "source-slug"\nrequire_for_new_pages = true',
            ),
            encoding="utf-8",
        )
        profiles = load_ingest_profiles(directory)

        assert (
            required_new_page_prefix(
                select_ingest_profiles(profiles, ["loose"]),
                "Sword World RPG - Complete Edition.pdf",
            )
            is None
        )
        assert (
            required_new_page_prefix(
                select_ingest_profiles(profiles, ["strict"]),
                "Sword World RPG - Complete Edition.pdf",
            )
            == "sword-world-rpg-complete-edition"
        )

    def test_naming_guard_comes_from_profile_flag(self, tmp_path: Path) -> None:
        directory = tmp_path / "profiles" / "ingest"
        _write_profile(directory, "loose")
        _write_profile(directory, "guarded", prevent_siblings=True)
        profiles = load_ingest_profiles(directory)

        assert not prevents_singular_plural_siblings(select_ingest_profiles(profiles, ["loose"]))
        assert prevents_singular_plural_siblings(select_ingest_profiles(profiles, ["guarded"]))

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
            require_namespace_for_new_pages=True,
            prevent_singular_plural_siblings=False,
            overlays={
                "pdf_map": "map {source_namespace}",
                "pdf_integrate": "integrate {source_namespace}",
            },
        )

        map_workflow = build_map_workflow(
            store,
            "2026-06-16",
            profiles=(profile,),
            source_locator="Sword World RPG - Complete Edition.pdf",
        )
        integrate_workflow = build_integrate_workflow(
            store,
            "2026-06-16",
            profiles=(profile,),
            source_locator="Sword World RPG - Complete Edition.pdf",
        )

        assert "map sword-world-rpg-complete-edition" in map_workflow.system_prompt_template
        assert (
            "integrate sword-world-rpg-complete-edition"
            in integrate_workflow.system_prompt_template
        )

    def test_namespace_profile_blocks_new_generic_pages(self, store: WikiStore) -> None:
        workflow = build_ingest_workflow(
            store,
            "2026-06-16",
            new_page_prefix="sword-world-rpg-complete-edition",
        )
        write = workflow.tools["write_page"].callable

        with pytest.raises(Exception, match="namespace prefix"):
            _plan_page(workflow, "half-elf", category="concept", summary="Half-elf rules.")

        _plan_page(
            workflow,
            "sword-world-rpg-complete-edition-half-elf",
            category="concept",
            summary="Half-elf rules.",
        )
        result = write(
            page_id="sword-world-rpg-complete-edition-half-elf",
            page_kind="concept",
            summary="Half-elf rules.",
            page_body="Body.",
        )
        assert "sword-world-rpg-complete-edition-half-elf" in result

    def test_profile_naming_guard_blocks_singular_plural_siblings(self, store: WikiStore) -> None:
        store.write_page(
            wiki_page(
                name="sword-world-rpg-complete-edition-wraiths",
                category="entity",
                summary="Wraith monster entry.",
                body="Monster body.",
                updated="2026-06-16",
            )
        )
        profile = IngestProfile(
            id="rulebook",
            enabled=True,
            description="Rules.",
            priority=100,
            namespace_mode="source-slug",
            require_namespace_for_new_pages=True,
            prevent_singular_plural_siblings=True,
            overlays={"ingest": "Use {source_namespace}."},
        )
        workflow = build_ingest_workflow(
            store,
            "2026-06-16",
            profiles=(profile,),
            source_locator="Sword World RPG - Complete Edition.pdf",
            new_page_prefix="sword-world-rpg-complete-edition",
        )
        write = workflow.tools["write_page"].callable

        with pytest.raises(Exception, match="singular/plural normalization"):
            _plan_page(
                workflow,
                "sword-world-rpg-complete-edition-wraith",
                category="concept",
                summary="Wraith Form concept.",
            )

        _plan_page(
            workflow,
            "sword-world-rpg-complete-edition-wraith-form",
            category="concept",
            summary="Wraith Form concept.",
        )
        result = write(
            page_id="sword-world-rpg-complete-edition-wraith-form",
            page_kind="concept",
            summary="Wraith Form concept.",
            page_body="Body.",
        )
        assert "sword-world-rpg-complete-edition-wraith-form" in result

    def test_namespace_profile_allows_existing_generic_page_after_read(
        self, store: WikiStore
    ) -> None:
        store.write_page(
            wiki_page(
                name="role-playing-game",
                category="concept",
                summary="Existing generic page.",
                body="Old body.",
                updated="2026-06-16",
            )
        )
        workflow = build_ingest_workflow(
            store,
            "2026-06-16",
            new_page_prefix="sword-world-rpg-complete-edition",
        )
        workflow.tools["read_page"].callable(page_id="role-playing-game")
        _plan_page(
            workflow,
            "role-playing-game",
            category="concept",
            summary="Existing generic page.",
            action="enrich",
        )

        result = workflow.tools["write_page"].callable(
            page_id="role-playing-game",
            page_kind="concept",
            summary="Existing generic page.",
            page_body="Old body plus sourced context.",
        )

        assert "role-playing-game" in result

    def test_pdf_map_large_page_preview_does_not_authorize_rewrite(self, store: WikiStore) -> None:
        store.write_page(
            wiki_page(
                name="big-chapter",
                category="source",
                summary="Large prior chapter.",
                body="Large body.\n" + ("x" * 7000),
                updated="2026-06-16",
            )
        )
        workflow = build_map_workflow(store, "2026-06-16")

        preview = workflow.tools["read_page"].callable(page_id="big-chapter")

        assert "[TRUNCATED: page preview" in preview
        repeated = workflow.tools["read_page"].callable(page_id="big-chapter")
        assert "already previewed" in repeated
        _plan_page(
            workflow,
            "big-chapter",
            summary="Large prior chapter.",
            action="enrich",
        )
        with pytest.raises(Exception, match="write_page replaces"):
            workflow.tools["write_page"].callable(
                page_id="big-chapter",
                page_kind="source",
                summary="Large prior chapter.",
                page_body="Accidental rewrite from preview.",
            )

    def test_pdf_integrate_writes_only_hub_page(self, store: WikiStore) -> None:
        store.write_page(
            wiki_page(
                name="sword-world-rpg-complete-edition",
                category="source",
                summary="Old hub.",
                body="Old hub body.",
                updated="2026-06-16",
            )
        )
        workflow = build_integrate_workflow(
            store,
            "2026-06-16",
            source_locator="Sword World RPG - Complete Edition.pdf",
        )
        _plan_page(
            workflow,
            "sword-world-rpg-complete-edition",
            summary="Hub page.",
            action="enrich",
        )
        workflow.tools["read_page"].callable(page_id="sword-world-rpg-complete-edition")

        result = workflow.tools["write_page"].callable(
            page_id="sword-world-rpg-complete-edition-chapter-13-2-1-humans",
            page_kind="source",
            summary="Hub page.",
            page_body="Hub body.",
        )

        assert "sword-world-rpg-complete-edition" in result
        assert "sword-world-rpg-complete-edition" in store.list_pages()
        assert "sword-world-rpg-complete-edition-chapter-13-2-1-humans" not in store.list_pages()
        assert "Hub body." in store.read_page("sword-world-rpg-complete-edition")

    def test_pdf_integrate_recovers_content_embedded_in_summary(self, store: WikiStore) -> None:
        workflow = build_integrate_workflow(
            store,
            "2026-06-16",
            source_locator="Sword World RPG - Complete Edition.pdf",
        )
        _plan_page(workflow, "sword-world-rpg-complete-edition", summary="Hub summary.")

        workflow.tools["write_page"].callable(
            summary="Hub summary.\nparameter=page_body>\n# Hub\n\n[[linked-page]]",
            **{" sources": '["Sword World RPG - Complete Edition.pdf"]'},
        )

        hub = store.read_page("sword-world-rpg-complete-edition")
        assert "summary: Hub summary." in hub
        assert "[[linked-page]]" in hub
        assert "Sword World RPG - Complete Edition.pdf" in hub

    def test_pdf_integrate_supplements_sparse_page_map_links(self, store: WikiStore) -> None:
        workflow = build_integrate_workflow(
            store,
            "2026-06-16",
            source_locator="Sword World RPG - Complete Edition.pdf",
            required_link_targets=("alpha", "beta", "gamma"),
            min_required_links=2,
        )
        _plan_page(workflow, "sword-world-rpg-complete-edition", summary="Sparse hub.")

        workflow.tools["write_page"].callable(
            summary="Sparse hub.",
            page_body="Only links [[alpha]].",
        )

        hub = store.read_page("sword-world-rpg-complete-edition")
        assert "Only links [[alpha]]." in hub
        assert "## Page-Map Navigation" in hub
        assert "[[beta]]" in hub
        assert "[[gamma]]" in hub

    def test_pdf_integrate_renders_source_summary_fields_as_hub_body(
        self, store: WikiStore
    ) -> None:
        workflow = build_integrate_workflow(
            store,
            "2026-06-16",
            source_locator="Sword World RPG - Complete Edition.pdf",
            required_link_targets=("alpha", "beta", "gamma"),
            min_required_links=2,
        )
        _plan_page(workflow, "sword-world-rpg-complete-edition", summary="Hub summary.")

        workflow.tools["write_page"].callable(
            summary="Hub summary.",
            source_record_text="Short source record.",
            claim_bullets=[
                {
                    "bullet_text": (
                        "A compact supported claim. "
                        "(raw/Sword World RPG - Complete Edition.pdf)"
                    ),
                    "covered_source_claims": ["source-claim-unit-0001-0001"],
                }
            ],
            sources=["Sword World RPG - Complete Edition.pdf"],
        )

        hub = store.read_page("sword-world-rpg-complete-edition")
        assert "## Source record" in hub
        assert "A compact supported claim." in hub
        assert "## Page-Map Navigation" in hub
        assert "[[alpha]]" in hub
        assert "[[beta]]" in hub
        assert "[[gamma]]" in hub

    def test_pdf_integrate_does_not_add_navigation_when_linked(self, store: WikiStore) -> None:
        workflow = build_integrate_workflow(
            store,
            "2026-06-16",
            source_locator="Sword World RPG - Complete Edition.pdf",
            required_link_targets=("alpha", "beta", "gamma"),
            min_required_links=2,
        )
        _plan_page(workflow, "sword-world-rpg-complete-edition", summary="Linked hub.")

        workflow.tools["write_page"].callable(
            summary="Linked hub.",
            page_body="Links [[alpha]] and [[beta]].",
        )

        hub = store.read_page("sword-world-rpg-complete-edition")
        assert "[[alpha]] and [[beta]]" in hub
        assert "## Page-Map Navigation" not in hub

    def test_write_page_accepts_single_source_string(self, store: WikiStore) -> None:
        workflow = build_map_workflow(store, "2026-06-16")
        _plan_page(
            workflow,
            "sword-world-rpg-complete-edition-test",
            summary="Test source.",
        )

        workflow.tools["write_page"].callable(
            page_id="sword-world-rpg-complete-edition-test",
            page_kind="source",
            summary="Test source.",
            page_body="Body.",
            sources="[Sword World RPG](raw/Sword World RPG - Complete Edition.pdf)",
        )

        assert "Sword World RPG - Complete Edition.pdf" in store.read_page(
            "sword-world-rpg-complete-edition-test"
        )
