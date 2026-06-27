"""Schema-input contracts: atom schemas, validator, and ranking policies.

These are the records the ``SchemaInputPort`` supplies to the domain: the
active atom schema set, the active extractor capability set, and the feature
signal, abstain reason, and calibration policies. They are portable and
source-neutral; renamed-domain source variants validate identically.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import AtomPayload
from llmwiki.domain.ledger.extraction import (
    AbstainReason,
    ActiveExtractorCapabilitySet,
    ExtractorCapability,
    FeatureSignal,
)
from llmwiki.domain.ledger.vocab import (
    ABSTAIN_REASON_KINDS,
    ABSTAIN_REASON_REQUIRED_FIELD,
    CALIBRATION_BUCKETS,
    EXTRACTOR_CAPABILITY_IDS,
    FEATURE_SIGNAL_KINDS,
    FORMULA_SUBTYPES,
    FORMULA_SURFACE_FORMS,
    PARSE_STATUSES,
    RULE_FORCES,
)

# -- atom schemas ----------------------------------------------------------


@dataclass(frozen=True)
class AtomSchema:
    atom_kind: str
    required_fields: tuple[str, ...]
    enumerated_fields: tuple[tuple[str, tuple[str, ...]], ...] = ()


@dataclass(frozen=True)
class AtomValidationResult:
    status: str  # "valid" | "invalid"
    detail: str = ""
    failed_fields: tuple[str, ...] = ()


@dataclass(frozen=True)
class AtomSchemaSet:
    schemas: tuple[AtomSchema, ...]

    def schema(self, atom_kind: str) -> AtomSchema | None:
        for candidate in self.schemas:
            if candidate.atom_kind == atom_kind:
                return candidate
        return None


class AtomValidator:
    """Validates atom candidate payloads against the active atom schema set."""

    def __init__(self, schema_set: AtomSchemaSet) -> None:
        self._schema_set = schema_set

    def validate(self, atom_kind: str, payload: AtomPayload | None) -> AtomValidationResult:
        schema = self._schema_set.schema(atom_kind)
        if schema is None:
            return AtomValidationResult("invalid", f"no schema for atom kind {atom_kind!r}")
        if payload is None:
            return AtomValidationResult("invalid", "no materialized payload", ("payload",))
        missing = tuple(
            field_name for field_name in schema.required_fields if _is_empty(payload, field_name)
        )
        if missing:
            return AtomValidationResult("invalid", "missing required fields", missing)
        bad = tuple(
            field_name
            for field_name, allowed in schema.enumerated_fields
            if getattr(payload, field_name, "") not in allowed
        )
        if bad:
            return AtomValidationResult("invalid", "value outside controlled vocabulary", bad)
        return AtomValidationResult("valid")


def _is_empty(payload: AtomPayload, field_name: str) -> bool:
    value = getattr(payload, field_name, None)
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (tuple, list)):
        return len(value) == 0
    return False


# -- ranking policies ------------------------------------------------------


@dataclass(frozen=True)
class FeatureSignalPolicy:
    allowed_kinds: tuple[str, ...] = FEATURE_SIGNAL_KINDS

    def is_valid_kind(self, kind: str) -> bool:
        return kind in self.allowed_kinds

    def validate(self, signal: FeatureSignal) -> bool:
        return self.is_valid_kind(signal.feature_signal_kind) and isinstance(
            signal.feature_signal_value, (int, float)
        )


@dataclass(frozen=True)
class AbstainReasonPolicy:
    allowed_kinds: tuple[str, ...] = ABSTAIN_REASON_KINDS

    def validate(self, reason: AbstainReason) -> bool:
        if reason.abstain_reason_kind not in self.allowed_kinds:
            return False
        required = ABSTAIN_REASON_REQUIRED_FIELD.get(reason.abstain_reason_kind)
        if required is None:
            return False
        return getattr(reason, required, None) is not None


@dataclass(frozen=True)
class CalibrationThreshold:
    extractor_capability_id: str
    high: float
    medium: float


@dataclass(frozen=True)
class CalibrationPolicy:
    active_capability_ids: tuple[str, ...]
    thresholds: tuple[CalibrationThreshold, ...]
    ranker_score_range: tuple[float, float] = (0.0, 1.0)
    calibration_bucket_set: tuple[str, ...] = CALIBRATION_BUCKETS

    def in_range(self, score: float) -> bool:
        low, high = self.ranker_score_range
        return low <= score <= high

    def threshold(self, capability_id: str) -> CalibrationThreshold | None:
        for candidate in self.thresholds:
            if candidate.extractor_capability_id == capability_id:
                return candidate
        return None

    def bucket_for(self, capability_id: str, score: float) -> str:
        threshold = self.threshold(capability_id)
        if threshold is None:
            return "low"
        if score >= threshold.high:
            return "high"
        if score >= threshold.medium:
            return "medium"
        return "low"


# -- default schema-input bundle -------------------------------------------


def default_atom_schema_set() -> AtomSchemaSet:
    return AtomSchemaSet(
        schemas=(
            AtomSchema(
                "table",
                ("raw_table_text", "parse_status", "source_locator"),
                (("parse_status", PARSE_STATUSES),),
            ),
            AtomSchema(
                "code-block",
                ("raw_code_text", "parse_status", "source_locator"),
                (("parse_status", PARSE_STATUSES),),
            ),
            AtomSchema(
                "formula",
                ("raw_formula_text", "formula_subtype", "formula_surface_form", "source_locator"),
                (
                    ("formula_subtype", FORMULA_SUBTYPES),
                    ("formula_surface_form", FORMULA_SURFACE_FORMS),
                ),
            ),
            AtomSchema(
                "figure",
                ("raw_figure_text", "parse_status", "source_locator"),
                (("parse_status", PARSE_STATUSES),),
            ),
            AtomSchema("procedure", ("procedure_text", "steps", "source_locator")),
            AtomSchema(
                "rule",
                ("rule_text", "rule_force", "source_locator"),
                (("rule_force", RULE_FORCES),),
            ),
            AtomSchema("worked-example", ("example_text", "source_locator")),
        )
    )


def default_active_extractor_capability_set() -> ActiveExtractorCapabilitySet:
    from llmwiki.domain.ledger.vocab import CAPABILITY_ATOM_KIND

    return ActiveExtractorCapabilitySet(
        capabilities=tuple(
            ExtractorCapability(capability_id, CAPABILITY_ATOM_KIND[capability_id])
            for capability_id in EXTRACTOR_CAPABILITY_IDS
        )
    )


def default_calibration_policy() -> CalibrationPolicy:
    # Uniform thresholds keyed only by capability id — never by source title,
    # filename, author, passage, or domain-specific term.
    return CalibrationPolicy(
        active_capability_ids=EXTRACTOR_CAPABILITY_IDS,
        thresholds=tuple(
            CalibrationThreshold(capability_id, high=0.66, medium=0.40)
            for capability_id in EXTRACTOR_CAPABILITY_IDS
        ),
    )
