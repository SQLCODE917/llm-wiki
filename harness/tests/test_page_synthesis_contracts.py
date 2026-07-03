from __future__ import annotations

from llmwiki.domain.ledger.page_synthesis import (
    DraftBlock,
    DraftClaim,
    DraftEvidenceRef,
    PageDraft,
    PageOutlineSection,
    PageSynthesisPlan,
    ledger_ref,
)
from llmwiki.domain.ledger.page_synthesis_rendering import render_page_draft
from llmwiki.domain.ledger.page_synthesis_validation import validate_page_draft
from llmwiki.domain.ledger.topic_terms import singular
from llmwiki.domain.pages import PageMetadata
from llmwiki.runtime.ledger_synthesis_pages import synthesize_page


def test_topic_singularization_preserves_common_non_stems() -> None:
    assert singular("bonuses") == "bonus"
    assert singular("always") == "always"


def test_page_draft_validator_rejects_contract_violations() -> None:
    plan = _plan()
    unknown = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", text="Alpha uses source support."),),
        (DraftClaim("c1", "Alpha uses source support.", (DraftEvidenceRef("ledger", "missing"),)),),
    )
    unmapped = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", text="Alpha has an unmapped sentence."),),
        (DraftClaim("c1", "Alpha uses source support.", (ledger_ref("e1"),)),),
    )
    copied = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", text="one two three four five six seven eight."),),
        (DraftClaim("c1", "one two three four five six seven eight.", (ledger_ref("e1"),)),),
    )
    placeholder = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", text="Alpha has TODO text."),),
        (DraftClaim("c1", "Alpha has TODO text.", (ledger_ref("e1"),)),),
    )
    weak = PageDraft(
        "alpha",
        "Alway",
        (DraftBlock("b1", "paragraph", text="Alway uses source support."),),
        (DraftClaim("c1", "Alway uses source support.", (ledger_ref("e1"),)),),
    )
    weak_plan = PageSynthesisPlan(
        "alpha",
        "concept",
        "topic-concept",
        "Alway",
        "source",
        "x.pdf",
        (),
        plan.outline,
        plan.selected_evidence,
    )

    assert _types(validate_page_draft(plan, unknown)) >= {"unknown-support-ref"}
    assert _types(validate_page_draft(plan, unmapped)) >= {"unmapped-factual-sentence"}
    assert _types(validate_page_draft(plan, copied)) >= {"copied-source-phrases"}
    assert _types(validate_page_draft(plan, placeholder)) >= {"placeholder-text"}
    assert _types(validate_page_draft(weak_plan, weak)) >= {"weak-topic-identity"}


def test_page_draft_renderer_adds_citations_source_trail_related_links_and_coverage() -> None:
    plan = _plan(related=True)
    draft = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", "Overview", "Alpha uses source support."),),
        (DraftClaim("c1", "Alpha uses source support.", (ledger_ref("e1"),)),),
    )
    rendered = render_page_draft(plan, draft)

    assert "Alpha uses source support. _(raw/x.pdf (r1))_" in rendered.page_body
    assert "- Source manifest: [[source]]" in rendered.page_body
    assert "- [[beta]] - shared statements" in rendered.page_body
    claim_entry = next(entry for entry in rendered.coverage.entries if entry.draft_claim_id == "c1")
    assert claim_entry.selected_ledger_entry_ids == ("e1",)
    assert claim_entry.draft_support_refs == ("ledger:e1",)


def test_invalid_synthesis_draft_rejects_page_without_extract_fallback() -> None:
    attempt = synthesize_page(
        _plan(),
        PageMetadata(
            "alpha",
            "concept",
            "Alpha summary.",
            page_family="topic-concept",
            sources=("raw/x.pdf",),
        ),
        _BadDraftProducer(),
        max_attempts=1,
    )

    assert attempt.page is None
    assert attempt.draft_record is None
    assert {finding.finding_type for finding in attempt.findings} >= {"unmapped-factual-sentence"}


def test_sword_world_character_creation_procedure_accepts_fake_draft() -> None:
    plan = _plan(
        "sword-world-rpg-complete-edition-procedure-create-character",
        "Create Character",
        "procedure",
        "procedure-guide",
    )
    attempt = synthesize_page(
        plan,
        PageMetadata(
            plan.page_id,
            "procedure",
            "Create Character summary.",
            page_family=plan.page_family,
            sources=("raw/x.pdf",),
        ),
        _GoodDraftProducer("Create Character follows a supported step order."),
        max_attempts=1,
    )

    assert attempt.page is not None
    assert "Create Character follows a supported step order." in attempt.page.page_body


