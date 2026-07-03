"""Contracts for staged ingest flow artifacts."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.pages import WikiPage

ARTIFACT_FORMAT = "llm-wiki-portable-artifact-v1"


@dataclass(frozen=True)
class SourcePlan:
    source_plan_id: str
    source_plan_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    source_page_id: str
    allowed_page_kinds: tuple[str, ...]
    allowed_page_families: tuple[str, ...]
    allowed_extractor_capability_ids: tuple[str, ...]
    allowed_technical_atom_kinds: tuple[str, ...]
    path_authority: str = "deterministic-page-metadata"


@dataclass(frozen=True)
class LedgerExtractionResult:
    extraction_result_id: str
    extraction_result_fingerprint: str
    artifact_format: str
    source_plan_id: str
    source_locator: str
    source_hash: str
    document_structure_artifact_id: str
    claim_ledger_id: str
    source_statement_ids: tuple[str, ...]
    accepted_entry_ids: tuple[str, ...]
    needs_review_entry_ids: tuple[str, ...]
    rejected_entry_ids: tuple[str, ...]
    technical_atom_ids: tuple[str, ...]
    extractor_decision_count: int
    rejected_candidate_count: int


@dataclass(frozen=True)
class StagedWikiPage:
    staged_page_id: str
    staged_page_fingerprint: str
    artifact_format: str
    source_plan_id: str
    page_id: str
    page_kind: str
    page_family: str
    source_locator: str
    page_body_hash: str
    projection_coverage_pointer: str
    page: WikiPage


@dataclass(frozen=True)
class StagedWikiPageSet:
    staged_page_set_id: str
    staged_page_set_fingerprint: str
    artifact_format: str
    source_plan_id: str
    pages: tuple[StagedWikiPage, ...]


@dataclass(frozen=True)
class ProjectionLintFinding:
    severity: str
    finding_type: str
    page_id: str
    message: str


@dataclass(frozen=True)
class ProjectionLintRun:
    lint_run_id: str
    lint_run_fingerprint: str
    artifact_format: str
    source_plan_id: str
    upstream_write_decision: str
    status: str
    accepted_page_ids: tuple[str, ...]
    rejected_page_ids: tuple[str, ...]
    findings: tuple[ProjectionLintFinding, ...]


@dataclass(frozen=True)
class PublishRun:
    publish_run_id: str
    publish_run_fingerprint: str
    artifact_format: str
    source_plan_id: str
    status: str
    accepted_page_ids: tuple[str, ...]
    rejected_page_ids: tuple[str, ...]
    blocked_reason: str = ""
