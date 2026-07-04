"""Typed source evidence records and validation."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, replace
from typing import Literal

from llmwiki.domain.prose_flow import structural_incompleteness_reason
from llmwiki.domain.source_map import SourceAnchor
from llmwiki.domain.source_profiles import EvidenceExtractionPlan

EvidenceRecordStatus = Literal["accepted", "fragmentary", "rejected", "needs_review"]
EvidenceRecordFindingSeverity = Literal["blocker", "warning", "info"]

EVIDENCE_RECORD_STATUSES: tuple[EvidenceRecordStatus, ...] = (
    "accepted",
    "fragmentary",
    "rejected",
    "needs_review",
)
_WEAK_CONFIDENCE = 0.5
_MODAL_ADVERB_TERMINAL = re.compile(
    r"\b(?:will|would|can|could|may|might|must|should|shall)\s+"
    r"(?:easily|also|only|then|again|therefore)[.!?]?$",
    re.IGNORECASE,
)
_DETERMINER_MODAL_JAM = re.compile(
    r"\b(?:a|an|the)\s+(?:will|can|may|must|should|shall)\s+\w+",
    re.IGNORECASE,
)
_CONJUNCTION_MODAL_JAM = re.compile(
    r"\b(?:destroys?|enters?|creates?|takes?)\s+(?:a|an|the)\s+"
    r"(?:will|can|may|must|should|shall)\b",
    re.IGNORECASE,
)
_CLIPPED_WILL_O_WISP = re.compile(
    r"\bcomes?\s+into\s+will\s*-\s*o\s*-\s*wisp",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class StructuredEvidencePayload:
    payload_kind: str
    payload_text: str
    normalized_fields: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "normalized_fields", tuple(self.normalized_fields))


@dataclass(frozen=True)
class EvidenceRecordFinding:
    finding_id: str
    typed_evidence_record_id: str
    severity: EvidenceRecordFindingSeverity
    finding_code: str
    source_anchor: SourceAnchor | None
    message: str


@dataclass(frozen=True)
class TypedEvidenceRecord:
    typed_evidence_record_id: str
    source_id: str
    source_locator: str
    source_hash: str
    evidence_record_type: str
    status: EvidenceRecordStatus
    canonical_text: str
    structured_payload: StructuredEvidencePayload | None
    source_anchors: tuple[SourceAnchor, ...]
    source_block_ids: tuple[str, ...]
    confidence: float
    findings: tuple[EvidenceRecordFinding, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in EVIDENCE_RECORD_STATUSES:
            raise ValueError(f"Unknown EvidenceRecordStatus: {self.status!r}.")
        if not 0 <= self.confidence <= 1:
            raise ValueError("TypedEvidenceRecord confidence must be between 0 and 1.")
        object.__setattr__(self, "source_anchors", tuple(self.source_anchors))
        object.__setattr__(self, "source_block_ids", tuple(self.source_block_ids))
        object.__setattr__(self, "findings", tuple(self.findings))

    @property
    def payload_text(self) -> str:
        return self.structured_payload.payload_text if self.structured_payload else ""

    @property
    def support_text(self) -> str:
        return self.payload_text or self.canonical_text


@dataclass(frozen=True)
class EvidenceRecordSet:
    evidence_record_set_id: str
    source_id: str
    source_locator: str
    source_hash: str
    source_profile_id: str
    evidence_extraction_plan_id: str
    records: tuple[TypedEvidenceRecord, ...]
    findings: tuple[EvidenceRecordFinding, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "records", tuple(self.records))
        object.__setattr__(self, "findings", tuple(self.findings))

    @property
    def accepted_records(self) -> tuple[TypedEvidenceRecord, ...]:
        return tuple(record for record in self.records if record.status == "accepted")

    @property
    def status_counts(self) -> dict[str, int]:
        counts: dict[str, int] = {status: 0 for status in EVIDENCE_RECORD_STATUSES}
        for record in self.records:
            counts[record.status] += 1
        return counts

    def render_status_counts(self) -> str:
        counts = self.status_counts
        return (
            f"Typed evidence records: {counts['accepted']} accepted, "
            f"{counts['fragmentary']} fragmentary, {counts['rejected']} rejected, "
            f"{counts['needs_review']} needs-review."
        )


def evidence_record_set(
    *,
    source_id: str,
    source_locator: str,
    source_hash: str,
    source_profile_id: str,
    evidence_extraction_plan_id: str,
    records: tuple[TypedEvidenceRecord, ...],
) -> EvidenceRecordSet:
    findings = tuple(finding for record in records for finding in record.findings)
    record_ids = ",".join(record.typed_evidence_record_id for record in records)
    return EvidenceRecordSet(
        evidence_record_set_id=stable_id("evidence-record-set", source_hash, record_ids),
        source_id=source_id,
        source_locator=source_locator,
        source_hash=source_hash,
        source_profile_id=source_profile_id,
        evidence_extraction_plan_id=evidence_extraction_plan_id,
        records=records,
        findings=findings,
    )


def validate_typed_evidence_record(
    record: TypedEvidenceRecord,
    plan: EvidenceExtractionPlan,
) -> TypedEvidenceRecord:
    findings = list(record.findings)
    status: EvidenceRecordStatus = "accepted"
    text = record.canonical_text.strip()
    if not record.source_anchors:
        findings.append(
            _finding(record, "blocker", "missing-source-anchor", "record has no source anchor")
        )
        status = "rejected"
    if record.evidence_record_type not in plan.allowed_record_types:
        findings.append(
            _finding(
                record,
                "blocker",
                "disallowed-evidence-record-type",
                "record type "
                f"{record.evidence_record_type!r} is not allowed by the extraction plan",
            )
        )
        status = "rejected"
    malformed = malformed_record_reason(text)
    if malformed:
        findings.append(_finding(record, "blocker", "malformed-record-text", malformed))
        status = "rejected"
    elif status != "rejected":
        fragment = fragmentary_record_reason(text)
        if fragment:
            findings.append(_finding(record, "warning", "fragmentary-record-text", fragment))
            status = "fragmentary"
    if status == "accepted" and record.confidence < _WEAK_CONFIDENCE:
        findings.append(
            _finding(
                record,
                "warning",
                "weak-evidence-confidence",
                "record is complete but has weak deterministic confidence",
            )
        )
        status = "needs_review"
    return replace(record, status=status, findings=tuple(findings))


def fragmentary_record_reason(text: str) -> str | None:
    reason = structural_incompleteness_reason(text)
    if reason:
        return reason
    if _MODAL_ADVERB_TERMINAL.search(_clean(text)):
        return "text ends with a modal/adverb phrase but no completed action"
    return None


def malformed_record_reason(text: str) -> str | None:
    cleaned = _clean(text)
    if _CONJUNCTION_MODAL_JAM.search(cleaned) or _DETERMINER_MODAL_JAM.search(cleaned):
        return "text appears to contain two sentence fragments jammed together"
    if _CLIPPED_WILL_O_WISP.search(cleaned):
        return "text appears to contain a clipped will-o-wisp phrase"
    return None


def stable_id(prefix: str, *parts: str) -> str:
    return f"{prefix}-{hashlib.sha256('|'.join(parts).encode('utf-8')).hexdigest()[:16]}"


def _finding(
    record: TypedEvidenceRecord,
    severity: EvidenceRecordFindingSeverity,
    code: str,
    message: str,
) -> EvidenceRecordFinding:
    return EvidenceRecordFinding(
        finding_id=stable_id("evidence-record-finding", record.typed_evidence_record_id, code),
        typed_evidence_record_id=record.typed_evidence_record_id,
        severity=severity,
        finding_code=code,
        source_anchor=record.source_anchors[0] if record.source_anchors else None,
        message=message,
    )


def _clean(text: str) -> str:
    return " ".join(text.split()).strip()
