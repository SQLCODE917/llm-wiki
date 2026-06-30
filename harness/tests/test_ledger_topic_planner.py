from llmwiki.domain.ledger.atom_context import TechnicalAtomContext
from llmwiki.domain.ledger.atoms import FormulaPayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis, SpatialScope
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
        _entry("entry-alpha", "node-alpha", "Alpha is the source section topic.", "Alpha")
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


def test_plan_source_topics_promotes_repeated_section_targets() -> None:
    ledger = _ledger(
        _entry("entry-alpha", "node-alpha", "Alpha field appears in one context.", "Alpha"),
        _entry("entry-beta", "node-beta", "Beta field appears in another context.", "Beta"),
    )
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-alpha", "section", "Shared Heading", "range-alpha", "source.pdf", 1
            ),
            StructureNode("node-beta", "section", "Shared Heading", "range-beta", "source.pdf", 2),
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
                topic_key="shared-heading",
                label="Shared Heading",
                page_kind="concept",
                structure_node_id="node-alpha",
                source_range_id="range-alpha",
                concept_keys=(),
                entry_ids=("entry-alpha",),
                atom_ids=(),
                attached_evidence=(),
            ),
            PageTarget(
                page_target_id="target-beta",
                topic_key="shared-heading",
                label="Shared Heading",
                page_kind="concept",
                structure_node_id="node-beta",
                source_range_id="range-beta",
                concept_keys=(),
                entry_ids=("entry-beta",),
                atom_ids=(),
                attached_evidence=(),
            ),
        ),
        source_coverage_map=(),
    )

    topics = plan_source_topics(ledger, structure, section_plan=section_plan)

    assert len(topics) == 1
    assert topics[0].topic_key == "shared-heading"
    assert topics[0].entry_ids == ("entry-alpha", "entry-beta")

    protected_topics = plan_source_topics(
        ledger, structure, section_plan=section_plan, max_topics=0
    )
    assert tuple(topic.topic_key for topic in protected_topics) == ("shared-heading",)


def test_repeated_section_topics_include_direct_topic_mentions_outside_targets() -> None:
    ledger = _ledger(
        _entry("entry-alpha", "node-alpha", "Alpha field appears in one context.", "Alpha"),
        _entry("entry-beta", "node-beta", "Beta field appears in another context.", "Beta"),
        _entry(
            "entry-extra",
            "node-other",
            "The shared heading is also described in a nearby catalog record.",
            "Shared Heading",
        ),
        _entry(
            "entry-noise",
            "node-other",
            "The heading appears in unrelated prose.",
            "Heading",
        ),
        _atom_entry("entry-atom-noise", "node-other", "atom-noise"),
        atoms=(_formula("atom-noise", "range-entry-atom-noise", "Unrelated=1"),),
        contexts=(
            _atom_context(
                "atom-noise",
                "The shared heading is mentioned near an unrelated formula.",
            ),
        ),
    )
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-alpha", "section", "Shared Heading", "range-alpha", "source.pdf", 1
            ),
            StructureNode("node-beta", "section", "Shared Heading", "range-beta", "source.pdf", 2),
            StructureNode("node-other", "section", "Catalog", "range-other", "source.pdf", 3),
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
                topic_key="shared-heading",
                label="Shared Heading",
                page_kind="concept",
                structure_node_id="node-alpha",
                source_range_id="range-alpha",
                concept_keys=(),
                entry_ids=("entry-alpha",),
                atom_ids=(),
                attached_evidence=(),
            ),
            PageTarget(
                page_target_id="target-beta",
                topic_key="shared-heading",
                label="Shared Heading",
                page_kind="concept",
                structure_node_id="node-beta",
                source_range_id="range-beta",
                concept_keys=(),
                entry_ids=("entry-beta",),
                atom_ids=(),
                attached_evidence=(),
            ),
        ),
        source_coverage_map=(),
    )

    topics = plan_source_topics(ledger, structure, section_plan=section_plan)

    assert len(topics) == 1
    assert set(topics[0].entry_ids) == {"entry-alpha", "entry-beta", "entry-extra"}
    assert "entry-noise" not in topics[0].entry_ids
    assert "atom-noise" not in topics[0].atom_ids


