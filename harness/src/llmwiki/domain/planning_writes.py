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
    Schema,
    SourceClaim,
    SourceClaimGroup,
    SourcePageGroup,
    SourcePlan,
    WikiMatch,
)
from llmwiki.domain.page_body_contracts import (
    ResolvedPageBodyContract,
    SourcePlanContractSelection,
    contract_by_id,
    contract_for_page_kind,
    resolve_page_body_contract,
    uncertainty_terms_in_text,
)
from llmwiki.domain.pages import PageMetadata, WikiStructure, slugify
from llmwiki.domain.planning_match_index import matches_by_unit_id, matches_for_units
from llmwiki.domain.source_summary_planning import source_summary_plan


def planned_writes(
    *,
    raw_source: RawSource,
    extracted_units: tuple[ExtractedUnit, ...],
    source_page_groups: tuple[SourcePageGroup, ...],
    existing_pages: dict[str, str],
    wiki_matches: tuple[WikiMatch, ...],
    claim_comparisons: tuple[ClaimComparison, ...],
    wiki_structure: WikiStructure,
    today: str,
    include_markdown_subject: bool,
    schema: Schema | None = None,
    source_plan: SourcePlan | None = None,
    source_claims: tuple[SourceClaim, ...] = (),
    source_claim_groups: tuple[SourceClaimGroup, ...] = (),
) -> tuple[PlannedPageWrite, ...]:
    active_schema = schema or Schema()
    selections = source_plan.page_body_contract_selections if source_plan is not None else ()
    writes: list[PlannedPageWrite] = []
    if not include_markdown_subject:
        units_by_id = {unit.unit_id: unit for unit in extracted_units}
        match_index = matches_by_unit_id(wiki_matches)
        writes.extend(
            _planned_write_for_group(
                raw_source,
                group,
                units_by_id,
                existing_pages,
                match_index,
                claim_comparisons,
                wiki_structure,
                today,
                active_schema,
                selections,
                source_claims,
                source_claim_groups,
            )
            for group in source_page_groups
        )
    hub = _hub_write(
        raw_source,
        extracted_units,
        existing_pages,
        wiki_matches,
        wiki_structure,
        today,
        active_schema,
        selections,
        source_claims,
        source_claim_groups,
        source_summary_enabled=include_markdown_subject,
    )
    writes.append(hub)
    return tuple(writes)


