"""Deterministic confidence gates for one raw source."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.claim_support import ClaimSupportSelection
from llmwiki.domain.claim_support_selection import select_claim_support_candidates
from llmwiki.domain.ingest_confidence import (
    IngestConfidenceGate,
    ValidationFinding,
    gate_status,
    validation_finding,
)
from llmwiki.domain.source_summary import SourceSummaryDraft, SourceSummaryDraftArtifact
from llmwiki.runtime.ingest_confidence_artifacts import PreparedIngestArtifacts
from llmwiki.runtime.ingest_confidence_gate_checks import (
    citation_findings,
    confidence_gate,
    evidence_policy_findings,
    evidence_registry_detail,
    evidence_registry_findings,
    graph_findings,
    index_findings,
    source_summary_detail,
    source_summary_findings,
)
from llmwiki.runtime.ingest_confidence_locator_gate import (
    locator_stability_detail,
    locator_stability_findings,
)
from llmwiki.runtime.ingest_confidence_page_scope import page_body, source_scoped_pages
from llmwiki.store import WikiStore


@dataclass(frozen=True)
class DeterministicConfidence:
    gates: tuple[IngestConfidenceGate, ...]
    findings: tuple[ValidationFinding, ...]
    claim_support_selection: ClaimSupportSelection | None

    @property
    def has_blockers(self) -> bool:
        return any(finding.severity == "blocker" for finding in self.findings)


def deterministic_confidence(
    *,
    store: WikiStore,
    source_locator: str,
    today: str,
    prepared: PreparedIngestArtifacts,
    max_claims: int,
) -> DeterministicConfidence:
    page_texts = store.page_texts()
    scoped_pages = source_scoped_pages(page_texts, source_locator)
    findings: list[ValidationFinding] = list(prepared.findings)
    gates = (
        _source_summary_gate(source_locator, prepared, scoped_pages, findings),
        _finding_gate(
            "citation-syntax",
            source_locator,
            findings,
            citation_findings(source_locator, store, scoped_pages),
        ),
        _finding_gate(
            "evidence-registry",
            source_locator,
            findings,
            evidence_registry_findings(source_locator, prepared.evidence_registry),
            evidence_registry_detail(prepared.evidence_registry),
        ),
        _finding_gate(
            "locator-stability",
            source_locator,
            findings,
            locator_stability_findings(
                source_locator,
                prepared.previous_evidence_locator_index,
                prepared.evidence_locator_index,
            ),
            locator_stability_detail(
                prepared.previous_evidence_locator_index,
                prepared.evidence_locator_index,
            ),
        ),
        _finding_gate(
            "source-range",
            source_locator,
            findings,
            evidence_policy_findings(
                source_locator,
                store,
                scoped_pages,
                prepared.evidence_registry,
                prepared.evidence_locator_index,
                include_source_range=True,
            ),
        ),
        _finding_gate(
            "evidence",
            source_locator,
            findings,
            evidence_policy_findings(
                source_locator,
                store,
                scoped_pages,
                prepared.evidence_registry,
                prepared.evidence_locator_index,
                include_source_range=False,
            ),
        ),
        _finding_gate(
            "graph",
            source_locator,
            findings,
            graph_findings(source_locator, store, page_texts, scoped_pages, today),
        ),
        _finding_gate(
            "index",
            source_locator,
            findings,
            index_findings(source_locator, store, page_texts, scoped_pages),
        ),
    )
    selection = _claim_support_selection(store, source_locator, prepared, page_texts, max_claims)
    return DeterministicConfidence(gates, tuple(findings), selection)


def _source_summary_gate(
    source_locator: str,
    prepared: PreparedIngestArtifacts,
    scoped_pages: dict[str, str],
    all_findings: list[ValidationFinding],
) -> IngestConfidenceGate:
    if prepared.page_plan is None:
        finding = validation_finding(
            severity="blocker",
            category="planning",
            source_locator=source_locator,
            message="Source summary quality gate skipped because PagePlan is unavailable.",
        )
        all_findings.append(finding)
        return confidence_gate(
            "source-summary-quality", "deterministic", source_locator, "skipped", (finding,)
        )
    gate_findings = source_summary_findings(source_locator, prepared.page_plan, scoped_pages)
    all_findings.extend(gate_findings)
    return confidence_gate(
        "source-summary-quality",
        "deterministic",
        source_locator,
        gate_status(gate_findings),
        gate_findings,
        source_summary_detail(prepared.page_plan, scoped_pages),
    )


def _finding_gate(
    gate_id: str,
    source_locator: str,
    all_findings: list[ValidationFinding],
    gate_findings: tuple[ValidationFinding, ...],
    detail: str = "",
) -> IngestConfidenceGate:
    all_findings.extend(gate_findings)
    return confidence_gate(
        gate_id,
        "deterministic",
        source_locator,
        gate_status(gate_findings),
        gate_findings,
        detail,
    )


def _claim_support_selection(
    store: WikiStore,
    source_locator: str,
    prepared: PreparedIngestArtifacts,
    page_texts: dict[str, str],
    max_claims: int,
) -> ClaimSupportSelection | None:
    if prepared.evidence_registry is None:
        return None
    return select_claim_support_candidates(
        page_texts,
        store.source_inventory(),
        (prepared.evidence_registry,),
        _current_source_summary_artifacts(store, source_locator, prepared, page_texts),
        max_claims=max_claims,
        source=f"raw/{source_locator}",
    )


def _current_source_summary_artifacts(
    store: WikiStore,
    source_locator: str,
    prepared: PreparedIngestArtifacts,
    page_texts: dict[str, str],
) -> tuple[SourceSummaryDraftArtifact, ...]:
    if prepared.page_plan is None:
        return ()
    current_write_ids = frozenset(write.write_id for write in prepared.page_plan.planned_writes)
    artifacts = store.read_source_summary_draft_artifacts(source_locator)
    return tuple(
        current_artifact
        for artifact in artifacts
        if artifact.write_id in current_write_ids
        if (current_artifact := _artifact_for_current_page(artifact, page_texts)) is not None
    )


def _artifact_for_current_page(
    artifact: SourceSummaryDraftArtifact, page_texts: dict[str, str]
) -> SourceSummaryDraftArtifact | None:
    text = page_texts.get(artifact.page_id_hint)
    if text is None:
        return None
    bullets = artifact.draft.claim_bullets
    if not bullets:
        return artifact
    body = page_body(text)
    current_bullets = tuple(bullet for bullet in bullets if bullet.bullet_text in body)
    if not current_bullets:
        return None
    return SourceSummaryDraftArtifact(
        source_locator=artifact.source_locator,
        write_id=artifact.write_id,
        page_id_hint=artifact.page_id_hint,
        draft=SourceSummaryDraft(
            source_record_text=artifact.draft.source_record_text,
            claim_bullets=current_bullets,
        ),
    )
