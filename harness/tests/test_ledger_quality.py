from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.pointers import quality_check_catalog_pointer
from llmwiki.domain.ledger.quality import build_ledger_quality_report, page_write_decision
from llmwiki.domain.ledger.quality_catalog import (
    default_quality_check_catalog,
    default_severity_policy,
)
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode


def test_unresolved_named_table_reference_warns_without_blocking_write() -> None:
    report = build_ledger_quality_report(
        _ledger_with_unresolved_table_reference(),
        DocumentStructure(
            root_node_id="node-root",
            structure_nodes=(
                StructureNode(
                    "node-root",
                    "root",
                    "rules.md",
                    "source-range-root",
                    "rules.md",
                    0,
                ),
            ),
        ),
        catalog=default_quality_check_catalog(),
        severity=default_severity_policy(),
        catalog_pointer=quality_check_catalog_pointer("catalog", "fingerprint"),
    )

    table_findings = [
        finding
        for finding in report.findings
        if finding.quality_check_id == "ck-named-table-reference-resolved"
    ]

    assert [finding.quality_finding_severity for finding in table_findings] == ["warning"]
    assert page_write_decision(report) == "write-with-review-work"


def _ledger_with_unresolved_table_reference() -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="claim-ledger-test",
        source_locator="rules.md",
        source_hash="source-hash",
        evidence_registry_hash="registry-hash",
        source_profile=SourceProfile(
            source_locator="rules.md",
            unit_count=0,
            accepted_entry_count=1,
            claim_count=1,
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
        entries=(
            LedgerEntry(
                ledger_entry_id="entry-table-ref",
                source_statement_id="statement-table-ref",
                ledger_entry_kind="claim",
                ledger_entry_status="usable",
                extraction_confidence="high",
                confidence_basis=ConfidenceBasis("test"),
                source_locator="rules.md",
                source_hash="source-hash",
                source_range_id="source-range-entry",
                evidence_ids=("evidence-table-ref",),
                source_text="Use reaction table to resolve the result.",
                subject="player",
                predicate="uses",
                object_value="reaction table",
                polarity="affirmative",
                claim_force="asserted",
            ),
        ),
        technical_atoms=(),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
