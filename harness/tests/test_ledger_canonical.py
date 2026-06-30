from __future__ import annotations

from dataclasses import dataclass

import pytest

from llmwiki.domain.ledger.artifacts import (
    ClaimLedgerArtifact,
    claim_ledger_artifact_fingerprint,
    claim_ledger_artifact_to_json,
)
from llmwiki.domain.ledger.canonical import canonical_json, to_jsonable
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.pointers import PortableArtifactPointer


@dataclass(frozen=True)
class TinyRecord:
    name: str
    value: int


@dataclass
class RecursiveRecord:
    name: str
    child: RecursiveRecord | None = None


def test_to_jsonable_serializes_repeated_dataclasses() -> None:
    records = tuple(TinyRecord(f"record-{index}", index) for index in range(20))

    assert to_jsonable(records)[0] == {"name": "record-0", "value": 0}


def test_to_jsonable_rejects_recursive_dataclass() -> None:
    record = RecursiveRecord("root")
    record.child = record

    with pytest.raises(TypeError):
        to_jsonable(record)


def test_claim_ledger_artifact_codec_matches_generic_canonical_json() -> None:
    artifact = ClaimLedgerArtifact(
        claim_ledger_id="claim-ledger-test",
        claim_ledger_fingerprint="",
        artifact_format="llm-wiki-ledger-v1",
        document_structure_pointer=PortableArtifactPointer(
            "document-structure-artifact", "document-structure-test", "fp-structure"
        ),
        ledger_quality_report_pointer=PortableArtifactPointer(
            "ledger-quality-report-artifact", "ledger-report-test", "fp-report"
        ),
        ledger=_empty_ledger(),
    )

    assert claim_ledger_artifact_to_json(artifact) == canonical_json(artifact)
    assert len(claim_ledger_artifact_fingerprint(artifact)) == 16


def _empty_ledger() -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="claim-ledger-test",
        source_locator="rules.pdf",
        source_hash="source-hash",
        evidence_registry_hash="registry-hash",
        source_profile=SourceProfile(
            source_locator="rules.pdf",
            unit_count=0,
            accepted_entry_count=0,
            claim_count=0,
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
        entries=(),
        technical_atoms=(),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
