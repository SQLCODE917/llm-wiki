from dataclasses import replace

from llmwiki.domain.ledger.staged_flow import (
    accepted_pages,
    build_lint_run,
    build_publish_run,
    build_source_plan,
    build_staged_page_set,
)
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.ledger_pipeline import build_source_ledger
from llmwiki.runtime.ledger_segmentation import ChunkText

_HASH = "a" * 16


def test_staged_pages_publish_only_after_lint_accepts_them() -> None:
    source_plan = build_source_plan(
        source_locator="src.pdf",
        source_hash=_HASH,
        source_page_id="src",
    )
    page = _page("src", "source", "source-manifest")
    staged = build_staged_page_set(source_plan, (page,))
    lint_run = build_lint_run(
        source_plan=source_plan,
        staged_page_set=staged,
        upstream_write_decision="write-authoritative-page",
    )
    publish_run = build_publish_run(source_plan, staged, lint_run)

    assert lint_run.status == "accepted"
    assert publish_run.status == "published"
    assert publish_run.accepted_page_ids == ("src",)
    assert accepted_pages(staged, publish_run) == (page,)


def test_staged_pages_block_unplanned_page_family_before_publish() -> None:
    source_plan = build_source_plan(
        source_locator="src.pdf",
        source_hash=_HASH,
        source_page_id="src",
    )
    restricted = replace(source_plan, allowed_page_families=("source-manifest",))
    page = _page("src-topic", "concept", "topic-concept")
    staged = build_staged_page_set(restricted, (page,))
    lint_run = build_lint_run(
        source_plan=restricted,
        staged_page_set=staged,
        upstream_write_decision="write-authoritative-page",
    )
    publish_run = build_publish_run(restricted, staged, lint_run)

    assert lint_run.status == "blocked"
    assert lint_run.findings[0].finding_type == "page-family-not-planned"
    assert publish_run.status == "blocked"
    assert publish_run.accepted_page_ids == ()
    assert accepted_pages(staged, publish_run) == ()


def test_source_ledger_persists_stage_artifacts_from_real_pipeline() -> None:
    result = build_source_ledger(
        source_locator="src.pdf",
        source_hash=_HASH,
        evidence_registry_hash="evidence-registry-hash",
        chunks=(
            ChunkText(
                "unit-1",
                "p.1",
                "Root",
                "# Root\n\nA meter has a dial.",
            ),
        ),
        today="2026-07-02",
    )

    assert result.source_plan.source_locator == "src.pdf"
    assert result.extraction_result.claim_ledger_id
    assert result.staged_page_set.source_plan_id == result.source_plan.source_plan_id
    assert result.lint_run.source_plan_id == result.source_plan.source_plan_id
    assert result.publish_run.status == "published"
    assert result.wiki_page is not None
    for filename in (
        "source-plan.json",
        "extraction-result.json",
        "staged-pages.json",
        "lint-run.json",
        "publish-run.json",
        "page-publication-plan.json",
        "evidence-pack-set.json",
        "publication-walkability-report.md",
    ):
        assert filename in result.artifact_files
    member_kinds = {
        member.portable_artifact_kind for member in result.portable_artifact_set.members
    }
    assert "source-plan-artifact" in member_kinds
    assert "publish-run-artifact" in member_kinds


def _page(page_id: str, page_kind: str, page_family: str) -> WikiPage:
    metadata = PageMetadata(
        page_id=page_id,
        page_kind=page_kind,
        page_family=page_family,
        summary=f"{page_id} summary.",
        sources=("raw/src.pdf",),
        projection_coverage_pointer=f"{page_id}@abc",
    )
    return WikiPage.from_metadata(metadata, f"# {page_id}\n")
