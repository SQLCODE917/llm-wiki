"""Typed decision-point evidence for procedure guides."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.procedure_language import action_type

_EXAMPLE_ONLY_ATOM_KINDS = frozenset({"worked-example"})
_EXAMPLE_ROLE_TAGS = frozenset({"worked-example", "example"})
_DECISION_ROLE_TAGS = frozenset({"procedure", "method", "requirement", "limitation", "constraint"})


@dataclass(frozen=True)
class DecisionPoint:
    entry: LedgerEntry
    decision_kind: str
    condition_text: str
    outcome_text: str
    supporting_atom_ids: tuple[str, ...]


def plan_decision_points(
    entries: tuple[LedgerEntry, ...], atoms: tuple[TechnicalAtom, ...]
) -> tuple[DecisionPoint, ...]:
    atoms_by_range = _atoms_by_range(atoms)
    points = tuple(
        point
        for entry in entries
        if (point := _decision_point(entry, atoms_by_range.get(entry.source_range_id, ())))
        is not None
    )
    return _unique_decision_points(points)


def _decision_point(entry: LedgerEntry, atoms: tuple[TechnicalAtom, ...]) -> DecisionPoint | None:
    if not entry.is_claim_like or not entry.is_usable:
        return None
    condition = entry.condition_text.strip()
    if not _is_decision_entry(entry):
        return None
    if _is_example_only(entry, atoms):
        return None
    return DecisionPoint(
        entry=entry,
        decision_kind="branch",
        condition_text=condition or _entry_text(entry),
        outcome_text=entry.object_value.strip() or _entry_text(entry),
        supporting_atom_ids=(),
    )


def _is_decision_entry(entry: LedgerEntry) -> bool:
    if entry.condition_scope != "conditional" or not entry.condition_text.strip():
        return False
    return bool(action_type(_entry_text(entry)) or set(entry.claim_role_tags) & _DECISION_ROLE_TAGS)


def _is_example_only(
    entry: LedgerEntry,
    atoms: tuple[TechnicalAtom, ...],
) -> bool:
    if set(entry.claim_role_tags) & _EXAMPLE_ROLE_TAGS:
        return True
    has_example_atom = any(atom.technical_atom_kind in _EXAMPLE_ONLY_ATOM_KINDS for atom in atoms)
    return has_example_atom


def _unique_decision_points(points: tuple[DecisionPoint, ...]) -> tuple[DecisionPoint, ...]:
    seen: set[tuple[str, str]] = set()
    unique: list[DecisionPoint] = []
    for point in points:
        key = (point.entry.source_range_id, _entry_text(point.entry))
        if key in seen:
            continue
        seen.add(key)
        unique.append(point)
    return tuple(unique)


def _atoms_by_range(atoms: tuple[TechnicalAtom, ...]) -> dict[str, tuple[TechnicalAtom, ...]]:
    grouped: dict[str, list[TechnicalAtom]] = {}
    for atom in atoms:
        grouped.setdefault(atom.source_range_id, []).append(atom)
    return {source_range_id: tuple(items) for source_range_id, items in grouped.items()}


def _entry_text(entry: LedgerEntry) -> str:
    return (entry.normalized_text or entry.source_text).strip()
