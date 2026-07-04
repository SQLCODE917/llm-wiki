"""Contracts for the single source ingest compiler."""

from __future__ import annotations

from dataclasses import dataclass, replace

from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT
from llmwiki.domain.pages import WikiPage


@dataclass(frozen=True)
class IngestCompilerInput:
    source_locator: str
    reextract: bool = False


@dataclass(frozen=True)
class CompilerFinding:
    finding_id: str
    stage_name: str
    severity: str
    finding_code: str
    page_id: str
    source_anchor: str
    message: str


@dataclass(frozen=True)
class CompilerStage:
    stage_name: str
    input_artifact_ids: tuple[str, ...]
    output_artifact_ids: tuple[str, ...]
    status: str
    elapsed_ms: int
    finding_count: int


@dataclass(frozen=True)
class IngestArtifactMember:
    artifact_kind: str
    artifact_id: str
    artifact_path: str
    fingerprint: str


@dataclass(frozen=True)
class IngestArtifactSet:
    ingest_artifact_set_id: str
    ingest_artifact_set_fingerprint: str
    artifact_format: str
    source_id: str
    source_locator: str
    source_hash: str
    run_id: str
    stages: tuple[CompilerStage, ...]
    artifacts: tuple[IngestArtifactMember, ...]
    findings: tuple[CompilerFinding, ...]
    accepted_page_ids: tuple[str, ...]
    rejected_page_ids: tuple[str, ...]


@dataclass(frozen=True)
class IngestCompilation:
    source_locator: str
    source_page_id: str
    source_hash: str
    accepted_pages: tuple[WikiPage, ...]
    artifact_files: dict[str, str]
    artifact_set: IngestArtifactSet
    report: str


def build_ingest_artifact_set(
    *,
    source_id: str,
    source_locator: str,
    source_hash: str,
    run_id: str,
    stages: tuple[CompilerStage, ...],
    artifacts: tuple[IngestArtifactMember, ...],
    findings: tuple[CompilerFinding, ...],
    accepted_page_ids: tuple[str, ...],
    rejected_page_ids: tuple[str, ...],
) -> IngestArtifactSet:
    draft = IngestArtifactSet(
        ingest_artifact_set_id=deterministic_id("ingest-artifact-set", source_hash, run_id),
        ingest_artifact_set_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_id=source_id,
        source_locator=source_locator,
        source_hash=source_hash,
        run_id=run_id,
        stages=stages,
        artifacts=artifacts,
        findings=findings,
        accepted_page_ids=accepted_page_ids,
        rejected_page_ids=rejected_page_ids,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("ingest_artifact_set_fingerprint",)
    )
    return replace(draft, ingest_artifact_set_fingerprint=fingerprint)
