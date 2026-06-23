"""Planned source summaries can be regenerated without page reconstruction."""

from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlan,
    IngestRoutePlanState,
    PlannedPage,
)
from llmwiki.domain.objects import PagePlan, PlannedPageWrite, RawSource, SourceBundle
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.source_summary import SourceSummaryPlan
from llmwiki.store import WikiStore
from llmwiki.workflows.tools import write_page_tool


def test_source_summary_plan_rewrites_existing_page_without_prior_read(
    store: WikiStore,
) -> None:
    store.write_page(_existing_page("book-front-matter", "Old generated body."))
    planned_write = _source_summary_write(
        "book-front-matter",
        "raw/book.pdf p.1-2",
        "source-claim-unit-0001-0001",
    )
    state = _accepted_route_state(planned_write)
    tool = write_page_tool(
        store,
        today="2026-06-23",
        read_tracker=set(),
        ingest_route_plan_state=state,
        recoverable_errors=True,
    )

    result = tool.callable(
        page_id="book-front-matter",
        page_kind="source",
        summary="Book front matter.",
        source_record_text="Opening matter for the book.",
        claim_bullets=[
            {
                "bullet_text": "The opening matter identifies the book. (raw/book.pdf p.1-2)",
                "covered_source_claims": ["source-claim-unit-0001-0001"],
            }
        ],
        sources=["raw/book.pdf p.1-2"],
    )

    page = store.read_page("book-front-matter")
    assert "Wrote wiki/book-front-matter.md" in result
    assert "Old generated body." not in page
    assert "The opening matter identifies the book. (raw/book.pdf p.1-2)" in page


def test_non_source_summary_rewrite_still_requires_prior_read(store: WikiStore) -> None:
    store.write_page(_existing_page("book-front-matter", "Old curated body."))
    tool = write_page_tool(
        store,
        today="2026-06-23",
        read_tracker=set(),
        recoverable_errors=True,
    )

    result = tool.callable(
        page_id="book-front-matter",
        page_kind="source",
        summary="Book front matter.",
        page_body="New body.",
        sources=["raw/book.pdf p.1-2"],
    )

    assert "already exists and write_page replaces it entirely" in result
    assert "Old curated body." in store.read_page("book-front-matter")


def _existing_page(page_id: str, body: str) -> WikiPage:
    return WikiPage(
        page_metadata=PageMetadata(
            page_id=page_id,
            page_kind="source",
            summary="Existing generated page.",
            sources=("raw/book.pdf p.1-2",),
        ),
        page_body=body,
    )


def _source_summary_write(page_id: str, citation: str, claim_id: str) -> PlannedPageWrite:
    return PlannedPageWrite(
        write_id=f"write-{page_id}",
        action="enrich-existing",
        page_metadata=PageMetadata(
            page_id=page_id,
            page_kind="source",
            summary="Book front matter.",
            sources=(citation,),
        ),
        extracted_units=("unit-0001",),
        source_summary_plan=SourceSummaryPlan(
            source_summary_plan_id=f"source-summary-plan-{page_id}",
            page_id=page_id,
            selected_source_claims=(claim_id,),
            required_source_citations=(citation,),
        ),
    )


def _accepted_route_state(planned_write: PlannedPageWrite) -> IngestRoutePlanState:
    raw_source = RawSource.from_locator("book.pdf")
    page_plan = PagePlan(
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
    state = IngestRoutePlanState(
        IngestRouteContext(
            source_locator="book.pdf",
            scope="pdf-chunk",
            chunk_id=1,
            page_plan=page_plan,
            existing_pages=frozenset({planned_write.page_metadata.page_id}),
        )
    )
    state.accept(
        IngestRoutePlan(
            source_locator="book.pdf",
            scope="pdf-chunk",
            chunk_id=1,
            profile_ids=(),
            planned_pages=(
                PlannedPage(
                    metadata=planned_write.page_metadata,
                    role="source-summary",
                    action="enrich",
                    source_scope="book.pdf p.1-2",
                    confidence="high",
                    rationale="The deterministic PagePlan authorizes this page.",
                ),
            ),
        )
    )
    return state
