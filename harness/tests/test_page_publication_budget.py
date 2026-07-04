from llmwiki.domain.ledger.page_publication import (
    PAGE_FAMILY_RECIPE_PATTERN,
    PAGE_FAMILY_SECTION_REFERENCE,
    PAGE_FAMILY_TOPIC_CONCEPT,
    PageCandidate,
    conservative_publication_budget,
)
from llmwiki.domain.ledger.page_publication_planning import (
    attach_typed_evidence_support,
    plan_publication,
)
from llmwiki.domain.ledger.page_title_lint import lint_page_title
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord

_HASH = "b" * 64


def test_title_linter_rejects_malformed_topic_labels() -> None:
    for title, page_id in (
        ("Alway", "src-alway"),
        ("Bonuse", "src-bonuse"),
        ("Needn", "src-needn"),
        ("Double Sixe", "src-double-sixe"),
    ):
        findings = lint_page_title(title, page_id, PAGE_FAMILY_TOPIC_CONCEPT)

        assert findings
        assert findings[0].severity == "blocking"


def test_fragmentary_or_rejected_typed_evidence_never_supports_candidate() -> None:
    candidate = _candidate("src-shade", "Shade")
    record_set = _record_set(
        _record("fragment", "definition", "Shade is a dark spirit.", status="fragmentary"),
        _record("rejected", "definition", "Shade creates darkness.", status="rejected"),
    )

    (supported,) = attach_typed_evidence_support((candidate,), record_set)

    assert supported.supporting_evidence_record_ids == ()


def test_candidate_without_accepted_typed_evidence_is_rejected() -> None:
    plan = _plan((_candidate("src-shade", "Shade"),), record_set=None)

    assert plan.accepted_candidates == ()
    assert plan.rejected_candidates[0].rejection_code == "insufficient-typed-evidence"
    assert plan.rejected_candidates[0].message


def test_over_budget_candidates_are_rejected_with_deterministic_code() -> None:
    candidates = tuple(
        _candidate(f"src-topic-{index}", f"Topic {index}", support=("a", "b"))
        for index in range(12)
    )

    plan = _plan(candidates)

    assert len(plan.accepted_candidates) == 10
    rejected_codes = {candidate.rejection_code for candidate in plan.rejected_candidates}
    assert rejected_codes == {"publication-budget-exceeded"}
    assert all(candidate.message for candidate in plan.rejected_candidates)


def test_section_reference_candidates_are_rejected_by_default_budget() -> None:
    candidate = _candidate(
        "src-section-shade",
        "Shade",
        family=PAGE_FAMILY_SECTION_REFERENCE,
        kind="source",
        support=("a",),
    )

    plan = _plan((candidate,))

    assert plan.accepted_candidates == ()
    assert plan.rejected_candidates[0].rejection_code == "section-reference-not-explicitly-accepted"


def test_explicit_section_acceptance_allows_named_section_candidate() -> None:
    accepted = _candidate(
        "src-section-shade",
        "Shade",
        family=PAGE_FAMILY_SECTION_REFERENCE,
        kind="source",
        support=("a",),
    )
    other = _candidate(
        "src-section-will-o-wisp",
        "Will O Wisp",
        family=PAGE_FAMILY_SECTION_REFERENCE,
        kind="source",
        support=("b",),
    )
    budget = conservative_publication_budget(
        "rpg-rules", explicit_section_page_ids=(accepted.page_id,)
    )

    plan = plan_publication(
        source_id="src",
        source_hash=_HASH,
        source_profile_kind="rpg-rules",
        budget=budget,
        candidates=(accepted, other),
    )

    assert plan.accepted_page_ids == (accepted.page_id,)
    assert plan.rejected_candidates[0].page_id == other.page_id


def test_javascript_recipe_candidate_is_supported_by_code_and_argument_evidence() -> None:
    recipe = _candidate(
        "js-recipe-map",
        "Map",
        family=PAGE_FAMILY_RECIPE_PATTERN,
        kind="recipe",
    )
    record_set = _record_set(
        _record("code", "code_example", "Array map applies a function to each value."),
        _record("argument", "argument", "Map is useful when transforming each value."),
    )
    (supported,) = attach_typed_evidence_support((recipe,), record_set)

    plan = _plan((supported,), profile="programming-prose")

    assert plan.accepted_page_ids == ("js-recipe-map",)


def _plan(
    candidates: tuple[PageCandidate, ...],
    *,
    record_set: EvidenceRecordSet | None = None,
    profile: str = "rpg-rules",
):
    supported = attach_typed_evidence_support(candidates, record_set)
    budget = conservative_publication_budget(profile)
    return plan_publication(
        source_id="src",
        source_hash=_HASH,
        source_profile_kind=profile,
        budget=budget,
        candidates=supported,
    )


def _candidate(
    page_id: str,
    title: str,
    *,
    family: str = PAGE_FAMILY_TOPIC_CONCEPT,
    kind: str = "concept",
    support: tuple[str, ...] = (),
) -> PageCandidate:
    return PageCandidate(
        page_candidate_id=f"candidate-{page_id}",
        source_id="src",
        source_hash=_HASH,
        source_profile_kind="rpg-rules",
        page_id=page_id,
        title=title,
        page_kind=kind,
        page_family=family,
        origin="test",
        rank_score=1.0,
        source_order=1,
        supporting_evidence_record_ids=support,
        title_findings=lint_page_title(title, page_id, family),
    )


def _record_set(*records: TypedEvidenceRecord) -> EvidenceRecordSet:
    return EvidenceRecordSet(
        evidence_record_set_id="records",
        source_id="src",
        source_locator="src.pdf",
        source_hash=_HASH,
        source_profile_id="rpg-rules",
        evidence_extraction_plan_id="plan",
        records=records,
    )


def _record(
    record_id: str,
    record_type: str,
    text: str,
    *,
    status: str = "accepted",
) -> TypedEvidenceRecord:
    return TypedEvidenceRecord(
        typed_evidence_record_id=record_id,
        source_id="src",
        source_locator="src.pdf",
        source_hash=_HASH,
        evidence_record_type=record_type,
        status=status,  # type: ignore[arg-type]
        canonical_text=text,
        structured_payload=None,
        source_anchors=(),
        source_block_ids=("block-1",),
        confidence=0.9,
    )
