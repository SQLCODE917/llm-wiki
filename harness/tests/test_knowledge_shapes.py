from llmwiki.domain.ledger.atoms import CodeBlockPayload, TablePayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import build_knowledge_shape_catalog
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.recipe_pages import build_recipe_pages
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode


def test_procedure_shape_uses_typed_child_state_flow_not_domain_words() -> None:
    structure = _structure(
        StructureNode("unit", "chapter", "7.3 Lumo", "r1", "x.pdf", 1),
        StructureNode("alpha", "section", "7.3.1 Nara", "r2", "x.pdf", 2, 1, "unit"),
        StructureNode("choice", "section", "[ Cavo ]", "r5", "x.pdf", 3, 1, "unit"),
        StructureNode("beta", "section", "7.3.2 Veda", "r3", "x.pdf", 3, 1, "unit"),
        StructureNode("field", "section", "《 Pavo 》", "r6", "x.pdf", 4, 1, "unit"),
        StructureNode("gamma", "section", "7.3.3 Sola", "r4", "x.pdf", 4, 1, "unit"),
    )
    ledger = _ledger(
        _entry("a", "alpha", "The nara output is recorded."),
        _entry("x", "choice", "The cavo option is referenced.", conditional=True),
        _entry("b", "beta", "The veda output depends on a branch.", conditional=True),
        _entry("y", "field", "The pavo field is referenced.", conditional=True),
        _entry("c", "gamma", "The sola output is finalized."),
        atoms=(
            _table_atom("t1", "beta"),
            _table_atom("t2", "gamma"),
        ),
    )

    catalog = build_knowledge_shape_catalog(ledger, structure)

    procedures = catalog.candidates_of_kind("procedure")
    assert [item.structure_node_id for item in procedures] == ["unit"]
    assert procedures[0].child_structure_node_ids == ("alpha", "beta", "gamma")


def test_structural_container_heading_does_not_become_procedure() -> None:
    structure = _structure(
        StructureNode("unit", "chapter", "Chapter 7", "r1", "x.pdf", 1),
        StructureNode("alpha", "section", "7.1 Nara", "r2", "x.pdf", 2, 1, "unit"),
        StructureNode("beta", "section", "7.2 Veda", "r3", "x.pdf", 3, 1, "unit"),
    )
    ledger = _ledger(
        _entry("a", "alpha", "The nara output is recorded.", conditional=True),
        _entry("b", "beta", "The veda output is finalized."),
        atoms=(_table_atom("t1", "alpha"), _table_atom("t2", "beta")),
    )

    catalog = build_knowledge_shape_catalog(ledger, structure)

    assert catalog.candidates_of_kind("procedure") == ()


def test_recipe_shape_survives_renamed_domain_nouns() -> None:
    structure = _structure(
        StructureNode("parent", "section", "Mav", "r1", "x.pdf", 1),
        StructureNode("one", "section", "Rin", "r2", "x.pdf", 2, 1, "parent"),
        StructureNode("two", "section", "Paz", "r3", "x.pdf", 3, 1, "parent"),
        StructureNode("three", "section", "Tov", "r4", "x.pdf", 4, 1, "parent"),
    )
    ledger = _ledger(
        _entry("e1", "one", "Rin arranges a reusable form."),
        _entry("e2", "two", "Paz arranges a reusable form."),
        _entry("e3", "three", "Tov arranges a reusable form."),
        atoms=(
            _code_atom("a1", "one"),
            _code_atom("a2", "two"),
            _code_atom("a3", "three"),
        ),
    )

    catalog = build_knowledge_shape_catalog(ledger, structure)
    pages = build_recipe_pages(
        ledger,
        structure,
        source_page_id="x",
        source_locator="x.pdf",
        today="2026-07-01",
        shape_catalog=catalog,
    )

    assert {page.page_kind for page in pages} == {"recipe"}
    assert {page.page_metadata.page_family for page in pages} == {"recipe-pattern"}
    assert {page.page_id for page in pages} == {"x-recipe-rin", "x-recipe-paz", "x-recipe-tov"}
    assert all("## Technical Atoms" in page.page_body for page in pages)


def test_catalog_like_child_sequence_is_container_not_procedure() -> None:
    structure = _structure(
        StructureNode("unit", "chapter", "[ Vorn ]", "r1", "x.pdf", 1),
        StructureNode("alpha", "section", "[ Nara ]", "r2", "x.pdf", 2, 5, "unit"),
        StructureNode("beta", "section", "[ Veda ]", "r3", "x.pdf", 3, 5, "unit"),
        StructureNode("gamma", "section", "8.2.1 Sola", "r4", "x.pdf", 4, 5, "unit"),
        StructureNode("delta", "section", "8.2.2 Tavi", "r5", "x.pdf", 5, 5, "unit"),
    )
    ledger = _ledger(
        _entry("a", "alpha", "The nara output is recorded.", conditional=True),
        _entry("b", "beta", "The veda output depends on a branch.", conditional=True),
        _entry("c", "gamma", "The sola output is finalized.", conditional=True),
        _entry("d", "delta", "The tavi output is finalized.", conditional=True),
        atoms=(
            _table_atom("t1", "alpha"),
            _table_atom("t2", "beta"),
        ),
    )

    catalog = build_knowledge_shape_catalog(ledger, structure)

    assert catalog.candidates_of_kind("procedure") == ()
    containers = catalog.candidates_of_kind("section-container")
    assert [item.structure_node_id for item in containers] == ["unit"]


