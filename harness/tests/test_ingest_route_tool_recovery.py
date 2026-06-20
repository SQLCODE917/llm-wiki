"""Tool-boundary recovery for ingest route plan misses."""

from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlan,
    IngestRoutePlanState,
    PlannedPage,
)
from llmwiki.domain.objects import PagePlan, PlannedPageWrite, RawSource, SourceBundle
from llmwiki.domain.pages import PageMetadata
from llmwiki.domain.source_summary import SourceSummaryPlan
from llmwiki.store import WikiStore
from llmwiki.workflows.ingest_route_tools import plan_pages_tool
from llmwiki.workflows.tools import write_page_tool


def test_plan_pages_route_plan_miss_is_model_correctable() -> None:
    state = IngestRoutePlanState(
        IngestRouteContext(
            source_locator="book.pdf",
            scope="pdf-chunk",
            new_page_prefix="book",
        )
    )
    tool = plan_pages_tool(state, recoverable_errors=True)

    result = tool.callable(
        planned_pages=[
            {
                "metadata": {
                    "page_id": "arrays-vs-linked-lists",
                    "page_kind": "concept",
                    "summary": "Arrays versus linked lists.",
                },
                "role": "side concept",
                "action": "create",
                "source_scope": "book.pdf p.126-140",
                "confidence": "medium",
                "rationale": "The chunk mentions this contrast.",
            }
        ],
        gaps=[],
    )

    assert "No ingest route plan was accepted" in result
    assert state.active_plan is None


def test_plan_pages_schema_error_is_model_correctable() -> None:
    state = IngestRoutePlanState(IngestRouteContext(source_locator="book.pdf", scope="pdf-chunk"))
    tool = plan_pages_tool(state, recoverable_errors=True)

    result = tool.callable(
        planned_pages=[
            {
                "metadata": {
                    "page_id": "book-front-matter",
                    "page_kind": "source",
                    "summary": "Book front matter.",
                },
                "role": "source section",
                "action": "create",
                "source_scope": "book.pdf p.1-7",
                "confidence": "high",
            }
        ],
        gaps=[],
    )

    assert "arguments did not match" in result
    assert "rationale" in result
    assert state.active_plan is None


def test_plan_pages_shorthand_is_rescued_from_page_plan() -> None:
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
        planned_writes=(
            PlannedPageWrite(
                write_id="write-book-front-matter",
                action="create-new",
                page_metadata=PageMetadata(
                    page_id="book-front-matter",
                    page_kind="source",
                    summary="Book front matter.",
                    sources=("raw/book.pdf p.1-7",),
                ),
                extracted_units=("unit-0001",),
            ),
        ),
    )
    state = IngestRoutePlanState(
        IngestRouteContext(
            source_locator="book.pdf",
            scope="pdf-chunk",
            chunk_id=1,
            page_plan=page_plan,
        )
    )
    tool = plan_pages_tool(state, recoverable_errors=True)

    result = tool.callable(
        planned_pages=[
            {
                "page_id": "book-front-matter",
                "page_kind": "source",
                "action": "create",
                "confidence": 1,
            }
        ],
        gaps=[],
    )

    assert "Validated ingest route plan" in result
    assert state.active_plan is not None
    planned = state.active_plan.planned_pages[0]
    assert planned.metadata.summary == "Book front matter."
    assert planned.metadata.sources == ("raw/book.pdf p.1-7",)
    assert planned.confidence == "high"


def test_write_page_route_plan_miss_is_model_correctable(store: WikiStore) -> None:
    state = IngestRoutePlanState(IngestRouteContext(source_locator="book.pdf", scope="pdf-chunk"))
    state.accept(
        IngestRoutePlan(
            source_locator="book.pdf",
            scope="pdf-chunk",
            profile_ids=(),
            planned_pages=(
                PlannedPage(
                    metadata=PageMetadata(
                        page_id="naming-functions",
                        page_kind="source",
                        summary="Naming functions.",
                    ),
                    role="source section",
                    action="create",
                    source_scope="book.pdf p.62-78",
                    confidence="high",
                    rationale="The chunk is about naming functions.",
                ),
            ),
        )
    )
    tool = write_page_tool(
        store,
        today="2026-06-19",
        ingest_route_plan_state=state,
        recoverable_errors=True,
    )

    result = tool.callable(
        page_id="named-function-expressions",
        page_kind="concept",
        summary="Named function expressions.",
        page_body="Body.",
    )

    assert "No page was written" in result
    assert store.list_pages() == []


