from llmwiki.domain.ledger.atom_context import TechnicalAtomContext
from llmwiki.domain.ledger.atoms import FormulaPayload, TablePayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.procedures import plan_procedure_guides
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode


def test_ordered_reference_catalog_with_tables_is_not_a_procedure() -> None:
    guides = plan_procedure_guides(
        _ledger(
            _entry("normal", "normal", "The normal equipment category applies when needed."),
            _entry("special", "special", "The special equipment category records exceptions."),
            _entry("other", "other", "Characters may obtain other equipment later."),
            atoms=(
                _table_atom("normal-table", "normal"),
                _formula_atom("special-formula", "special"),
            ),
        ),
        _structure(
            (
                _section("catalog", "1 Equipment Catalog", 1),
                _section("normal", "1.1 Normal Equipment", 2, parent="catalog"),
                _section("special", "1.2 Special Equipment", 3, parent="catalog"),
                _section("other", "1.3 Other Equipment", 4, parent="catalog"),
            )
        ),
        source_page_id="book",
    )

    assert guides == ()


def test_formula_sequence_can_depend_on_prior_step_output_without_action_headings() -> None:
    guides = plan_procedure_guides(
        _ledger(
            _entry("input", "input", "The input value is established by the source formula."),
            _entry("result", "result", "The derived result uses the input value."),
            atoms=(
                _formula_atom("input-formula", "input"),
                _formula_atom("result-formula", "result"),
            ),
        ),
        _structure(
            (
                _section("calculation", "1 Calculation Matrix", 1),
                _section("input", "1.1 Input Value", 2, parent="calculation"),
                _section("result", "1.2 Derived Result", 3, parent="calculation"),
            )
        ),
        source_page_id="book",
    )

    assert len(guides) == 1
    assert guides[0].state_flow.prior_output_dependency_count == 1


def test_claim_output_dependency_can_confirm_taxonomy_headings() -> None:
    guides = plan_procedure_guides(
        _ledger(
            _entry("first", "first", "Both sides roll dice to resolve the first check."),
            _entry("second", "second", "Determine the second result."),
            atoms=(
                _formula_atom("first-formula", "first"),
                _formula_atom(
                    "second-formula",
                    "second",
                    raw_formula_text="if first check succeeds, second result = first result + 1",
                ),
            ),
            atom_entries=False,
            atom_contexts=(
                _atom_context("first-formula", "first"),
                _atom_context("second-formula", "second"),
            ),
        ),
        _operation_structure(),
        source_page_id="book",
    )

    assert len(guides) == 1
    assert guides[0].state_flow.prior_output_dependency_count == 1


def test_source_order_places_atoms_under_nearest_section_heading() -> None:
    guides = plan_procedure_guides(
        _ledger(
            _entry("first", "first", "Both sides roll dice to resolve the first check."),
            _entry("second", "second", "Determine the second result."),
            atoms=(
                _formula_atom("first-formula", "first", source_range_id="source-range-test-0011"),
                _formula_atom(
                    "second-formula",
                    "second",
                    raw_formula_text="if first check succeeds, second result = first result + 1",
                    source_range_id="source-range-test-0021",
                ),
            ),
            atom_entries=False,
        ),
        _operation_structure(first_order=10, second_order=20),
        source_page_id="book",
    )

    assert len(guides) == 1
    assert [len(step.technical_atoms) for step in guides[0].steps] == [1, 1]
    assert guides[0].state_flow.prior_output_dependency_count == 1


def _operation_structure(*, first_order: int = 2, second_order: int = 3) -> DocumentStructure:
    return _structure(
        (
            _section("operation", "1 Operation Resolution", 1),
            _section("first", "1.1 First Check", first_order, parent="operation"),
            _section("second", "1.2 Second Result", second_order, parent="operation"),
        )
    )


def _section(node_id: str, heading: str, source_order: int, *, parent: str = "") -> StructureNode:
    return StructureNode(
        node_id,
        "section",
        heading,
        f"range-{node_id}",
        "book.pdf",
        source_order,
        parent_structure_node_id=parent,
    )


def _structure(nodes: tuple[StructureNode, ...]) -> DocumentStructure:
    return DocumentStructure(
        "root",
        (StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0), *nodes),
    )


def _entry(entry_id: str, node_id: str, text: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="book.pdf",
        source_hash="sourcehash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id, "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _table_atom(atom_id: str, node_id: str) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="table",
        payload=TablePayload(
            raw_table_text="Table 1: Backgrounds\nRoll | Result",
            parse_status="parsed",
            source_locator="book.pdf",
        ),
        source_locator="book.pdf",
        source_range_id=f"range-{node_id}",
        evidence_ids=("ev-table",),
    )


def _formula_atom(
    atom_id: str,
    node_id: str,
    *,
    raw_formula_text: str = "result = input + 1",
    source_range_id: str | None = None,
) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="formula",
        payload=FormulaPayload(
            raw_formula_text=raw_formula_text,
            formula_subtype="equation",
            formula_surface_form=raw_formula_text,
            source_locator="book.pdf",
        ),
        source_locator="book.pdf",
        source_range_id=source_range_id or f"range-{node_id}",
        evidence_ids=("ev-formula",),
    )


def _atom_context(atom_id: str, entry_id: str) -> TechnicalAtomContext:
    return TechnicalAtomContext(
        technical_atom_context_id=f"context-{atom_id}",
        technical_atom_id=atom_id,
        context_role="introduced-by-source-prose",
        context_text="test context",
        context_entry_ids=(entry_id,),
        context_source_range_ids=(f"range-{entry_id}",),
        demonstrated_concept_keys=(),
        evidence_ids=("ev-context",),
        confidence_basis=ConfidenceBasis("test"),
    )


def _ledger(
    *entries: LedgerEntry,
    atoms: tuple[TechnicalAtom, ...] = (),
    atom_entries: bool = True,
    atom_contexts: tuple[TechnicalAtomContext, ...] = (),
) -> ClaimLedger:
    atom_ledger_entries = (
        tuple(
            LedgerEntry(
                ledger_entry_id=f"entry-{atom.technical_atom_id}",
                source_statement_id=f"statement-{atom.technical_atom_id}",
                ledger_entry_kind="technical-atom",
                ledger_entry_status="usable",
                extraction_confidence="high",
                confidence_basis=ConfidenceBasis("test"),
                source_locator="book.pdf",
                source_hash="sourcehash",
                source_range_id=atom.source_range_id,
                evidence_ids=atom.evidence_ids,
                source_text="",
                structure_node_ids=(atom.source_range_id.removeprefix("range-"), "root"),
                technical_atom_kind=atom.technical_atom_kind,
                technical_atom_id=atom.technical_atom_id,
            )
            for atom in atoms
        )
        if atom_entries
        else ()
    )
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="book.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registryhash",
        source_profile=SourceProfile(
            "book.pdf",
            len(entries),
            len(entries) + len(atom_ledger_entries),
            len(entries),
            0,
            0,
            0,
            {},
            {},
        ),
        source_family_assignment=SourceFamilyAssignment((FamilyLabelScore("technical", 1.0),), 1.0),
        entries=(*entries, *atom_ledger_entries),
        technical_atoms=atoms,
        technical_atom_contexts=atom_contexts,
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