def test_flat_shapes_compete_before_recipe_projection() -> None:
    structure = _structure(
        StructureNode("parent", "section", "Mav", "r1", "x.pdf", 1),
        StructureNode("recipe", "section", "Reusable Rin", "r2", "x.pdf", 2, 1, "parent"),
        StructureNode("field", "section", "Nol Field", "r3", "x.pdf", 3, 1, "parent"),
        StructureNode("catalog", "section", "Paz Entry", "r4", "x.pdf", 4, 1, "parent"),
        StructureNode("fragment", "section", "Kelm?", "r5", "x.pdf", 5, 1, "parent"),
    )
    ledger = _ledger(
        _entry("e1", "recipe", "Rin arranges a reusable form."),
        _entry("e2", "field", "Nol defines a reusable field.", force="required", kind="concept"),
        _entry("e3", "catalog", "Paz has structured values."),
        _entry("e4", "fragment", "Kelm explains a fragment."),
        atoms=(
            _code_atom("c1", "recipe"),
            _table_atom("t3", "catalog"),
            _code_atom("c2", "fragment"),
        ),
    )

    catalog = build_knowledge_shape_catalog(ledger, structure)
    shape_by_node = {
        candidate.structure_node_id: candidate.shape_kind for candidate in catalog.candidates
    }
    pages = build_recipe_pages(
        ledger,
        structure,
        source_page_id="x",
        source_locator="x.pdf",
        today="2026-07-01",
        shape_catalog=catalog,
    )

    assert shape_by_node["recipe"] == "recipe"
    assert shape_by_node["field"] == "reference-field"
    assert shape_by_node["catalog"] == "catalog-entry"
    assert shape_by_node["fragment"] == "concept-explanation"
    assert [page.page_id for page in pages] == ["x-recipe-reusable-rin"]


def _structure(*nodes: StructureNode) -> DocumentStructure:
    root = StructureNode("root", "root", "x.pdf", "root", "x.pdf", 0)
    return DocumentStructure("root", (root, *nodes))


def _entry(
    entry_id: str,
    node_id: str,
    text: str,
    *,
    conditional: bool = False,
    force: str = "asserted",
    kind: str = "claim",
) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind=kind,
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="x.pdf",
        source_hash="hash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id, "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force=force,
        condition_scope="conditional" if conditional else "",
        condition_text=text if conditional else "",
    )


def _code_atom(atom_id: str, node_id: str) -> TechnicalAtom:
    _ = node_id
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="code-block",
        payload=CodeBlockPayload(
            raw_code_text="alpha(beta)",
            parse_status="parsed",
            source_locator="x.pdf",
        ),
        source_locator="x.pdf",
        source_range_id=f"range-{atom_id}",
        evidence_ids=(f"ev-{atom_id}",),
    )


def _table_atom(atom_id: str, node_id: str) -> TechnicalAtom:
    _ = node_id
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="table",
        payload=TablePayload(
            raw_table_text="Roll | Result\n1 | Alpha",
            parse_status="parsed",
            source_locator="x.pdf",
        ),
        source_locator="x.pdf",
        source_range_id=f"range-{atom_id}",
        evidence_ids=(f"ev-{atom_id}",),
    )


def _ledger(*entries: LedgerEntry, atoms: tuple[TechnicalAtom, ...] = ()) -> ClaimLedger:
    atom_entries = tuple(
        LedgerEntry(
            ledger_entry_id=f"entry-{atom.technical_atom_id}",
            source_statement_id=f"statement-{atom.technical_atom_id}",
            ledger_entry_kind="technical-atom",
            ledger_entry_status="usable",
            extraction_confidence="high",
            confidence_basis=ConfidenceBasis("test"),
            source_locator="x.pdf",
            source_hash="hash",
            source_range_id=atom.source_range_id,
            evidence_ids=atom.evidence_ids,
            source_text="",
            structure_node_ids=(_atom_node_id(atom.technical_atom_id), "root"),
            technical_atom_kind=atom.technical_atom_kind,
            technical_atom_id=atom.technical_atom_id,
        )
        for atom in atoms
    )
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="x.pdf",
        source_hash="hash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="x.pdf",
            unit_count=1,
            accepted_entry_count=len(entries) + len(atom_entries),
            claim_count=len(entries),
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={atom.technical_atom_kind: 1 for atom in atoms},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("synthetic", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=(*entries, *atom_entries),
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )


def _atom_node_id(atom_id: str) -> str:
    return {
        "a1": "one",
        "a2": "two",
        "a3": "three",
        "c1": "recipe",
        "c2": "fragment",
        "t1": "beta",
        "t2": "gamma",
        "t3": "catalog",
    }[atom_id]
