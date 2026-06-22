"""Tests for Claim Support Audit selection, checks, and workflow filing."""

import json

from helpers import wiki_page

from llmwiki.config import WikiPaths
from llmwiki.domain.claim_support import ClaimSupportAuditReport
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
from llmwiki.store import WikiStore

TODAY = "2026-06-22"


def test_selector_prefers_source_summary_bullets_and_links_evidence() -> None:
    selection = select_claim_support_candidates(
        {
            "alpha": _page_text(
                "alpha",
                "- Alpha is supported. (raw/alpha.md)\n- Prose fallback. (raw/alpha.md)",
            )
        },
        _inventory("alpha.md"),
        (_registry("alpha.md", "alpha", "claim-alpha", "Alpha is supported."),),
        (
            _artifact(
                "alpha.md",
                "alpha",
                SourceSummaryBullet("Alpha is supported. (raw/alpha.md)", ("claim-alpha",)),
            ),
        ),
        max_claims=5,
    )

    assert selection.candidate_count == 2
    assert selection.candidates[0].candidate_kind == "source-summary"
    assert selection.candidates[0].source_claim_ids == ("claim-alpha",)
    assert selection.candidates[0].evidence_ids
    assert "Alpha is supported." in selection.candidates[0].evidence_excerpts[0]


def test_source_summary_candidates_include_page_citation_evidence() -> None:
    registry = EvidenceRegistry(
        registry_id="registry-alpha",
        source_texts=(source_text_from_text("alpha.md", "Broad page support."),),
        source_ranges=(
            SourceRange(
                source_range_id="range-alpha",
                page_id="alpha",
                source_locator="alpha.md",
                page_range=None,
                line_range=None,
                heading_path="Alpha",
            ),
        ),
        evidence_records=(
            EvidenceRecord(
                evidence_id="evidence-narrow",
                source_locator="alpha.md",
                source_hash="hash",
                source_range_id="range-alpha",
                line_range=None,
                excerpt="Narrow source-claim support.",
                excerpt_digest="narrow",
                evidence_kind="source-claim",
                source_claim_id="claim-alpha",
            ),
            EvidenceRecord(
                evidence_id="evidence-broad",
                source_locator="alpha.md",
                source_hash="hash",
                source_range_id="range-alpha",
                line_range=None,
                excerpt="Broad page support.",
                excerpt_digest="broad",
                evidence_kind="citation",
            ),
        ),
    )

    selection = select_claim_support_candidates(
        {"alpha": _page_text("alpha", "Alpha is supported. (raw/alpha.md)")},
        _inventory("alpha.md"),
        (registry,),
        (
            _artifact(
                "alpha.md",
                "alpha",
                SourceSummaryBullet("Alpha is supported. (raw/alpha.md)", ("claim-alpha",)),
            ),
        ),
        max_claims=1,
    )

    assert "evidence-narrow" in selection.candidates[0].evidence_ids
    assert "evidence-broad" in selection.candidates[0].evidence_ids


def test_source_summary_excerpts_rank_citation_evidence_by_claim_terms() -> None:
    source = source_text_from_text(
        "alpha.md",
        "A character sheet stores notes.\n"
        "Players choose a race such as human, dwarf, grassrunner, elf, or half-elf.\n",
    )
    source_range = SourceRange(
        source_range_id="range-alpha",
        page_id="alpha",
        source_locator="alpha.md",
        page_range=None,
        line_range=(1, source.line_count),
        heading_path="Alpha",
    )
    registry = EvidenceRegistry(
        registry_id="registry-alpha",
        source_texts=(source,),
        source_ranges=(source_range,),
        evidence_records=(
            EvidenceRecord(
                evidence_id="evidence-irrelevant",
                source_locator="alpha.md",
                source_hash=source.source_hash,
                source_range_id=source_range.source_range_id,
                line_range=(1, 1),
                excerpt="A character sheet stores notes.",
                excerpt_digest="irrelevant",
                evidence_kind="citation",
            ),
            EvidenceRecord(
                evidence_id="evidence-races",
                source_locator="alpha.md",
                source_hash=source.source_hash,
                source_range_id=source_range.source_range_id,
                line_range=(2, 2),
                excerpt=(
                    "Players choose a race such as human, dwarf, grassrunner, elf, "
                    "or half-elf."
                ),
                excerpt_digest="races",
                evidence_kind="citation",
            ),
        ),
    )

    selection = select_claim_support_candidates(
        {
            "alpha": _page_text(
                "alpha",
                "Players choose a race such as human, dwarf, grassrunner, elf, "
                "or half-elf. (raw/alpha.md)",
            )
        },
        _inventory("alpha.md"),
        (registry,),
        (
            _artifact(
                "alpha.md",
                "alpha",
                SourceSummaryBullet(
                    "Players choose a race such as human, dwarf, grassrunner, elf, "
                    "or half-elf. (raw/alpha.md)",
                    ("stale-claim-id",),
                ),
            ),
        ),
        max_claims=1,
    )

    assert selection.candidates[0].evidence_excerpts[0].startswith("evidence-races:")