def test_javascript_allonge_recipe_accepts_fake_draft() -> None:
    plan = _plan(
        "javascriptallonge-recipe-tail-call",
        "Tail Call Recipe",
        "recipe",
        "recipe-pattern",
    )
    attempt = synthesize_page(
        plan,
        PageMetadata(
            plan.page_id,
            "recipe",
            "Tail Call summary.",
            page_family=plan.page_family,
            sources=("raw/x.pdf",),
        ),
        _GoodDraftProducer("Tail Call Recipe has applicability evidence."),
        max_attempts=1,
    )

    assert attempt.page is not None
    assert "Tail Call Recipe has applicability evidence." in attempt.page.page_body


def test_malformed_topic_labels_do_not_publish() -> None:
    for label in ("Alway", "Bonuse"):
        plan = _plan(label.lower(), label, "concept", "topic-concept")
        attempt = synthesize_page(
            plan,
            PageMetadata(
                plan.page_id,
                "concept",
                f"{label} summary.",
                page_family=plan.page_family,
                sources=("raw/x.pdf",),
            ),
            _GoodDraftProducer(f"{label} uses source support."),
            max_attempts=1,
        )
        assert attempt.page is None
        assert {finding.finding_type for finding in attempt.findings} >= {"weak-topic-identity"}

    plan = _plan("ability-bonuse", "Ability Bonuses", "concept", "topic-concept")
    attempt = synthesize_page(
        plan,
        PageMetadata(
            plan.page_id,
            "concept",
            "Ability Bonuses summary.",
            page_family=plan.page_family,
            sources=("raw/x.pdf",),
        ),
        _GoodDraftProducer("Ability Bonuses uses source support."),
        max_attempts=1,
    )
    assert attempt.page is None
    assert {finding.finding_type for finding in attempt.findings} >= {"weak-topic-identity"}


def _types(result) -> set[str]:  # type: ignore[no-untyped-def]
    return {finding.finding_type for finding in result.findings}


class _BadDraftProducer:
    def draft_page(self, plan: PageSynthesisPlan, findings=()) -> PageDraft:  # type: ignore[no-untyped-def]
        return PageDraft(
            plan.page_id,
            plan.title,
            (DraftBlock("b1", "paragraph", text="This sentence has no claim."),),
            (DraftClaim("c1", "Different supported sentence.", (ledger_ref("e1"),)),),
        )


class _GoodDraftProducer:
    def __init__(self, sentence: str) -> None:
        self.sentence = sentence

    def draft_page(self, plan: PageSynthesisPlan, findings=()) -> PageDraft:  # type: ignore[no-untyped-def]
        return PageDraft(
            plan.page_id,
            plan.title,
            (DraftBlock("b1", "paragraph", "Overview", self.sentence),),
            (DraftClaim("c1", self.sentence, (ledger_ref("e1"),)),),
        )


def _plan(
    page_id: str = "alpha",
    title: str = "Alpha",
    page_kind: str = "concept",
    page_family: str = "topic-concept",
    *,
    related: bool = False,
) -> PageSynthesisPlan:
    evidence = _evidence_card()
    links = ()
    if related:
        from llmwiki.domain.ledger.page_synthesis import PageSynthesisRelatedLink

        links = (
            PageSynthesisRelatedLink(
                "beta",
                "Beta",
                "shared statements",
                (ledger_ref("e1"),),
            ),
        )
    return PageSynthesisPlan(
        page_id,
        page_kind,
        page_family,
        title,
        "source",
        "x.pdf",
        ("source-section",),
        (PageOutlineSection("Overview", "test", (ledger_ref("e1"),), "paragraph"),),
        (evidence,),
        links,
    )


def _evidence_card():
    from llmwiki.domain.ledger.page_synthesis import DraftEvidenceCard

    return DraftEvidenceCard(
        ledger_ref("e1"),
        "x.pdf",
        "r1",
        "Alpha uses source support",
        "one two three four five six seven eight nine ten",
        "Section",
        "raw/x.pdf (r1)",
    )
