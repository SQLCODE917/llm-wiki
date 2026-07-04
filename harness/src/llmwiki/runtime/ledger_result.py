"""Runtime result DTO for one source-ledger ingest."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.article_lint_artifacts import ArticleLintArtifact
from llmwiki.domain.ledger.artifacts import BlockedWriteDiagnosticArtifact, PortableArtifactSet
from llmwiki.domain.ledger.evidence_pack import EvidencePackSet
from llmwiki.domain.ledger.human_article import HumanArticleOutput
from llmwiki.domain.ledger.page_publication import (
    PagePublicationPlan,
    PublicationWalkabilityReport,
)
from llmwiki.domain.ledger.quality import LedgerQualityReport
from llmwiki.domain.ledger.staged_contracts import (
    LedgerExtractionResult,
    ProjectionLintRun,
    PublishRun,
    SourcePlan,
    StagedWikiPageSet,
)
from llmwiki.domain.pages import WikiPage


@dataclass(frozen=True)
class SourceLedgerResult:
    page_id: str
    wiki_page: WikiPage | None
    topic_pages: tuple[WikiPage, ...]
    page_write_decision: str
    ledger_report: LedgerQualityReport
    projection_report: LedgerQualityReport
    blocked_write_diagnostic: BlockedWriteDiagnosticArtifact | None
    artifact_files: dict[str, str]
    portable_artifact_set: PortableArtifactSet
    source_plan: SourcePlan
    extraction_result: LedgerExtractionResult
    staged_page_set: StagedWikiPageSet
    lint_run: ProjectionLintRun
    publish_run: PublishRun
    summary: str
    page_publication_plan: PagePublicationPlan | None = None
    publication_walkability_report: PublicationWalkabilityReport | None = None
    evidence_pack_set: EvidencePackSet | None = None
    human_article_output: HumanArticleOutput | None = None
    article_lint_artifact: ArticleLintArtifact | None = None
