"""Tests for persisted ingest-confidence artifact reuse."""

import pytest

from llmwiki.config import WikiPaths
from llmwiki.domain.evidence_registry import build_evidence_registry, source_text_from_text
from llmwiki.domain.evidence_registry_io import registry_to_json
from llmwiki.domain.objects import SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import (
    build_markdown_page_plan,
    observation_report,
    page_plan_to_json,
)
from llmwiki.runtime.ingest_confidence_artifacts import prepare_ingest_confidence_artifacts
from llmwiki.store import WikiStore


def test_missing_atoms_are_built_from_persisted_registry(
    paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
) -> None:
    source_text = "# Alpha\n\n**Damage** = power + modifier"
    (paths.raw_dir / "alpha.md").write_text(source_text, encoding="utf-8")
    store = WikiStore(paths)
    raw_source = store.raw_source("alpha.md")
    plan = build_markdown_page_plan(
        plan_id="persisted-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=source_text,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-22",
    )
    registry = build_evidence_registry(plan, (source_text_from_text("alpha.md", source_text),))
    store.write_page_plan_artifacts("alpha.md", page_plan_to_json(plan), observation_report(plan))
    store.write_evidence_registry_artifact("alpha.md", registry_to_json(registry))

    def fail_rebuild(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("persisted artifacts should be reused")

    monkeypatch.setattr(
        "llmwiki.runtime.ingest_confidence_artifacts.pdf_extraction_artifact",
        fail_rebuild,
    )
    monkeypatch.setattr(
        "llmwiki.runtime.ingest_confidence_artifacts.build_current_registry",
        fail_rebuild,
    )

    prepared = prepare_ingest_confidence_artifacts(
        store=store,
        cache_dir=paths.cache_dir,
        source_locator="alpha.md",
        today="2026-06-22",
    )

    assert prepared.technical_atom_catalog is not None
    assert prepared.technical_atom_catalog.technical_atoms
    assert store.read_technical_atom_catalog_artifact("alpha.md") is not None
    assert any(
        decision.artifact_kind == "evidence-registry"
        and decision.decision == "reuse"
        and "matching source hash" in decision.reason
        for decision in prepared.decisions
    )
