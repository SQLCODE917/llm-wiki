"""Quality check catalog and the reason/severity policies.

The catalog names every exact rule that can create a quality finding, mapping
each to a source-neutral ``QualityFindingReason``. The reason-applicability
policy bounds which report scopes and subject kinds a reason may use, and the
severity policy maps each reason to one severity. These are portable: the
catalog fingerprint changes only when a check or policy changes, never per
source.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from llmwiki.domain.ledger.canonical import content_fingerprint
from llmwiki.domain.ledger.vocab import QUALITY_FINDING_SUBJECT_KINDS, REASON_SEVERITY


@dataclass(frozen=True)
class QualityCheckDefinition:
    quality_check_id: str
    quality_finding_reason: str
    allowed_quality_report_scopes: tuple[str, ...]
    allowed_quality_finding_subject_kinds: tuple[str, ...]
    quality_finding_subject_field: str = "whole-object"


@dataclass(frozen=True)
class ReasonApplicabilityPolicy:
    allowed_scopes: dict[str, tuple[str, ...]]
    allowed_subject_kinds: dict[str, tuple[str, ...]]


@dataclass(frozen=True)
class QualityFindingSeverityPolicy:
    reason_severity: dict[str, str] = field(default_factory=lambda: dict(REASON_SEVERITY))

    def severity(self, reason: str) -> str:
        return self.reason_severity[reason]


@dataclass(frozen=True)
class QualityCheckCatalog:
    definitions: tuple[QualityCheckDefinition, ...]

    def definition(self, quality_check_id: str) -> QualityCheckDefinition | None:
        for candidate in self.definitions:
            if candidate.quality_check_id == quality_check_id:
                return candidate
        return None


_LEDGER = ("ledger-build", "page-projection", "cross-source-projection")
_ALL = ("ledger-build", "page-projection", "blocked-write", "cross-source-projection")

_APPLICABILITY = ReasonApplicabilityPolicy(
    allowed_scopes={
        "traceability-failure": _LEDGER,
        "coverage-gap": _LEDGER,
        "technical-atom-fidelity-failure": _LEDGER,
        "schema-invalid": _ALL,
        "controlled-vocabulary-invalid": _ALL,
        "canonical-order-invalid": _ALL,
        "page-hash-invalid": ("page-projection", "cross-source-projection"),
        "review-required": _LEDGER,
        "audit-metric": _ALL,
    },
    allowed_subject_kinds={
        "traceability-failure": (
            "raw-source",
            "source-range",
            "source-citation",
            "claim-ledger-artifact",
            "ledger-entry",
            "source-statement",
            "technical-atom",
            "wiki-page",
            "page-body",
            "projection-coverage-artifact",
            "projection-coverage-entry",
            "generated-page-claim",
            "rendered-technical-atom-block",
            "source-review-item",
            "source-backed-position",
            "cross-source-relationship",
        ),
        "coverage-gap": (
            "document-structure-artifact",
            "structure-node",
            "extracted-unit",
            "extractor-decision",
            "claim-ledger-artifact",
            "ledger-entry",
            "technical-atom",
            "wiki-page",
            "page-body",
            "projection-coverage-artifact",
            "projection-coverage-entry",
            "generated-page-claim",
            "rendered-technical-atom-block",
            "source-structure-section",
            "synthesis-section",
            "source-review-section",
            "source-review-item",
            "disposition-count",
        ),
        "technical-atom-fidelity-failure": (
            "atom-candidate",
            "technical-atom",
            "rendered-technical-atom-block",
            "projection-coverage-entry",
            "generated-page-claim",
        ),
        "schema-invalid": QUALITY_FINDING_SUBJECT_KINDS,
        "controlled-vocabulary-invalid": QUALITY_FINDING_SUBJECT_KINDS,
        "canonical-order-invalid": (
            "portable-artifact-set",
            "claim-ledger-artifact",
            "projection-coverage-artifact",
            "quality-report",
            "ledger-quality-report-artifact",
            "quality-check-catalog-artifact",
        ),
        "page-hash-invalid": ("wiki-page", "page-body", "projection-coverage-artifact"),
        "review-required": (
            "source-statement",
            "ledger-entry",
            "atom-candidate",
            "technical-atom",
            "generated-page-claim",
            "source-review-section",
            "source-review-item",
        ),
        "audit-metric": (
            "portable-artifact-set",
            "quality-report",
            "ledger-quality-report-artifact",
            "quality-check-catalog-artifact",
            "claim-ledger-artifact",
            "source-profile",
            "source-family-assignment",
            "extractor-decision",
            "extracted-unit",
            "projection-coverage-artifact",
            "blocked-write-diagnostic-artifact",
        ),
    },
)


def default_reason_applicability_policy() -> ReasonApplicabilityPolicy:
    return _APPLICABILITY


def default_severity_policy() -> QualityFindingSeverityPolicy:
    return QualityFindingSeverityPolicy()


def default_quality_check_catalog() -> QualityCheckCatalog:
    return QualityCheckCatalog(_CHECKS)


def catalog_fingerprint(
    catalog: QualityCheckCatalog,
    applicability: ReasonApplicabilityPolicy,
    severity: QualityFindingSeverityPolicy,
) -> str:
    return content_fingerprint((catalog, applicability, severity))


def _ck(
    check_id: str, reason: str, scopes: tuple[str, ...], subjects: tuple[str, ...]
) -> QualityCheckDefinition:
    return QualityCheckDefinition(check_id, reason, scopes, subjects)


_CHECKS: tuple[QualityCheckDefinition, ...] = (
    _ck(
        "ck-extracted-unit-disposition-present",
        "coverage-gap",
        ("ledger-build",),
        ("extracted-unit",),
    ),
    _ck(
        "ck-extractor-decision-per-capability",
        "coverage-gap",
        ("ledger-build",),
        ("extracted-unit",),
    ),
    _ck(
        "ck-extractor-decision-fields", "schema-invalid", ("ledger-build",), ("extractor-decision",)
    ),
    _ck("ck-ranker-score-range", "schema-invalid", ("ledger-build",), ("ranker-score",)),
    _ck(
        "ck-calibration-bucket-vocabulary",
        "controlled-vocabulary-invalid",
        ("ledger-build",),
        ("calibration-bucket",),
    ),
    _ck("ck-claim-required-fields", "schema-invalid", ("ledger-build",), ("ledger-entry",)),
    _ck(
        "ck-technical-atom-payload",
        "technical-atom-fidelity-failure",
        ("ledger-build",),
        ("technical-atom",),
    ),
    _ck("ck-needs-review-reason", "review-required", ("ledger-build",), ("ledger-entry",)),
    _ck(
        "ck-entry-evidence-traceable", "traceability-failure", ("ledger-build",), ("ledger-entry",)
    ),
    _ck(
        "ck-entry-controlled-vocabulary",
        "controlled-vocabulary-invalid",
        ("ledger-build",),
        ("ledger-entry",),
    ),
    _ck("ck-ledger-status-metric", "audit-metric", ("ledger-build",), ("claim-ledger-artifact",)),
    _ck(
        "ck-family-assignment-metric",
        "audit-metric",
        ("ledger-build",),
        ("source-family-assignment",),
    ),
    _ck("ck-extractor-decision-metric", "audit-metric", ("ledger-build",), ("extractor-decision",)),
    _ck(
        "ck-generated-claim-traceable",
        "traceability-failure",
        ("page-projection",),
        ("generated-page-claim",),
    ),
    _ck(
        "ck-generated-claim-usable", "coverage-gap", ("page-projection",), ("generated-page-claim",)
    ),
    _ck("ck-accepted-atom-rendered", "coverage-gap", ("page-projection",), ("technical-atom",)),
    _ck(
        "ck-atom-block-payload",
        "technical-atom-fidelity-failure",
        ("page-projection",),
        ("rendered-technical-atom-block",),
    ),
    _ck(
        "ck-page-body-no-internal-ids", "traceability-failure", ("page-projection",), ("page-body",)
    ),
    _ck(
        "ck-source-review-item-fields",
        "coverage-gap",
        ("page-projection",),
        ("source-review-item",),
    ),
    _ck(
        "ck-projection-coverage-metric",
        "audit-metric",
        ("page-projection",),
        ("projection-coverage-artifact",),
    ),
)
