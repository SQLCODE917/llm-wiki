from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.current_topics import _term_topics
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.objects import Evidence, PagePlan, RawSource, SourceBundle, SourceClaim


def test_term_topics_build_from_bounded_term_claim_map() -> None:
    raw = RawSource("rules.pdf", "pdf")
    claims = tuple(_claim(raw, f"claim-{index}", ("alpha", f"term{index}")) for index in range(300))
    entries = tuple(_entry(f"entry-{index}", f"claim-{index}") for index in range(300))
    entries_by_claim = {f"claim-{index}": entries[index] for index in range(300)}

    topics = _term_topics(_page_plan(raw, claims), entries_by_claim, _ledger(entries))

    alpha = next(topic for topic in topics if topic.topic_key == "alpha")
    assert len(alpha.entry_ids) == 300
    assert all(topic.topic_key != "term299" for topic in topics)


def _page_plan(raw: RawSource, claims: tuple[SourceClaim, ...]) -> PagePlan:
    return PagePlan(
        plan_id="plan",
        source_bundle=SourceBundle.one(raw),
        extracted_units=(),
        source_claims=claims,
        source_claim_groups=(),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(),
    )


def _claim(raw: RawSource, claim_id: str, terms: tuple[str, ...]) -> SourceClaim:
    return SourceClaim(
        source_claim_id=claim_id,
        statement="statement",
        evidence=Evidence(raw, "p.1", "Rules", "statement"),
        extracted_unit_id="unit",
        source_span="p.1",
        subject_terms=terms,
    )


def _entry(entry_id: str, claim_id: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=claim_id,
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="rules.pdf",
        source_hash="hash",
        source_range_id="range",
        evidence_ids=("ev",),
        source_text="statement",
    )


def _ledger(entries: tuple[LedgerEntry, ...]) -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="rules.pdf",
        source_hash="hash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile("rules.pdf", 0, len(entries), len(entries), 0, 0, 0, {}, {}),
        source_family_assignment=SourceFamilyAssignment((), 0.0),
        entries=entries,
        technical_atoms=(),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
