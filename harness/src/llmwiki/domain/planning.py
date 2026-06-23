"""Global ingest planning from source units to planned wiki writes."""

from __future__ import annotations

import re
from dataclasses import replace
from pathlib import Path

from pydantic import PydanticUserError, TypeAdapter

from llmwiki.domain.objects import (
    Evidence,
    ExtractedUnit,
    PagePlan,
    PlannedPageWrite,
    RawSource,
    Schema,
    SourceBundle,
    SourceClaim,
    SourcePlan,
)
from llmwiki.domain.page_plan_io import page_plan_to_json_text
from llmwiki.domain.pages import WikiStructure
from llmwiki.domain.planning_analysis import (
    build_extracted_unit,
    candidate_claims,
    candidate_entities,
    candidate_topics,
    claim_comparisons,
    topic_clusters,
    wiki_matches,
)
from llmwiki.domain.planning_writes import planned_writes
from llmwiki.domain.source_claims import (
    source_claim_groups,
    source_claims,
)
from llmwiki.domain.source_page_groups import source_page_groups
from llmwiki.domain.source_summary import render_source_summary_claim_requirement
from llmwiki.domain.source_summary_quality import (
    source_summary_quality_report as source_summary_quality_report,
)

_PAGE_PLAN_ADAPTER = TypeAdapter(PagePlan)
_HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)


def build_markdown_page_plan(
    *,
    plan_id: str,
    source_bundle: SourceBundle,
    raw_source: RawSource,
    source_text: str,
    existing_pages: dict[str, str],
    wiki_structure: WikiStructure,
    today: str,
    schema: Schema | None = None,
    source_plan: SourcePlan | None = None,
    new_page_prefix: str | None = None,
) -> PagePlan:
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="document",
        heading_path=_document_title(source_text, raw_source.source_locator),
        text=source_text,
    )
    return build_page_plan(
        plan_id=plan_id,
        source_bundle=source_bundle,
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages=existing_pages,
        wiki_structure=wiki_structure,
        today=today,
        schema=schema,
        source_plan=source_plan,
        include_markdown_subject=True,
        new_page_prefix=new_page_prefix,
    )


def build_page_plan(
    *,
    plan_id: str,
    source_bundle: SourceBundle,
    raw_source: RawSource,
    extracted_units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    wiki_structure: WikiStructure,
    today: str,
    include_markdown_subject: bool = False,
    schema: Schema | None = None,
    source_plan: SourcePlan | None = None,
    new_page_prefix: str | None = None,
) -> PagePlan:
    active_schema = schema or Schema()
    source_claim_items = source_claims(extracted_units, active_schema)
    source_claim_group_items = source_claim_groups(source_claim_items)
    claims = candidate_claims(extracted_units)
    topics = candidate_topics(extracted_units, claims)
    entities = candidate_entities(extracted_units, claims)
    clusters = topic_clusters(extracted_units, claims, topics, source_claim_group_items)
    matches = wiki_matches(extracted_units, existing_pages, raw_source.source_locator)
    comparisons = claim_comparisons(claims, matches)
    source_page_group_items = (
        ()
        if include_markdown_subject
        else source_page_groups(
            raw_source=raw_source,
            extracted_units=extracted_units,
            existing_pages=existing_pages,
            wiki_matches=matches,
            source_claims=source_claim_items,
            new_page_prefix=new_page_prefix,
        )
    )
    writes = _unique_write_ids(
        planned_writes(
            raw_source=raw_source,
            extracted_units=extracted_units,
            source_page_groups=source_page_group_items,
            existing_pages=existing_pages,
            wiki_matches=matches,
            claim_comparisons=comparisons,
            wiki_structure=wiki_structure,
            today=today,
            include_markdown_subject=include_markdown_subject,
            schema=active_schema,
            source_plan=source_plan,
            source_claims=source_claim_items,
            source_claim_groups=source_claim_group_items,
        )
    )
    return PagePlan(
        plan_id=plan_id,
        source_bundle=source_bundle,
        extracted_units=extracted_units,
        source_claims=source_claim_items,
        source_claim_groups=source_claim_group_items,
        candidate_claims=claims,
        candidate_topics=topics,
        candidate_entities=entities,
        topic_clusters=clusters,
        wiki_matches=matches,
        claim_comparisons=comparisons,
        planned_writes=writes,
        source_page_groups=source_page_group_items,
    )


def page_plan_to_json(plan: PagePlan) -> str:
    return page_plan_to_json_text(plan)


def page_plan_from_json(text: str) -> PagePlan:
    try:
        return _PAGE_PLAN_ADAPTER.validate_json(text)
    except PydanticUserError as exc:
        if exc.code != "class-not-fully-defined":
            raise
        _PAGE_PLAN_ADAPTER.rebuild(force=True, _types_namespace={"Evidence": Evidence})
        return _PAGE_PLAN_ADAPTER.validate_json(text)


