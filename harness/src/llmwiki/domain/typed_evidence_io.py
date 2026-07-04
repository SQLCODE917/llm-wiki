"""JSON persistence for typed evidence record artifacts."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import cast

from llmwiki.domain.source_map import SourceAnchor
from llmwiki.domain.typed_evidence import (
    EvidenceRecordFinding,
    EvidenceRecordFindingSeverity,
    EvidenceRecordSet,
    EvidenceRecordStatus,
    StructuredEvidencePayload,
    TypedEvidenceRecord,
)


def evidence_record_set_to_json(record_set: EvidenceRecordSet) -> str:
    return json.dumps(asdict(record_set), indent=2, ensure_ascii=False)


def evidence_record_set_from_json(text: str) -> EvidenceRecordSet:
    data = json.loads(text)
    return EvidenceRecordSet(
        evidence_record_set_id=str(data["evidence_record_set_id"]),
        source_id=str(data["source_id"]),
        source_locator=str(data["source_locator"]),
        source_hash=str(data["source_hash"]),
        source_profile_id=str(data["source_profile_id"]),
        evidence_extraction_plan_id=str(data["evidence_extraction_plan_id"]),
        records=tuple(_record_from_data(item) for item in data["records"]),
        findings=tuple(_finding_from_data(item) for item in data.get("findings", ())),
    )


def _record_from_data(data: dict[str, object]) -> TypedEvidenceRecord:
    payload_data = data.get("structured_payload")
    return TypedEvidenceRecord(
        typed_evidence_record_id=str(data["typed_evidence_record_id"]),
        source_id=str(data["source_id"]),
        source_locator=str(data["source_locator"]),
        source_hash=str(data["source_hash"]),
        evidence_record_type=str(data["evidence_record_type"]),
        status=cast(EvidenceRecordStatus, data["status"]),
        canonical_text=str(data["canonical_text"]),
        structured_payload=(
            _payload_from_data(payload_data) if isinstance(payload_data, dict) else None
        ),
        source_anchors=tuple(
            _anchor_from_data(item) for item in _sequence_from_data(data["source_anchors"])
        ),
        source_block_ids=tuple(str(item) for item in _sequence_from_data(data["source_block_ids"])),
        confidence=_float_from_data(data["confidence"]),
        findings=tuple(
            _finding_from_data(item) for item in _sequence_from_data(data.get("findings", ()))
        ),
    )


def _payload_from_data(data: dict[str, object]) -> StructuredEvidencePayload:
    return StructuredEvidencePayload(
        payload_kind=str(data["payload_kind"]),
        payload_text=str(data["payload_text"]),
        normalized_fields=tuple(
            _pair_from_data(item)
            for item in _sequence_from_data(data.get("normalized_fields", ()))
        ),
    )


def _finding_from_data(data: object) -> EvidenceRecordFinding:
    if not isinstance(data, dict):
        raise ValueError("evidence record finding must be an object")
    anchor_data = data.get("source_anchor")
    return EvidenceRecordFinding(
        finding_id=str(data["finding_id"]),
        typed_evidence_record_id=str(data["typed_evidence_record_id"]),
        severity=cast(EvidenceRecordFindingSeverity, data["severity"]),
        finding_code=str(data["finding_code"]),
        source_anchor=_anchor_from_data(anchor_data) if isinstance(anchor_data, dict) else None,
        message=str(data["message"]),
    )


def _anchor_from_data(data: object) -> SourceAnchor:
    if not isinstance(data, dict):
        raise ValueError("source anchor must be an object")
    return SourceAnchor(
        source_locator=str(data["source_locator"]),
        source_hash=str(data["source_hash"]),
        page_span=_int_pair_from_data(data["page_span"]),
        element_path=tuple(str(item) for item in _sequence_from_data(data["element_path"])),
        text_fingerprint=str(data["text_fingerprint"]),
        bounding_boxes=tuple(
            _float_quad_from_data(item) for item in data.get("bounding_boxes", ())
        ),
    )


def _pair_from_data(data: object) -> tuple[str, str]:
    if not isinstance(data, list | tuple) or len(data) != 2:
        raise ValueError("expected a two-item pair")
    return (str(data[0]), str(data[1]))


def _int_pair_from_data(data: object) -> tuple[int, int]:
    if not isinstance(data, list | tuple) or len(data) != 2:
        raise ValueError("expected a two-item integer pair")
    return (_int_from_data(data[0]), _int_from_data(data[1]))


def _float_quad_from_data(data: object) -> tuple[float, float, float, float]:
    if not isinstance(data, list | tuple) or len(data) != 4:
        raise ValueError("expected a four-item float tuple")
    return (
        _float_from_data(data[0]),
        _float_from_data(data[1]),
        _float_from_data(data[2]),
        _float_from_data(data[3]),
    )


def _sequence_from_data(data: object) -> tuple[object, ...]:
    if not isinstance(data, list | tuple):
        raise ValueError("expected a sequence")
    return tuple(data)


def _int_from_data(data: object) -> int:
    if isinstance(data, int | str):
        return int(data)
    raise ValueError("expected an integer value")


def _float_from_data(data: object) -> float:
    if isinstance(data, int | float | str):
        return float(data)
    raise ValueError("expected a numeric value")
