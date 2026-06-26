"""The ``LedgerEntry`` record — the unit of a claim ledger.

A ledger entry is one source-derived claim, event, relationship, concept,
quotation, technical-atom reference, or source note. Claim-like entries
(``claim``, ``event``) carry structured proposition fields; concept and
relationship entries carry facets and a typed predicate. Every entry carries
its evidence, source-close ``normalized_text``, status, and confidence.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from llmwiki.domain.ledger.common import (
    ConfidenceBasis,
    ReviewReason,
    SpatialScope,
    TemporalScope,
)


@dataclass(frozen=True)
class LedgerEntry:
    ledger_entry_id: str
    source_statement_id: str
    ledger_entry_kind: str
    ledger_entry_status: str
    extraction_confidence: str
    confidence_basis: ConfidenceBasis
    source_locator: str
    source_hash: str
    source_range_id: str
    evidence_ids: tuple[str, ...]
    source_text: str
    structure_node_ids: tuple[str, ...] = ()
    review_reason: ReviewReason | None = None
    quotation_text: str = ""
    normalized_text: str = ""
    resolution_basis: str = ""
    # claim-like proposition fields
    subject: str = ""
    predicate: str = ""
    object_value: str = ""
    polarity: str = ""
    claim_force: str = ""
    condition_scope: str = ""
    condition_text: str = ""
    exception_text: str = ""
    temporal_scope: TemporalScope | None = None
    spatial_scope: SpatialScope | None = None
    claim_role_tags: tuple[str, ...] = ()
    # technical-atom / concept / relationship fields
    technical_atom_kind: str = ""
    technical_atom_id: str = ""
    concept_facets: tuple[str, ...] = ()
    relationship_kind: str = ""
    related_entry_ids: tuple[str, ...] = ()
    derived_entry_ids: tuple[str, ...] = ()
    statement_relationship: str = ""

    @property
    def is_claim_like(self) -> bool:
        return self.ledger_entry_kind in ("claim", "event")

    @property
    def is_usable(self) -> bool:
        return self.ledger_entry_status == "usable"


@dataclass(frozen=True)
class SourceStatement:
    """One source-bounded statement that can produce multiple ledger entries."""

    source_statement_id: str
    source_range_id: str
    source_text: str
    derived_entry_ids: tuple[str, ...] = field(default_factory=tuple)