def observation_report(
    plan: PagePlan,
    target_page_ids: tuple[str, ...] | None = None,
    target_write_ids: tuple[str, ...] | None = None,
) -> str:
    visible_writes = _visible_writes(plan, target_page_ids, target_write_ids)
    enriched = sum(1 for write in visible_writes if write.action == "enrich-existing")
    created = sum(1 for write in visible_writes if write.action == "create-new")
    deferred = sum(1 for write in visible_writes if write.action == "defer")
    contradictions = sum(
        1 for comparison in plan.claim_comparisons if comparison.relation == "contradiction"
    )
    source_claims = {claim.source_claim_id: claim for claim in plan.source_claims}
    paths = "\n".join(
        f"- `{write.page_metadata.page_id}` | plan_pages action "
        f"`{_route_action(write.action)}` | PagePlan action `{write.action}` | "
        f"PageKind `{write.page_metadata.page_kind}` | "
        f"ResolvedPageBodyContract `{write.resolved_page_body_contract.contract_id}` | "
        f"{_source_summary_plan_label(write, source_claims)}"
        f"sources `{', '.join(write.page_metadata.sources)}` | "
        f"path `{write.projection.page_path if write.projection else ''}`"
        for write in visible_writes
    )
    if not paths:
        paths = "- None."
    return (
        "# Ingest Observation Report\n\n"
        f"- ExtractedUnits: {len(plan.extracted_units)}\n"
        f"- SourceClaims: {len(plan.source_claims)}\n"
        f"- SourceClaimGroups: {len(plan.source_claim_groups)}\n"
        f"- SourcePageGroups: {len(plan.source_page_groups)}\n"
        f"- TopicClusters: {len(plan.topic_clusters)}\n"
        f"- Planned page targets shown: {len(visible_writes)} of {len(plan.planned_writes)}\n"
        f"- Pages enriched: {enriched}\n"
        f"- Pages created: {created}\n"
        f"- Contradictions: {contradictions}\n"
        f"- Deferrals: {deferred}\n\n"
        "## Planned Page Targets\n\n"
        f"{paths}\n"
    )


def _visible_writes(
    plan: PagePlan,
    target_page_ids: tuple[str, ...] | None,
    target_write_ids: tuple[str, ...] | None,
) -> tuple[PlannedPageWrite, ...]:
    if target_write_ids is not None:
        target_set = frozenset(target_write_ids)
        return tuple(write for write in plan.planned_writes if write.write_id in target_set)
    if target_page_ids is None:
        return plan.planned_writes
    target_set = frozenset(target_page_ids)
    return tuple(
        write for write in plan.planned_writes if write.page_metadata.page_id in target_set
    )


def _unique_write_ids(writes: tuple[PlannedPageWrite, ...]) -> tuple[PlannedPageWrite, ...]:
    counts: dict[str, int] = {}
    for write in writes:
        counts[write.write_id] = counts.get(write.write_id, 0) + 1
    seen: dict[str, int] = {}
    unique: list[PlannedPageWrite] = []
    for write in writes:
        if counts[write.write_id] == 1:
            unique.append(write)
            continue
        seen[write.write_id] = seen.get(write.write_id, 0) + 1
        suffix = "-".join(write.extracted_units) or str(seen[write.write_id])
        unique.append(replace(write, write_id=f"{write.write_id}-{suffix}"))
    return tuple(unique)


def _document_title(source_text: str, source_locator: str) -> str:
    match = _HEADING_RE.search(source_text)
    if match:
        return match.group(1).strip()
    return Path(source_locator).stem.replace("-", " ").replace("_", " ").strip()


def _route_action(page_plan_action: str) -> str:
    if page_plan_action == "enrich-existing":
        return "enrich"
    if page_plan_action == "create-new":
        return "create"
    return "route-gap"


def _source_summary_plan_label(write: object, source_claims: dict[str, SourceClaim]) -> str:
    summary_plan = getattr(write, "source_summary_plan", None)
    if summary_plan is None:
        return ""
    contract = getattr(write, "resolved_page_body_contract", None)
    citations = ", ".join(getattr(contract, "required_source_citations", ()))
    uncertainty_terms = ", ".join(getattr(contract, "required_uncertainty_terms", ()))
    constraints = []
    if citations:
        constraints.append(f"put citation `{citations}` in every bullet_text")
    if uncertainty_terms:
        constraints.append(f"include one uncertainty term `{uncertainty_terms}`")
    max_words = getattr(contract, "max_words", 0) if contract is not None else 0
    if max_words:
        constraints.append(f"stay under {max_words} words")
    constraint_text = "; ".join(constraints) or "use source-summary fields"
    claims = _source_summary_claim_labels(summary_plan, source_claims)
    return (
        "SourceSummaryPlan selected claim IDs "
        "(use claim_id only in covered_source_claims; read the raw source, then "
        "write fresh short paraphrases; cue terms are labels, not reusable prose): "
        f"{claims} | constraints: {constraint_text} | "
    )


def _source_summary_claim_labels(
    summary_plan: object,
    source_claims: dict[str, SourceClaim],
) -> str:
    requirements = getattr(summary_plan, "selected_claim_requirements", ())
    if requirements:
        return "; ".join(
            render_source_summary_claim_requirement(requirement)
            for requirement in requirements
        )
    selected_claims = tuple(
        str(claim_id) for claim_id in getattr(summary_plan, "selected_source_claims", ())
    )
    return "; ".join(
        _source_claim_label(source_claims[claim_id])
        for claim_id in selected_claims
        if claim_id in source_claims
    )


def _source_claim_label(claim: SourceClaim) -> str:
    roles = ", ".join(claim.claim_role_tags) or "unlabeled"
    terms = ", ".join(claim.subject_terms) or "no subject terms"
    return (
        f"claim_id `{claim.source_claim_id}` [{roles}] "
        f"eligibility `{claim.claim_eligibility}` centrality `{claim.claim_centrality}` "
        f"cue_terms `{terms}`"
    )
