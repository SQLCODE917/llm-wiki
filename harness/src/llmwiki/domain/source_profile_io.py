"""JSON persistence mapping for source-profile artifacts."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import cast

from llmwiki.domain.source_profiles import (
    EvidenceExtractionFinding,
    EvidenceExtractionPlan,
    EvidenceExtractionSeverity,
    EvidenceVocabulary,
    SourceProfile,
    SourceProfileArtifact,
    profile_kind,
    record_type_tuple,
)


def source_profile_artifact_to_json(artifact: SourceProfileArtifact) -> str:
    return json.dumps(asdict(artifact), indent=2, ensure_ascii=False)


def source_profile_artifact_from_json(text: str) -> SourceProfileArtifact:
    data = json.loads(text)
    return SourceProfileArtifact(
        source_profile=_source_profile_from_data(data["source_profile"]),
        evidence_vocabulary=_vocabulary_from_data(data["evidence_vocabulary"]),
        findings=tuple(_finding_from_data(item) for item in data.get("findings", ())),
    )


def evidence_extraction_plan_to_json(plan: EvidenceExtractionPlan) -> str:
    return json.dumps(asdict(plan), indent=2, ensure_ascii=False)


def evidence_extraction_plan_from_json(text: str) -> EvidenceExtractionPlan:
    data = json.loads(text)
    return EvidenceExtractionPlan(
        evidence_extraction_plan_id=str(data["evidence_extraction_plan_id"]),
        source_profile_id=str(data["source_profile_id"]),
        source_locator=str(data["source_locator"]),
        source_hash=str(data["source_hash"]),
        source_block_ids=tuple(str(item) for item in _sequence_from_data(data["source_block_ids"])),
        allowed_record_types=record_type_tuple(_sequence_from_data(data["allowed_record_types"])),
        extraction_instructions=str(data["extraction_instructions"]),
    )


def _source_profile_from_data(data: dict[str, object]) -> SourceProfile:
    return SourceProfile(
        source_profile_id=str(data["source_profile_id"]),
        source_id=str(data["source_id"]),
        source_locator=str(data["source_locator"]),
        source_hash=str(data["source_hash"]),
        profile_id=profile_kind(data["profile_id"]),
        evidence_vocabulary_id=str(data["evidence_vocabulary_id"]),
        selection_reason=str(data["selection_reason"]),
        confidence=_float_from_data(data["confidence"]),
        matched_signals=tuple(str(item) for item in _sequence_from_data(data["matched_signals"])),
    )


def _vocabulary_from_data(data: dict[str, object]) -> EvidenceVocabulary:
    return EvidenceVocabulary(
        evidence_vocabulary_id=str(data["evidence_vocabulary_id"]),
        profile_id=profile_kind(data["profile_id"]),
        allowed_record_types=record_type_tuple(_sequence_from_data(data["allowed_record_types"])),
    )


def _finding_from_data(data: dict[str, object]) -> EvidenceExtractionFinding:
    return EvidenceExtractionFinding(
        finding_id=str(data["finding_id"]),
        severity=cast(EvidenceExtractionSeverity, data["severity"]),
        finding_code=str(data["finding_code"]),
        record_type=str(data["record_type"]),
        message=str(data["message"]),
    )


def _sequence_from_data(data: object) -> tuple[object, ...]:
    if not isinstance(data, list | tuple):
        raise ValueError("expected a sequence")
    return tuple(data)


def _float_from_data(data: object) -> float:
    if isinstance(data, int | float | str):
        return float(data)
    raise ValueError("expected a numeric value")
