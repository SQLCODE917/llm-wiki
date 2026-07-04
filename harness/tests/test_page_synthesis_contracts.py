from __future__ import annotations

import json

from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.domain.ledger.page_synthesis import (
    DraftBlock,
    DraftClaim,
    EvidenceSupportRef,
    NavigationSummary,
    PageDraft,
    PageEvidenceItem,
    PageEvidenceSet,
    PageOutlineSection,
    PageSynthesisPlan,
    PromptContextDigest,
    RelatedLinkPreview,
    atom_ref,
    ledger_ref,
)
from llmwiki.domain.ledger.page_synthesis_drafting import RejectingPageDraftProducer
from llmwiki.domain.ledger.page_synthesis_rendering import render_page_draft
from llmwiki.domain.ledger.page_synthesis_validation import validate_page_draft
from llmwiki.domain.ledger.topic_terms import singular
from llmwiki.domain.pages import PageMetadata
from llmwiki.runtime.ledger_synthesis_metadata import with_synthesis_coverage
from llmwiki.runtime.ledger_synthesis_pages import synthesize_page
from llmwiki.runtime.page_synthesis_forge import ForgePageDraftProducer


def test_topic_singularization_preserves_common_non_stems() -> None:
    assert singular("bonuses") == "bonus"
    assert singular("always") == "always"


def test_page_draft_validator_rejects_contract_violations() -> None:
    plan = _plan()
    unknown = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", text="Alpha uses source support."),),
        (
            DraftClaim(
                "c1",
                "Alpha uses source support.",
                (EvidenceSupportRef("ledger", "missing"),),
            ),
        ),
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
        plan.evidence_set,
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
    assert "- [[beta]] - shared statements: Alpha source support preview" in rendered.page_body
    assert "_(supports: ledger:e1)_" in rendered.page_body
    claim_entry = next(entry for entry in rendered.coverage.entries if entry.draft_claim_id == "c1")
    assert claim_entry.selected_ledger_entry_ids == ("e1",)
    assert claim_entry.draft_support_refs == ("ledger:e1",)


def test_page_draft_validator_rejects_shade_style_clipped_fragments() -> None:
    plan = _plan(
        evidence_text=(
            "The shade is also very fragile and will easily disintegrate if exposed to "
            "strong light. Furthermore if an opponent destroys a shade with a weapon, "
            "the opponent will also suffer the same damage. If a shade itself comes "
            "into contact with a will-o-wisp's body or enters the area lit by it, the "
            "shade suffers damage."
        )
    )

    for fragment in (
        "The shade is also very fragile and will easily.",
        "Furthermore if an opponent destroys a will also suffer the same damage.",
        "If a shade itself comes into will-o-wisp's body or enters the area.",
    ):
        draft = PageDraft(
            "alpha",
            "Alpha",
            (DraftBlock("b1", "paragraph", text=fragment),),
            (DraftClaim("c1", fragment, (ledger_ref("e1"),)),),
        )
        assert _types(validate_page_draft(plan, draft)) >= {"clipped-evidence-fragment"}


def test_page_draft_validator_rejects_navigation_summary_and_prompt_digest_text() -> None:
    summary_sentence = "Alpha preview text is only for navigation."
    digest_sentence = "Alpha compressed prompt context is not renderable."
    plan = _plan(
        evidence_set=PageEvidenceSet(
            "alpha",
            (_evidence_item(),),
            navigation_summaries=(
                NavigationSummary("alpha", summary_sentence, "accepted-page-preview"),
            ),
            prompt_context_digests=(
                PromptContextDigest(digest_sentence, (ledger_ref("e1"),)),
            ),
        )
    )

    summary_draft = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", text=summary_sentence),),
        (DraftClaim("c1", summary_sentence, (ledger_ref("e1"),)),),
    )
    digest_draft = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", text=digest_sentence),),
        (DraftClaim("c1", digest_sentence, (ledger_ref("e1"),)),),
    )

    assert _types(validate_page_draft(plan, summary_draft)) >= {"navigation-summary-prose"}
    assert _types(validate_page_draft(plan, digest_draft)) >= {"prompt-context-digest-prose"}


