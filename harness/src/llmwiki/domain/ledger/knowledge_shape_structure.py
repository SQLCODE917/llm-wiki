"""Source-structure predicates for knowledge-shape classification."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.knowledge_shape_evidence import (
    UnitEvidence,
    unit_has_catalog_entry_shape,
    unit_has_concept_explanation_shape,
    unit_has_recipe_shape,
    unit_has_reference_field_shape,
)
from llmwiki.domain.ledger.procedure_language import action_type, clean_title, has_task_noun
from llmwiki.domain.ledger.structure import StructureNode

_STRUCTURAL_CONTAINER_PREFIX = re.compile(
    r"^(chapter|part|appendix|volume|book)\b(?:\s+[ivxlcdm\d]+)?\s*:?\s*(.*)$",
    re.IGNORECASE,
)
_STRUCTURED_STEP_NUMBER = re.compile(r"^\s*\d+(?:\.\d+)+\b")
_SECTION_NUMBER = re.compile(r"^\s*(\d+(?:\.\d+)*)\b")
_BRACKETED_HEADING = re.compile(r"^\s*[\[【《].+[]】》]\s*")
_HEADING_SENTENCE_BOUNDARY = re.compile(r"[.!?]\s+\S")


def is_unanchored_container(node: StructureNode, direct_unit: UnitEvidence) -> bool:
    title = clean_title(node.heading_text)
    match = _STRUCTURAL_CONTAINER_PREFIX.match(title)
    if match is None:
        return False
    remainder = match.group(2).strip()
    if remainder and (has_task_noun(remainder) or action_type(remainder)):
        return False
    return "procedure" not in direct_unit.roles and not any(
        atom.technical_atom_kind == "procedure" for atom in direct_unit.atoms
    )


def has_structured_child_sequence(child_units: tuple[UnitEvidence, ...]) -> bool:
    return bool(procedure_child_units(None, child_units))


def procedure_child_units(
    node: StructureNode | None, child_units: tuple[UnitEvidence, ...]
) -> tuple[UnitEvidence, ...]:
    numbered = tuple(
        unit for unit in child_units if _STRUCTURED_STEP_NUMBER.match(unit.node.heading_text)
    )
    if node is not None and (parent_number := _section_number(node.heading_text)):
        prefixed = tuple(
            unit
            for unit in numbered
            if (child_number := _section_number(unit.node.heading_text))
            and child_number.startswith(f"{parent_number}.")
        )
        return prefixed if len(prefixed) >= 2 else ()
    if len(numbered) >= 2 and len(numbered) >= len(child_units) / 2:
        return numbered
    return ()


def has_catalog_child_sequence(
    node: StructureNode, child_units: tuple[UnitEvidence, ...]
) -> bool:
    bracketed = tuple(
        unit for unit in child_units if _BRACKETED_HEADING.match(unit.node.heading_text)
    )
    if _BRACKETED_HEADING.match(node.heading_text) and bracketed:
        return True
    return len(bracketed) >= len(child_units) / 2


def leaf_shape_kind(node: StructureNode, unit: UnitEvidence) -> str | None:
    if unit_has_catalog_entry_shape(unit):
        return "catalog-entry"
    if unit_has_reference_field_shape(unit):
        return "reference-field"
    if has_fragment_heading(node):
        return "concept-explanation"
    if unit_has_recipe_shape(unit):
        return "recipe"
    if unit_has_concept_explanation_shape(unit):
        return "concept-explanation"
    return None


def has_fragment_heading(node: StructureNode) -> bool:
    heading = " ".join(node.heading_text.split()).strip()
    if not heading:
        return True
    if heading.endswith(":") or heading.endswith("?"):
        return True
    return bool(_HEADING_SENTENCE_BOUNDARY.search(heading))


def _section_number(heading_text: str) -> str:
    match = _SECTION_NUMBER.match(heading_text)
    return match.group(1) if match is not None else ""
