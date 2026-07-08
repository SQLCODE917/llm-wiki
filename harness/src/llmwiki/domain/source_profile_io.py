"""JSON persistence mapping for source-profile artifacts."""

from __future__ import annotations

import json
from dataclasses import asdict

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
from llmwiki.domain.strict_json import (
    expect_array,
    expect_float,
    expect_literal,
    expect_object,
    expect_str,
)

_EVIDENCE_EXTRACTION_SEVERITIES: tuple[EvidenceExtractionSeverity, ...] = (
    "blocker",
    "warning",
    "info",
)


def source_profile_artifact_to_json(artifact: SourceProfileArtifact) -> str:
    return json.dumps(asdict(artifact), indent=2, ensure_ascii=False)


def source_profile_artifact_from_json(text: str) -> SourceProfileArtifact:
    data = expect_object(json.loads(text), "source profile artifact")
    return SourceProfileArtifact(
        source_profile=_source_profile_from_data(data["source_profile"]),
        evidence_vocabulary=_vocabulary_from_data(data["evidence_vocabulary"]),
        findings=tuple(
            _finding_from_data(item)
            for item in expect_array(data.get("findings", []), "findings")
        ),
    )


def evidence_extraction_plan_to_json(plan: EvidenceExtractionPlan) -> str:
    return json.dumps(asdict(plan), indent=2, ensure_ascii=False)


def evidence_extraction_plan_from_json(text: str) -> EvidenceExtractionPlan:
    data = expect_object(json.loads(text), "evidence extraction plan")
    return EvidenceExtractionPlan(
        evidence_extraction_plan_id=expect_str(
            data["evidence_extraction_plan_id"], "evidence_extraction_plan_id"
        ),
        source_profile_id=expect_str(data["source_profile_id"], "source_profile_id"),
        source_locator=expect_str(data["source_locator"], "source_locator"),
        source_hash=expect_str(data["source_hash"], "source_hash"),
        source_block_ids=tuple(
            expect_str(item, "source_block_id")
            for item in expect_array(data["source_block_ids"], "source_block_ids")
        ),
        allowed_record_types=record_type_tuple(
            expect_array(data["allowed_record_types"], "allowed_record_types")
        ),
        extraction_instructions=expect_str(
            data["extraction_instructions"], "extraction_instructions"
        ),
    )


def _source_profile_from_data(raw: object) -> SourceProfile:
    data = expect_object(raw, "source profile")
    return SourceProfile(
        source_profile_id=expect_str(data["source_profile_id"], "source_profile_id"),
        source_id=expect_str(data["source_id"], "source_id"),
        source_locator=expect_str(data["source_locator"], "source_locator"),
        source_hash=expect_str(data["source_hash"], "source_hash"),
        profile_id=profile_kind(expect_str(data["profile_id"], "profile_id")),
        evidence_vocabulary_id=expect_str(
            data["evidence_vocabulary_id"], "evidence_vocabulary_id"
        ),
        selection_reason=expect_str(data["selection_reason"], "selection_reason"),
        confidence=expect_float(data["confidence"], "confidence"),
        matched_signals=tuple(
            expect_str(item, "matched_signal")
            for item in expect_array(data["matched_signals"], "matched_signals")
        ),
    )


def _vocabulary_from_data(raw: object) -> EvidenceVocabulary:
    data = expect_object(raw, "evidence vocabulary")
    return EvidenceVocabulary(
        evidence_vocabulary_id=expect_str(
            data["evidence_vocabulary_id"], "evidence_vocabulary_id"
        ),
        profile_id=profile_kind(expect_str(data["profile_id"], "profile_id")),
        allowed_record_types=record_type_tuple(
            expect_array(data["allowed_record_types"], "allowed_record_types")
        ),
    )


def _finding_from_data(raw: object) -> EvidenceExtractionFinding:
    data = expect_object(raw, "evidence extraction finding")
    return EvidenceExtractionFinding(
        finding_id=expect_str(data["finding_id"], "finding_id"),
        severity=expect_literal(
            data["severity"], _EVIDENCE_EXTRACTION_SEVERITIES, "severity"
        ),
        finding_code=expect_str(data["finding_code"], "finding_code"),
        record_type=expect_str(data["record_type"], "record_type"),
        message=expect_str(data["message"], "message"),
    )
