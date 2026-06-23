"""Replay accepted source-summary drafts with current technical atoms."""

import json

from llmwiki.domain.objects import Evidence, PagePlan, PlannedPageWrite, RawSource, SourceBundle
from llmwiki.domain.pages import PageMetadata
from llmwiki.domain.source_summary import SourceSummaryClaimRequirement, SourceSummaryPlan
from llmwiki.domain.technical_atom_io import technical_atom_catalog_to_json
from llmwiki.domain.technical_atoms import TechnicalAtom, TechnicalAtomCatalog
from llmwiki.pdf.manifest import ChunkRecord
from llmwiki.runtime.source_summary_replay import replay_source_summary_work_unit
from llmwiki.store import WikiStore


def test_replay_refreshes_page_with_current_technical_atoms(store: WikiStore) -> None:
    raw_source = RawSource.from_locator("book.pdf")
    planned_write = _planned_source_summary_write(raw_source)
    page_plan = _page_plan(raw_source, planned_write)
    store.write_source_summary_draft_artifact(
        "book.pdf",
        "write-book-functions",
        json.dumps(
            {
                "source_record_text": "Functions are introduced with runnable examples.",
                "claim_bullets": [
                    {
                        "bullet_text": "Functions are shown through code. (raw/book.pdf p.1-2)",
                        "covered_source_claims": ["source-claim-unit-0001-0001"],
                    }
                ],
            }
        ),
    )
    store.write_technical_atom_catalog_artifact(
        "book.pdf", technical_atom_catalog_to_json(_technical_atom_catalog())
    )

    replay = replay_source_summary_work_unit(
        store,
        "2026-06-23",
        "book.pdf",
        page_plan,
        (ChunkRecord(1, "Functions", 1, 2, 300),),
    )

    page = store.read_page("book-functions")
    assert replay is not None
    assert replay.page_ids == ("book-functions",)
    assert "## Technical details" in page
    assert "const square = (n) => n * n;" in page


def test_replay_accepts_prior_draft_when_inferred_coverage_is_complete(
    store: WikiStore,
) -> None:
    raw_source = RawSource.from_locator("book.pdf")
    planned_write = PlannedPageWrite(
        write_id="write-book-problem",
        action="enrich-existing",
        page_metadata=PageMetadata(
            page_id="book-problem",
            page_kind="source",
            summary="Book problem.",
            sources=("raw/book.pdf p.10-12",),
        ),
        extracted_units=("unit-0001",),
        evidence=(Evidence(raw_source=raw_source, locator="p.10-12"),),
        source_summary_plan=SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-book-problem",
            page_id="book-problem",
            selected_source_claims=("claim-hidden", "claim-calls", "claim-moves"),
            selected_claim_requirements=(
                SourceSummaryClaimRequirement("claim-hidden", cue_terms=("board", "hidden")),
                SourceSummaryClaimRequirement("claim-calls", cue_terms=("calls", "direction")),
                SourceSummaryClaimRequirement(
                    "claim-moves", cue_terms=("player", "moves", "chequer", "following")
                ),
            ),
            required_source_citations=("raw/book.pdf p.10-12",),
        ),
    )
    store.write_source_summary_draft_artifact(
        "book.pdf",
        "write-book-problem",
        json.dumps(
            {
                "source_record_text": "The board has unknown size and hidden contents.",
                "claim_bullets": [
                    {
                        "bullet_text": "The board is hidden. (raw/book.pdf p.10-12)",
                        "covered_source_claims": ["claim-hidden"],
                    },
                    {
                        "bullet_text": (
                            "The player moves the chequer while calling directions. "
                            "(raw/book.pdf p.10-12)"
                        ),
                        "covered_source_claims": ["claim-calls"],
                    },
                ],
            }
        ),
    )

    replay = replay_source_summary_work_unit(
        store,
        "2026-06-23",
        "book.pdf",
        _page_plan(raw_source, planned_write),
        (ChunkRecord(1, "Problem", 10, 12, 300),),
    )

    page = store.read_page("book-problem")
    assert replay is not None
    assert page.count("- ") == 2
    assert "The player moves the chequer while calling directions." in page


def _planned_source_summary_write(raw_source: RawSource) -> PlannedPageWrite:
    return PlannedPageWrite(
        write_id="write-book-functions",
        action="enrich-existing",
        page_metadata=PageMetadata(
            page_id="book-functions",
            page_kind="source",
            summary="Book functions.",
            sources=("raw/book.pdf p.1-2",),
        ),
        extracted_units=("unit-0001",),
        evidence=(Evidence(raw_source=raw_source, locator="p.1-2"),),
        source_summary_plan=SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-book-functions",
            page_id="book-functions",
            selected_source_claims=("source-claim-unit-0001-0001",),
            required_source_citations=("raw/book.pdf p.1-2",),
        ),
    )


def _page_plan(raw_source: RawSource, planned_write: PlannedPageWrite) -> PagePlan:
    return PagePlan(
        plan_id="plan-book",
        source_bundle=SourceBundle.one(raw_source),
        extracted_units=(),
        source_claims=(),
        source_claim_groups=(),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(planned_write,),
    )


def _technical_atom_catalog() -> TechnicalAtomCatalog:
    return TechnicalAtomCatalog(
        catalog_id="technical-atom-catalog-book",
        source_locator="book.pdf",
        artifact_fingerprint="plan-book",
        technical_atoms=(
            TechnicalAtom(
                technical_atom_id="technical-atom-square",
                source_locator="book.pdf",
                page_id="book-functions",
                atom_kind="code",
                title="square function",
                technical_payload="const square = (n) => n * n;",
                normalized_fields=(
                    ("language", "javascript"),
                    ("source_citation", "raw/book.pdf p.1-2"),
                ),
                source_claim_ids=("source-claim-unit-0001-0001",),
                evidence_ids=("evidence-book-functions",),
                source_range_id="source-range-book-functions",
            ),
        ),
    )
