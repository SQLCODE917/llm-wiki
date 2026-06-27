from llmwiki.domain.ledger.atom_context import TechnicalAtomContext
from llmwiki.domain.ledger.atoms import CodeBlockPayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.pointers import PortableArtifactPointer
from llmwiki.domain.ledger.projection import (
    LedgerProjectionPlan,
    PlannedAtomBlock,
    PlannedSection,
    ProjectionSourceSupport,
)
from llmwiki.domain.ledger.renderer import render_source_page


def test_source_page_renders_technical_atom_context() -> None:
    rendered = render_source_page(
        LedgerProjectionPlan(
            wiki_page_locator="rules",
            page_kind="source",
            title="Rules",
            source_support=ProjectionSourceSupport(
                "support-rules",
                "source-hash",
                "rules.md",
                PortableArtifactPointer("claim-ledger-artifact", "ledger", "fingerprint"),
                PortableArtifactPointer("document-structure-artifact", "structure", "fingerprint"),
            ),
            sections=(
                PlannedSection(
                    "node-rules",
                    "Rules",
                    1,
                    1,
                    (),
                    (PlannedAtomBlock("atom-code", 2, "rules.md (source-range-code)"),),
                ),
            ),
            review_items=(),
            disposition_counts=(),
        ),
        _ledger_with_code_context(),
    )

    assert "> Context: Use this helper when mapping values." in rendered.page_body
    assert "```javascript" in rendered.page_body


def _ledger_with_code_context() -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="claim-ledger-test",
        source_locator="rules.md",
        source_hash="source-hash",
        evidence_registry_hash="registry-hash",
        source_profile=SourceProfile(
            source_locator="rules.md",
            unit_count=1,
            accepted_entry_count=0,
            claim_count=0,
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={"code-block": 1},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("coding", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=(),
        technical_atoms=(
            TechnicalAtom(
                technical_atom_id="atom-code",
                technical_atom_kind="code-block",
                payload=CodeBlockPayload(
                    raw_code_text="value => value + 1",
                    parse_status="parsed",
                    source_locator="rules.md",
                    language_tag="javascript",
                ),
                source_locator="rules.md",
                source_range_id="source-range-code",
                evidence_ids=("evidence-code",),
            ),
        ),
        technical_atom_contexts=(
            TechnicalAtomContext(
                technical_atom_context_id="context-code",
                technical_atom_id="atom-code",
                context_role="introduced-by-source-prose",
                context_text="Use this helper when mapping values.",
                context_entry_ids=(),
                context_source_range_ids=("source-range-context",),
                demonstrated_concept_keys=("mapping",),
                evidence_ids=("evidence-context",),
                confidence_basis=ConfidenceBasis("test"),
            ),
        ),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
