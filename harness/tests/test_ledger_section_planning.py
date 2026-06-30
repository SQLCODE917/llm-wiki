from llmwiki.domain.ledger import section_planning
from llmwiki.domain.ledger.common import ConfidenceBasis, SpatialScope
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.section_planning import build_section_grounded_plan
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode


def test_section_planning_builds_table_identity_once(monkeypatch) -> None:
    calls = 0

    def fake_table_identity_names_by_atom_id(
        ledger: ClaimLedger, structure: DocumentStructure
    ) -> dict[str, tuple[str, ...]]:
        nonlocal calls
        calls += 1
        return {}

    monkeypatch.setattr(
        section_planning,
        "table_identity_names_by_atom_id",
        fake_table_identity_names_by_atom_id,
    )

    plan = build_section_grounded_plan(_ledger(), _structure())

    assert calls == 1
    assert len(plan.page_targets) == 2


def test_section_planning_rejects_standalone_unresolved_context_pointer() -> None:
    structure = DocumentStructure(
        root_node_id="node-root",
        structure_nodes=(
            StructureNode("node-root", "root", "rules.pdf", "range-root", "rules.pdf", 0),
            StructureNode(
                "node-summary",
                "section",
                "Acquiring Rune Master Skills",
                "range-summary",
                "rules.pdf",
                1,
            ),
        ),
    )
    ledger = _ledger(
        _context_pointer_entry(
            "entry-summary",
            "node-summary",
            "Here is a summary of how to acquire each rune master skill.",
        )
    )

    plan = build_section_grounded_plan(ledger, structure)

    assert plan.page_targets == ()


def test_section_planning_keeps_context_pointer_when_substantive_evidence_exists() -> None:
    structure = DocumentStructure(
        root_node_id="node-root",
        structure_nodes=(
            StructureNode("node-root", "root", "rules.pdf", "range-root", "rules.pdf", 0),
            StructureNode(
                "node-summary",
                "section",
                "Acquiring Rune Master Skills",
                "range-summary",
                "rules.pdf",
                1,
            ),
            StructureNode(
                "node-sorcerer",
                "section",
                "Sorcerer Skill",
                "range-sorcerer",
                "rules.pdf",
                2,
                parent_structure_node_id="node-summary",
            ),
        ),
    )
    ledger = _ledger(
        _context_pointer_entry(
            "entry-summary",
            "node-summary",
            "Here is a summary of how to acquire each rune master skill.",
        ),
        _entry(
            "entry-sorcerer",
            "node-sorcerer",
            "Acquiring a sorcerer skill requires training.",
            structure_node_ids=("node-sorcerer", "node-summary"),
        ),
    )

    plan = build_section_grounded_plan(ledger, structure)

    targets = {target.topic_key: target for target in plan.page_targets}
    assert "acquiring-rune-master-skill" in targets
    assert set(targets["acquiring-rune-master-skill"].entry_ids) == {
        "entry-summary",
        "entry-sorcerer",
    }


def _structure() -> DocumentStructure:
    return DocumentStructure(
        root_node_id="node-root",
        structure_nodes=(
            StructureNode("node-root", "root", "rules.pdf", "range-root", "rules.pdf", 0),
            StructureNode("node-alpha", "section", "Alpha Topic", "range-alpha", "rules.pdf", 1),
            StructureNode("node-beta", "section", "Beta Topic", "range-beta", "rules.pdf", 2),
        ),
    )


def _ledger(*entries: LedgerEntry) -> ClaimLedger:
    if not entries:
        entries = (
            _entry("entry-alpha", "node-alpha", "Alpha Topic"),
            _entry("entry-beta", "node-beta", "Beta Topic"),
        )
    return ClaimLedger(
        claim_ledger_id="claim-ledger-test",
        source_locator="rules.pdf",
        source_hash="source-hash",
        evidence_registry_hash="registry-hash",
        source_profile=SourceProfile(
            source_locator="rules.pdf",
            unit_count=2,
            accepted_entry_count=2,
            claim_count=2,
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("rules", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=entries,
        technical_atoms=(),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )


def _entry(
    entry_id: str,
    node_id: str,
    subject: str,
    *,
    structure_node_ids: tuple[str, ...] | None = None,
) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="rules.pdf",
        source_hash="source-hash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"evidence-{entry_id}",),
        source_text=f"{subject} has source-local evidence.",
        structure_node_ids=structure_node_ids or (node_id,),
        normalized_text=f"{subject} has source-local evidence.",
        subject=subject,
        predicate="has",
        object_value="source-local evidence",
        polarity="positive",
        claim_force="asserted",
    )


def _context_pointer_entry(entry_id: str, node_id: str, text: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="medium",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="rules.pdf",
        source_hash="source-hash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"evidence-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id,),
        normalized_text=text,
        subject="Here",
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
        spatial_scope=SpatialScope(
            spatial_text="Here",
            spatial_kind="relative-location",
            spatial_confidence="low",
        ),
        claim_role_tags=("identity",),
    )
