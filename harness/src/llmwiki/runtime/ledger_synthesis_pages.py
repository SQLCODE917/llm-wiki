"""Build synthesized high-value linked pages from ledger projection plans."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.collection_pages import CollectionPlan
from llmwiki.domain.ledger.coverage import RenderedPage
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_synthesis import (
    PageDraftCoverage,
    PageDraftRecord,
    PageSynthesisFinding,
    PageSynthesisOutput,
    PageSynthesisPlan,
)
from llmwiki.domain.ledger.page_synthesis_drafting import (
    DeterministicPageDraftProducer,
    PageDraftProducer,
)
from llmwiki.domain.ledger.page_synthesis_planning import (
    collection_synthesis_plan,
    procedure_synthesis_plan,
    recipe_synthesis_plan,
    topic_synthesis_plan,
)
from llmwiki.domain.ledger.page_synthesis_rendering import render_page_draft
from llmwiki.domain.ledger.page_synthesis_validation import validate_page_draft
from llmwiki.domain.ledger.procedures import (
    ProcedureGuide,
    plan_procedure_guides,
    procedure_aliases,
)
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.projection_policy import topic_projection_policy
from llmwiki.domain.ledger.recipe_pages import plan_recipe_patterns
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink, related_topic_links
from llmwiki.domain.ledger.walkability import audit_related_links
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify

_MAX_DRAFT_ATTEMPTS = 2


@dataclass(frozen=True)
class SynthesizedLinkedPages:
    pages: tuple[WikiPage, ...]
    collection_plans: tuple[CollectionPlan, ...]
    synthesis_output: PageSynthesisOutput


@dataclass(frozen=True)
class SynthesizedPageAttempt:
    page: WikiPage | None
    draft_record: PageDraftRecord | None
    findings: tuple[PageSynthesisFinding, ...]


def build_synthesized_linked_pages(
    *,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    shape_catalog: KnowledgeShapeCatalog,
    projection_context: ProjectionContext,
    topics: tuple[SourceTopic, ...],
    source_page_id: str,
    source_locator: str,
    today: str,
    related_pages_by_topic: dict[str, tuple[RelatedTopicLink, ...]] | None = None,
    draft_producer: PageDraftProducer | None = None,
) -> SynthesizedLinkedPages:
    producer = draft_producer or DeterministicPageDraftProducer()
    plans: list[PageSynthesisPlan] = []
    records: list[PageDraftRecord] = []
    findings: list[PageSynthesisFinding] = []
    pages: list[WikiPage] = []

    topic_related = related_topic_links(topics, source_page_id=source_page_id)
    extra_related = related_pages_by_topic or {}
    for topic in topics:
        page_id = slugify(f"{source_page_id}-{topic.topic_key}")
        related_pages = _topic_related_pages(
            topic, page_id, topic_related, extra_related, ledger, projection_context
        )
        policy = topic_projection_policy(topic, ledger, projection_context)
        plan = topic_synthesis_plan(
            topic,
            ledger,
            structure,
            page_id=page_id,
            page_family=policy.page_family,
            source_page_id=source_page_id,
            source_locator=source_locator,
            related_pages=related_pages,
        )
        _record_attempt(
            plan,
            synthesize_page(plan, _topic_metadata(plan, topic, source_locator, today), producer),
            plans,
            records,
            findings,
            pages,
        )

    for guide in plan_procedure_guides(
        ledger, structure, source_page_id=source_page_id, shape_catalog=shape_catalog
    ):
        plan = procedure_synthesis_plan(
            guide,
            source_page_id=source_page_id,
            source_locator=source_locator,
        )
        _record_attempt(
            plan,
            synthesize_page(
                plan,
                _procedure_metadata(plan, guide, source_locator, today),
                producer,
            ),
            plans,
            records,
            findings,
            pages,
        )

    collection_plans = collection_plans_for_source(ledger, structure, source_page_id, shape_catalog)
    for collection in collection_plans:
        plan = collection_synthesis_plan(
            collection, ledger, source_page_id=source_page_id, source_locator=source_locator
        )
        _record_attempt(
            plan,
            synthesize_page(
                plan,
                _collection_metadata(plan, collection, source_locator, today),
                producer,
            ),
            plans,
            records,
            findings,
            pages,
        )

    for pattern in plan_recipe_patterns(ledger, structure, source_page_id, shape_catalog):
        plan = recipe_synthesis_plan(
            pattern,
            source_page_id=source_page_id,
            source_locator=source_locator,
        )
        _record_attempt(
            plan,
            synthesize_page(
                plan,
                _recipe_metadata(plan, pattern.title, source_locator, today),
                producer,
            ),
            plans,
            records,
            findings,
            pages,
        )

    return SynthesizedLinkedPages(
        pages=tuple(pages),
        collection_plans=collection_plans,
        synthesis_output=PageSynthesisOutput(tuple(plans), tuple(records), tuple(findings)),
    )


def synthesize_page(
    plan: PageSynthesisPlan,
    metadata: PageMetadata,
    producer: PageDraftProducer,
    *,
    max_attempts: int = _MAX_DRAFT_ATTEMPTS,
) -> SynthesizedPageAttempt:
    current_findings: tuple[PageSynthesisFinding, ...] = ()
    for _ in range(max_attempts):
        draft = producer.draft_page(plan, current_findings)
        result = validate_page_draft(plan, draft)
        if result.accepted:
            rendered = render_page_draft(plan, draft)
            record = PageDraftRecord(
                draft,
                PageDraftCoverage(plan.page_id, rendered.page_body_hash, rendered.coverage),
            )
            page = WikiPage.from_metadata(
                _with_coverage(metadata, plan, rendered),
                rendered.page_body,
            )
            return SynthesizedPageAttempt(page, record, ())
        current_findings = result.findings
    return SynthesizedPageAttempt(None, None, current_findings)


def collection_plans_for_source(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    source_page_id: str,
    shape_catalog: KnowledgeShapeCatalog,
) -> tuple[CollectionPlan, ...]:
    from llmwiki.domain.ledger.collection_pages import collection_plans

    return collection_plans(ledger, structure, source_page_id, shape_catalog)


def _record_attempt(
    plan: PageSynthesisPlan,
    attempt: SynthesizedPageAttempt,
    plans: list[PageSynthesisPlan],
    records: list[PageDraftRecord],
    findings: list[PageSynthesisFinding],
    pages: list[WikiPage],
) -> None:
    plans.append(plan)
    if attempt.page is None or attempt.draft_record is None:
        findings.extend(attempt.findings)
        return
    records.append(attempt.draft_record)
    pages.append(attempt.page)


def _topic_related_pages(
    topic: SourceTopic,
    page_id: str,
    related: dict[str, tuple[RelatedTopicLink, ...]],
    extra: dict[str, tuple[RelatedTopicLink, ...]],
    ledger: ClaimLedger,
    projection_context: ProjectionContext,
) -> tuple[RelatedTopicLink, ...]:
    links = tuple(
        dict.fromkeys((*related.get(topic.topic_key, ()), *extra.get(topic.topic_key, ())))
    )
    return audit_related_links(
        page_id,
        links,
        ledger,
        projection_context=projection_context,
    ).accepted_links


def _with_coverage(
    metadata: PageMetadata, plan: PageSynthesisPlan, rendered: RenderedPage
) -> PageMetadata:
    return PageMetadata(
        page_id=metadata.page_id,
        page_kind=metadata.page_kind,
        summary=metadata.summary,
        page_family=metadata.page_family,
        sources=metadata.sources,
        updated=metadata.updated,
        domain=metadata.domain,
        category_path=metadata.category_path,
        project_id=metadata.project_id,
        source_id=metadata.source_id,
        tags=metadata.tags,
        aliases=metadata.aliases,
        projection_coverage_pointer=f"page-synthesis-{plan.page_id}@{rendered.page_body_hash}",
    )


def _topic_metadata(
    plan: PageSynthesisPlan, topic: SourceTopic, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind=plan.page_kind,
        page_family=plan.page_family,
        summary=f"{topic.label}: synthesized source-backed topic page from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"{topic.page_kind}s",
    )


def _procedure_metadata(
    plan: PageSynthesisPlan, guide: ProcedureGuide, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind="procedure",
        page_family=plan.page_family,
        summary=f"{plan.title}: synthesized procedure guide from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"procedures/{plan.source_page_id}",
        source_id=source_locator,
        aliases=procedure_aliases(guide),
    )


def _recipe_metadata(
    plan: PageSynthesisPlan, title: str, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind="recipe",
        page_family=plan.page_family,
        summary=f"{title}: synthesized recipe pattern from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"recipes/{plan.source_page_id}",
        source_id=source_locator,
        aliases=(slugify(title),),
    )


def _collection_metadata(
    plan: PageSynthesisPlan, collection: CollectionPlan, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind="source",
        page_family=plan.page_family,
        summary=f"{collection.title}: synthesized collection page from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"sources/{plan.source_page_id}/collections",
        source_id=source_locator,
    )
