from llmwiki.domain.ledger.atoms import TablePayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.procedure_pages import build_procedure_pages
from llmwiki.domain.ledger.procedures import plan_procedure_guides
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.search import search_pages


def test_procedure_guides_surface_ordered_task_sections() -> None:
    pages = build_procedure_pages(
        _ledger(
            _entry("race", "choose-race", "First, the character's race must be chosen."),
            _entry("scores", "scores", "Next, roll dice and calculate ability scores."),
            _entry(
                "score-choice-a",
                "scores",
                "If choosing a mixed heritage, validate any skill restrictions.",
                range_id="range-score-choice",
            ),
            _entry(
                "score-choice-b",
                "scores",
                "If choosing a mixed heritage, validate any skill restrictions.",
                range_id="range-score-choice",
            ),
            _entry("skills", "skills", "Then spend experience points to increase skills."),
            _entry(
                "equipment",
                "equipment-detail",
                "Finally, purchase equipment and record money.",
            ),
            atoms=(_table_atom("background-table", "equipment"),),
        ),
        _structure(),
        source_page_id="book",
        source_locator="book.pdf",
        today="2026-06-30",
    )

    page = next(page for page in pages if page.page_id == "book-procedure-create-character")

    assert page.page_kind == "procedure"
    assert page.page_metadata.page_family == "procedure-guide"
    assert page.page_metadata.aliases == ("create-character", "character-creation")
    assert "# Create Character" in page.page_body
    assert "## Procedure Steps" in page.page_body
    assert "1. **Choose Race** (`choose`)" in page.page_body
    assert "2. **Determine Ability Scores** (`generate`)" in page.page_body
    assert "3. **Increase Skills Experience Points** (`allocate`)" in page.page_body
    assert "4. **Purchasing Other Equipment** (`acquire`)" in page.page_body
    assert page.page_body.count("If choosing a mixed heritage") == 1
    assert "## Tables And Formulas" in page.page_body
    assert "Table 1: Backgrounds" in page.page_body
    assert "[[book-section-1-4-character-creation" in page.page_body


def test_sparse_descriptive_sections_do_not_become_procedures() -> None:
    guides = plan_procedure_guides(
        _ledger(_entry("lore", "lore", "The citadel is ancient and weathered.")),
        DocumentStructure(
            "root",
            (
                StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
                StructureNode("lore", "section", "Citadel Lore", "r1", "book.pdf", 1),
            ),
        ),
        source_page_id="book",
    )

    assert guides == ()


def test_procedure_guides_can_emerge_without_action_verb_headings() -> None:
    guides = plan_procedure_guides(
        _ledger(
            _entry(
                "input",
                "input",
                "The input state is established by the source table.",
                role_tags=("procedure",),
            ),
            _entry(
                "values",
                "values",
                "The values section records the table result.",
                role_tags=("procedure",),
            ),
            _entry(
                "output",
                "output",
                "The output state is recorded after the value is resolved.",
                role_tags=("procedure",),
            ),
            atoms=(_table_atom("operation-table", "values"),),
        ),
        DocumentStructure(
            "root",
            (
                StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
                StructureNode("operation", "section", "1 Operation Matrix", "r1", "book.pdf", 1),
                StructureNode(
                    "input",
                    "section",
                    "1.1 Input State",
                    "r2",
                    "book.pdf",
                    2,
                    parent_structure_node_id="operation",
                ),
                StructureNode(
                    "values",
                    "section",
                    "1.2 Values Table",
                    "r3",
                    "book.pdf",
                    3,
                    parent_structure_node_id="operation",
                ),
                StructureNode(
                    "output",
                    "section",
                    "1.3 Output State",
                    "r4",
                    "book.pdf",
                    4,
                    parent_structure_node_id="operation",
                ),
            ),
        ),
        source_page_id="book",
    )

    assert len(guides) == 1
    assert [step.title for step in guides[0].steps] == [
        "Input State",
        "Values Table",
        "Output State",
    ]
    assert [step.action_type for step in guides[0].steps] == ["step", "step", "step"]


def test_action_verbs_alone_do_not_create_procedure_guides() -> None:
    guides = plan_procedure_guides(
        _ledger(
            _entry("choose", "choose", "Choose the listed option."),
            _entry("roll", "roll", "Roll the listed dice."),
            _entry("record", "record", "Record the listed value."),
        ),
        DocumentStructure(
            "root",
            (
                StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
                StructureNode("notes", "section", "1 Reference Notes", "r1", "book.pdf", 1),
                StructureNode(
                    "choose",
                    "section",
                    "1.1 Choose",
                    "r2",
                    "book.pdf",
                    2,
                    parent_structure_node_id="notes",
                ),
                StructureNode(
                    "roll",
                    "section",
                    "1.2 Roll",
                    "r3",
                    "book.pdf",
                    3,
                    parent_structure_node_id="notes",
                ),
                StructureNode(
                    "record",
                    "section",
                    "1.3 Record",
                    "r4",
                    "book.pdf",
                    4,
                    parent_structure_node_id="notes",
                ),
            ),
        ),
        source_page_id="book",
    )

    assert guides == ()


def test_task_search_boosts_procedure_pages() -> None:
    pages = {
        "book-character": (
            "---\npage_id: book-character\npage_kind: concept\n"
            "summary: Character concept.\n---\n\nCharacter is a general concept."
        ),
        "book-procedure-create-character": (
            "---\npage_id: book-procedure-create-character\npage_kind: procedure\n"
            "summary: Create Character.\naliases: create-character, character-creation\n---\n\n"
            "# Create Character\n\n## Procedure Steps\n\n1. Choose a race."
        ),
    }

    hits = search_pages(pages, "how do I create a character")

    assert hits[0].name == "book-procedure-create-character"


def _structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
            StructureNode("creation", "section", "1.4 Character Creation", "r1", "book.pdf", 1),
            StructureNode(
                "choose-race",
                "section",
                "1.4.1 Choose Race",
                "r2",
                "book.pdf",
                2,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "scores",
                "section",
                "1.4.2 Determine Ability Scores",
                "r3",
                "book.pdf",
                3,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "skills",
                "section",
                "1.4.3 Increase Skills",
                "r4",
                "book.pdf",
                4,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "skill-detail",
                "section",
                "1.4.3 Increase Skills / Experience Points",
                "r4b",
                "book.pdf",
                5,
                parent_structure_node_id="skills",
            ),
            StructureNode(
                "equipment",
                "section",
                "1.4.4 Purchasing Other",
                "r5",
                "book.pdf",
                6,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "equipment-detail",
                "section",
                "Equipment",
                "r5b",
                "book.pdf",
                7,
                parent_structure_node_id="creation",
            ),
        ),
    )


def _entry(
    entry_id: str,
    node_id: str,
    text: str,
    *,
    range_id: str | None = None,
    role_tags: tuple[str, ...] = (),
) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="book.pdf",
        source_hash="sourcehash",
        source_range_id=range_id or f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id, "creation", "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
        claim_role_tags=role_tags,
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


def _ledger(*entries: LedgerEntry, atoms: tuple[TechnicalAtom, ...] = ()) -> ClaimLedger:
    atom_entries = tuple(
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
            structure_node_ids=(atom.source_range_id.removeprefix("range-"), "creation", "root"),
            technical_atom_kind=atom.technical_atom_kind,
            technical_atom_id=atom.technical_atom_id,
        )
        for atom in atoms
    )
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="book.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="book.pdf",
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
            labels=(FamilyLabelScore("general-prose", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=(*entries, *atom_entries),
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
