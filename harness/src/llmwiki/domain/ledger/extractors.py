"""Deterministic extractor/ranker for one source segment.

For each segment and each active extractor capability the ranker scores the
capability from the segment's feature signals, applies the calibration policy,
and either materializes one atom candidate (validated against the atom schema
set) or records an abstain decision with a typed abstain reason. Exactly one
``ExtractorDecision`` is produced per segment and capability.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import AtomCandidate, AtomPayload, payload_fingerprint
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.extraction import (
    AbstainReason,
    ActiveExtractorCapabilitySet,
    EvidenceRequirement,
    ExtractedUnitProfile,
    ExtractorDecision,
    SchemaFailure,
    ScoreGate,
    UnsupportedModality,
)
from llmwiki.domain.ledger.materialize import (
    materialize_code_block,
    materialize_figure,
    materialize_formula,
    materialize_procedure,
    materialize_rule,
    materialize_table,
    materialize_worked_example,
)
from llmwiki.domain.ledger.schemas import AtomValidator, CalibrationPolicy
from llmwiki.domain.ledger.segments import SourceSegment

_CAPABILITY_SIGNAL = {
    "table-extractor": "table-density",
    "code-block-extractor": "code-density",
    "formula-extractor": "formula-density",
    "figure-extractor": "figure-density",
    "procedure-extractor": "procedure-density",
    "rule-extractor": "rule-language-density",
    "worked-example-extractor": "relationship-density",
}
_TABLE_GATE = 0.15
_MAX_DECISION_SIGNAL_IDS = 32
# A segment's modality decides which extractors may materialize: a code fence
# yields only a code atom, a tabular block only a table, prose only the prose
# atom kinds. Other capabilities abstain (unsupported modality), so each
# capability still records exactly one decision per segment.
_PROSE_CAPABILITIES = frozenset(
    {"formula-extractor", "rule-extractor", "procedure-extractor", "worked-example-extractor"}
)
_KIND_CAPABILITIES: dict[str, frozenset[str]] = {
    "code-fence": frozenset({"code-block-extractor"}),
    "table-block": frozenset({"table-extractor"}),
    "figure": frozenset({"figure-extractor"}),
    "paragraph": _PROSE_CAPABILITIES,
    "list": _PROSE_CAPABILITIES,
    "heading": frozenset(),
    "blank": frozenset(),
}


@dataclass(frozen=True)
class SegmentExtraction:
    decisions: tuple[ExtractorDecision, ...]
    candidates: tuple[AtomCandidate, ...]


def extract_segment(
    segment: SourceSegment,
    profile: ExtractedUnitProfile,
    *,
    capabilities: ActiveExtractorCapabilitySet,
    calibration: CalibrationPolicy,
    validator: AtomValidator,
) -> SegmentExtraction:
    decisions: list[ExtractorDecision] = []
    candidates: list[AtomCandidate] = []
    signal_ids = _decision_signal_ids(profile)
    for capability in capabilities.capabilities:
        signal_kind = _CAPABILITY_SIGNAL.get(capability.extractor_capability_id, "")
        score = round(profile.value(signal_kind), 4) if signal_kind else 0.0
        bucket = calibration.bucket_for(capability.extractor_capability_id, score)
        payload, review_reason = (
            _materialize(capability.extractor_capability_id, segment, profile)
            if _passes_score_gate(capability.extractor_capability_id, score, calibration)
            else (None, None)
        )
        decision_id = deterministic_id(
            "extractor-decision",
            segment.source_hash,
            segment.source_range_id,
            capability.extractor_capability_id,
        )
        if payload is not None:
            candidate = _candidate(
                segment,
                capability.extractor_capability_id,
                payload,
                review_reason,
                score,
                bucket,
                signal_ids,
                decision_id,
                validator,
            )
            candidates.append(candidate)
            decisions.append(
                ExtractorDecision(
                    extractor_decision_id=decision_id,
                    source_range_id=segment.source_range_id,
                    extractor_capability_id=capability.extractor_capability_id,
                    extractor_decision_status="candidate-produced",
                    feature_signal_ids=signal_ids,
                    ranker_score=score,
                    calibration_bucket=bucket,
                    atom_candidate_id=candidate.atom_candidate_id,
                )
            )
        else:
            decisions.append(
                ExtractorDecision(
                    extractor_decision_id=decision_id,
                    source_range_id=segment.source_range_id,
                    extractor_capability_id=capability.extractor_capability_id,
                    extractor_decision_status="abstained",
                    feature_signal_ids=signal_ids,
                    ranker_score=score,
                    calibration_bucket=bucket,
                    abstain_reason=_abstain_reason(
                        segment, score, calibration, capability.extractor_capability_id
                    ),
                )
            )
    return SegmentExtraction(tuple(decisions), tuple(candidates))


def _decision_signal_ids(profile: ExtractedUnitProfile) -> tuple[str, ...]:
    signal_ids: list[str] = []
    for signal in profile.feature_signals:
        signal_ids.append(signal.feature_signal_id)
        if len(signal_ids) >= _MAX_DECISION_SIGNAL_IDS:
            break
    return tuple(signal_ids)


def _materialize(
    capability_id: str, segment: SourceSegment, profile: ExtractedUnitProfile
) -> tuple[AtomPayload | None, ReviewReason | None]:
    allowed = _KIND_CAPABILITIES.get(segment.segment_kind, _PROSE_CAPABILITIES)
    if capability_id not in allowed:
        return None, None
    if capability_id == "code-block-extractor":
        result = materialize_code_block(segment)
        return (result[0], None) if result else (None, None)
    if capability_id == "table-extractor":
        if profile.value("table-density") < _TABLE_GATE:
            return None, None
        return materialize_table(segment)
    if capability_id == "formula-extractor":
        return materialize_formula(segment), None
    if capability_id == "figure-extractor":
        return materialize_figure(segment), None
    if capability_id == "rule-extractor":
        rule_result = materialize_rule(segment)
        return rule_result if rule_result is not None else (None, None)
    if capability_id == "procedure-extractor":
        return materialize_procedure(segment), None
    if capability_id == "worked-example-extractor":
        return materialize_worked_example(segment), None
    return None, None


def _passes_score_gate(capability_id: str, score: float, calibration: CalibrationPolicy) -> bool:
    if capability_id == "code-block-extractor":
        return True
    if capability_id == "table-extractor":
        return score >= _TABLE_GATE
    if capability_id == "figure-extractor":
        return score >= 1.0
    threshold = calibration.threshold(capability_id)
    gate = threshold.medium if threshold is not None else 0.4
    return score >= gate


def _candidate(
    segment: SourceSegment,
    capability_id: str,
    payload: AtomPayload,
    review_reason: ReviewReason | None,
    score: float,
    bucket: str,
    signal_ids: tuple[str, ...],
    decision_id: str,
    validator: AtomValidator,
) -> AtomCandidate:
    atom_kind = _atom_kind(capability_id)
    result = validator.validate(atom_kind, payload)
    candidate_id = deterministic_id(
        "atom-candidate",
        segment.source_hash,
        segment.source_range_id,
        capability_id,
        payload_fingerprint(payload),
    )
    return AtomCandidate(
        atom_candidate_id=candidate_id,
        extractor_decision_id=decision_id,
        extractor_capability_id=capability_id,
        technical_atom_kind=atom_kind,
        ranker_score=score,
        calibration_bucket=bucket,
        source_range_id=segment.source_range_id,
        feature_signal_ids=signal_ids,
        evidence_ids=segment.evidence_ids,
        payload=payload,
        review_reason=review_reason,
        validation_status=result.status,
        validation_detail=result.detail,
    )


def _abstain_reason(
    segment: SourceSegment, score: float, calibration: CalibrationPolicy, capability_id: str
) -> AbstainReason:
    allowed = _KIND_CAPABILITIES.get(segment.segment_kind, _PROSE_CAPABILITIES)
    if capability_id not in allowed:
        return AbstainReason(
            "unsupported-modality",
            unsupported_modality=UnsupportedModality(f"segment modality {segment.segment_kind!r}"),
        )
    if not segment.text.strip():
        return AbstainReason(
            "insufficient-evidence",
            evidence_requirement=EvidenceRequirement("segment has no source text"),
        )
    if not calibration.in_range(score):
        return AbstainReason(
            "schema-mismatch",
            schema_failure=SchemaFailure(("ranker_score",), "score outside calibration range"),
        )
    threshold = calibration.threshold(capability_id)
    gate = threshold.medium if threshold is not None else 0.4
    return AbstainReason("low-ranker-score", score_gate=ScoreGate(score, gate))


def _atom_kind(capability_id: str) -> str:
    from llmwiki.domain.ledger.vocab import CAPABILITY_ATOM_KIND

    return CAPABILITY_ATOM_KIND[capability_id]
