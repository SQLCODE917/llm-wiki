"""The ``ClaimLedger`` aggregate and its source-profile classification.

The ledger is the first generated source-derived artifact for one raw source.
It holds the ordered ledger entries, the materialized technical atoms, the
extractor decisions retained for audit, and the rejected candidates retained
for completeness — plus the source profile and emergent family labels derived
after extraction. It carries source locators and evidence ids as authority,
never local file paths.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import cast

from llmwiki.domain.ledger.atom_context import TechnicalAtomContext
from llmwiki.domain.ledger.atoms import AtomCandidate, TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry, SourceStatement
from llmwiki.domain.ledger.extraction import ExtractorDecision


@dataclass(frozen=True)
class FamilyLabelScore:
    label: str
    score: float


@dataclass(frozen=True)
class SourceFamilyAssignment:
    """Scored emergent labels derived from a source profile.

    Labels describe the source after extraction. They never gate which atom
    kinds can be extracted; atom schemas decide that.
    """

    labels: tuple[FamilyLabelScore, ...]
    assignment_confidence: float

    @property
    def top_label(self) -> str:
        if not self.labels:
            return "unknown"
        return max(self.labels, key=lambda item: item.score).label


@dataclass(frozen=True)
class SourceProfile:
    source_locator: str
    unit_count: int
    accepted_entry_count: int
    claim_count: int
    event_count: int
    concept_count: int
    relationship_count: int
    atom_kind_counts: dict[str, int]
    feature_signal_means: dict[str, float]


@dataclass(frozen=True)
class ClaimLedger:
    claim_ledger_id: str
    source_locator: str
    source_hash: str
    evidence_registry_hash: str
    source_profile: SourceProfile
    source_family_assignment: SourceFamilyAssignment
    entries: tuple[LedgerEntry, ...]
    technical_atoms: tuple[TechnicalAtom, ...]
    technical_atom_contexts: tuple[TechnicalAtomContext, ...]
    source_statements: tuple[SourceStatement, ...]
    extractor_decisions: tuple[ExtractorDecision, ...]
    rejected_candidates: tuple[AtomCandidate, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "entries", _as_tuple(self.entries, LedgerEntry))
        object.__setattr__(
            self,
            "technical_atoms",
            _as_tuple(self.technical_atoms, TechnicalAtom),
        )
        object.__setattr__(
            self,
            "technical_atom_contexts",
            _as_tuple(self.technical_atom_contexts, TechnicalAtomContext),
        )
        object.__setattr__(
            self,
            "source_statements",
            _as_tuple(self.source_statements, SourceStatement),
        )
        object.__setattr__(
            self,
            "extractor_decisions",
            _as_tuple(self.extractor_decisions, ExtractorDecision),
        )
        object.__setattr__(
            self,
            "rejected_candidates",
            _as_tuple(self.rejected_candidates, AtomCandidate),
        )

    def entry(self, entry_id: str) -> LedgerEntry | None:
        for candidate in self.entries:
            if candidate.ledger_entry_id == entry_id:
                return candidate
        return None

    def atom(self, atom_id: str) -> TechnicalAtom | None:
        for candidate in self.technical_atoms:
            if candidate.technical_atom_id == atom_id:
                return candidate
        return None

    def atom_contexts(self, atom_id: str) -> tuple[TechnicalAtomContext, ...]:
        return tuple(
            context
            for context in self.technical_atom_contexts
            if context.technical_atom_id == atom_id
        )

    @property
    def usable_entries(self) -> tuple[LedgerEntry, ...]:
        return tuple(entry for entry in self.entries if entry.is_usable)

    @property
    def needs_review_entries(self) -> tuple[LedgerEntry, ...]:
        return tuple(entry for entry in self.entries if entry.ledger_entry_status == "needs-review")


def _as_tuple[T](value: object, item_type: type[T]) -> tuple[T, ...]:
    if isinstance(value, tuple):
        return cast(tuple[T, ...], value)
    if isinstance(value, item_type):
        return (value,)
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
        return tuple(cast(Iterable[T], value))
    return ()
