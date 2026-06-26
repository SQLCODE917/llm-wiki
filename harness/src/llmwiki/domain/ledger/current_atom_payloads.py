"""Map current TechnicalAtom records into ledger technical-atom payloads."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import (
    AtomPayload,
    CodeBlockPayload,
    FormulaPayload,
    ProcedurePayload,
    RulePayload,
    TablePayload,
    WorkedExamplePayload,
)
from llmwiki.domain.technical_atoms import TechnicalAtom, TechnicalAtomCatalog


def ledger_atom_kind(kind: str) -> str:
    return {
        "code": "code-block",
        "formula": "formula",
        "procedure": "procedure",
        "table": "table",
        "table-row": "table",
        "requirement": "rule",
        "exception": "rule",
        "worked-example": "worked-example",
    }[kind]


def ledger_atom_payload(catalog: TechnicalAtomCatalog, atom: TechnicalAtom) -> AtomPayload:
    fields = dict(atom.normalized_fields)
    if atom.atom_kind == "code":
        return CodeBlockPayload(
            raw_code_text=atom.technical_payload,
            parse_status="parsed",
            source_locator=atom.source_locator,
            language_tag=fields.get("language", ""),
            language_detected=bool(fields.get("language")),
            language_confidence="medium" if fields.get("language") else "",
            line_count=atom.technical_payload.count("\n") + 1,
        )
    if atom.atom_kind == "formula":
        return FormulaPayload(
            raw_formula_text=atom.technical_payload,
            formula_subtype=_formula_subtype(atom.technical_payload),
            formula_surface_form="equation" if "=" in atom.technical_payload else "prose",
            source_locator=atom.source_locator,
            parse_status="parsed",
        )
    if atom.atom_kind == "procedure":
        return ProcedurePayload(
            procedure_text=atom.technical_payload,
            source_locator=atom.source_locator,
            steps=_procedure_steps(fields.get("ordered_steps", atom.technical_payload)),
        )
    if atom.atom_kind in ("requirement", "exception"):
        return RulePayload(
            rule_text=atom.technical_payload,
            rule_force="required" if atom.atom_kind == "requirement" else "asserted-constraint",
            source_locator=atom.source_locator,
        )
    if atom.atom_kind == "worked-example":
        return WorkedExamplePayload(
            example_text=atom.technical_payload,
            source_locator=atom.source_locator,
        )
    table = catalog.table_for_atom(atom)
    return TablePayload(
        raw_table_text=table.markdown if table is not None else atom.technical_payload,
        parse_status="parsed" if table is not None else "unparsed",
        source_locator=atom.source_locator,
        caption=atom.title,
    )


def _formula_subtype(text: str) -> str:
    return "symbolic-formula" if re.search(r"[=+\-*/×÷∑√]", text) else "procedural-formula"


def _procedure_steps(text: str) -> tuple[str, ...]:
    steps = tuple(line.strip() for line in text.splitlines() if line.strip())
    return steps or (text.strip(),)
