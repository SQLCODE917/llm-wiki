from llmwiki.domain.ledger.atoms import TablePayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.structure import (
    DocumentStructure,
    ExtractedUnitDispositionRecord,
    StructureNode,
)
from llmwiki.domain.ledger.table_identity import (
    explicit_forward_reference,
    has_matching_table_name,
    named_table_references,
    normalize_table_name,
    table_identity_names_by_atom_id,
)


def test_table_identity_tolerates_malformed_source_order() -> None:
    ledger = _ledger_with_table()
    structure = DocumentStructure(
        root_node_id="node-root",
        structure_nodes=(
            StructureNode(
                "node-root",
                "root",
                "rules.pdf",
                "source-range-root",
                "rules.pdf",
                0,
            ),
            StructureNode(
                "node-cue",
                "section",
                "The following table",
                "source-range-cue",
                "rules.pdf",
                "not-a-number",  # type: ignore[arg-type]
            ),
        ),
        dispositions=(
            ExtractedUnitDispositionRecord(
                "unit-table",
                "source-range-table",
                "accepted",
                source_order=object(),  # type: ignore[arg-type]
            ),
        ),
    )

    names = table_identity_names_by_atom_id(ledger, structure)

    assert names == {"atom-table-0": ("reaction",)}


def test_table_identity_skips_forward_cues_for_table_heavy_ledgers() -> None:
    ledger = _ledger_with_tables(70)
    structure = DocumentStructure(
        root_node_id="node-root",
        structure_nodes=(
            StructureNode(
                "node-root",
                "root",
                "rules.pdf",
                "source-range-root",
                "rules.pdf",
                0,
            ),
            StructureNode(
                "node-cue",
                "section",
                "The following table",
                "source-range-cue",
                "rules.pdf",
                "not-a-number",  # type: ignore[arg-type]
            ),
        ),
        dispositions=(
            ExtractedUnitDispositionRecord(
                "unit-table",
                "source-range-table-0",
                "accepted",
                source_order=object(),  # type: ignore[arg-type]
            ),
        ),
    )

    names = table_identity_names_by_atom_id(ledger, structure)

    assert names["atom-table-0"] == ("reaction",)


def test_table_identity_skips_structure_heading_names_for_large_sources() -> None:
    ledger = _ledger_with_table_heading_entry()
    structure = DocumentStructure(
        root_node_id="node-root",
        structure_nodes=(
            StructureNode("node-root", "root", "rules.pdf", "source-range-root", "rules.pdf", 0),
            StructureNode(
                "node-table",
                "section",
                "Reaction Result Table",
                "source-range-section",
                "rules.pdf",
                1,
            ),
            *(
                StructureNode(
                    f"node-extra-{index}",
                    "section",
                    f"Extra {index}",
                    f"source-range-extra-{index}",
                    "rules.pdf",
                    index + 2,
                )
                for index in range(520)
            ),
        ),
    )

    names = table_identity_names_by_atom_id(ledger, structure)

    assert names["atom-table-0"] == ("dice",)


def test_table_name_matching_bounds_pathological_names() -> None:
    reference = "reaction " + ("2d d6 42 noise " * 10_000)
    table_names = ("reaction table", "other " + ("d20 noise " * 10_000))

    assert has_matching_table_name(reference, table_names)


def test_normalize_table_name_uses_bounded_lexical_identity() -> None:
    long_name = "Reaction " + ("noisy-value " * 10_000)

    assert normalize_table_name("Table 12-3: Reaction Table") == "reaction"
    assert normalize_table_name(long_name).split()[0] == "reaction"
    assert len(normalize_table_name(long_name).split()) <= 8


def test_normalize_table_name_tolerates_pdf_unicode_glyph_noise() -> None:
    assert normalize_table_name("Table 1: Mārdan Ā① Reaction") == "m rdan reaction"


def test_table_name_matching_requires_alphabetic_identity_overlap() -> None:
    assert not has_matching_table_name(
        "12 1 1 normal languages",
        ("2 1", "baseline scores", "2 1 baseline scores"),
    )
    assert not has_matching_table_name("12 1 2 normal languages of", ("2", "races"))


def test_table_reference_detection_bounds_pathological_text() -> None:
    forward_text = "table below " + ("noise " * 20_000)
    named_text = "use reaction table " + ("noise " * 20_000)

    assert explicit_forward_reference(forward_text)
    assert named_table_references(named_text) == ("reaction",)


def _ledger_with_table() -> ClaimLedger:
    return _ledger_with_tables(1)


def _ledger_with_table_heading_entry() -> ClaimLedger:
    ledger = _ledger_with_tables(1, caption="Dice table")
    entry = LedgerEntry(
        ledger_entry_id="entry-table-0",
        source_statement_id="statement-table-0",
        ledger_entry_kind="technical-atom",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="rules.pdf",
        source_hash="source-hash",
        source_range_id="source-range-table-0",
        evidence_ids=("evidence-table",),
        source_text="",
        structure_node_ids=("node-table", "node-root"),
        technical_atom_kind="table",
        technical_atom_id="atom-table-0",
    )
    return ClaimLedger(
        claim_ledger_id=ledger.claim_ledger_id,
        source_locator=ledger.source_locator,
        source_hash=ledger.source_hash,
        evidence_registry_hash=ledger.evidence_registry_hash,
        source_profile=ledger.source_profile,
        source_family_assignment=ledger.source_family_assignment,
        entries=(entry,),
        technical_atoms=ledger.technical_atoms,
        technical_atom_contexts=ledger.technical_atom_contexts,
        source_statements=ledger.source_statements,
        extractor_decisions=ledger.extractor_decisions,
        rejected_candidates=ledger.rejected_candidates,
    )


def _ledger_with_tables(count: int, *, caption: str = "Reaction table") -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="claim-ledger-test",
        source_locator="rules.pdf",
        source_hash="source-hash",
        evidence_registry_hash="registry-hash",
        source_profile=SourceProfile(
            source_locator="rules.pdf",
            unit_count=1,
            accepted_entry_count=0,
            claim_count=0,
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={"table": count},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("rules", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=(),
        technical_atoms=tuple(
            TechnicalAtom(
                technical_atom_id=f"atom-table-{index}",
                technical_atom_kind="table",
                payload=TablePayload(
                    raw_table_text="| Roll | Reaction |\n| 2 | Hostile |",
                    parse_status="parsed",
                    source_locator="rules.pdf",
                    caption=caption,
                ),
                source_locator="rules.pdf",
                source_range_id=f"source-range-table-{index}",
                evidence_ids=("evidence-table",),
            )
            for index in range(count)
        ),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