def test_selector_builds_prose_candidates_and_source_filter() -> None:
    selection = select_claim_support_candidates(
        {
            "alpha": _page_text("alpha", "Alpha prose. (raw/alpha.md)"),
            "beta": _page_text("beta", "Beta prose. (raw/beta.md)"),
        },
        _inventory("alpha.md", "beta.md"),
        (
            _registry("alpha.md", "alpha", "claim-alpha", "Alpha prose."),
            _registry("beta.md", "beta", "claim-beta", "Beta prose."),
        ),
        (),
        max_claims=5,
        source="raw/beta.md",
    )

    assert [candidate.page_id for candidate in selection.candidates] == ["beta"]
    assert selection.candidates[0].citation_texts == ("raw/beta.md",)


def test_source_summary_source_filter_skips_stale_cross_source_artifacts() -> None:
    selection = select_claim_support_candidates(
        {
            "alpha": _page_text("alpha", "Alpha prose. (raw/alpha.md)"),
            "beta": _page_text("beta", "Beta prose. (raw/beta.md)"),
        },
        _inventory("alpha.md", "beta.md"),
        (
            _registry("alpha.md", "alpha", "claim-alpha", "Alpha prose."),
            _registry("beta.md", "beta", "claim-beta", "Beta prose."),
        ),
        (
            _artifact(
                "alpha.md",
                "alpha",
                SourceSummaryBullet("Beta prose. (raw/beta.md)", ("claim-beta",)),
            ),
            _artifact(
                "alpha.md",
                "alpha",
                SourceSummaryBullet("Alpha prose. (raw/alpha.md)", ("claim-alpha",)),
                SourceSummaryBullet("Alpha prose. (raw/alpha.md)", ("claim-alpha",)),
            ),
        ),
        max_claims=5,
        source="raw/alpha.md",
    )

    assert selection.candidate_count == 1
    assert [candidate.claim_text for candidate in selection.candidates] == ["Alpha prose."]


def test_missing_evidence_skips_model_judgment() -> None:
    selection = select_claim_support_candidates(
        {"alpha": _page_text("alpha", "Alpha is unsupported. (raw/alpha.md)")},
        _inventory("alpha.md"),
        (),
        (),
        max_claims=5,
    )

    assert selection.candidates == ()
    assert selection.blocked_candidates[0].page_id == "alpha"
    assert selection.deterministic_findings[0].category == "missing-evidence"


def test_locator_mismatch_source_range_and_copied_evidence_findings_render() -> None:
    registry = _registry(
        "alpha.md",
        "alpha",
        "claim-alpha",
        "Actual evidence.",
        source_text="Actual evidence.\nNearby line.",
        line_range=(1, 1),
    )
    selection = select_claim_support_candidates(
        {
            "alpha": _page_text(
                "alpha",
                '"Wrong evidence." (raw/alpha.md normalized:L1)\n'
                "Outside line. (raw/alpha.md normalized:L2)\n"
                '"Different copied text." (raw/alpha.md)',
            )
        },
        _inventory("alpha.md"),
        (registry,),
        (),
        max_claims=5,
    )

    categories = {finding.category for finding in selection.deterministic_findings}
    assert {"locator-mismatch", "source-range", "copied-evidence"} <= categories
    report = ClaimSupportAuditReport(
        run_id="test-run",
        selection=selection,
        verdicts=(),
        model_report="No model calls.",
    ).render()
    assert "locator-mismatch" in report
    assert "source-range" in report
    assert "copied-evidence" in report


def test_store_reads_source_summary_draft_artifacts(paths: WikiPaths) -> None:
    store = WikiStore(paths)
    store.write_source_summary_draft_artifact(
        "alpha.md",
        "write-alpha",
        json.dumps(
            {
                "source_record_text": "Alpha record.",
                "claim_bullets": [
                    {
                        "bullet_text": "Alpha is supported. (raw/alpha.md)",
                        "covered_source_claims": ["claim-alpha"],
                    }
                ],
            }
        ),
    )

    artifacts = store.read_source_summary_draft_artifacts("alpha.md")

    assert artifacts[0].page_id_hint == "alpha"
    assert artifacts[0].draft.claim_bullets[0].covered_source_claims == ("claim-alpha",)


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


def _inventory(*source_locators: str):
    from llmwiki.domain.citations import SourceInventory

    return SourceInventory.from_raw_relative_paths(source_locators)


def _artifact(
    source_locator: str, page_id: str, *bullets: SourceSummaryBullet
) -> SourceSummaryDraftArtifact:
    return SourceSummaryDraftArtifact(
        source_locator=source_locator,
        write_id=f"write-{page_id}",
        page_id_hint=page_id,
        draft=SourceSummaryDraft("Source record.", bullets),
    )


def _registry(
    source_locator: str,
    page_id: str,
    claim_id: str,
    excerpt: str,
    *,
    source_text: str | None = None,
    line_range: tuple[int, int] | None = None,
) -> EvidenceRegistry:
    text = source_text or excerpt
    source = source_text_from_text(source_locator, text)
    source_range = SourceRange(
        source_range_id=f"source-range-{page_id}",
        page_id=page_id,
        source_locator=source_locator,
        page_range=None,
        line_range=line_range or (1, source.line_count),
        heading_path=page_id,
    )
    return EvidenceRegistry(
        registry_id=f"registry-{page_id}",
        source_texts=(source,),
        source_ranges=(source_range,),
        evidence_records=(
            EvidenceRecord(
                evidence_id=f"evidence-{claim_id}",
                source_locator=source_locator,
                source_hash=source.source_hash,
                source_range_id=source_range.source_range_id,
                line_range=None,
                excerpt=excerpt,
                excerpt_digest="digest",
                evidence_kind="source-claim",
                source_claim_id=claim_id,
            ),
        ),
    )
