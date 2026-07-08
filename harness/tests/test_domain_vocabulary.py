"""Checks for the canonical domain vocabulary and its boundary mapping rules."""

from pathlib import Path

import pytest

from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlanError,
    IngestRoutePlanState,
)
from llmwiki.domain.pages import PageError, PageMetadata
from llmwiki.workflows.ingest_route_tools import plan_pages_tool

ROOT = Path(__file__).resolve().parents[2]
VOCABULARY_PATH = ROOT / "docs" / "domain-vocabulary.md"
WRITING_TDDS_PATH = ROOT / "docs" / "writing-tdds.md"
AGENTS_PATH = ROOT / "AGENTS.md"
SCHEMA_PATH = ROOT / "SCHEMA.md"


def test_domain_vocabulary_contains_required_headings_and_classifications() -> None:
    text = VOCABULARY_PATH.read_text(encoding="utf-8")

    for heading in (
        "## Canonical Terms",
        "## Domain Object Inventory",
        "## Boundary Shape Inventory",
        "## Adoption Rules",
    ):
        assert heading in text

    for term in (
        "first-level domain object",
        "second-level domain object",
        "boundary DTO",
        "deterministic boundary",
        "model output boundary",
        "boundary recovery",
        "check plan",
        "contract source of truth",
        "forbidden pattern",
        "agent workflow",
        "persistence model",
        "view model",
    ):
        assert f"| {term} |" in text


def test_domain_vocabulary_classifies_tdd_domain_terms() -> None:
    text = VOCABULARY_PATH.read_text(encoding="utf-8")
    first_level = text.split("### First-Level Domain Objects", 1)[1].split(
        "### Second-Level Domain Objects", 1
    )[0]
    second_level = text.split("### Second-Level Domain Objects", 1)[1].split(
        "## Boundary Shape Inventory", 1
    )[0]

    for term in (
        "RawSource",
        "SourceBundle",
        "WikiPage",
        "WikiStructure",
        "IngestRun",
        "WikiGraph",
        "CandidateBacklog",
        "ChatSession",
        "PdfIngestManifest",
        "SchemaDocument",
        "QueryRun",
        "LintRun",
        "MaintenanceRun",
    ):
        assert f"| {term} |" in first_level

    for term in (
        "PageMetadata",
        "IngestRoutePlan",
        "PlannedPage",
        "RouteGap",
        "GroundingVerdict",
        "ContradictionFinding",
        "CandidateRecord",
        "Citation",
        "EvidenceLocator",
        "SourceExcerpt",
        "LintFinding",
        "SalienceSignal",
        "PageLink",
        "PageWrite",
    ):
        assert f"| {term} |" in second_level


def test_writing_tdds_references_domain_vocabulary() -> None:
    text = WRITING_TDDS_PATH.read_text(encoding="utf-8")

    assert "docs/domain-vocabulary.md" in text
    assert "DeterministicBoundary" in text
    assert "ModelOutputBoundary" in text
    assert "BoundaryRecovery" in text


def test_agent_guidance_contains_deterministic_boundary_rule() -> None:
    text = AGENTS_PATH.read_text(encoding="utf-8")

    assert "### Boundary validation" in text
    assert "Deterministic project-owned boundaries must fail fast" in text
    assert "Invalid model output must not become accepted state directly" in text


def test_schema_describes_strict_compiler_artifacts() -> None:
    text = SCHEMA_PATH.read_text(encoding="utf-8")

    assert "schema-owned generated state" in text
    assert "strict compiler contracts" in text


def test_page_metadata_rejects_invalid_page_id() -> None:
    with pytest.raises(PageError, match="Invalid page_id"):
        PageMetadata(page_id="Bad Name", page_kind="source", summary="Bad page.")


def test_plan_pages_boundary_dto_maps_transport_sources_into_page_metadata() -> None:
    state = IngestRoutePlanState(IngestRouteContext(source_locator="moon.md", scope="source"))
    tool = plan_pages_tool(state)

    result = tool.callable(
        planned_pages=[
            {
                "metadata": {
                    "page_id": "moon",
                    "page_kind": "source",
                    "summary": "Lunar notes.",
                    "sources": "(raw/moon.md)",
                },
                "role": "primary source page",
                "action": "create",
                "source_scope": "moon.md",
                "confidence": "high",
                "rationale": "The source is about the Moon.",
            }
        ],
        gaps=[],
    )

    assert "Validated ingest route plan" in result
    assert state.active_plan is not None
    planned = state.active_plan.planned_pages[0]
    assert isinstance(planned.metadata, PageMetadata)
    assert planned.metadata.page_id == "moon"
    assert planned.metadata.page_kind == "source"
    assert planned.metadata.sources == ("moon.md",)


def test_plan_pages_boundary_dto_reaches_domain_rule_after_mapping() -> None:
    state = IngestRoutePlanState(
        IngestRouteContext(
            source_locator="moon.md",
            scope="source",
            existing_pages=frozenset({"moon"}),
        )
    )
    tool = plan_pages_tool(state)

    with pytest.raises(IngestRoutePlanError, match="exists"):
        tool.callable(
            planned_pages=[
                {
                    "metadata": {
                        "page_id": "moon",
                        "page_kind": "source",
                        "summary": "Lunar notes.",
                        "sources": "(raw/moon.md)",
                    },
                    "role": "primary source page",
                    "action": "create",
                    "source_scope": "moon.md",
                    "confidence": "high",
                    "rationale": "The source is about the Moon.",
                }
            ],
            gaps=[],
        )

    assert state.active_plan is None
