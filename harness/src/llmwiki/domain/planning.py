"""Global ingest planning from source units to planned wiki writes."""

from __future__ import annotations

import json
import re
from dataclasses import asdict
from pathlib import Path

from llmwiki.domain.objects import (
    ExtractedUnit,
    PagePlan,
    RawSource,
    Schema,
    SourceBundle,
    SourcePlan,
)
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
) -> PagePlan:
    claims = candidate_claims(extracted_units)
    topics = candidate_topics(extracted_units, claims)
    entities = candidate_entities(extracted_units, claims)
    clusters = topic_clusters(extracted_units, claims, topics)
    matches = wiki_matches(extracted_units, existing_pages, raw_source.source_locator)
    comparisons = claim_comparisons(claims, matches)
    writes = planned_writes(
        raw_source=raw_source,
        extracted_units=extracted_units,
        existing_pages=existing_pages,
        wiki_matches=matches,
        claim_comparisons=comparisons,
        wiki_structure=wiki_structure,
        today=today,
        include_markdown_subject=include_markdown_subject,
        schema=schema,
        source_plan=source_plan,
    )
    return PagePlan(
        plan_id=plan_id,
        source_bundle=source_bundle,
        extracted_units=extracted_units,
        candidate_claims=claims,
        candidate_topics=topics,
        candidate_entities=entities,
        topic_clusters=clusters,
        wiki_matches=matches,
        claim_comparisons=comparisons,
        planned_writes=writes,
    )


def page_plan_to_json(plan: PagePlan) -> str:
    return json.dumps(asdict(plan), indent=2, ensure_ascii=False, sort_keys=True)


def observation_report(plan: PagePlan) -> str:
    enriched = sum(1 for write in plan.planned_writes if write.action == "enrich-existing")
    created = sum(1 for write in plan.planned_writes if write.action == "create-new")
    deferred = sum(1 for write in plan.planned_writes if write.action == "defer")
    contradictions = sum(
        1 for comparison in plan.claim_comparisons if comparison.relation == "contradiction"
    )
    paths = "\n".join(
        f"- `{write.page_metadata.page_id}` | plan_pages action "
        f"`{_route_action(write.action)}` | PagePlan action `{write.action}` | "
        f"PageKind `{write.page_metadata.page_kind}` | "
        f"ResolvedPageBodyContract `{write.resolved_page_body_contract.contract_id}` | "
        f"sources `{', '.join(write.page_metadata.sources)}` | "
        f"path `{write.projection.page_path if write.projection else ''}`"
        for write in plan.planned_writes
    )
    return (
        "# Ingest Observation Report\n\n"
        f"- ExtractedUnits: {len(plan.extracted_units)}\n"
        f"- TopicClusters: {len(plan.topic_clusters)}\n"
        f"- Pages enriched: {enriched}\n"
        f"- Pages created: {created}\n"
        f"- Contradictions: {contradictions}\n"
        f"- Deferrals: {deferred}\n\n"
        "## Planned Page Targets\n\n"
        f"{paths}\n"
    )


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
