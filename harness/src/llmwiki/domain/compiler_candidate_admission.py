"""Admission gates for compiler page candidates before publication budgeting."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.page_publication import (
    PAGE_FAMILY_COLLECTION_PAGE,
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_RECIPE_PATTERN,
    PAGE_FAMILY_TOPIC_CONCEPT,
    PageCandidate,
)
from llmwiki.domain.source_records import SourceRecordPlan
from llmwiki.domain.source_structure_integrity import SourceStructureIntegrityReport
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord


@dataclass(frozen=True)
class CandidateAdmissionFinding:
    severity: str
    finding_code: str
    candidate_id: str
    page_id: str
    message: str


@dataclass(frozen=True)
class CandidateAdmissionReport:
    source_id: str
    source_hash: str
    accepted_candidate_ids: tuple[str, ...]
    rejected_candidate_ids: tuple[str, ...]
    findings: tuple[CandidateAdmissionFinding, ...]


@dataclass(frozen=True)
class CandidateAdmissionResult:
    accepted_candidates: tuple[PageCandidate, ...]
    report: CandidateAdmissionReport


def admit_compiler_page_candidates(
    *,
    source_id: str,
    source_hash: str,
    candidates: tuple[PageCandidate, ...],
    record_set: EvidenceRecordSet,
    structure_report: SourceStructureIntegrityReport,
    record_plan: SourceRecordPlan,
) -> CandidateAdmissionResult:
    records_by_id = {
        record.typed_evidence_record_id: record for record in record_set.accepted_records
    }
    accepted: list[PageCandidate] = []
    findings: list[CandidateAdmissionFinding] = []
    for candidate in candidates:
        finding = _candidate_finding(candidate, records_by_id, structure_report, record_plan)
        if finding is not None:
            findings.append(finding)
            continue
        accepted.append(candidate)
    report = CandidateAdmissionReport(
        source_id,
        source_hash,
        tuple(candidate.page_candidate_id for candidate in accepted),
        tuple(finding.candidate_id for finding in findings),
        tuple(findings),
    )
    return CandidateAdmissionResult(tuple(accepted), report)


def _candidate_finding(
    candidate: PageCandidate,
    records_by_id: dict[str, TypedEvidenceRecord],
    structure_report: SourceStructureIntegrityReport,
    record_plan: SourceRecordPlan,
) -> CandidateAdmissionFinding | None:
    if not structure_report.section_can_drive_pages(candidate.title):
        return _finding(
            candidate,
            "source-structure-cannot-drive-page",
            "candidate title maps to a source section reserved for evidence only",
        )
    records = tuple(
        record
        for record_id in candidate.supporting_evidence_record_ids
        if (record := records_by_id.get(record_id)) is not None
    )
    if candidate.page_family == PAGE_FAMILY_PROCEDURE_GUIDE:
        return _procedure_finding(candidate, records)
    if candidate.page_family == PAGE_FAMILY_RECIPE_PATTERN:
        return _recipe_finding(candidate, records)
    if candidate.page_family == PAGE_FAMILY_TOPIC_CONCEPT:
        return _topic_finding(candidate, records)
    if candidate.page_family == PAGE_FAMILY_COLLECTION_PAGE:
        return _collection_finding(candidate, records, record_plan)
    return None


def _procedure_finding(
    candidate: PageCandidate, records: tuple[TypedEvidenceRecord, ...]
) -> CandidateAdmissionFinding | None:
    steps = tuple(record for record in records if record.evidence_record_type == "procedure_step")
    dependency_count = sum(
        1 for record in records if record.evidence_record_type in {"formula", "rule", "table_fact"}
    )
    if len(steps) < 2:
        return _finding(
            candidate,
            "procedure-shape-too-few-steps",
            "procedure has fewer than two steps",
        )
    if dependency_count == 0:
        return _finding(
            candidate,
            "procedure-evidence-closure-missing",
            "procedure has no rule, formula, or table evidence closure",
        )
    return None


def _recipe_finding(
    candidate: PageCandidate, records: tuple[TypedEvidenceRecord, ...]
) -> CandidateAdmissionFinding | None:
    has_code = any(record.evidence_record_type == "code_example" for record in records)
    has_context = any(
        record.evidence_record_type in {"argument", "definition", "procedure_step"}
        for record in records
    )
    if not has_code or not has_context:
        return _finding(
            candidate,
            "recipe-evidence-closure-missing",
            "recipe needs code evidence plus explanatory context",
        )
    return None


def _topic_finding(
    candidate: PageCandidate, records: tuple[TypedEvidenceRecord, ...]
) -> CandidateAdmissionFinding | None:
    substantive = tuple(
        record
        for record in records
        if record.evidence_record_type
        in {"argument", "definition", "entity_fact", "formula", "rule", "table_fact"}
    )
    if len(substantive) < 2:
        return _finding(
            candidate,
            "topic-evidence-closure-too-small",
            "topic needs at least two substantive evidence records",
        )
    return None


def _collection_finding(
    candidate: PageCandidate,
    records: tuple[TypedEvidenceRecord, ...],
    record_plan: SourceRecordPlan,
) -> CandidateAdmissionFinding | None:
    if len(records) >= 3:
        return None
    if record_plan.record_count >= 3:
        return None
    return _finding(
        candidate,
        "collection-record-closure-too-small",
        "collection needs at least three evidence records or recovered source records",
    )


def _finding(candidate: PageCandidate, code: str, message: str) -> CandidateAdmissionFinding:
    return CandidateAdmissionFinding(
        "blocking",
        code,
        candidate.page_candidate_id,
        candidate.page_id,
        message,
    )
