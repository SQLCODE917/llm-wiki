"""Controlled vocabularies for the claim-ledger domain.

Every value here names a reusable category — a linguistic, structural,
semantic-role, notation, or domain-contract category that applies to any
source. Under the Universal Standard, production logic derives from these
categories and never from one source's particular vocabulary, title, author,
character, API, or game term.
"""

from __future__ import annotations

from typing import Final

# -- ledger entries --------------------------------------------------------

LEDGER_ENTRY_KINDS: Final = (
    "claim",
    "event",
    "relationship",
    "concept",
    "quotation",
    "technical-atom",
    "source-note",
)
CLAIM_LIKE_ENTRY_KINDS: Final = ("claim", "event")
LEDGER_ENTRY_STATUSES: Final = ("usable", "needs-review", "rejected")
EXTRACTION_CONFIDENCES: Final = ("high", "medium", "low")

# -- extracted-unit dispositions -------------------------------------------

EXTRACTED_UNIT_DISPOSITIONS: Final = (
    "accepted",
    "structural",
    "needs-review",
    "rejected",
    "non-claim",
)

# -- document structure ----------------------------------------------------

STRUCTURE_NODE_KINDS: Final = (
    "root",
    "chapter",
    "section",
    "heading",
    "glossary-entry",
    "index-entry",
    "reference-entry",
    "other",
)

# -- claim proposition fields ----------------------------------------------

POLARITIES: Final = ("affirmative", "negative")
CLAIM_FORCES: Final = (
    "asserted",
    "possible",
    "required",
    "forbidden",
    "permitted",
    "recommended",
)
CONDITION_SCOPES: Final = ("unconditional", "conditional", "exception")
TEMPORAL_KINDS: Final = (
    "instant",
    "date",
    "range",
    "duration",
    "sequence",
    "recurring",
    "unknown",
)
SPATIAL_KINDS: Final = (
    "place",
    "region",
    "range",
    "setting",
    "relative-location",
    "unknown",
)
SCOPE_CONFIDENCES: Final = ("resolved", "partially-resolved", "unresolved")

# -- technical atoms -------------------------------------------------------

TECHNICAL_ATOM_KINDS: Final = (
    "table",
    "code-block",
    "formula",
    "figure",
    "procedure",
    "rule",
    "worked-example",
)
PARSE_STATUSES: Final = ("parsed", "partially-parsed", "unparsed")
FORMULA_SUBTYPES: Final = ("symbolic-formula", "procedural-formula")
FORMULA_SURFACE_FORMS: Final = ("equation", "prose", "table-cell", "list-item", "mixed")
RULE_FORCES: Final = (
    "required",
    "forbidden",
    "permitted",
    "recommended",
    "asserted-constraint",
)

# -- relationships ---------------------------------------------------------

RELATIONSHIP_KINDS: Final = (
    "causes",
    "coincides-with",
    "precedes",
    "participates-in",
    "located-in",
    "defines",
    "exemplifies",
    "constrains",
    "contrasts-with",
)
CROSS_SOURCE_RELATIONSHIP_KINDS: Final = (
    "conflicts-with",
    "agrees-with",
    "qualifies",
    "supersedes",
)

# -- extraction ranking ----------------------------------------------------

FEATURE_SIGNAL_KINDS: Final = (
    "table-density",
    "code-density",
    "formula-density",
    "figure-density",
    "entity-date-density",
    "rule-language-density",
    "procedure-density",
    "definition-density",
    "relationship-density",
)
EXTRACTOR_CAPABILITY_IDS: Final = (
    "table-extractor",
    "code-block-extractor",
    "formula-extractor",
    "figure-extractor",
    "procedure-extractor",
    "rule-extractor",
    "worked-example-extractor",
)
CAPABILITY_ATOM_KIND: Final = {
    "table-extractor": "table",
    "code-block-extractor": "code-block",
    "formula-extractor": "formula",
    "figure-extractor": "figure",
    "procedure-extractor": "procedure",
    "rule-extractor": "rule",
    "worked-example-extractor": "worked-example",
}
EXTRACTOR_DECISION_STATUSES: Final = ("candidate-produced", "abstained")
ABSTAIN_REASON_KINDS: Final = (
    "insufficient-evidence",
    "ambiguous-unit",
    "schema-mismatch",
    "low-ranker-score",
    "unsupported-modality",
)
ABSTAIN_REASON_REQUIRED_FIELD: Final = {
    "insufficient-evidence": "evidence_requirement",
    "ambiguous-unit": "ambiguity_basis",
    "schema-mismatch": "schema_failure",
    "low-ranker-score": "score_gate",
    "unsupported-modality": "unsupported_modality",
}
CALIBRATION_BUCKETS: Final = ("high", "medium", "low")

