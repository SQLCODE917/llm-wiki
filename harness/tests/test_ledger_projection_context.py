from llmwiki.domain.ledger.artifacts import build_projection_context_artifact
from llmwiki.domain.ledger.atom_addressing import technical_atom_anchor_id
from llmwiki.domain.ledger.atom_frames import build_atom_frames
from llmwiki.domain.ledger.atoms import FormulaPayload, TechnicalAtom
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.common import ConfidenceBasis, SpatialScope
from llmwiki.domain.ledger.entries import LedgerEntry, SourceStatement
from llmwiki.domain.ledger.evidence_blocks import EvidenceBlock
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.projection_context import build_projection_context
from llmwiki.domain.ledger.projection_policy import (
    PAGE_FAMILY_BROAD_TOPIC,
    PROJECTION_ELIGIBILITY_CONTEXTUAL_ONLY,
    ProjectionBudget,
    ledger_entry_projection_eligibility,
    topic_projection_policy,
)
from llmwiki.domain.ledger.structure import (
    DocumentStructure,
    ExtractedUnitDispositionRecord,
    StructureNode,
)
from llmwiki.domain.ledger.topic_render import render_topic_page
from llmwiki.domain.ledger.topics import SourceTopic


def test_topic_projection_renders_source_blocks_and_atom_frames() -> None:
    ledger = _ledger(
        entries=(
            _claim(
                "entry-description-one",
                "statement-description",
                "range-description",
                "A skeleton warrior is a formidable warrior.",
            ),
            _claim(
                "entry-description-two",
                "statement-description",
                "range-description",
                "This spell is what creates that formidable warrior.",
            ),
            _claim(
                "entry-command-one",
                "statement-command",
                "range-command",
                "Only the caster can give commands.",
            ),
            _claim(
                "entry-command-two",
                "statement-command",
                "range-command",
                "They cannot understand overly complex commands.",
            ),
            _atom_entry("entry-cost", "atom-cost", "range-cost"),
            _atom_entry("entry-distance", "atom-distance", "range-distance"),
        ),
        atoms=(
            _formula("atom-cost", "range-cost", "Base Mental Power Cost=20"),
            _formula("atom-distance", "range-distance", "Distance=Touch"),
        ),
        statements=(
            SourceStatement(
                "statement-description",
                "range-description",
                (
                    "A skeleton warrior is a formidable warrior. This spell is what "
                    "creates that formidable warrior."
                ),
                ("entry-description-one", "entry-description-two"),
            ),
            SourceStatement(
                "statement-command",
                "range-command",
                (
                    "The caster can give commands to the skeleton warrior. Only the "
                    "caster can give commands. They cannot understand overly complex "
                    "commands."
                ),
                ("entry-command-one", "entry-command-two"),
            ),
        ),
    )
    context = build_projection_context(ledger, _structure())
    topic = SourceTopic(
        topic_key="skeleton-warrior",
        label="Skeleton Warrior",
        page_kind="concept",
        match_terms=("skeleton", "warrior"),
        entry_ids=(
            "entry-description-one",
            "entry-description-two",
            "entry-command-one",
            "entry-command-two",
        ),
        atom_ids=("atom-cost", "atom-distance"),
        from_heading=True,
        salience=10,
    )

    rendered = render_topic_page(
        topic,
        ledger,
        wiki_page_locator="source-skeleton-warrior",
        source_page_id="source",
        projection_context=context,
    )

    body = rendered.page_body

    assert (
        "- A skeleton warrior is a formidable warrior. This spell is what creates "
        "that formidable warrior."
    ) in body
    assert (
        "- The caster can give commands to the skeleton warrior. Only the caster "
        "can give commands. They cannot understand overly complex commands."
    ) in body
    assert "- This spell is what creates that formidable warrior." not in body
    assert "- Only the caster can give commands." not in body
    assert "### Skeleton Warrior" in body
    assert "### Technical frame 1: Skeleton Warrior" in body
    assert "**Context:** _(source.pdf (range-description))_" in body
    assert technical_atom_anchor_id("atom-cost") in body
    assert technical_atom_anchor_id("atom-distance") in body
    assert "Base Mental Power Cost=20" in body
    assert "Distance=Touch" in body


