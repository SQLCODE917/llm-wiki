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
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_render import render_topic_page
from llmwiki.runtime.ledger_pages import build_topic_pages


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

    assert "**Context:** _(rules.md (source-range-context))_" in rendered.page_body
    assert "> Use this helper when mapping values." in rendered.page_body
    assert "**Atom:** _(rules.md (source-range-code))_" in rendered.page_body
    assert "```javascript" in rendered.page_body


def test_topic_page_pairs_context_with_technical_atom() -> None:
    rendered = render_topic_page(
        SourceTopic(
            topic_key="mapping",
            label="Mapping",
            page_kind="concept",
            match_terms=("mapping",),
            entry_ids=(),
            atom_ids=("atom-code",),
            from_heading=False,
            salience=1.0,
        ),
        _ledger_with_code_context(),
        wiki_page_locator="rules-mapping",
        source_page_id="rules",
    )

    assert "### Technical atom 1" in rendered.page_body
    assert rendered.page_body.index("**Context:**") < rendered.page_body.index("**Atom:**")
    assert "**Atom:** _(rules.md (source-range-code))_" in rendered.page_body


def test_topic_page_renders_all_selected_technical_atoms() -> None:
    rendered = render_topic_page(
        SourceTopic(
            topic_key="mapping",
            label="Mapping",
            page_kind="concept",
            match_terms=("mapping",),
            entry_ids=(),
            atom_ids=("atom-code",) * 7,
            from_heading=False,
            salience=1.0,
        ),
        _ledger_with_code_context(),
        wiki_page_locator="rules-mapping",
        source_page_id="rules",
    )

    assert "_Showing 6 of 7 technical atoms selected for this topic._" not in rendered.page_body
    assert "### Technical atom 7" in rendered.page_body


def test_topic_pages_render_bidirectional_related_links() -> None:
    pages = build_topic_pages(
        (
            SourceTopic(
                topic_key="list",
                label="List",
                page_kind="concept",
                match_terms=("list",),
                entry_ids=(),
                atom_ids=("atom-code",),
                from_heading=False,
                salience=3.0,
            ),
            SourceTopic(
                topic_key="linked-list",
                label="Linked List",
                page_kind="concept",
                match_terms=("linked", "list"),
                entry_ids=(),
                atom_ids=("atom-code",),
                from_heading=False,
                salience=2.0,
            ),
        ),
        _ledger_with_code_context(),
        source_page_id="rules",
        source_locator="rules.md",
        today="2026-06-27",
    )

    by_id = {page.page_id: page.page_body for page in pages}
    assert "[[rules-linked-list]] - narrower topic (1 shared atom(s))" in by_id["rules-list"]
    assert "[[rules-list]] - broader topic (1 shared atom(s))" in by_id["rules-linked-list"]


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
