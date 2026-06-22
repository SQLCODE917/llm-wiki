"""Tests for source-level ingest confidence reporting."""

import pytest

from llmwiki.cli import _build_parser, _run
from llmwiki.config import WikiPaths
from llmwiki.domain.ingest_confidence import (
    ArtifactFingerprint,
    ArtifactReuseDecision,
    IngestConfidenceGate,
    IngestConfidenceReport,
    decide_artifact_reuse,
    validation_finding,
)
from llmwiki.domain.objects import Schema, SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import (
    build_markdown_page_plan,
    observation_report,
    page_plan_from_json,
    page_plan_to_json,
)
from llmwiki.runtime.ingest_confidence_artifacts import prepare_ingest_confidence_artifacts
from llmwiki.store import WikiStore


def test_artifact_reuse_requires_matching_fingerprint() -> None:
    current = _fingerprint("alpha-hash")

    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=_fingerprint("alpha-hash"),
            artifact_exists=True,
        ).decision
        == "reuse"
    )
    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=_fingerprint("stale-hash"),
            artifact_exists=True,
        ).decision
        == "rebuild"
    )
    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=current,
            artifact_exists=False,
        ).decision
        == "missing"
    )
    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=current,
            artifact_exists=True,
            fresh=True,
        ).decision
        == "rebuild"
    )


def test_report_rendering_keeps_skipped_gate_visible() -> None:
    finding = validation_finding(
        severity="info",
        category="claim-support",
        source_locator="alpha.md",
        message="Skipped because there are no candidates.",
    )
    report = IngestConfidenceReport(
        run_id="test-run",
        source_locator="alpha.md",
        artifact_decisions=(
            ArtifactReuseDecision(
                "page-plan",
                "cache/page-plan.json",
                "reuse",
                "fingerprint matches",
                "abc123",
            ),
        ),
        gates=(
            IngestConfidenceGate(
                "claim-support",
                "model-assisted",
                "raw/alpha.md",
                "skipped",
                (finding.finding_id,),
                finding.message,
            ),
        ),
        findings=(finding,),
    )

    rendered = report.render()

    assert "Confidence status: passed" in rendered
    assert "### claim-support" in rendered
    assert "Status: skipped" in rendered
    assert "Skipped because there are no candidates." in rendered


@pytest.mark.asyncio
async def test_ingest_confidence_files_report_and_reuses_artifacts(
    paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
) -> None:
    (paths.raw_dir / "alpha.md").write_text("# Alpha\n\nAlpha source text.", encoding="utf-8")

    async def fail_backend(_config: object) -> object:
        raise AssertionError("ingest-confidence should skip the model for blocker gates")

    monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
    parser = _build_parser()

    first = await _run(
        parser.parse_args(
            [
                "--root",
                str(paths.root),
                "ingest-confidence",
                "raw/alpha.md",
                "--max-claims",
                "1",
            ]
        )
    )
    second = await _run(
        parser.parse_args(
            [
                "--root",
                str(paths.root),
                "ingest-confidence",
                "raw/alpha.md",
                "--max-claims",
                "1",
            ]
        )
    )

    store = WikiStore(paths)
    filed = store.read_page("wiki-ingest-confidence")
    log_text = paths.log_path.read_text(encoding="utf-8")

    assert "page-plan: missing" in first.output
    assert "Skipped because deterministic blockers exist." in first.output
    assert "page-plan: reuse" in second.output
    assert "evidence-registry: reuse" in second.output
    assert "Source: raw/alpha.md" in filed
    assert "ingest-confidence" in log_text


def test_ingest_confidence_uses_persisted_page_plan_without_fingerprint(
    paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
) -> None:
    source_path = paths.raw_dir / "alpha.md"
    source_path.write_text("# Alpha\n\nAlpha source text.", encoding="utf-8")
    store = WikiStore(paths)
    raw_source = store.raw_source("alpha.md")
    plan = build_markdown_page_plan(
        plan_id="persisted-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=source_path.read_text(encoding="utf-8"),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-22",
    )
    store.write_page_plan_artifacts("alpha.md", page_plan_to_json(plan), observation_report(plan))
    plan_path = store.page_plan_artifact_dir("alpha.md") / "page-plan.json"
    assert plan_path.is_file()
    assert page_plan_from_json(plan_path.read_text(encoding="utf-8")).plan_id == "persisted-plan"

    def fail_rebuild(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("persisted page plan should be reused")

    monkeypatch.setattr(
        "llmwiki.runtime.ingest_confidence_artifacts._build_current_page_plan",
        fail_rebuild,
    )

    prepared = prepare_ingest_confidence_artifacts(
        store=store,
        cache_dir=paths.cache_dir,
        source_locator="alpha.md",
        today="2026-06-22",
    )

    assert prepared.page_plan is not None
    assert prepared.page_plan.plan_id == "persisted-plan"
    assert prepared.evidence_registry is not None
    assert any(
        decision.artifact_kind == "page-plan"
        and decision.decision == "reuse"
        and "parsed persisted" in decision.reason
        for decision in prepared.decisions
    )


def _fingerprint(source_hash: str) -> ArtifactFingerprint:
    return ArtifactFingerprint.from_schema(
        source_locator="alpha.md",
        source_hash=source_hash,
        schema=Schema(),
    )