def test_atom_frames_accept_single_evidence_block_context() -> None:
    ledger = _ledger(
        entries=(_atom_entry("entry-cost", "atom-cost", "range-cost"),),
        atoms=(_formula("atom-cost", "range-cost", "Base Mental Power Cost=20"),),
        statements=(),
    )
    block = EvidenceBlock(
        evidence_block_id="block-context",
        source_statement_id="statement-context",
        source_range_id="range-description",
        source_range_ids=("range-description",),
        source_locator="source.pdf",
        source_text="The spell context explains the cost.",
        entry_ids=(),
        structure_node_ids=("node-skeleton-warrior",),
        source_order=4,
        section_label="Skeleton Warrior",
    )

    frames = build_atom_frames(ledger, _structure(), block)

    assert frames[0].context_block_id == "block-context"


def test_topic_projection_groups_ambiguous_claims_by_source_section() -> None:
    ledger = _ledger(
        entries=(
            _claim(
                "entry-cure-wounds-limitation",
                "statement-cure-wounds-limitation",
                "range-cure-wounds-limitation",
                "This has no effect on magical creatures that do not have normal life.",
                node_id="node-cure-wounds",
                subject="This",
            ),
        ),
        atoms=(),
        statements=(
            SourceStatement(
                "statement-cure-wounds-limitation",
                "range-cure-wounds-limitation",
                "This has no effect on magical creatures that do not have normal life.",
                ("entry-cure-wounds-limitation",),
            ),
        ),
    )
    context = build_projection_context(ledger, _context_structure())
    topic = SourceTopic(
        topic_key="skeleton-warrior",
        label="Skeleton Warrior",
        page_kind="concept",
        match_terms=("skeleton", "warrior"),
        entry_ids=("entry-cure-wounds-limitation",),
        atom_ids=(),
        from_heading=True,
        salience=3,
    )

    rendered = render_topic_page(
        topic,
        ledger,
        wiki_page_locator="source-skeleton-warrior",
        source_page_id="source",
        projection_context=context,
    )

    assert "### Magic / Cure Wounds" in rendered.page_body
    assert (
        "- This has no effect on magical creatures that do not have normal life."
        " _(source.pdf (range-cure-wounds-limitation))_"
    ) in rendered.page_body


def test_projection_context_merges_adjacent_mid_sentence_fragments() -> None:
    ledger = _ledger(
        entries=(
            _claim(
                "entry-dark-priest-start",
                "statement-dark-priest-start",
                "range-dark-priest-start",
                "The method is almost the same. However, many dark gods that dark priests",
            ),
            _claim(
                "entry-dark-priest-continuation",
                "statement-dark-priest-continuation",
                "range-dark-priest-continuation",
                "believe in have no temples.",
            ),
        ),
        atoms=(),
        statements=(
            SourceStatement(
                "statement-dark-priest-start",
                "range-dark-priest-start",
                "The method is almost the same. However, many dark gods that dark priests",
                ("entry-dark-priest-start",),
            ),
            SourceStatement(
                "statement-dark-priest-continuation",
                "range-dark-priest-continuation",
                "believe in have no temples.",
                ("entry-dark-priest-continuation",),
            ),
        ),
    )
    context = build_projection_context(ledger, _continuation_structure())
    topic = SourceTopic(
        topic_key="dark-priest-skill",
        label="Dark Priest Skill",
        page_kind="concept",
        match_terms=("dark", "priest"),
        entry_ids=("entry-dark-priest-start", "entry-dark-priest-continuation"),
        atom_ids=(),
        from_heading=True,
        salience=3,
    )

    rendered = render_topic_page(
        topic,
        ledger,
        wiki_page_locator="source-dark-priest-skill",
        source_page_id="source",
        projection_context=context,
    )

    assert (
        "- The method is almost the same. However, many dark gods that dark priests "
        "believe in have no temples. _(source.pdf (range-dark-priest-start, "
        "range-dark-priest-continuation))_"
    ) in rendered.page_body
    assert "- believe in have no temples." not in rendered.page_body


