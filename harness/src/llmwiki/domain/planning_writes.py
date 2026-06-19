"""Planned write projection for global ingest planning."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.objects import (
    ClaimComparison,
    Evidence,
    ExtractedUnit,
    PlannedPageWrite,
    ProjectionMetadata,
    RawSource,
    WikiMatch,
)
from llmwiki.domain.pages import PageMetadata, WikiStructure, slugify
from llmwiki.domain.planning_analysis import same_section_identity, unit_match


def planned_writes(
    *,
    raw_source: RawSource,
    extracted_units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    wiki_matches: tuple[WikiMatch, ...],
    claim_comparisons: tuple[ClaimComparison, ...],
    wiki_structure: WikiStructure,
    today: str,
    include_markdown_subject: bool,
) -> tuple[PlannedPageWrite, ...]:
    writes: list[PlannedPageWrite] = []
    if not include_markdown_subject:
        writes.extend(
            _planned_write_for_unit(
                raw_source,
                unit,
                existing_pages,
                wiki_matches,
                claim_comparisons,
                wiki_structure,
                today,
            )
            for unit in extracted_units
        )
    hub = _hub_write(
        raw_source, extracted_units, existing_pages, wiki_matches, wiki_structure, today
    )
    writes.append(hub)
    return tuple(writes)


def _planned_write_for_unit(
    raw_source: RawSource,
    unit: ExtractedUnit,
    existing_pages: dict[str, str],
    wiki_matches: tuple[WikiMatch, ...],
    comparisons: tuple[ClaimComparison, ...],
    structure: WikiStructure,
    today: str,
) -> PlannedPageWrite:
    page_id = _target_page_id(unit, existing_pages)
    metadata = PageMetadata(
        page_id=page_id,
        page_kind="source",
        summary=f"{unit.heading_path} from raw/{raw_source.source_locator}.",
        sources=(f"raw/{raw_source.source_locator} {unit.locator}".strip(),),
        updated=today,
        source_id=raw_source.source_locator,
    )
    return _planned_write(
        write_id=f"write-{page_id}",
        action="enrich-existing" if page_id in existing_pages else "create-new",
        metadata=metadata,
        structure=structure,
        extracted_units=(unit.unit_id,),
        evidence=(Evidence(raw_source, unit.locator),),
        wiki_matches=tuple(match for match in wiki_matches if unit_match(match, unit.unit_id)),
        comparisons=tuple(item for item in comparisons if item.page_id == page_id),
    )


def _hub_write(
    raw_source: RawSource,
    units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    matches: tuple[WikiMatch, ...],
    structure: WikiStructure,
    today: str,
) -> PlannedPageWrite:
    page_id = _hub_page_id(raw_source)
    metadata = PageMetadata(
        page_id=page_id,
        page_kind="source",
        summary=f"Hub page for raw/{raw_source.source_locator}.",
        sources=(f"raw/{raw_source.source_locator}",),
        updated=today,
        source_id=raw_source.source_locator,
    )
    return _planned_write(
        write_id=f"write-{page_id}",
        action="enrich-existing" if page_id in existing_pages else "create-new",
        metadata=metadata,
        structure=structure,
        extracted_units=tuple(unit.unit_id for unit in units),
        evidence=(Evidence(raw_source),),
        wiki_matches=matches[:8],
        comparisons=(),
    )


def _planned_write(
    *,
    write_id: str,
    action: str,
    metadata: PageMetadata,
    structure: WikiStructure,
    extracted_units: tuple[str, ...],
    evidence: tuple[Evidence, ...],
    wiki_matches: tuple[WikiMatch, ...],
    comparisons: tuple[ClaimComparison, ...],
) -> PlannedPageWrite:
    return PlannedPageWrite(
        write_id=write_id,
        action=action,
        page_metadata=metadata,
        extracted_units=extracted_units,
        evidence=evidence,
        wiki_matches=wiki_matches,
        claim_comparisons=comparisons,
        projection=ProjectionMetadata(metadata, str(structure.render_path(metadata))),
        existing_page_id=metadata.page_id if action == "enrich-existing" else "",
    )


def _target_page_id(unit: ExtractedUnit, existing_pages: dict[str, str]) -> str:
    default_page_id = slugify(unit.heading_path)
    if default_page_id in existing_pages:
        return default_page_id
    for page_id in existing_pages:
        if same_section_identity(unit.heading_path, page_id):
            return page_id
    return default_page_id


def _hub_page_id(raw_source: RawSource) -> str:
    return slugify(Path(raw_source.source_locator).stem)
