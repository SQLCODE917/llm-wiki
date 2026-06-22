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
from llmwiki.domain.objects import Schema
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


def _fingerprint(source_hash: str) -> ArtifactFingerprint:
    return ArtifactFingerprint.from_schema(
        source_locator="alpha.md",
        source_hash=source_hash,
        schema=Schema(),
    )
