"""Typed evidence roles used by knowledge-shape classification."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.structure import StructureNode

CODE_ATOM_KINDS = frozenset({"code-block"})
EXAMPLE_ATOM_KINDS = frozenset({"code-block", "worked-example"})
STRUCTURED_STATE_ATOM_KINDS = frozenset({"table", "formula", "procedure", "rule"})


@dataclass(frozen=True)
class UnitEvidence:
    node: StructureNode
    entries: tuple[LedgerEntry, ...]
    atoms: tuple[TechnicalAtom, ...]
    roles: frozenset[str]

    @property
    def has_evidence(self) -> bool:
        return bool(self.entries or self.atoms)


def roles_for_evidence(
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    child_units: tuple[UnitEvidence, ...],
) -> tuple[str, ...]:
    roles: list[str] = []
    for entry in entries:
        roles.extend(entry_roles(entry))
    for atom in atoms:
        roles.extend(atom_roles(atom))
    for child in child_units:
        roles.extend(child.roles)
    return tuple(dict.fromkeys(roles))


def unit_transforms_state(unit: UnitEvidence) -> bool:
    return bool(unit.roles & {"structured-state", "constraint", "decision", "procedure"})


def unit_has_branch(unit: UnitEvidence) -> bool:
    return bool(unit.roles & {"decision", "constraint", "structured-state"})


def unit_has_recipe_shape(unit: UnitEvidence) -> bool:
    return bool(unit.entries and code_atoms(unit.atoms))


def unit_has_reference_field_shape(unit: UnitEvidence) -> bool:
    if code_atoms(unit.atoms) or not unit.entries:
        return False
    return "definition" in unit.roles and bool(unit.roles & {"constraint", "decision", "example"})


def unit_has_catalog_entry_shape(unit: UnitEvidence) -> bool:
    if code_atoms(unit.atoms):
        return False
    return bool(structured_state_atoms(unit.atoms))


def unit_has_concept_explanation_shape(unit: UnitEvidence) -> bool:
    if not unit.entries or code_atoms(unit.atoms) or structured_state_atoms(unit.atoms):
        return False
    return bool(unit.roles & {"definition", "explanation", "example"})


def code_atoms(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    return tuple(atom for atom in atoms if atom.technical_atom_kind in CODE_ATOM_KINDS)


def example_atoms(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    return tuple(atom for atom in atoms if atom.technical_atom_kind in EXAMPLE_ATOM_KINDS)


def structured_state_atoms(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    return tuple(atom for atom in atoms if atom.technical_atom_kind in STRUCTURED_STATE_ATOM_KINDS)


def entry_roles(entry: LedgerEntry) -> tuple[str, ...]:
    roles: list[str] = []
    if entry.condition_scope or entry.condition_text or entry.exception_text:
        roles.append("decision")
    if entry.claim_force in {"required", "forbidden", "permitted"}:
        roles.append("constraint")
    if entry.ledger_entry_kind == "concept" or "definition" in entry.claim_role_tags:
        roles.append("definition")
    if "example" in entry.claim_role_tags:
        roles.append("example")
    if "procedure" in entry.claim_role_tags or "method" in entry.claim_role_tags:
        roles.append("procedure")
    if not roles and entry.ledger_entry_kind in {"claim", "event", "relationship"}:
        roles.append("explanation")
    return tuple(roles)


def atom_roles(atom: TechnicalAtom) -> tuple[str, ...]:
    if atom.technical_atom_kind in EXAMPLE_ATOM_KINDS:
        return ("example",)
    if atom.technical_atom_kind in STRUCTURED_STATE_ATOM_KINDS:
        return ("structured-state",)
    return ("technical-atom",)
