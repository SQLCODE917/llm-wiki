from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.section_navigation import section_page_id
from llmwiki.domain.ledger.section_pages import build_section_pages
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.topic_models import SourceTopic


def test_section_pages_roll_up_descendants_and_link_repeated_topic_contexts() -> None:
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode("chapter", "chapter", "1.4 Character Creation", "r1", "source.pdf", 1),
            StructureNode(
                "combat-sheet",
                "section",
                "Filling out the Character Sheet",
                "r2",
                "source.pdf",
                2,
                parent_structure_node_id="chapter",
            ),
            StructureNode(
                "magic-sheet",
                "section",
                "Filling out the Character Sheet",
                "r3",
                "source.pdf",
                3,
                parent_structure_node_id="chapter",
            ),
        ),
    )
    ledger = _ledger(
        _entry("entry-combat", "combat-sheet", "Write combat totals on the sheet."),
        _entry("entry-magic", "magic-sheet", "Write magic fields on the sheet."),
    )
    pages = build_section_pages(
        ledger,
        structure,
        source_page_id="source",
        source_locator="source.pdf",
        today="2026-06-27",
        topics=(
            SourceTopic(
                topic_key="filling-character-sheet",
                label="Filling out the Character Sheet",
                page_kind="concept",
                match_terms=("filling", "character", "sheet"),
                entry_ids=("entry-combat", "entry-magic"),
                atom_ids=(),
                from_heading=True,
                salience=5.0,
            ),
        ),
    )

    by_id = {page.page_id: page.page_body for page in pages}
    chapter = structure.node("chapter")
    combat = structure.node("combat-sheet")
    magic = structure.node("magic-sheet")
    assert chapter is not None
    assert combat is not None
    assert magic is not None
    chapter_id = section_page_id("source", structure, chapter)
    combat_id = section_page_id("source", structure, combat)
    magic_id = section_page_id("source", structure, magic)

    assert "# 1.4 Character Creation" in by_id[chapter_id]
    assert "## Statements by subsection" in by_id[chapter_id]
    assert "### 1.4 Character Creation / Filling out the Character Sheet" in by_id[chapter_id]
    assert "Write combat totals on the sheet." in by_id[chapter_id]
    assert "Write magic fields on the sheet." in by_id[chapter_id]

    assert "# 1.4 Character Creation / Filling out the Character Sheet" in by_id[combat_id]
    assert f"[[{chapter_id}]] - broader source section" in by_id[combat_id]
    assert "[[source-filling-character-sheet]] - topic hub" in by_id[combat_id]
    assert f"[[{magic_id}]] - same source heading" in by_id[combat_id]


def _entry(entry_id: str, node_id: str, text: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id, "chapter", "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _ledger(*entries: LedgerEntry) -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="source.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="source.pdf",
            unit_count=1,
            accepted_entry_count=len(entries),
            claim_count=len(entries),
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("general-prose", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=entries,
        technical_atoms=(),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