def test_repeated_numbered_compound_topics_do_not_include_adverbial_prefix_noise() -> None:
    ledger = _ledger(
        _entry(
            "entry-language-one",
            "node-language-one",
            "Normal languages are words used for communication.",
            "Normal languages",
        ),
        _entry(
            "entry-language-two",
            "node-language-two",
            "Only normal languages are described in monster language fields.",
            "Only normal languages",
        ),
        _entry(
            "entry-resistance",
            "node-resistance",
            "Normally, this would never succeed, but our 2D roll is 12.",
            "Normally, this",
        ),
    )
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-language-one",
                "section",
                "12.1.1 Normal Languages",
                "range-language-one",
                "source.pdf",
                1,
            ),
            StructureNode(
                "node-language-two",
                "section",
                "12.1.2 Normal Languages of Monsters",
                "range-language-two",
                "source.pdf",
                2,
            ),
            StructureNode(
                "node-resistance",
                "section",
                "Resistance Rolls",
                "range-resistance",
                "source.pdf",
                3,
            ),
        ),
    )
    section_plan = SectionGroundedPlan(
        section_grounded_plan_id="section-plan",
        section_grounded_plan_fingerprint="fingerprint",
        source_locator="source.pdf",
        source_hash="sourcehash",
        page_targets=(
            PageTarget(
                page_target_id="target-language-one",
                topic_key="12-normal-language",
                label="12.1.1 Normal Languages",
                page_kind="concept",
                structure_node_id="node-language-one",
                source_range_id="range-language-one",
                concept_keys=(),
                entry_ids=("entry-language-one",),
                atom_ids=(),
                attached_evidence=(),
            ),
            PageTarget(
                page_target_id="target-language-two",
                topic_key="12-normal-language",
                label="12.1.2 Normal Languages of Monsters",
                page_kind="concept",
                structure_node_id="node-language-two",
                source_range_id="range-language-two",
                concept_keys=(),
                entry_ids=("entry-language-two",),
                atom_ids=(),
                attached_evidence=(),
            ),
        ),
        source_coverage_map=(),
    )

    topics = plan_source_topics(ledger, structure, section_plan=section_plan)

    assert len(topics) == 1
    assert set(topics[0].entry_ids) == {"entry-language-one", "entry-language-two"}
    assert "entry-resistance" not in topics[0].entry_ids


def test_section_component_topic_uses_section_evidence_when_match_is_context_pointer() -> None:
    ledger = _ledger(
        _context_pointer_entry(
            "entry-summary",
            "node-acquiring",
            "Here is a summary of how to acquire and increase each rune master skill.",
        ),
        _entry(
            "entry-sorcerer",
            "node-sorcerer",
            "The sorcerer skill is increased by spending experience points.",
            "The sorcerer skill",
        ),
    )
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-acquiring",
                "section",
                "11.4 Acquiring Rune Master Skills and Increasing Levels",
                "range-acquiring",
                "source.pdf",
                1,
            ),
            StructureNode(
                "node-sorcerer",
                "section",
                "Sorcerer Skill",
                "range-sorcerer",
                "source.pdf",
                2,
                parent_structure_node_id="node-acquiring",
            ),
        ),
    )
    section_plan = SectionGroundedPlan(
        section_grounded_plan_id="section-plan",
        section_grounded_plan_fingerprint="fingerprint",
        source_locator="source.pdf",
        source_hash="sourcehash",
        page_targets=(
            PageTarget(
                page_target_id="target-acquiring",
                topic_key="acquiring-rune-master-skill-and-increasing-level",
                label="11.4 Acquiring Rune Master Skills and Increasing Levels",
                page_kind="concept",
                structure_node_id="node-acquiring",
                source_range_id="range-acquiring",
                concept_keys=("acquiring-rune-master-skill",),
                entry_ids=("entry-summary", "entry-sorcerer"),
                atom_ids=(),
                attached_evidence=(),
            ),
        ),
        source_coverage_map=(),
    )

    topics = plan_source_topics(ledger, structure, section_plan=section_plan)

    target = next(topic for topic in topics if topic.topic_key == "acquiring-rune-master-skill")
    assert set(target.entry_ids) == {"entry-summary", "entry-sorcerer"}


def _entry(entry_id: str, node_id: str, text: str, subject: str) -> LedgerEntry:
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
        structure_node_ids=(node_id,),
        normalized_text=text,
        subject=subject,
        predicate="is",
        object_value=text,
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
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
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


def _atom_entry(entry_id: str, node_id: str, atom_id: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="technical-atom",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text="",
        structure_node_ids=(node_id,),
        technical_atom_kind="formula",
        technical_atom_id=atom_id,
    )


def _formula(atom_id: str, range_id: str, text: str) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="formula",
        payload=FormulaPayload(
            raw_formula_text=text,
            formula_subtype="field",
            formula_surface_form=text,
            source_locator="source.pdf",
            parse_status="parsed",
        ),
        source_locator="source.pdf",
        source_range_id=range_id,
        evidence_ids=(range_id,),
    )


def _atom_context(atom_id: str, text: str) -> TechnicalAtomContext:
    return TechnicalAtomContext(
        technical_atom_context_id=f"context-{atom_id}",
        technical_atom_id=atom_id,
        context_role="explained-by-source-prose",
        context_text=text,
        context_entry_ids=(),
        context_source_range_ids=(f"range-{atom_id}",),
        demonstrated_concept_keys=tuple(text.lower().split()),
        evidence_ids=(f"range-{atom_id}",),
        confidence_basis=ConfidenceBasis("test"),
    )


def _ledger(
    *entries: LedgerEntry,
    atoms: tuple[TechnicalAtom, ...] = (),
    contexts: tuple[TechnicalAtomContext, ...] = (),
) -> ClaimLedger:
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
        technical_atoms=atoms,
        technical_atom_contexts=contexts,
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