def test_projection_context_serializes_as_portable_artifact() -> None:
    ledger = _ledger(
        entries=(
            _claim(
                "entry-description-one",
                "statement-description",
                "range-description",
                "A source-backed statement.",
            ),
        ),
        atoms=(),
        statements=(
            SourceStatement(
                "statement-description",
                "range-description",
                "A source-backed statement.",
                ("entry-description-one",),
            ),
        ),
    )
    context = build_projection_context(ledger, _structure())

    artifact = build_projection_context_artifact(
        source_locator="source.pdf",
        source_hash="sourcehash",
        projection_context=context,
    )
    payload = canonical_json(artifact)

    assert artifact.projection_context_artifact_id.startswith("projection-context-")
    assert "projection_context" in payload
    assert "range-description" in payload


def test_contextual_only_entries_do_not_render_as_fallback_claims() -> None:
    entry = _claim(
        "entry-contextual",
        "statement-contextual",
        "range-contextual",
        "This provides the relative identity.",
        subject="This",
    )
    entry = entry.__class__(
        **{
            **vars(entry),
            "spatial_scope": SpatialScope(
                spatial_text="this",
                spatial_kind="relative-location",
                spatial_confidence="high",
            ),
            "claim_role_tags": ("identity",),
        }
    )
    ledger = _ledger(
        entries=(entry,),
        atoms=(),
        statements=(
            SourceStatement(
                "statement-contextual",
                "range-contextual",
                "This provides the relative identity.",
                ("entry-contextual",),
            ),
        ),
    )
    topic = SourceTopic(
        topic_key="relative-entry",
        label="Relative Entry",
        page_kind="concept",
        match_terms=("relative", "entry"),
        entry_ids=("entry-contextual",),
        atom_ids=(),
        from_heading=False,
        salience=1,
    )

    rendered = render_topic_page(
        topic,
        ledger,
        wiki_page_locator="source-relative-entry",
        source_page_id="source",
        projection_context=None,
    )

    assert ledger_entry_projection_eligibility(entry) == PROJECTION_ELIGIBILITY_CONTEXTUAL_ONLY
    assert "This provides the relative identity" not in rendered.page_body
    assert "range-contextual" not in rendered.page_body


def test_broad_topic_policy_limits_evidence_blocks_by_source_section() -> None:
    ledger = _ledger(
        entries=(
            _claim("entry-a1", "statement-a1", "range-a1", "Alpha first.", node_id="node-a"),
            _claim("entry-a2", "statement-a2", "range-a2", "Alpha second.", node_id="node-a"),
            _claim("entry-b1", "statement-b1", "range-b1", "Beta first.", node_id="node-b"),
            _claim("entry-c1", "statement-c1", "range-c1", "Gamma first.", node_id="node-c"),
        ),
        atoms=(),
        statements=(
            SourceStatement("statement-a1", "range-a1", "Alpha first.", ("entry-a1",)),
            SourceStatement("statement-a2", "range-a2", "Alpha second.", ("entry-a2",)),
            SourceStatement("statement-b1", "range-b1", "Beta first.", ("entry-b1",)),
            SourceStatement("statement-c1", "range-c1", "Gamma first.", ("entry-c1",)),
        ),
    )
    context = build_projection_context(ledger, _broad_structure())
    topic = SourceTopic(
        topic_key="large-topic",
        label="Large Topic",
        page_kind="concept",
        match_terms=("large", "topic"),
        entry_ids=("entry-a1", "entry-a2", "entry-b1", "entry-c1"),
        atom_ids=(),
        from_heading=False,
        salience=4,
    )
    policy = topic_projection_policy(
        topic,
        ledger,
        context,
        budget=ProjectionBudget(
            broad_topic_min_entries=99,
            broad_topic_min_sections=2,
            broad_topic_min_source_order_span=99,
            broad_topic_max_blocks_per_section=1,
            broad_topic_max_sections=2,
        ),
    )

    rendered = render_topic_page(
        topic,
        ledger,
        wiki_page_locator="source-large-topic",
        source_page_id="source",
        projection_context=context,
        projection_policy=policy,
    )

    assert policy.page_family == PAGE_FAMILY_BROAD_TOPIC
    assert "## Statements by source section" in rendered.page_body
    assert "Alpha first." in rendered.page_body
    assert "Alpha second." not in rendered.page_body
    assert "Beta first." in rendered.page_body
    assert "Gamma first." not in rendered.page_body


