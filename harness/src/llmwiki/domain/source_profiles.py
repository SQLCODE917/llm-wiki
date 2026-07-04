"""Source-purpose profiles and evidence vocabulary contracts."""

from __future__ import annotations

import hashlib
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Literal, cast

from llmwiki.domain.source_map import NormalizedSourceMap

EvidenceRecordType = Literal[
    "rule",
    "procedure_step",
    "formula",
    "table_fact",
    "code_example",
    "argument",
    "definition",
    "entity_fact",
    "navigation_note",
]
SourceProfileKind = Literal["rpg-rules", "programming-prose", "reference", "general-prose"]
EvidenceExtractionSeverity = Literal["blocker", "warning", "info"]

ALL_EVIDENCE_RECORD_TYPES: tuple[EvidenceRecordType, ...] = (
    "rule",
    "procedure_step",
    "formula",
    "table_fact",
    "code_example",
    "argument",
    "definition",
    "entity_fact",
    "navigation_note",
)
PROFILE_KINDS: tuple[SourceProfileKind, ...] = (
    "rpg-rules",
    "programming-prose",
    "reference",
    "general-prose",
)


@dataclass(frozen=True)
class EvidenceVocabulary:
    evidence_vocabulary_id: str
    profile_id: SourceProfileKind
    allowed_record_types: tuple[EvidenceRecordType, ...]

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "allowed_record_types",
            record_type_tuple(self.allowed_record_types),
        )
        if not self.allowed_record_types:
            raise ValueError("EvidenceVocabulary requires at least one record type.")
        if "claim" in cast(tuple[str, ...], self.allowed_record_types):
            raise ValueError("EvidenceVocabulary must not use generic claim records.")


@dataclass(frozen=True)
class SourceProfile:
    source_profile_id: str
    source_id: str
    source_locator: str
    source_hash: str
    profile_id: SourceProfileKind
    evidence_vocabulary_id: str
    selection_reason: str
    confidence: float
    matched_signals: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "matched_signals", tuple(self.matched_signals))
        if not 0 <= self.confidence <= 1:
            raise ValueError("SourceProfile confidence must be between 0 and 1.")


@dataclass(frozen=True)
class EvidenceExtractionPlan:
    evidence_extraction_plan_id: str
    source_profile_id: str
    source_locator: str
    source_hash: str
    source_block_ids: tuple[str, ...]
    allowed_record_types: tuple[EvidenceRecordType, ...]
    extraction_instructions: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "source_block_ids", tuple(self.source_block_ids))
        object.__setattr__(
            self,
            "allowed_record_types",
            record_type_tuple(self.allowed_record_types),
        )


@dataclass(frozen=True)
class EvidenceExtractionFinding:
    finding_id: str
    severity: EvidenceExtractionSeverity
    finding_code: str
    record_type: str
    message: str


@dataclass(frozen=True)
class SourceProfileArtifact:
    source_profile: SourceProfile
    evidence_vocabulary: EvidenceVocabulary
    findings: tuple[EvidenceExtractionFinding, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "findings", tuple(self.findings))


def default_evidence_vocabularies() -> dict[SourceProfileKind, EvidenceVocabulary]:
    return {
        "rpg-rules": _vocabulary(
            "rpg-rules",
            (
                "rule",
                "procedure_step",
                "formula",
                "table_fact",
                "entity_fact",
                "definition",
                "navigation_note",
            ),
        ),
        "programming-prose": _vocabulary(
            "programming-prose",
            (
                "code_example",
                "argument",
                "definition",
                "procedure_step",
                "entity_fact",
                "navigation_note",
            ),
        ),
        "reference": _vocabulary(
            "reference",
            ("definition", "table_fact", "formula", "entity_fact", "navigation_note"),
        ),
        "general-prose": _vocabulary(
            "general-prose",
            ("argument", "definition", "entity_fact", "navigation_note"),
        ),
    }


