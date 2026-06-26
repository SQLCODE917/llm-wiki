"""Extraction-time records: feature signals, decisions, and abstain reasons.

These are source-neutral. ``FeatureSignal`` records measured properties of one
extracted unit (table-density, code-density, ...). The extractor adapter ranks
capabilities from those signals and records exactly one ``ExtractorDecision``
per extracted unit and active extractor capability. Feature signals alone never
accept an atom — atom schema validation remains the acceptance boundary.
"""

from __future__ import annotations

from dataclasses import dataclass

# -- feature signals -------------------------------------------------------


@dataclass(frozen=True)
class FeatureSignal:
    feature_signal_id: str
    feature_signal_kind: str
    feature_signal_value: float
    feature_signal_confidence: str
    source_range_id: str
    evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class ExtractedUnitProfile:
    """Measured feature signals for one extracted unit (no ranker scores)."""

    extracted_unit_id: str
    source_range_id: str
    feature_signals: tuple[FeatureSignal, ...]

    def value(self, kind: str) -> float:
        for signal in self.feature_signals:
            if signal.feature_signal_kind == kind:
                return signal.feature_signal_value
        return 0.0


# -- extractor capabilities ------------------------------------------------


@dataclass(frozen=True)
class ExtractorCapability:
    extractor_capability_id: str
    atom_kind: str
    required_evidence: str = "source-range"


@dataclass(frozen=True)
class ActiveExtractorCapabilitySet:
    capabilities: tuple[ExtractorCapability, ...]


# -- abstain reasons -------------------------------------------------------


@dataclass(frozen=True)
class EvidenceRequirement:
    missing_evidence: str


@dataclass(frozen=True)
class AmbiguityBasis:
    ambiguity: str


@dataclass(frozen=True)
class SchemaFailure:
    failed_fields: tuple[str, ...]
    detail: str = ""


@dataclass(frozen=True)
class ScoreGate:
    score: float
    threshold: float


@dataclass(frozen=True)
class UnsupportedModality:
    modality: str


@dataclass(frozen=True)
class AbstainReason:
    abstain_reason_kind: str
    evidence_ids: tuple[str, ...] = ()
    evidence_requirement: EvidenceRequirement | None = None
    ambiguity_basis: AmbiguityBasis | None = None
    schema_failure: SchemaFailure | None = None
    score_gate: ScoreGate | None = None
    unsupported_modality: UnsupportedModality | None = None


# -- extractor decisions ---------------------------------------------------


@dataclass(frozen=True)
class ExtractorDecision:
    extractor_decision_id: str
    source_range_id: str
    extractor_capability_id: str
    extractor_decision_status: str
    feature_signal_ids: tuple[str, ...] = ()
    ranker_score: float = 0.0
    calibration_bucket: str = ""
    abstain_reason: AbstainReason | None = None
    atom_candidate_id: str = ""
