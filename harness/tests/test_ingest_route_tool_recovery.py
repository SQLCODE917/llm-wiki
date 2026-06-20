"""Tool-boundary recovery for ingest route plan misses."""

from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlan,
    IngestRoutePlanState,
    PlannedPage,
)
from llmwiki.domain.pages import PageMetadata
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
