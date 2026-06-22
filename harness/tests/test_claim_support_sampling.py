"""Tests for claim-support sample ordering and coverage reports."""

from helpers import wiki_page

from llmwiki.domain.citations import SourceInventory
from llmwiki.domain.claim_support_sampling import claim_support_risk_tags
from llmwiki.domain.claim_support_selection import select_claim_support_candidates
from llmwiki.domain.evidence_registry import (
    EvidenceRecord,
    EvidenceRegistry,
    SourceRange,
    source_text_from_text,
)
from llmwiki.domain.pages import render_page
from llmwiki.domain.source_summary import (
    SourceSummaryBullet,
    SourceSummaryDraft,
    SourceSummaryDraftArtifact,
)

TODAY = "2026-06-22"


def test_stratified_selector_covers_more_source_buckets_under_same_cap() -> None:
    pages, artifacts, registry = _multi_page_source_summary_frame(
        "book.md",
        (
            ("book-1-alpha", ("One A is supported.", "One B is supported.")),
            ("book-2-beta", ("Two A is supported.", "Two B is supported.")),
            ("book-3-gamma", ("Three A is supported.", "Three B is supported.")),
            ("book-4-delta", ("Four A is supported.", "Four B is supported.")),
        ),
    )

    ordered = select_claim_support_candidates(
        pages,
        SourceInventory.from_raw_relative_paths(("book.md",)),
        (registry,),
        artifacts,
        max_claims=4,
        source="raw/book.md",
        sample_strategy="ordered",
    )
    stratified = select_claim_support_candidates(
        pages,
        SourceInventory.from_raw_relative_paths(("book.md",)),
        (registry,),
        artifacts,
        max_claims=4,
        source="raw/book.md",
        sample_strategy="stratified",
    )

    assert ordered.sample_coverage is not None
    assert stratified.sample_coverage is not None
    assert ordered.sample_coverage.sampled_source_buckets == 2
    assert stratified.sample_coverage.sampled_source_buckets == 4
    assert stratified.sample_coverage.sampled_pages == 4


def test_sample_coverage_reports_risk_tags_and_candidate_kinds() -> None:
    pages, artifacts, registry = _multi_page_source_summary_frame(
        "book.md",
        (
            ("book-1-alpha", ("A roll must beat target score 12.",)),
            ("book-2-prose", ("A character cannot act without spending 2 points.",)),
        ),
    )

    selection = select_claim_support_candidates(
        pages,
        SourceInventory.from_raw_relative_paths(("book.md",)),
        (registry,),
        artifacts[:1],
        max_claims=2,
        source="raw/book.md",
        sample_strategy="stratified",
    )

    assert claim_support_risk_tags("A roll must beat target score 12.") == (
        "requirement",
        "quantitative",
        "procedure",
        "mechanism",
    )
    assert selection.sample_coverage is not None
    assert {candidate.candidate_kind for candidate in selection.candidates} == {
        "source-summary",
        "prose-line",
    }
    rendered = selection.sample_coverage.render()
    assert "source-summary: 1/1" in rendered
    assert "prose-line: 1/1" in rendered
    assert "requirement: 1/1" in rendered


def test_page_band_coverage_uses_available_candidate_frame() -> None:
    pages, artifacts, registry = _multi_page_source_summary_frame(
        "book.md",
        tuple((f"topic-{index}", (f"Topic {index} is supported.",)) for index in range(1, 7)),
    )

    selection = select_claim_support_candidates(
        pages,
        SourceInventory.from_raw_relative_paths(("book.md",)),
        (registry,),
        artifacts,
        max_claims=2,
        source="raw/book.md",
        sample_strategy="stratified",
    )

    assert selection.sample_coverage is not None
    assert (
        selection.sample_coverage.sampled_source_buckets
        <= selection.sample_coverage.available_source_buckets
    )


def _multi_page_source_summary_frame(
    source_locator: str,
    pages: tuple[tuple[str, tuple[str, ...]], ...],
) -> tuple[dict[str, str], tuple[SourceSummaryDraftArtifact, ...], EvidenceRegistry]:
    source_text = "\n".join(
        claim_text for _, claim_texts in pages for claim_text in claim_texts
    )
    source = source_text_from_text(source_locator, source_text)
    page_texts: dict[str, str] = {}
    artifacts: list[SourceSummaryDraftArtifact] = []
    ranges: list[SourceRange] = []
    records: list[EvidenceRecord] = []
    line_number = 1
    for page_id, claim_texts in pages:
        bullets: list[SourceSummaryBullet] = []
        page_lines: list[str] = []
        for index, claim_text in enumerate(claim_texts, start=1):
            claim_id = f"claim-{page_id}-{index}"
            bullet_text = f"{claim_text} (raw/{source_locator})"
            bullets.append(SourceSummaryBullet(bullet_text, (claim_id,)))
            page_lines.append(f"- {bullet_text}")
            range_id = f"source-range-{page_id}-{index}"
            ranges.append(
                SourceRange(
                    source_range_id=range_id,
                    page_id=page_id,
                    source_locator=source_locator,
                    page_range=None,
                    line_range=(line_number, line_number),
                    heading_path=page_id,
                )
            )
            records.append(
                EvidenceRecord(
                    evidence_id=f"evidence-{claim_id}",
                    source_locator=source_locator,
                    source_hash=source.source_hash,
                    source_range_id=range_id,
                    line_range=(line_number, line_number),
                    excerpt=claim_text,
                    excerpt_digest=claim_id,
                    evidence_kind="source-claim",
                    source_claim_id=claim_id,
                )
            )
            line_number += 1
        page_texts[page_id] = _page_text(page_id, "\n".join(page_lines))
        artifacts.append(_artifact(source_locator, page_id, *bullets))
    return (
        page_texts,
        tuple(artifacts),
        EvidenceRegistry(
            registry_id=f"registry-{source_locator}",
            source_texts=(source,),
            source_ranges=tuple(ranges),
            evidence_records=tuple(records),
        ),
    )


def _page_text(page_id: str, body: str) -> str:
    return render_page(
        wiki_page(
            name=page_id,
            category="source",
            summary=f"About {page_id}.",
            body=body,
            sources=(f"{page_id}.md",),
            updated=TODAY,
        )
    )


def _artifact(
    source_locator: str, page_id: str, *bullets: SourceSummaryBullet
) -> SourceSummaryDraftArtifact:
    return SourceSummaryDraftArtifact(
        source_locator=source_locator,
        write_id=f"write-{page_id}",
        page_id_hint=page_id,
        draft=SourceSummaryDraft("Source record.", bullets),
    )
