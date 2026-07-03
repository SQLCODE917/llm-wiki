from __future__ import annotations

from llmwiki.domain.ledger.atoms import CodeBlockPayload, TechnicalAtom
from llmwiki.domain.ledger.collection_pages import CollectionMember, CollectionPlan
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.page_synthesis_planning import (
    collection_synthesis_plan,
    procedure_synthesis_plan,
    recipe_synthesis_plan,
    topic_synthesis_plan,
)
from llmwiki.domain.ledger.procedure_state_flow import ProcedureStateFlow
from llmwiki.domain.ledger.procedures import ProcedureGuide, ProcedureStep
from llmwiki.domain.ledger.recipe_pages import RecipePattern
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.topic_models import SourceTopic


def test_page_synthesis_plan_selection_for_topic_procedure_recipe_and_collection() -> None:
    structure = _structure(StructureNode("node", "section", "Character Creation", "r1", "x.pdf", 1))
    entry = _entry("e1", "node", "characters choose a race before rolling abilities")
    atom = _atom("a1")
    ledger = _ledger(entry, atoms=(atom,))

    topic = SourceTopic(
        "character-creation",
        "Character Creation",
        "concept",
        ("character",),
        ("e1",),
        ("a1",),
        True,
        1.0,
    )
    topic_plan = topic_synthesis_plan(
        topic,
        ledger,
        structure,
        page_id="x-character-creation",
        page_family="topic-concept",
        source_page_id="x",
        source_locator="x.pdf",
    )
    assert topic_plan.selected_support_codes >= {"ledger:e1", "atom:a1"}

    guide = ProcedureGuide(
        "x-procedure-create-character",
        "Create Character",
        "create a character",
        structure.structure_nodes[1],
        "x-character-creation",
        (
            ProcedureStep(
                1,
                "Choose Race",
                "choose",
                "choose",
                "x-character-creation",
                (entry,),
                (),
            ),
        ),
        (),
        (atom,),
        ProcedureStateFlow(1, 0, 1, 0),
    )
    assert (
        procedure_synthesis_plan(guide, source_page_id="x", source_locator="x.pdf").page_family
        == "procedure-guide"
    )

    recipe = RecipePattern(
        "x-recipe-closure",
        "Closure Recipe",
        structure.structure_nodes[1],
        "x-character-creation",
        (entry,),
        (atom,),
        ("example",),
    )
    assert (
        recipe_synthesis_plan(recipe, source_page_id="x", source_locator="x.pdf").page_family
        == "recipe-pattern"
    )

    collection = CollectionPlan(
        "x-collection-races",
        "Races",
        "x-races",
        "node",
        (CollectionMember("node", "Human", "x-human", 1, 0, ("e1",), ()),),
        ("sibling-structure", "repeated-peer-shape"),
    )
    assert (
        collection_synthesis_plan(
            collection,
            ledger,
            source_page_id="x",
            source_locator="x.pdf",
        ).page_family
        == "collection-page"
    )


def _structure(*nodes: StructureNode) -> DocumentStructure:
    root = StructureNode("root", "root", "x.pdf", "root", "x.pdf", 0)
    return DocumentStructure("root", (root, *nodes))


def _entry(entry_id: str, node_id: str, text: str) -> LedgerEntry:
    return LedgerEntry(
        entry_id,
        f"statement-{entry_id}",
        "claim",
        "usable",
        "high",
        ConfidenceBasis("test"),
        "x.pdf",
        "hash",
        f"range-{entry_id}",
        (f"ev-{entry_id}",),
        text,
        (node_id, "root"),
        normalized_text=text,
        subject="Character",
        predicate="uses",
        object_value="source support",
        polarity="positive",
        claim_force="asserted",
    )


def _atom(atom_id: str) -> TechnicalAtom:
    return TechnicalAtom(
        atom_id,
        "code-block",
        CodeBlockPayload("alpha(beta)", "parsed", "x.pdf"),
        "x.pdf",
        f"range-{atom_id}",
        (f"ev-{atom_id}",),
    )


def _ledger(*entries: LedgerEntry, atoms: tuple[TechnicalAtom, ...] = ()) -> ClaimLedger:
    atom_entries = tuple(
        LedgerEntry(
            f"entry-{atom.technical_atom_id}",
            f"statement-{atom.technical_atom_id}",
            "technical-atom",
            "usable",
            "high",
            ConfidenceBasis("test"),
            "x.pdf",
            "hash",
            atom.source_range_id,
            atom.evidence_ids,
            "",
            ("node", "root"),
            technical_atom_kind=atom.technical_atom_kind,
            technical_atom_id=atom.technical_atom_id,
        )
        for atom in atoms
    )
    return ClaimLedger(
        "ledger",
        "x.pdf",
        "hash",
        "registry",
        SourceProfile("x.pdf", 1, len(entries) + len(atom_entries), len(entries), 0, 0, 0, {}, {}),
        SourceFamilyAssignment((FamilyLabelScore("test", 1.0),), 1.0),
        (*entries, *atom_entries),
        atoms,
        (),
        (),
        (),
        (),
    )
