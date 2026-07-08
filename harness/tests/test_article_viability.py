from __future__ import annotations

from llmwiki.domain.article_viability import select_article_viable_candidates
from llmwiki.domain.ledger.page_publication import (
    PAGE_FAMILY_COLLECTION_PAGE,
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_RECIPE_PATTERN,
    PAGE_FAMILY_TOPIC_CONCEPT,
    PageCandidate,
)
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord

_HASH = "d" * 64


def test_non_reader_candidates_do_not_outrank_reader_pages() -> None:
    result = select_article_viable_candidates(
        source_id="javascriptallonge",
        source_hash=_HASH,
        candidates=(
            _candidate(
                "copyright",
                "Copyright Notice",
                PAGE_FAMILY_TOPIC_CONCEPT,
                tuple(f"copyright-{index}" for index in range(200)),
            ),
            _candidate(
                "map",
                "Generating Iterables",
                PAGE_FAMILY_RECIPE_PATTERN,
                ("code", "argument", "definition", "step"),
            ),
        ),
        record_set=_record_set(
            *(_record(f"copyright-{index}", "argument") for index in range(200)),
            _record("code", "code_example"),
            _record("argument", "argument"),
            _record("definition", "definition"),
            _record("step", "procedure_step"),
        ),
    )

    assert [candidate.page_id for candidate in result.candidates] == ["map"]
    assert result.report.findings[0].finding_code == "non-reader-article-candidate"


def test_raw_support_count_alone_cannot_make_top_candidate() -> None:
    result = select_article_viable_candidates(
        source_id="sword",
        source_hash=_HASH,
        candidates=(
            _candidate(
                "giant",
                "Currency",
                PAGE_FAMILY_TOPIC_CONCEPT,
                tuple(f"currency-{index}" for index in range(100)),
            ),
            _candidate(
                "balanced",
                "Grapple",
                PAGE_FAMILY_PROCEDURE_GUIDE,
                ("step-1", "step-2", "rule-1", "rule-2", "formula-1", "table-1"),
            ),
        ),
        record_set=_record_set(
            *(_record(f"currency-{index}", "entity_fact") for index in range(100)),
            _record("step-1", "procedure_step"),
            _record("step-2", "procedure_step"),
            _record("rule-1", "rule"),
            _record("rule-2", "rule"),
            _record("formula-1", "formula"),
            _record("table-1", "table_fact"),
        ),
    )

    by_page = {candidate.page_id: candidate.rank_score for candidate in result.candidates}
    assert by_page["balanced"] > by_page["giant"]


def test_duplicate_topic_and_collection_candidates_collapse_to_article_candidate() -> None:
    result = select_article_viable_candidates(
        source_id="sword",
        source_hash=_HASH,
        candidates=(
            _candidate(
                "topic-shade",
                "Shade",
                PAGE_FAMILY_TOPIC_CONCEPT,
                ("definition", "rule", "entity"),
            ),
            _candidate(
                "collection-shade",
                "Shade",
                PAGE_FAMILY_COLLECTION_PAGE,
                tuple(f"collection-{index}" for index in range(30)),
            ),
        ),
        record_set=_record_set(
            _record("definition", "definition"),
            _record("rule", "rule"),
            _record("entity", "entity_fact"),
            *(_record(f"collection-{index}", "entity_fact") for index in range(30)),
        ),
    )

    assert [candidate.page_id for candidate in result.candidates] == ["topic-shade"]
    assert {
        finding.finding_code for finding in result.report.findings
    } == {"duplicate-article-candidate"}