def _planned_write_for_group(
    raw_source: RawSource,
    group: SourcePageGroup,
    units_by_id: dict[str, ExtractedUnit],
    existing_pages: dict[str, str],
    match_index: dict[str, tuple[WikiMatch, ...]],
    comparisons: tuple[ClaimComparison, ...],
    structure: WikiStructure,
    today: str,
    schema: Schema,
    contract_selections: tuple[SourcePlanContractSelection, ...],
    source_claims: tuple[SourceClaim, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
) -> PlannedPageWrite:
    units = tuple(
        units_by_id[unit_id] for unit_id in group.extracted_units if unit_id in units_by_id
    )
    page_id = group.page_id
    metadata = PageMetadata(
        page_id=page_id,
        page_kind="source",
        summary=_source_page_group_summary(group, raw_source),
        sources=tuple(f"raw/{raw_source.source_locator} {unit.locator}".strip() for unit in units),
        updated=today,
        source_id=raw_source.source_locator,
    )
    unit_ids = frozenset(group.extracted_units)
    target_source_claims = tuple(
        claim for claim in source_claims if claim.extracted_unit_id in unit_ids
    )
    return _planned_write(
        write_id=f"write-{page_id}",
        action="enrich-existing" if page_id in existing_pages else "create-new",
        metadata=metadata,
        structure=structure,
        extracted_units=group.extracted_units,
        evidence=tuple(Evidence(raw_source, unit.locator) for unit in units),
        wiki_matches=matches_for_units(match_index, unit_ids),
        comparisons=tuple(item for item in comparisons if item.page_id == page_id),
        schema=schema,
        contract_selections=contract_selections,
        required_uncertainty_terms=_required_source_uncertainty_terms(target_source_claims),
        source_claims=target_source_claims,
        source_claim_groups=tuple(
            group_item
            for group_item in source_claim_groups
            if unit_ids.intersection(group_item.extracted_units)
        ),
    )


def _hub_write(
    raw_source: RawSource,
    units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    matches: tuple[WikiMatch, ...],
    structure: WikiStructure,
    today: str,
    schema: Schema,
    contract_selections: tuple[SourcePlanContractSelection, ...],
    source_claims: tuple[SourceClaim, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
    source_summary_enabled: bool,
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
        schema=schema,
        contract_selections=contract_selections,
        required_uncertainty_terms=_required_source_uncertainty_terms(source_claims),
        source_claims=source_claims,
        source_claim_groups=source_claim_groups,
        source_summary_enabled=source_summary_enabled,
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
    schema: Schema,
    contract_selections: tuple[SourcePlanContractSelection, ...],
    required_uncertainty_terms: tuple[str, ...],
    source_claims: tuple[SourceClaim, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
    source_summary_enabled: bool = True,
) -> PlannedPageWrite:
    resolved_contract = _resolved_page_body_contract(
        schema=schema,
        selections=contract_selections,
        page_id=metadata.page_id,
        page_kind=metadata.page_kind,
        required_link_page_ids=_required_link_page_ids(metadata.page_id, wiki_matches),
        required_source_citations=tuple(dict.fromkeys(metadata.sources)),
        required_uncertainty_terms=required_uncertainty_terms,
    )
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
        resolved_page_body_contract=resolved_contract,
        source_summary_plan=(
            source_summary_plan(
                page_id=metadata.page_id,
                contract=resolved_contract,
                claims=source_claims,
                groups=source_claim_groups,
            )
            if source_summary_enabled
            else None
        ),
    )


def _resolved_page_body_contract(
    *,
    schema: Schema,
    selections: tuple[SourcePlanContractSelection, ...],
    page_id: str,
    page_kind: str,
    required_link_page_ids: tuple[str, ...],
    required_source_citations: tuple[str, ...],
    required_uncertainty_terms: tuple[str, ...],
) -> ResolvedPageBodyContract:
    selection = _source_plan_contract_selection(selections, page_id, page_kind)
    contract = (
        contract_by_id(schema, selection.contract_id)
        if selection
        else contract_for_page_kind(schema, page_kind)
    )
    return resolve_page_body_contract(
        contract,
        required_link_page_ids=required_link_page_ids,
        required_source_citations=required_source_citations,
        required_uncertainty_terms=required_uncertainty_terms,
        selection=selection,
    )


def _source_plan_contract_selection(
    selections: tuple[SourcePlanContractSelection, ...],
    page_id: str,
    page_kind: str,
) -> SourcePlanContractSelection | None:
    for selection in selections:
        if page_id in selection.page_ids:
            return selection
    for selection in selections:
        if page_kind in selection.match_page_kinds:
            return selection
    return None


def _required_link_page_ids(page_id: str, wiki_matches: tuple[WikiMatch, ...]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(match.page_id for match in wiki_matches if match.page_id != page_id))


def _required_source_uncertainty_terms(
    source_claims: tuple[SourceClaim, ...],
) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            term
            for claim in source_claims
            if "source-uncertainty" in claim.claim_role_tags
            for term in uncertainty_terms_in_text(claim.statement)
        )
    )


def _source_page_group_summary(group: SourcePageGroup, raw_source: RawSource) -> str:
    if group.first_heading == group.last_heading:
        return f"{group.first_heading} from raw/{raw_source.source_locator}."
    return (
        f"{group.first_heading} through {group.last_heading} from raw/{raw_source.source_locator}."
    )


def _hub_page_id(raw_source: RawSource) -> str:
    return slugify(Path(raw_source.source_locator).stem)