def test_planned_write_uses_page_plan_metadata_after_route_authorization(
    store: WikiStore,
) -> None:
    raw_source = RawSource.from_locator("book.pdf")
    planned_write = PlannedPageWrite(
        write_id="write-book-front-matter",
        action="create-new",
        page_metadata=PageMetadata(
            page_id="book-front-matter",
            page_kind="source",
            summary="Book front matter from deterministic PagePlan.",
            sources=("raw/book.pdf p.1-7",),
        ),
        extracted_units=("unit-0001",),
    )
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
                    metadata=PageMetadata(
                        page_id="book-front-matter",
                        page_kind="source",
                        summary="Model summary …",
                        sources=("raw/book.pdf",),
                    ),
                    role="source-summary",
                    action="create",
                    source_scope="book.pdf p.1-7",
                    confidence="high",
                    rationale="The deterministic PagePlan authorizes this page.",
                ),
            ),
        )
    )
    tool = write_page_tool(
        store,
        today="2026-06-20",
        ingest_route_plan_state=state,
    )

    result = tool.callable(
        page_id="book-front-matter",
        page_kind="source",
        summary="Write-time model summary …",
        sources=["raw/book.pdf"],
        page_body="## Source record\n\nClean body.\n\n## Key supported claims\n\n- Claim.",
    )

    page = store.read_page("book-front-matter")
    assert "Wrote wiki/book-front-matter.md" in result
    assert "summary: Book front matter from deterministic PagePlan." in page
    assert "sources: raw/book.pdf p.1-7" in page
    assert "Model summary …" not in page
    assert "Write-time model summary …" not in page


def test_write_page_rescues_claim_id_bullets_for_source_summary(
    store: WikiStore,
) -> None:
    raw_source = RawSource.from_locator("book.pdf")
    selected_claims = (
        "source-claim-unit-0001-0001",
        "source-claim-unit-0001-0002",
        "source-claim-unit-0001-0003",
    )
    planned_write = PlannedPageWrite(
        write_id="write-book-copyright",
        action="create-new",
        page_metadata=PageMetadata(
            page_id="book-copyright",
            page_kind="source",
            summary="Book copyright notice.",
            sources=("raw/book.pdf p.1-2",),
        ),
        extracted_units=("unit-0001",),
        source_summary_plan=SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-book-copyright",
            page_id="book-copyright",
            selected_source_claims=selected_claims,
            required_source_citations=("raw/book.pdf p.1-2",),
        ),
    )
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
                    action="create",
                    source_scope="book.pdf p.1-2",
                    confidence="high",
                    rationale="The deterministic PagePlan authorizes this page.",
                ),
            ),
        )
    )
    tool = write_page_tool(
        store,
        today="2026-06-20",
        ingest_route_plan_state=state,
        recoverable_errors=True,
    )

    result = tool.callable(
        page_id="book-copyright",
        page_kind="source",
        summary="Book copyright notice.",
        sources=["raw/book.pdf p.1-2"],
        source_record_text="Copyright and author note for the book.",
        claim_bullets=[
            {
                "claim_id": selected_claims[0],
                "text": "The book has a copyright notice. (raw/book.pdf p.1-2)",
            },
            {
                "claim_id": selected_claims[1],
                "text": "Image rights are listed separately. (raw/book.pdf p.1-2)",
            },
            {
                "claim_id": selected_claims[2],
                "text": "Author contact details are included. (raw/book.pdf p.1-2)",
            },
        ],
    )

    page = store.read_page("book-copyright")
    assert "Wrote wiki/book-copyright.md" in result
    assert "Image rights are listed separately." in page
    assert "source-claim-unit" not in page
