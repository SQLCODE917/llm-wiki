"""LedgerQualityReport builders for claim-ledger artifacts.

Each report is scoped to ``ledger-build`` and holds ``QualityFinding`` records
that resolve their check id through the catalog pointer. This repo keeps page
synthesis in the existing source-summary/technical-detail renderer, so the
ledger module does not own a page-write boundary.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import PortableArtifactPointer
from llmwiki.domain.ledger.quality_catalog import (
    QualityCheckCatalog,
    QualityFindingSeverityPolicy,
)
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.vocab import (
    CALIBRATION_BUCKETS,
    CLAIM_FORCES,
    EXTRACTION_CONFIDENCES,
    EXTRACTOR_CAPABILITY_IDS,
    LEDGER_ENTRY_KINDS,
    LEDGER_ENTRY_STATUSES,
    POLARITIES,
)


@dataclass(frozen=True)
class QualityFindingSubject:
    quality_finding_subject_kind: str
    quality_finding_subject_id: str
    quality_finding_subject_field: str = "whole-object"


@dataclass(frozen=True)
class QualityFindingLocator:
    quality_finding_locator_kind: str
    quality_finding_subject_id: str = ""
    source_locator: str = ""
    source_hash: str = ""
    source_range_id: str = ""
    wiki_page_locator: str = ""


@dataclass(frozen=True)
class QualityFinding:
    quality_check_id: str
    quality_report_scope: str
    quality_finding_severity: str
    quality_finding_reason: str
    quality_finding_subject: QualityFindingSubject
    quality_finding_locator: QualityFindingLocator
    review_reason: ReviewReason | None = None


@dataclass(frozen=True)
class LedgerQualityReport:
    quality_report_scope: str
    quality_check_catalog_pointer: PortableArtifactPointer
    findings: tuple[QualityFinding, ...]

    def has_severity(self, severity: str) -> bool:
        return any(f.quality_finding_severity == severity for f in self.findings)


class _Finder:
    def __init__(
        self, scope: str, catalog: QualityCheckCatalog, severity: QualityFindingSeverityPolicy
    ) -> None:
        self._scope = scope
        self._catalog = catalog
        self._severity = severity
        self.findings: list[QualityFinding] = []

    def add(
        self,
        check_id: str,
        subject_kind: str,
        subject_id: str,
        *,
        review_reason: ReviewReason | None = None,
    ) -> None:
        definition = self._catalog.definition(check_id)
        if definition is None:
            raise KeyError(f"unknown quality check {check_id!r}")
        reason = definition.quality_finding_reason
        self.findings.append(
            QualityFinding(
                quality_check_id=check_id,
                quality_report_scope=self._scope,
                quality_finding_severity=self._severity.severity(reason),
                quality_finding_reason=reason,
                quality_finding_subject=QualityFindingSubject(subject_kind, subject_id),
                quality_finding_locator=QualityFindingLocator("domain-id-locator", subject_id),
                review_reason=review_reason,
            )
        )


def build_ledger_quality_report(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    catalog: QualityCheckCatalog,
    severity: QualityFindingSeverityPolicy,
    catalog_pointer: PortableArtifactPointer,
) -> LedgerQualityReport:
    finder = _Finder("ledger-build", catalog, severity)
    _check_dispositions(finder, ledger, structure)
    _check_decisions(finder, ledger)
    _check_atoms(finder, ledger)
    _check_entries(finder, ledger)
    _ledger_metrics(finder, ledger)
    return LedgerQualityReport("ledger-build", catalog_pointer, tuple(finder.findings))


def _check_dispositions(finder: _Finder, ledger: ClaimLedger, structure: DocumentStructure) -> None:
    if len(structure.dispositions) != ledger.source_profile.unit_count:
        finder.add(
            "ck-extracted-unit-disposition-present", "extracted-unit", ledger.claim_ledger_id
        )


def _check_decisions(finder: _Finder, ledger: ClaimLedger) -> None:
    by_range: dict[str, set[str]] = {}
    for decision in ledger.extractor_decisions:
        by_range.setdefault(decision.source_range_id, set()).add(decision.extractor_capability_id)
        if (
            decision.extractor_decision_status == "candidate-produced"
            and not decision.atom_candidate_id
        ):
            finder.add(
                "ck-extractor-decision-fields", "extractor-decision", decision.extractor_decision_id
            )
        if decision.extractor_decision_status == "abstained" and decision.abstain_reason is None:
            finder.add(
                "ck-extractor-decision-fields", "extractor-decision", decision.extractor_decision_id
            )
        if not 0.0 <= decision.ranker_score <= 1.0:
            finder.add("ck-ranker-score-range", "ranker-score", decision.extractor_decision_id)
        if decision.calibration_bucket and decision.calibration_bucket not in CALIBRATION_BUCKETS:
            finder.add(
                "ck-calibration-bucket-vocabulary",
                "calibration-bucket",
                decision.extractor_decision_id,
            )
    for source_range_id, capability_ids in by_range.items():
        if capability_ids != set(EXTRACTOR_CAPABILITY_IDS):
            finder.add("ck-extractor-decision-per-capability", "extracted-unit", source_range_id)


def _check_atoms(finder: _Finder, ledger: ClaimLedger) -> None:
    from llmwiki.domain.ledger.atoms import atom_raw_text

    for atom in ledger.technical_atoms:
        if not atom_raw_text(atom.payload).strip():
            finder.add("ck-technical-atom-payload", "technical-atom", atom.technical_atom_id)


def _check_entries(finder: _Finder, ledger: ClaimLedger) -> None:
    for entry in ledger.entries:
        if (
            entry.ledger_entry_kind not in LEDGER_ENTRY_KINDS
            or entry.ledger_entry_status not in LEDGER_ENTRY_STATUSES
            or entry.extraction_confidence not in EXTRACTION_CONFIDENCES
        ):
            finder.add("ck-entry-controlled-vocabulary", "ledger-entry", entry.ledger_entry_id)
        if entry.is_usable and not entry.evidence_ids:
            finder.add("ck-entry-evidence-traceable", "ledger-entry", entry.ledger_entry_id)
        if entry.is_usable and entry.is_claim_like:
            _check_claim_fields(finder, entry)
        if entry.ledger_entry_status == "needs-review":
            finder.add(
                "ck-needs-review-reason",
                "ledger-entry",
                entry.ledger_entry_id,
                review_reason=entry.review_reason
                or ReviewReason("needs-review", "entry requires review"),
            )


def _check_claim_fields(finder: _Finder, entry: object) -> None:
    subject = getattr(entry, "subject", "")
    predicate = getattr(entry, "predicate", "")
    object_value = getattr(entry, "object_value", "")
    polarity = getattr(entry, "polarity", "")
    claim_force = getattr(entry, "claim_force", "")
    entry_id = getattr(entry, "ledger_entry_id", "")
    complete = bool(subject and predicate and object_value)
    valid_vocab = polarity in POLARITIES and claim_force in CLAIM_FORCES
    if not (complete and valid_vocab):
        finder.add("ck-claim-required-fields", "ledger-entry", entry_id)


def _ledger_metrics(finder: _Finder, ledger: ClaimLedger) -> None:
    finder.add("ck-ledger-status-metric", "claim-ledger-artifact", ledger.claim_ledger_id)
    finder.add("ck-family-assignment-metric", "source-family-assignment", ledger.claim_ledger_id)
    finder.add("ck-extractor-decision-metric", "extractor-decision", ledger.claim_ledger_id)
