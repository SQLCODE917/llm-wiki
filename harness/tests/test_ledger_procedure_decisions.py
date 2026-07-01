from llmwiki.domain.ledger.atoms import TechnicalAtom, WorkedExamplePayload
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.procedure_pages import render_procedure_page
from llmwiki.domain.ledger.procedures import plan_procedure_guides
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode


def test_example_evaluation_with_except_is_not_a_decision_point() -> None:
    guide = _single_guide(
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry(
            "example",
            "choose",
            "This sample output is average except for one excellent attribute.",
            role_tags=("quantitative", "identity"),
            range_id="range-example",
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
        atoms=(_worked_example_atom("range-example"),),
    )

    assert all("sample output" not in point.outcome_text for point in guide.decision_points)
    assert "## Decision Points" not in render_procedure_page(guide, "book")


def test_conditional_branch_becomes_typed_decision_point() -> None:
    guide = _single_guide(
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry(
            "branch",
            "choose",
            "If the input value is unavailable, choose a fallback value.",
            condition_scope="conditional",
            condition_text="If the input value is unavailable, choose a fallback value.",
            role_tags=("requirement",),
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
    )

    assert [point.decision_kind for point in guide.decision_points] == ["branch"]
    assert "If the input value is unavailable" in render_procedure_page(guide, "book")


def test_conditional_worked_example_is_not_a_decision_point() -> None:
    guide = _single_guide(
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry(
            "example",
            "choose",
            "If the sample roll is high, this sample output is unusually strong.",
            condition_scope="conditional",
            condition_text="If the sample roll is high, this sample output is unusually strong.",
            role_tags=("worked-example", "quantitative"),
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
    )

    assert guide.decision_points == ()


def _single_guide(*entries: LedgerEntry, atoms: tuple[TechnicalAtom, ...] = ()):
    guides = plan_procedure_guides(
        _ledger(*entries, atoms=atoms), _structure(), source_page_id="book"
    )
    assert len(guides) == 1
    return guides[0]


def _structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
            StructureNode("workflow", "section", "1 Create Output", "r1", "book.pdf", 1),
            StructureNode(
                "choose",
                "section",
                "1.1 Choose Input",
                "r2",
                "book.pdf",
                2,
                parent_structure_node_id="workflow",
            ),
            StructureNode(
                "record",
                "section",
                "1.2 Record Output",
                "r3",
                "book.pdf",
                3,
                parent_structure_node_id="workflow",
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
    condition_scope: str = "unconditional",
    condition_text: str = "",
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
        structure_node_ids=(node_id, "workflow", "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
        condition_scope=condition_scope,
        condition_text=condition_text,
        claim_role_tags=role_tags,
    )


def _worked_example_atom(source_range_id: str) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id="example-atom",
        technical_atom_kind="worked-example",
        payload=WorkedExamplePayload(
            example_text="This sample output is average except for one excellent attribute.",
            source_locator="book.pdf",
        ),
        source_locator="book.pdf",
        source_range_id=source_range_id,
        evidence_ids=("ev-example",),
    )


def _ledger(*entries: LedgerEntry, atoms: tuple[TechnicalAtom, ...] = ()) -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="book.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registryhash",
        source_profile=SourceProfile(
            "book.pdf", len(entries), len(entries), len(entries), 0, 0, 0, {}, {}
        ),
        source_family_assignment=SourceFamilyAssignment((FamilyLabelScore("technical", 1.0),), 1.0),
        entries=entries,
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
