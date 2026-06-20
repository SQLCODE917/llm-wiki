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
from llmwiki.domain.planning_analysis import same_section_identity, unit_match
from llmwiki.domain.source_claims import source_summary_plan


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
    schema: Schema | None = None,
    source_plan: SourcePlan | None = None,
    source_claims: tuple[SourceClaim, ...] = (),
    source_claim_groups: tuple[SourceClaimGroup, ...] = (),
) -> tuple[PlannedPageWrite, ...]:
    active_schema = schema or Schema()
    selections = source_plan.page_body_contract_selections if source_plan is not None else ()
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
                active_schema,
                selections,
                source_claims,
                source_claim_groups,
            )
            for unit in extracted_units
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
    schema: Schema,
    contract_selections: tuple[SourcePlanContractSelection, ...],
    source_claims: tuple[SourceClaim, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
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
        schema=schema,
        contract_selections=contract_selections,
        required_uncertainty_terms=uncertainty_terms_in_text(unit.text),
        source_claims=tuple(
            claim for claim in source_claims if claim.extracted_unit_id == unit.unit_id
        ),
        source_claim_groups=tuple(
            group for group in source_claim_groups if unit.unit_id in group.extracted_units
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
        required_uncertainty_terms=uncertainty_terms_in_text(
            "\n\n".join(unit.text for unit in units)
        ),
        source_claims=source_claims,
        source_claim_groups=source_claim_groups,
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
        source_summary_plan=source_summary_plan(
            page_id=metadata.page_id,
            contract=resolved_contract,
            claims=source_claims,
            groups=source_claim_groups,
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
