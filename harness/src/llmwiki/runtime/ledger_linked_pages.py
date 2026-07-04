"""Build source-linked wiki pages from ledger projection artifacts."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.artifacts import (
    LedgerQualityReportArtifact,
    PageSynthesisFindingsArtifact,
    PageSynthesisPlanArtifact,
    ProjectionCoverageArtifact,
    build_page_synthesis_findings_artifact,
    build_page_synthesis_plan_artifact,
    build_projection_coverage_artifact,
)
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.coverage import ProjectionCoverage, RenderedPage
from llmwiki.domain.ledger.evidence_pack import EvidencePackSet, build_evidence_pack_set
from llmwiki.domain.ledger.human_article import ArticleWriter, HumanArticleOutput
from llmwiki.domain.ledger.human_article_artifacts import (
    HumanArticleArtifact,
    HumanArticleFindingsArtifact,
    build_human_article_artifact,
    build_human_article_findings_artifact,
)
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_publication import (
    PagePublicationPlan,
    PublicationWalkabilityReport,
    conservative_publication_budget,
)
from llmwiki.domain.ledger.page_publication_planning import (
    attach_typed_evidence_support,
    plan_publication,
    publication_walkability_report,
)
from llmwiki.domain.ledger.pointers import ledger_quality_report_pointer
from llmwiki.domain.ledger.projection import ProjectionSourceSupport
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.section_pages import build_section_pages
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.source_manifest_navigation import (
    build_source_navigation_plan,
    render_source_manifest,
    source_review_section,
)
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.pages import WikiPage
from llmwiki.domain.source_map import NormalizedSourceMap
from llmwiki.domain.typed_evidence import EvidenceRecordSet
from llmwiki.runtime.ledger_human_article_pages import build_human_article_linked_pages
from llmwiki.runtime.ledger_pages import (
    build_source_wiki_page,
    ledger_summary,
)
from llmwiki.runtime.ledger_publication_candidates import build_publication_candidate_inputs


@dataclass(frozen=True)
class LinkedPageProjection:
    source_page: WikiPage
    linked_pages: tuple[WikiPage, ...]
    coverage_artifact: ProjectionCoverageArtifact
    page_synthesis_plan_artifact: PageSynthesisPlanArtifact
    page_synthesis_findings_artifact: PageSynthesisFindingsArtifact
    human_article_artifact: HumanArticleArtifact
    human_article_findings_artifact: HumanArticleFindingsArtifact
    page_publication_plan: PagePublicationPlan
    publication_walkability_report: PublicationWalkabilityReport
    evidence_pack_set: EvidencePackSet
    human_article_output: HumanArticleOutput


def build_linked_page_projection(
    *,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    section_plan: SectionGroundedPlan,
    shape_catalog: KnowledgeShapeCatalog,
    projection_context: ProjectionContext,
    topics: tuple[SourceTopic, ...],
    page_id: str,
    title: str,
    source_locator: str,
    today: str,
    decision: str,
    rendered: RenderedPage,
    support: ProjectionSourceSupport,
    projection_report_artifact: LedgerQualityReportArtifact,
    article_writer: ArticleWriter | None = None,
    evidence_record_set: EvidenceRecordSet | None = None,
    source_profile_kind: str = "general-prose",
    source_map: NormalizedSourceMap | None = None,
) -> LinkedPageProjection:
    publication_inputs = build_publication_candidate_inputs(
        ledger=ledger,
        structure=structure,
        section_plan=section_plan,
        shape_catalog=shape_catalog,
        projection_context=projection_context,
        topics=topics,
        source_page_id=page_id,
        source_profile_kind=source_profile_kind,
    )
    supported_candidates = attach_typed_evidence_support(
        publication_inputs.candidates, evidence_record_set
    )
    budget = conservative_publication_budget(source_profile_kind)
    publication_plan = plan_publication(
        source_id=page_id,
        source_hash=ledger.source_hash,
        source_profile_kind=budget.source_profile_kind,
        budget=budget,
        candidates=supported_candidates,
    )
    publication_report = publication_walkability_report(publication_plan)
    evidence_pack_set = build_evidence_pack_set(
        publication_plan=publication_plan,
        evidence_record_set=evidence_record_set,
        source_map=source_map,
    )
    accepted_page_ids = frozenset(evidence_pack_set.valid_page_ids)
    section_pages = build_section_pages(
        ledger,
        structure,
        source_page_id=page_id,
        source_locator=source_locator,
        today=today,
        topics=topics,
        projection_context=projection_context,
        accepted_page_ids=accepted_page_ids,
    )
    human_articles = build_human_article_linked_pages(
        evidence_pack_set=evidence_pack_set,
        source_locator=source_locator,
        today=today,
        article_writer=article_writer,
        collection_plans=publication_inputs.collection_plans,
    )
    linked_pages = (*human_articles.pages, *section_pages)
    page_synthesis_plan_artifact = build_page_synthesis_plan_artifact(
        source_hash=ledger.source_hash, plans=()
    )
    page_synthesis_findings_artifact = build_page_synthesis_findings_artifact(
        source_hash=ledger.source_hash, findings=()
    )
    human_article_artifact = build_human_article_artifact(
        source_hash=ledger.source_hash, records=human_articles.article_output.records
    )
    human_article_findings_artifact = build_human_article_findings_artifact(
        source_hash=ledger.source_hash, findings=human_articles.article_output.findings
    )
    navigation = build_source_navigation_plan(
        source_page_id=page_id,
        title=title,
        source_locator=source_locator,
        ledger_summary=ledger_summary(ledger, decision, len(linked_pages)),
        linked_pages=linked_pages,
        structure=structure,
        collection_plans=human_articles.collection_plans,
        publication_report=publication_report,
    )
    source_body = render_source_manifest(navigation)
    review = source_review_section(rendered.page_body)
    if review:
        source_body = f"{source_body.rstrip()}\n\n{review}\n"
    coverage_artifact = build_projection_coverage_artifact(
        wiki_page_locator=page_id,
        page_body_hash=short_digest(source_body, 32),
        support_set=(support,),
        coverage=ProjectionCoverage(()),
        ledger_quality_report_pointer=ledger_quality_report_pointer(
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    source_page = build_source_wiki_page(
        page_id,
        source_locator,
        title,
        ledger_summary(ledger, decision, len(linked_pages)),
        today,
        source_body,
        coverage_artifact,
    )
    return LinkedPageProjection(
        source_page,
        linked_pages,
        coverage_artifact,
        page_synthesis_plan_artifact,
        page_synthesis_findings_artifact,
        human_article_artifact,
        human_article_findings_artifact,
        publication_plan,
        publication_report,
        evidence_pack_set,
        human_articles.article_output,
    )