def build_evidence_extraction_plan(
    source_map: NormalizedSourceMap,
    source_profile: SourceProfile,
    evidence_vocabulary: EvidenceVocabulary,
) -> EvidenceExtractionPlan:
    source_block_ids = tuple(
        block.source_block_id
        for block in sorted(source_map.source_blocks, key=lambda item: item.source_order)
        if block.source_text.strip()
    )
    allowed = evidence_vocabulary.allowed_record_types
    instructions = (
        "Extract typed evidence from source blocks using only these record types: "
        f"{', '.join(allowed)}. "
        "Reject or report any model output that names a record type outside this vocabulary."
    )
    return EvidenceExtractionPlan(
        evidence_extraction_plan_id=stable_id(
            "evidence-extraction-plan",
            source_profile.source_profile_id,
            ",".join(source_block_ids),
            ",".join(allowed),
        ),
        source_profile_id=source_profile.source_profile_id,
        source_locator=source_map.source_locator,
        source_hash=source_map.source_hash,
        source_block_ids=source_block_ids,
        allowed_record_types=allowed,
        extraction_instructions=instructions,
    )


def validate_evidence_record_types(
    plan: EvidenceExtractionPlan, proposed_record_types: Iterable[str]
) -> tuple[EvidenceExtractionFinding, ...]:
    findings: list[EvidenceExtractionFinding] = []
    known = set(ALL_EVIDENCE_RECORD_TYPES)
    allowed = set(plan.allowed_record_types)
    for index, record_type in enumerate(proposed_record_types, start=1):
        if record_type not in known:
            code = "unknown-evidence-record-type"
            message = f"Unknown evidence record type {record_type!r}; use the plan vocabulary only."
        elif record_type not in allowed:
            code = "disallowed-evidence-record-type"
            message = f"Evidence record type {record_type!r} is not allowed by this source profile."
        else:
            continue
        findings.append(
            EvidenceExtractionFinding(
                finding_id=stable_id(
                    "evidence-extraction-finding",
                    plan.evidence_extraction_plan_id,
                    code,
                    str(index),
                ),
                severity="blocker",
                finding_code=code,
                record_type=record_type,
                message=message,
            )
        )
    return tuple(findings)


def make_source_profile(
    source_map: NormalizedSourceMap,
    profile_id: SourceProfileKind,
    vocabulary: EvidenceVocabulary,
    *,
    confidence: float,
    matched_signals: tuple[str, ...],
) -> SourceProfile:
    signal_text = (
        ", ".join(matched_signals) if matched_signals else "no specialized source-map signals"
    )
    reason = (
        f"Selected {profile_id} from normalized source map signals: {signal_text}. "
        f"Confidence {confidence:.2f}."
    )
    return SourceProfile(
        source_profile_id=stable_id(
            "source-profile", source_map.source_id, profile_id, source_map.source_hash
        ),
        source_id=source_map.source_id,
        source_locator=source_map.source_locator,
        source_hash=source_map.source_hash,
        profile_id=profile_id,
        evidence_vocabulary_id=vocabulary.evidence_vocabulary_id,
        selection_reason=reason,
        confidence=confidence,
        matched_signals=matched_signals,
    )


def low_confidence_profile_finding(profile: SourceProfile) -> EvidenceExtractionFinding:
    return EvidenceExtractionFinding(
        finding_id=stable_id(
            "evidence-extraction-finding",
            profile.source_profile_id,
            "low-confidence",
        ),
        severity="warning",
        finding_code="low-confidence-source-profile",
        record_type="",
        message="No specialized source-map profile signal was strong enough; using general-prose.",
    )


def profile_kind(value: object) -> SourceProfileKind:
    if value not in PROFILE_KINDS:
        raise ValueError(f"Unknown source profile: {value!r}.")
    return value


def record_type_tuple(data: Iterable[object]) -> tuple[EvidenceRecordType, ...]:
    values = tuple(str(item) for item in data)
    unknown = sorted(set(values) - set(ALL_EVIDENCE_RECORD_TYPES))
    if unknown:
        raise ValueError(f"Unknown evidence record type(s): {', '.join(unknown)}.")
    return cast(tuple[EvidenceRecordType, ...], values)


def stable_id(prefix: str, *parts: str) -> str:
    return f"{prefix}-{hashlib.sha256('|'.join(parts).encode('utf-8')).hexdigest()[:16]}"


def _vocabulary(
    profile_id: SourceProfileKind, allowed_record_types: tuple[EvidenceRecordType, ...]
) -> EvidenceVocabulary:
    return EvidenceVocabulary(
        evidence_vocabulary_id=stable_id(
            "evidence-vocabulary",
            profile_id,
            ",".join(allowed_record_types),
        ),
        profile_id=profile_id,
        allowed_record_types=allowed_record_types,
    )
