from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.section_planning import PageTarget, SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.topic_planner import plan_source_topics


def test_plan_source_topics_does_not_duplicate_exact_section_targets() -> None:
    ledger = _ledger(
        LedgerEntry(
            ledger_entry_id="entry-alpha",
            source_statement_id="statement-alpha",
            ledger_entry_kind="claim",
            ledger_entry_status="usable",
            extraction_confidence="high",
            confidence_basis=ConfidenceBasis("test"),
            source_locator="source.pdf",
            source_hash="sourcehash",
            source_range_id="range-alpha",
            evidence_ids=("ev-alpha",),
            source_text="Alpha is the source section topic.",
            structure_node_ids=("node-alpha",),
            normalized_text="Alpha is the source section topic.",
            subject="Alpha",
            predicate="is",
            object_value="the source section topic",
            polarity="positive",
            claim_force="asserted",
        )
    )
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode("node-alpha", "section", "Alpha", "range-alpha", "source.pdf", 1),
        ),
    )
    section_plan = SectionGroundedPlan(
        section_grounded_plan_id="section-plan",
        section_grounded_plan_fingerprint="fingerprint",
        source_locator="source.pdf",
        source_hash="sourcehash",
        page_targets=(
            PageTarget(
                page_target_id="target-alpha",
                topic_key="alpha",
                label="Alpha",
                page_kind="concept",
                structure_node_id="node-alpha",
                source_range_id="range-alpha",
                concept_keys=(),
                entry_ids=("entry-alpha",),
                atom_ids=(),
                attached_evidence=(),
            ),
        ),
        source_coverage_map=(),
    )

    assert plan_source_topics(ledger, structure, section_plan=section_plan) == ()


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