def test_recipe_viability_prefers_clean_article_evidence_over_risky_raw_support() -> None:
    result = select_article_viable_candidates(
        source_id="javascriptallonge",
        source_hash=_HASH,
        candidates=(
            _candidate(
                "risky",
                "Naming Functions > function declaration caveats 34",
                PAGE_FAMILY_RECIPE_PATTERN,
                ("risky-code", "risky-colon", "risky-short", "risky-arg", "risky-def"),
            ),
            _candidate(
                "clean",
                "Mutation > building with mutation",
                PAGE_FAMILY_RECIPE_PATTERN,
                ("clean-code", "clean-def", "clean-arg", "clean-step"),
            ),
        ),
        record_set=_record_set(
            _record("risky-code", "code_example", payload="foo()\n//=> value?"),
            _record("risky-colon", "argument", payload="Although this example is:"),
            _record("risky-short", "argument", payload="and;"),
            _record("risky-arg", "argument"),
            _record("risky-def", "definition"),
            _record("clean-code", "code_example", payload="const copy = node => node;"),
            _record(
                "clean-def",
                "definition",
                payload="Mutation can be used while building a new data structure.",
            ),
            _record(
                "clean-arg",
                "argument",
                payload="The recipe uses mutation to avoid extra copying.",
            ),
            _record(
                "clean-step",
                "procedure_step",
                payload="Create each new node before linking the next node.",
            ),
        ),
    )

    by_page = {candidate.page_id: candidate.rank_score for candidate in result.candidates}
    assert by_page["clean"] > by_page["risky"]


def test_standalone_connective_title_is_rejected() -> None:
    result = select_article_viable_candidates(
        source_id="javascriptallonge",
        source_hash=_HASH,
        candidates=(
            _candidate(
                "and-also",
                "And also:",
                PAGE_FAMILY_RECIPE_PATTERN,
                ("code", "argument", "definition"),
            ),
            _candidate(
                "once",
                "Once",
                PAGE_FAMILY_RECIPE_PATTERN,
                ("once-code", "once-argument", "once-definition"),
            ),
        ),
        record_set=_record_set(
            _record("code", "code_example"),
            _record("argument", "argument"),
            _record("definition", "definition"),
            _record("once-code", "code_example"),
            _record("once-argument", "argument"),
            _record("once-definition", "definition"),
        ),
    )

    assert [candidate.page_id for candidate in result.candidates] == ["once"]
    assert {finding.finding_code for finding in result.report.findings} == {
        "weak-reader-title"
    }


def test_source_title_topic_stub_is_rejected() -> None:
    result = select_article_viable_candidates(
        source_id="sword-world-rpg-complete-edition",
        source_hash=_HASH,
        candidates=(
            _candidate(
                "rulebook",
                "Sword World RPG: Complete Edition Rulebook",
                PAGE_FAMILY_TOPIC_CONCEPT,
                ("rulebook-def", "rulebook-rule"),
                source_id="sword-world-rpg-complete-edition",
            ),
            _candidate(
                "shade",
                "Shade",
                PAGE_FAMILY_TOPIC_CONCEPT,
                ("shade-def", "shade-rule"),
                source_id="sword-world-rpg-complete-edition",
            ),
        ),
        record_set=_record_set(
            _record("rulebook-def", "definition"),
            _record("rulebook-rule", "rule"),
            _record("shade-def", "definition"),
            _record("shade-rule", "rule"),
        ),
    )

    assert [candidate.page_id for candidate in result.candidates] == ["shade"]
    assert {finding.finding_code for finding in result.report.findings} == {
        "non-reader-article-candidate"
    }


def _candidate(
    page_id: str,
    title: str,
    family: str,
    support: tuple[str, ...],
    *,
    source_id: str = "source",
) -> PageCandidate:
    return PageCandidate(
        page_candidate_id=f"candidate-{page_id}",
        source_id=source_id,
        source_hash=_HASH,
        source_profile_kind="programming-prose",
        page_id=page_id,
        title=title,
        page_kind="concept",
        page_family=family,
        origin="test",
        rank_score=float(len(support)),
        source_order=1,
        supporting_evidence_record_ids=support,
    )


def _record_set(*records: TypedEvidenceRecord) -> EvidenceRecordSet:
    return EvidenceRecordSet(
        evidence_record_set_id="records",
        source_id="source",
        source_locator="source.pdf",
        source_hash=_HASH,
        source_profile_id="programming-prose",
        evidence_extraction_plan_id="plan",
        records=records,
    )


def _record(record_id: str, record_type: str, *, payload: str = "") -> TypedEvidenceRecord:
    return TypedEvidenceRecord(
        typed_evidence_record_id=record_id,
        source_id="source",
        source_locator="source.pdf",
        source_hash=_HASH,
        evidence_record_type=record_type,
        status="accepted",
        canonical_text=payload or f"{record_type} evidence {record_id}",
        structured_payload=None,
        source_anchors=(),
        source_block_ids=("block",),
        confidence=0.9,
    )