# -- source profiles -------------------------------------------------------

SOURCE_FAMILY_LABELS: Final = (
    "history",
    "coding",
    "rules-reference",
    "general-prose",
    "unknown",
)

# -- quality ---------------------------------------------------------------

QUALITY_REPORT_SCOPES: Final = (
    "ledger-build",
    "page-projection",
    "blocked-write",
    "cross-source-projection",
)
QUALITY_FINDING_SEVERITIES: Final = ("blocking", "warning", "info")
QUALITY_FINDING_SEVERITY_ORDER: Final = ("blocking", "warning", "info")
QUALITY_FINDING_REASONS: Final = (
    "traceability-failure",
    "coverage-gap",
    "technical-atom-fidelity-failure",
    "schema-invalid",
    "controlled-vocabulary-invalid",
    "canonical-order-invalid",
    "page-hash-invalid",
    "review-required",
    "audit-metric",
)
REASON_SEVERITY: Final = {
    "traceability-failure": "blocking",
    "coverage-gap": "blocking",
    "technical-atom-fidelity-failure": "blocking",
    "schema-invalid": "blocking",
    "controlled-vocabulary-invalid": "blocking",
    "canonical-order-invalid": "blocking",
    "page-hash-invalid": "blocking",
    "review-required": "warning",
    "audit-metric": "info",
}
PAGE_WRITE_DECISIONS: Final = (
    "block-authoritative-write",
    "write-with-review-work",
    "write-authoritative-page",
)
PROJECTION_COVERAGE_UNIT_KINDS: Final = (
    "generated-page-claim",
    "rendered-technical-atom-block",
    "source-review-item",
    "disposition-count",
    "cross-source-relationship",
    "related-page-link",
)
QUALITY_FINDING_LOCATOR_KINDS: Final = (
    "source-locator",
    "source-range-locator",
    "wiki-page-locator",
    "page-text-range-locator",
    "artifact-locator",
    "domain-id-locator",
)
QUALITY_FINDING_SUBJECT_KINDS: Final = (
    "portable-artifact-set",
    "portable-artifact-member",
    "portable-artifact-pointer",
    "typed-artifact-pointer-alias",
    "raw-source",
    "source-range",
    "document-structure-artifact",
    "structure-node",
    "extracted-unit",
    "source-citation",
    "extractor-capability",
    "active-extractor-capability-set",
    "extractor-decision",
    "atom-candidate",
    "feature-signal",
    "abstain-reason",
    "ranker-score",
    "calibration-bucket",
    "calibration-threshold",
    "calibration-policy",
    "confidence-policy",
    "claim-ledger-artifact",
    "ledger-entry",
    "source-statement",
    "technical-atom",
    "domain-concept",
    "relationship-entry",
    "wiki-page",
    "page-body",
    "projection-source-support",
    "projection-coverage-artifact",
    "projection-coverage-entry",
    "generated-page-claim",
    "rendered-technical-atom-block",
    "source-structure-section",
    "synthesis-section",
    "source-review-section",
    "source-review-item",
    "disposition-count",
    "source-backed-position",
    "cross-source-relationship",
    "related-page-link",
    "quality-report",
    "ledger-quality-report-artifact",
    "quality-finding",
    "quality-check-catalog-artifact",
    "blocked-write-diagnostic-artifact",
    "source-profile",
    "source-family-assignment",
)

# -- portable artifacts ----------------------------------------------------

ARTIFACT_FORMAT: Final = "canonical-json"
PORTABLE_ARTIFACT_KINDS: Final = (
    "portable-artifact-set",
    "document-structure-artifact",
    "claim-ledger-artifact",
    "source-coverage-artifact",
    "projection-coverage-artifact",
    "ledger-quality-report-artifact",
    "quality-check-catalog-artifact",
    "blocked-write-diagnostic-artifact",
)


def reason_severity(reason: str) -> str:
    """Deterministic ``QualityFindingSeverityPolicy`` mapping."""
    return REASON_SEVERITY[reason]
