from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)


def test_claim_ledger_normalizes_singleton_entries_to_tuples() -> None:
    entry = LedgerEntry(
        ledger_entry_id="entry-one",
        source_statement_id="statement-one",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="rules.md",
        source_hash="source-hash",
        source_range_id="range-one",
        evidence_ids=("evidence-one",),
        source_text="Rules are source-derived.",
    )

    ledger = ClaimLedger(
        claim_ledger_id="claim-ledger-test",
        source_locator="rules.md",
        source_hash="source-hash",
        evidence_registry_hash="registry-hash",
        source_profile=SourceProfile(
            source_locator="rules.md",
            unit_count=1,
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
        entries=entry,  # type: ignore[arg-type]
        technical_atoms=(),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )

    assert ledger.entries == (entry,)
