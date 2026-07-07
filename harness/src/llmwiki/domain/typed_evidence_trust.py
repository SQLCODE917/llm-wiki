"""Trust decisions for typed structured evidence records."""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from typing import Literal

from llmwiki.domain.notation import is_formula_line
from llmwiki.domain.typed_evidence import EvidenceRecordFinding, TypedEvidenceRecord, stable_id

_SENTENCE_END = re.compile(r"[.!?;:]\s*$")
_CODE_MARKER = re.compile(r"[{}()[\];=]|=>|->|//|#|</?|\\|::|:=|\b(?:const|let|var|def|fn)\b")
_FENCE = re.compile(r"^\s*(```|~~~)")


@dataclass(frozen=True)
class TypedEvidenceTrustDecision:
    typed_evidence_record_id: str
    trust_status: str
    trust_reasons: tuple[str, ...]

    @property
    def authoritative(self) -> bool:
        return self.trust_status == "trusted"


def assess_typed_evidence_trust(record: TypedEvidenceRecord) -> TypedEvidenceTrustDecision:
    text = record.payload_text.strip() or record.canonical_text.strip()
    if not text:
        return TypedEvidenceTrustDecision(
            record.typed_evidence_record_id,
            "rejected",
            ("empty-payload",),
        )
    if record.evidence_record_type == "table_fact":
        reasons = _table_reasons(text)
    elif record.evidence_record_type == "code_example":
        reasons = _code_reasons(text)
    elif record.evidence_record_type == "formula":
        reasons = () if is_formula_line(text) else ("formula-shape-untrusted",)
    else:
        reasons = ()
    status = "trusted" if not reasons else "review-only"
    return TypedEvidenceTrustDecision(record.typed_evidence_record_id, status, reasons)


def apply_typed_evidence_trust(record: TypedEvidenceRecord) -> TypedEvidenceRecord:
    decision = assess_typed_evidence_trust(record)
    if decision.authoritative:
        return record
    severity: Literal["blocker", "warning", "info"] = (
        "blocker" if decision.trust_status == "rejected" else "warning"
    )
    status: Literal["accepted", "fragmentary", "rejected", "needs_review"] = (
        "rejected" if decision.trust_status == "rejected" else "needs_review"
    )
    finding = EvidenceRecordFinding(
        finding_id=stable_id(
            "evidence-record-finding",
            record.typed_evidence_record_id,
            "typed-evidence-trust",
        ),
        typed_evidence_record_id=record.typed_evidence_record_id,
        severity=severity,
        finding_code="typed-evidence-trust",
        source_anchor=record.source_anchors[0] if record.source_anchors else None,
        message=", ".join(decision.trust_reasons) or "typed evidence is not authoritative",
    )
    return replace(record, status=status, findings=(*record.findings, finding))


def _table_reasons(raw: str) -> tuple[str, ...]:
    reasons: list[str] = []
    lines = [line for line in raw.splitlines() if line.strip()]
    if not _raw_table_like(lines):
        reasons.append("table-unparsed")
    if _raw_table_has_prose_contamination(lines):
        reasons.append("table-raw-text-contaminated-by-prose")
    return tuple(reasons)


def _code_reasons(raw: str) -> tuple[str, ...]:
    reasons: list[str] = []
    if any(_FENCE.match(line) for line in raw.splitlines()):
        reasons.append("code-contains-nested-fence")
    if _prose_lines_inside_code(raw):
        reasons.append("code-block-contaminated-by-prose")
    if not any(_code_line(line) for line in raw.splitlines()):
        reasons.append("code-shape-untrusted")
    return tuple(reasons)


def _raw_table_like(lines: list[str]) -> bool:
    table_like = sum(
        1 for line in lines if "|" in line or len(re.split(r"\s{2,}", line.strip())) >= 2
    )
    enumerated = sum(1 for line in lines if re.match(r"^\s*\d{1,3}\b\s+\S+", line))
    return table_like >= 2 or enumerated >= 2


def _raw_table_has_prose_contamination(lines: list[str]) -> bool:
    prose_lines = [
        line
        for line in lines
        if "|" not in line
        and len(_words(line)) >= 7
        and (_SENTENCE_END.search(line.strip()) or line.strip()[:1].islower())
    ]
    return len(prose_lines) >= 2


def _prose_lines_inside_code(raw: str) -> bool:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    code_lines = sum(1 for line in lines if _code_line(line))
    prose_lines = sum(1 for line in lines if _prose_line_in_code(line))
    return code_lines > 0 and prose_lines > 0


def _code_line(line: str) -> bool:
    stripped = line.strip()
    return bool(_CODE_MARKER.search(stripped)) or stripped.startswith(("//", "#", "/*", "*"))


def _prose_line_in_code(line: str) -> bool:
    stripped = line.strip()
    if not stripped or _code_line(stripped):
        return False
    words = _words(stripped)
    return len(words) >= 5 or (len(words) >= 3 and _SENTENCE_END.search(stripped) is not None)


def _words(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"[A-Za-z0-9]+", text))
