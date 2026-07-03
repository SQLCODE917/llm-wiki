"""Candidate scoring rules for source-grounded procedure guides."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.procedure_language import (
    action_type,
    clean_title,
    has_condition,
    has_task_noun,
)
from llmwiki.domain.ledger.structure import StructureNode

_STRUCTURAL_CONTAINER_PREFIX = re.compile(
    r"^(chapter|part|appendix|volume|book)\b(?:\s+[ivxlcdm\d]+)?\s*:?\s*(.*)$",
    re.IGNORECASE,
)


def procedure_candidate_score(
    *,
    heading_text: str,
    entry_texts: tuple[str, ...],
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    step_action_types: tuple[str, ...],
    step_count: int,
) -> int:
    text = f"{heading_text} {' '.join(entry_texts[:12])}"
    action_types = {action for action in step_action_types if action != "step"}
    has_task = has_task_noun(heading_text)
    has_role = has_procedure_role(entries)
    has_atoms = has_procedure_atoms(atoms)
    has_decisions = has_condition(text)
    score = step_count
    if step_count >= 2:
        score += 2
    if has_task:
        score += 1
    if len(action_types) >= 3 and (has_task or has_role or has_atoms or has_decisions):
        score += 1
    if has_role:
        score += 2
    if has_atoms:
        score += 2
    if has_decisions:
        score += 1
    return score


def has_step_evidence(entries: tuple[LedgerEntry, ...], atoms: tuple[TechnicalAtom, ...]) -> bool:
    return bool(entries or has_procedure_atoms(atoms))


def has_procedure_role(entries: tuple[LedgerEntry, ...]) -> bool:
    return any(
        "procedure" in entry.claim_role_tags or "method" in entry.claim_role_tags
        for entry in entries
    )


def has_procedure_atoms(atoms: tuple[TechnicalAtom, ...]) -> bool:
    return any(atom.technical_atom_kind in {"table", "formula", "procedure"} for atom in atoms)


def is_unanchored_structural_container(
    node: StructureNode,
    direct_entries: tuple[LedgerEntry, ...],
    direct_atoms: tuple[TechnicalAtom, ...],
) -> bool:
    title = clean_title(node.heading_text)
    match = _STRUCTURAL_CONTAINER_PREFIX.match(title)
    if match is None:
        return False
    remainder = match.group(2).strip()
    if remainder and (has_task_noun(remainder) or action_type(remainder)):
        return False
    return not _has_local_procedure_anchor(direct_entries, direct_atoms)


def _has_local_procedure_anchor(
    entries: tuple[LedgerEntry, ...], atoms: tuple[TechnicalAtom, ...]
) -> bool:
    return has_procedure_role(entries) or any(
        atom.technical_atom_kind == "procedure" for atom in atoms
    )
