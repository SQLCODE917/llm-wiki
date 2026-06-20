"""PagePlan authorization is scoped by ingest phase."""

import pytest

from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlan,
    IngestRoutePlanError,
    PlannedPage,
    validate_ingest_route_plan,
)
from llmwiki.domain.objects import RawSource, SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE, PageMetadata
from llmwiki.domain.planning import build_page_plan
from llmwiki.domain.planning_analysis import build_extracted_unit


def _page_plan():
    raw_source = RawSource.from_locator("book.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1-10",
        heading_path="Functions",
        text="Functions are values.",
    )
    return build_page_plan(
        plan_id="plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )


def _route_plan(page_id: str, scope: str, chunk_id: int | None = None) -> IngestRoutePlan:
    return IngestRoutePlan(
        source_locator="book.pdf",
        scope=scope,  # type: ignore[arg-type]
        chunk_id=chunk_id,
        profile_ids=(),
        planned_pages=(
            PlannedPage(
                metadata=PageMetadata(page_id=page_id, page_kind="source", summary="Page."),
                role="source page",
                action="create",
                source_scope="book.pdf",
                confidence="high",
                rationale="A planned page.",
            ),
        ),
    )


def test_pdf_chunk_scope_rejects_hub_page_from_global_page_plan() -> None:
    context = IngestRouteContext(
        source_locator="book.pdf",
        scope="pdf-chunk",
        chunk_id=1,
        page_plan=_page_plan(),
    )

    with pytest.raises(IngestRoutePlanError, match="PagePlan does not authorize"):
        validate_ingest_route_plan(_route_plan("book", "pdf-chunk", chunk_id=1), context)


def test_pdf_integrate_scope_rejects_chunk_page_from_global_page_plan() -> None:
    context = IngestRouteContext(
        source_locator="book.pdf",
        scope="pdf-integrate",
        page_plan=_page_plan(),
    )

    with pytest.raises(IngestRoutePlanError, match="PagePlan does not authorize"):
        validate_ingest_route_plan(_route_plan("functions", "pdf-integrate"), context)