def test_page_draft_renderer_displays_atom_payload_text() -> None:
    plan = _plan(
        evidence_set=PageEvidenceSet(
            "alpha",
            (
                PageEvidenceItem(
                    atom_ref("a1"),
                    "technical-atom",
                    "x.pdf",
                    ("r2",),
                    "Distance=20 meters",
                    "Section",
                    "raw/x.pdf (r2)",
                    technical_atom_id="a1",
                ),
            ),
        )
    )
    draft = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", "Technical Evidence", "Distance=20 meters."),),
        (DraftClaim("c1", "Distance=20 meters.", (atom_ref("a1"),)),),
    )
    rendered = render_page_draft(plan, draft)

    assert "Distance=20 meters. _(raw/x.pdf (r2))_" in rendered.page_body
    claim_entry = next(entry for entry in rendered.coverage.entries if entry.draft_claim_id == "c1")
    assert claim_entry.technical_atom_id == "a1"
    assert claim_entry.draft_support_refs == ("atom:a1",)


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


def test_default_rejection_producer_publishes_no_fallback_page() -> None:
    attempt = synthesize_page(
        _plan(),
        PageMetadata(
            "alpha",
            "concept",
            "Alpha summary.",
            page_family="topic-concept",
            sources=("raw/x.pdf",),
        ),
        RejectingPageDraftProducer(),
        max_attempts=1,
    )

    assert attempt.page is None
    assert attempt.draft_record is None
    assert {finding.finding_type for finding in attempt.findings} >= {"empty-draft"}


def test_accepted_page_navigation_summary_comes_from_rendered_page() -> None:
    plan = _plan()
    draft = PageDraft(
        "alpha",
        "Alpha",
        (DraftBlock("b1", "paragraph", "Overview", "Alpha uses source support."),),
        (DraftClaim("c1", "Alpha uses source support.", (ledger_ref("e1"),)),),
    )
    rendered = render_page_draft(plan, draft)
    metadata = with_synthesis_coverage(
        PageMetadata(
            "alpha",
            "concept",
            "Old evidence-card summary.",
            page_family="topic-concept",
            sources=("raw/x.pdf",),
        ),
        plan,
        rendered,
    )

    assert metadata.summary == "Alpha: Alpha uses source support."


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


def test_forge_page_draft_producer_uses_structured_draft_tool_with_full_evidence() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="draft_page",
                    args={
                        "page_id": "alpha",
                        "title": "Alpha",
                        "blocks": [
                            {
                                "block_id": "b1",
                                "block_kind": "paragraph",
                                "heading": "Overview",
                                "text": "Alpha uses source support.",
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Alpha uses source support.",
                                "support_refs": ["ledger:e1"],
                            }
                        ],
                    },
                )
            ]
        ]
    )
    producer = ForgePageDraftProducer(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="schema",
    )

    draft = producer.draft_page(_plan(evidence_text="Full source evidence sentence."))

    assert draft.claims[0].support_refs[0].code == "ledger:e1"
    sent = json.dumps(client.sent)
    assert "Full source evidence sentence." in sent
    assert "evidence_text" in sent
    assert '"summary"' not in sent


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
    evidence_text: str = "one two three four five six seven eight nine ten",
    evidence_set: PageEvidenceSet | None = None,
) -> PageSynthesisPlan:
    evidence = _evidence_item(evidence_text=evidence_text)
    evidence_set = evidence_set or PageEvidenceSet(page_id, (evidence,))
    links = ()
    if related:
        links = (
            RelatedLinkPreview(
                "beta",
                "Beta",
                "shared statements",
                "Alpha source support preview",
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
        evidence_set,
        links,
    )


def _evidence_item(
    *, evidence_text: str = "one two three four five six seven eight nine ten"
) -> PageEvidenceItem:
    return PageEvidenceItem(
        support_ref=ledger_ref("e1"),
        evidence_kind="ledger-entry",
        source_locator="x.pdf",
        source_range_ids=("r1",),
        evidence_text=evidence_text,
        section_label="Section",
        citation="raw/x.pdf (r1)",
        ledger_entry_ids=("e1",),
    )
