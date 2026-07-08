"""JSON persistence for typed evidence record artifacts."""

from __future__ import annotations

import json
from dataclasses import asdict

from llmwiki.domain.source_map import SourceAnchor
from llmwiki.domain.strict_json import (
    expect_array,
    expect_float,
    expect_int,
    expect_literal,
    expect_object,
    expect_str,
    optional_object,
)
from llmwiki.domain.typed_evidence import (
    EVIDENCE_RECORD_STATUSES,
    EvidenceRecordFinding,
    EvidenceRecordFindingSeverity,
    EvidenceRecordSet,
    StructuredEvidencePayload,
    TypedEvidenceRecord,
)

_EVIDENCE_RECORD_FINDING_SEVERITIES: tuple[EvidenceRecordFindingSeverity, ...] = (
    "blocker",
    "warning",
    "info",
)


def evidence_record_set_to_json(record_set: EvidenceRecordSet) -> str:
    return json.dumps(asdict(record_set), indent=2, ensure_ascii=False)


def evidence_record_set_from_json(text: str) -> EvidenceRecordSet:
    data = expect_object(json.loads(text), "evidence record set")
    return EvidenceRecordSet(
        evidence_record_set_id=expect_str(
            data["evidence_record_set_id"], "evidence_record_set_id"
        ),
        source_id=expect_str(data["source_id"], "source_id"),
        source_locator=expect_str(data["source_locator"], "source_locator"),
        source_hash=expect_str(data["source_hash"], "source_hash"),
        source_profile_id=expect_str(data["source_profile_id"], "source_profile_id"),
        evidence_extraction_plan_id=expect_str(
            data["evidence_extraction_plan_id"], "evidence_extraction_plan_id"
        ),
        records=tuple(
            _record_from_data(item) for item in expect_array(data["records"], "records")
        ),
        findings=tuple(
            _finding_from_data(item)
            for item in expect_array(data.get("findings", []), "findings")
        ),
    )


def _record_from_data(raw: object) -> TypedEvidenceRecord:
    data = expect_object(raw, "typed evidence record")
    payload_data = optional_object(data.get("structured_payload"), "structured_payload")
    return TypedEvidenceRecord(
        typed_evidence_record_id=expect_str(
            data["typed_evidence_record_id"], "typed_evidence_record_id"
        ),
        source_id=expect_str(data["source_id"], "source_id"),
        source_locator=expect_str(data["source_locator"], "source_locator"),
        source_hash=expect_str(data["source_hash"], "source_hash"),
        evidence_record_type=expect_str(data["evidence_record_type"], "evidence_record_type"),
        status=expect_literal(data["status"], EVIDENCE_RECORD_STATUSES, "status"),
        canonical_text=expect_str(data["canonical_text"], "canonical_text"),
        structured_payload=_payload_from_data(payload_data) if payload_data is not None else None,
        source_anchors=tuple(
            _anchor_from_data(item)
            for item in expect_array(data["source_anchors"], "source_anchors")
        ),
        source_block_ids=tuple(
            expect_str(item, "source_block_id")
            for item in expect_array(data["source_block_ids"], "source_block_ids")
        ),
        confidence=expect_float(data["confidence"], "confidence"),
        findings=tuple(
            _finding_from_data(item)
            for item in expect_array(data.get("findings", []), "findings")
        ),
    )


def _payload_from_data(data: dict[str, object]) -> StructuredEvidencePayload:
    return StructuredEvidencePayload(
        payload_kind=expect_str(data["payload_kind"], "payload_kind"),
        payload_text=expect_str(data["payload_text"], "payload_text"),
        normalized_fields=tuple(
            _pair_from_data(item)
            for item in expect_array(data.get("normalized_fields", []), "normalized_fields")
        ),
    )


def _finding_from_data(data: object) -> EvidenceRecordFinding:
    data = expect_object(data, "evidence record finding")
    anchor_data = optional_object(data.get("source_anchor"), "source_anchor")
    return EvidenceRecordFinding(
        finding_id=expect_str(data["finding_id"], "finding_id"),
        typed_evidence_record_id=expect_str(
            data["typed_evidence_record_id"], "typed_evidence_record_id"
        ),
        severity=expect_literal(
            data["severity"], _EVIDENCE_RECORD_FINDING_SEVERITIES, "severity"
        ),
        finding_code=expect_str(data["finding_code"], "finding_code"),
        source_anchor=_anchor_from_data(anchor_data) if anchor_data is not None else None,
        message=expect_str(data["message"], "message"),
    )


def _anchor_from_data(data: object) -> SourceAnchor:
    data = expect_object(data, "source anchor")
    return SourceAnchor(
        source_locator=expect_str(data["source_locator"], "source_locator"),
        source_hash=expect_str(data["source_hash"], "source_hash"),
        page_span=_int_pair_from_data(data["page_span"]),
        element_path=tuple(
            expect_str(item, "element_path item")
            for item in expect_array(data["element_path"], "element_path")
        ),
        text_fingerprint=expect_str(data["text_fingerprint"], "text_fingerprint"),
        bounding_boxes=tuple(
            _float_quad_from_data(item)
            for item in expect_array(data.get("bounding_boxes", []), "bounding_boxes")
        ),
    )


def _pair_from_data(data: object) -> tuple[str, str]:
    if not isinstance(data, list) or len(data) != 2:
        raise ValueError("expected a two-item pair")
    return (expect_str(data[0], "pair[0]"), expect_str(data[1], "pair[1]"))


def _int_pair_from_data(data: object) -> tuple[int, int]:
    if not isinstance(data, list) or len(data) != 2:
        raise ValueError("expected a two-item integer pair")
    return (expect_int(data[0], "int_pair[0]"), expect_int(data[1], "int_pair[1]"))


def _float_quad_from_data(data: object) -> tuple[float, float, float, float]:
    if not isinstance(data, list) or len(data) != 4:
        raise ValueError("expected a four-item float tuple")
    return (
        expect_float(data[0], "float_quad[0]"),
        expect_float(data[1], "float_quad[1]"),
        expect_float(data[2], "float_quad[2]"),
        expect_float(data[3], "float_quad[3]"),
    )