def _structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-skeleton-warrior",
                "section",
                "Skeleton Warrior",
                "range-heading",
                "source.pdf",
                1,
                parent_structure_node_id="root",
            ),
        ),
        (
            ExtractedUnitDispositionRecord("unit-heading", "range-heading", "structural", 1),
            ExtractedUnitDispositionRecord("unit-cost", "range-cost", "accepted", 2),
            ExtractedUnitDispositionRecord("unit-distance", "range-distance", "accepted", 3),
            ExtractedUnitDispositionRecord("unit-description", "range-description", "accepted", 4),
            ExtractedUnitDispositionRecord("unit-command", "range-command", "accepted", 5),
        ),
    )


def _broad_structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-a",
                "section",
                "Section A",
                "range-heading-a",
                "source.pdf",
                1,
                parent_structure_node_id="root",
            ),
            StructureNode(
                "node-b",
                "section",
                "Section B",
                "range-heading-b",
                "source.pdf",
                2,
                parent_structure_node_id="root",
            ),
            StructureNode(
                "node-c",
                "section",
                "Section C",
                "range-heading-c",
                "source.pdf",
                3,
                parent_structure_node_id="root",
            ),
        ),
        (
            ExtractedUnitDispositionRecord("unit-a1", "range-a1", "accepted", 1),
            ExtractedUnitDispositionRecord("unit-a2", "range-a2", "accepted", 2),
            ExtractedUnitDispositionRecord("unit-b1", "range-b1", "accepted", 100),
            ExtractedUnitDispositionRecord("unit-c1", "range-c1", "accepted", 200),
        ),
    )


def _continuation_structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-dark-priest",
                "section",
                "Dark Priest Skill",
                "range-dark-priest-heading",
                "source.pdf",
                1,
                parent_structure_node_id="root",
            ),
        ),
        (
            ExtractedUnitDispositionRecord(
                "unit-dark-priest-heading", "range-dark-priest-heading", "structural", 1
            ),
            ExtractedUnitDispositionRecord(
                "unit-dark-priest-start", "range-dark-priest-start", "accepted", 10
            ),
            ExtractedUnitDispositionRecord("unit-noise", "range-noise", "structural", 11),
            ExtractedUnitDispositionRecord(
                "unit-dark-priest-continuation",
                "range-dark-priest-continuation",
                "accepted",
                12,
            ),
        ),
    )


def _context_structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-magic",
                "chapter",
                "Magic",
                "range-magic",
                "source.pdf",
                1,
                parent_structure_node_id="root",
            ),
            StructureNode(
                "node-cure-wounds",
                "section",
                "Cure Wounds",
                "range-cure-wounds",
                "source.pdf",
                2,
                parent_structure_node_id="node-magic",
            ),
        ),
        (
            ExtractedUnitDispositionRecord("unit-magic", "range-magic", "structural", 1),
            ExtractedUnitDispositionRecord(
                "unit-cure-wounds", "range-cure-wounds", "structural", 2
            ),
            ExtractedUnitDispositionRecord(
                "unit-cure-wounds-limitation",
                "range-cure-wounds-limitation",
                "accepted",
                3,
            ),
        ),
    )


def _claim(
    entry_id: str,
    statement_id: str,
    range_id: str,
    text: str,
    *,
    node_id: str = "node-skeleton-warrior",
    subject: str = "Skeleton Warrior",
) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=statement_id,
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=range_id,
        evidence_ids=(range_id,),
        source_text=text,
        structure_node_ids=(node_id,),
        normalized_text=text,
        subject=subject,
        predicate="has detail",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _atom_entry(entry_id: str, atom_id: str, range_id: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="technical-atom",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=range_id,
        evidence_ids=(range_id,),
        source_text="",
        structure_node_ids=("node-skeleton-warrior",),
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


def _ledger(
    *,
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    statements: tuple[SourceStatement, ...],
) -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="source.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="source.pdf",
            unit_count=len(entries),
            accepted_entry_count=len(entries),
            claim_count=4,
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={"formula": len(atoms)},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("rules-reference", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=entries,
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=statements,
        extractor_decisions=(),
        rejected_candidates=(),
    )
