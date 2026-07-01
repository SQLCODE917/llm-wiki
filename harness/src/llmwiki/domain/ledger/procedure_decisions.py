"""Typed decision-point evidence for procedure guides."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry, SourceStatement
from llmwiki.domain.ledger.procedure_language import action_type

_EXAMPLE_ONLY_ATOM_KINDS = frozenset({"worked-example"})
_EXAMPLE_ROLE_TAGS = frozenset({"worked-example", "example"})
_DECISION_ROLE_TAGS = frozenset({"procedure", "method", "requirement", "limitation", "constraint"})
_DEICTIC_START = re.compile(r"^\s*(this|that|these|those)\b", re.IGNORECASE)
_BARE_DEICTIC = re.compile(r"\b(this|that|these|those)\b(?=\s*(?:[,.;:]|$))", re.IGNORECASE)
_FIRST_PERSON = re.compile(r"\b(i|me|my|mine|we|us|our|ours)\b", re.IGNORECASE)
_UNNAMED_BRANCH_ACTOR = re.compile(r"\b(if|when|whenever)\s+(he|she|they)(?:'|\b)", re.IGNORECASE)
_CONTEXT_POINTER = re.compile(r"\b(here|there)\b", re.IGNORECASE)
_PRECEDING_CONTEXT_CUE = re.compile(
    r"\b(since|therefore|thus|hence|also|however|of these|on the other hand)\b",
    re.IGNORECASE,
)
_PROPOSITIONAL_VERB = re.compile(
    r"\b(is|are|was|were|be|been|being|has|have|had|do|does|did|requires?|provides?"
    r"|uses?|makes?|gives?|allows?|causes?|means|consists?|contains?|includes?)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ProjectionCompleteness:
    complete: bool
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class DecisionEvidenceBlock:
    source_statement_id: str
    source_range_id: str
    source_range_ids: tuple[str, ...]
    source_text: str


@dataclass(frozen=True)
class DecisionPoint:
    entry: LedgerEntry
    decision_kind: str
    condition_text: str
    outcome_text: str
    supporting_atom_ids: tuple[str, ...]
    projection_completeness: ProjectionCompleteness
    evidence_block: DecisionEvidenceBlock


def plan_decision_points(
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    source_statements: tuple[SourceStatement, ...] = (),
) -> tuple[DecisionPoint, ...]:
    atoms_by_range = _atoms_by_range(atoms)
    source_text_by_statement = {
        statement.source_statement_id: statement.source_text for statement in source_statements
    }
    source_text_by_range = {
        statement.source_range_id: statement.source_text for statement in source_statements
    }
    previous_entry_by_statement = _previous_entry_by_statement(entries)
    points = tuple(
        point
        for entry in entries
        if (
            point := _decision_point(
                entry,
                atoms_by_range.get(entry.source_range_id, ()),
                source_text_by_statement.get(entry.source_statement_id, ""),
                source_text_by_range,
                previous_entry_by_statement.get(entry.source_statement_id),
            )
        )
        is not None
    )
    return _unique_decision_points(points)


def _decision_point(
    entry: LedgerEntry,
    atoms: tuple[TechnicalAtom, ...],
    source_statement_text: str,
    source_text_by_range: dict[str, str],
    previous_entry: LedgerEntry | None,
) -> DecisionPoint | None:
    if not entry.is_claim_like or not entry.is_usable:
        return None
    condition = entry.condition_text.strip()
    if not _is_decision_entry(entry):
        return None
    if _is_example_only(entry, atoms):
        return None
    completeness = _projection_completeness(entry)
    if not completeness.complete:
        return None
    return DecisionPoint(
        entry=entry,
        decision_kind="branch",
        condition_text=condition or _entry_text(entry),
        outcome_text=entry.object_value.strip() or _entry_text(entry),
        supporting_atom_ids=(),
        projection_completeness=completeness,
        evidence_block=_evidence_block(
            entry,
            source_statement_text,
            source_text_by_range,
            previous_entry,
        ),
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


def _projection_completeness(entry: LedgerEntry) -> ProjectionCompleteness:
    text = _entry_text(entry)
    reasons: list[str] = []
    if _has_unresolved_reference(text):
        reasons.append("unresolved-reference")
    if reason := _condition_shape_reason(text, entry.condition_text):
        reasons.append(reason)
    return ProjectionCompleteness(complete=not reasons, reasons=tuple(reasons))


def _has_unresolved_reference(text: str) -> bool:
    return bool(
        _DEICTIC_START.search(text)
        or _BARE_DEICTIC.search(text)
        or _FIRST_PERSON.search(text)
        or _UNNAMED_BRANCH_ACTOR.search(text)
        or _CONTEXT_POINTER.search(text)
    )


def _condition_shape_reason(text: str, condition_text: str) -> str:
    prefix = _prefix_before_condition(text, condition_text)
    if prefix is None:
        return "condition-not-grounded-in-entry"
    if not prefix:
        return ""
    if action_type(prefix):
        return ""
    if _PROPOSITIONAL_VERB.search(prefix):
        return "embedded-condition-without-actionable-outcome"
    return ""


def _prefix_before_condition(text: str, condition_text: str) -> str | None:
    condition = _normalized(condition_text)
    if not condition:
        return ""
    normalized_text = _normalized(text)
    index = normalized_text.find(condition)
    if index < 0:
        return None
    return normalized_text[:index].strip(" ,;:")


def _normalized(text: str) -> str:
    return " ".join(text.casefold().split())


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


def _evidence_block(
    entry: LedgerEntry,
    source_statement_text: str,
    source_text_by_range: dict[str, str],
    previous_entry: LedgerEntry | None,
) -> DecisionEvidenceBlock:
    current_text = source_statement_text.strip() or _entry_text(entry)
    range_ids: tuple[str, ...] = (entry.source_range_id,)
    if _needs_preceding_context(current_text) and previous_entry is not None:
        previous_text = source_text_by_range.get(previous_entry.source_range_id, "").strip()
        if previous_text and previous_text not in current_text:
            current_text = f"{previous_text} {current_text}"
            range_ids = (previous_entry.source_range_id, entry.source_range_id)
    return DecisionEvidenceBlock(
        source_statement_id=entry.source_statement_id,
        source_range_id=entry.source_range_id,
        source_range_ids=range_ids,
        source_text=current_text,
    )


def _needs_preceding_context(text: str) -> bool:
    return bool(_PRECEDING_CONTEXT_CUE.search(text))


def _previous_entry_by_statement(entries: tuple[LedgerEntry, ...]) -> dict[str, LedgerEntry]:
    previous_by_statement: dict[str, LedgerEntry] = {}
    previous_by_node: dict[str, LedgerEntry] = {}
    for entry in sorted(entries, key=_entry_source_order):
        node_id = entry.structure_node_ids[0] if entry.structure_node_ids else ""
        if node_id and entry.source_statement_id not in previous_by_statement:
            previous = previous_by_node.get(node_id)
            if previous is not None:
                previous_by_statement[entry.source_statement_id] = previous
        if node_id:
            previous_by_node[node_id] = entry
    return previous_by_statement


def _entry_source_order(entry: LedgerEntry) -> int:
    match = re.search(r"-(\d+)$", entry.source_range_id)
    return int(match.group(1)) if match is not None else 0


def _atoms_by_range(atoms: tuple[TechnicalAtom, ...]) -> dict[str, tuple[TechnicalAtom, ...]]:
    grouped: dict[str, list[TechnicalAtom]] = {}
    for atom in atoms:
        grouped.setdefault(atom.source_range_id, []).append(atom)
    return {source_range_id: tuple(items) for source_range_id, items in grouped.items()}


def _entry_text(entry: LedgerEntry) -> str:
    return (entry.normalized_text or entry.source_text).strip()
