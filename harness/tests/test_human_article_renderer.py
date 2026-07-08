from __future__ import annotations

import json

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.domain.article_write_queue import (
    ArticleWriteQueuePolicy,
    article_write_queue_policy_for_source,
)
from llmwiki.domain.ledger.evidence_pack import (
    EvidencePack,
    EvidencePackCoverage,
    EvidencePackItem,
    EvidencePackSet,
    SupportRef,
)
from llmwiki.domain.ledger.human_article import (
    ArticleBlock,
    ArticleClaim,
    ArticleRelatedLink,
    ArticleSection,
    HumanArticle,
    RejectingArticleWriter,
)
from llmwiki.domain.ledger.human_article_rendering import render_human_article
from llmwiki.domain.ledger.human_article_validation import validate_human_article
from llmwiki.domain.ledger.page_title_lint import PageTitleFinding
from llmwiki.domain.pages import PageMetadata, render_page
from llmwiki.domain.source_map import SourceAnchor
from llmwiki.runtime.human_article_forge import ForgeHumanArticleWriter
from llmwiki.runtime.ledger_human_article_pages import (
    build_human_article_linked_pages,
    write_human_article_page,
)
from llmwiki.workflows.human_article_write import (
    article_prompt_evidence_items,
    article_support_aliases,
    human_article_from_json,
    human_article_to_json,
)

_HASH = "d" * 64
_SUPPORT = SupportRef("typed-evidence-record", "record-shade")
_SECOND_SUPPORT = SupportRef("typed-evidence-record", "record-wisp")


def test_article_support_aliases_are_deterministic_and_canonicalize() -> None:
    aliases = article_support_aliases(_pack_with_two_items())

    assert aliases.allowed_aliases == ("S1", "S2")
    assert aliases.support_ref_for("S1") == _SUPPORT
    assert aliases.support_ref_for("S2") == _SECOND_SUPPORT
    with pytest.raises(ValueError, match="Unknown support alias 'support-1'"):
        aliases.support_ref_for("support-1")
    assert "S1, S2" in aliases.allowed_aliases_text


def test_human_article_json_keeps_canonical_support_refs_not_aliases() -> None:
    article = _article("Shade creates darkness around the target.")
    payload = human_article_to_json(article)

    assert "typed-evidence-record:record-shade" in payload
    assert '"S1"' not in payload
    assert human_article_from_json(payload) == article


def test_human_article_json_rejects_aliases_and_model_rescue_shapes() -> None:
    article = _article("Shade creates darkness around the target.")
    payload = json.loads(human_article_to_json(article))
    payload["claims"][0]["support_refs"] = ["S1"]

    with pytest.raises(ValueError, match="Support ref must be formatted"):
        human_article_from_json(json.dumps(payload))

    payload = json.loads(human_article_to_json(article))
    payload["sections"] = payload["sections"][0]

    with pytest.raises(ValueError):
        human_article_from_json(json.dumps(payload))


def test_article_prompt_evidence_items_bound_large_source_text() -> None:
    pack = _pack(source_text="source " * 20_000, payload="payload " * 20_000)
    prompt_items = article_prompt_evidence_items(pack)

    assert len(prompt_items) == 1
    assert prompt_items[0].alias == "S1"
    assert len(prompt_items[0].source_text) <= 1_600
    assert len(prompt_items[0].payload_text) <= 1_200
    assert prompt_items[0].source_text_omitted_chars > 0
    assert prompt_items[0].payload_text_omitted_chars > 0
    assert prompt_items[0].item.support_ref == _SUPPORT


def test_article_queue_continues_after_writer_failure() -> None:
    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(
            _pack(page_id="bad", title="Bad"),
            _pack(page_id="good", title="Good"),
        ),
        source_locator="sword.pdf",
        today="2026-07-07",
        article_writer=_FailsPageWriter("bad"),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="rpg-rules",
            target_accepted_articles=1,
            max_public_articles=2,
            max_attempted_packs=2,
            max_attempts_per_pack=1,
        ),
    )

    assert [page.page_id for page in result.pages] == ["good"]
    assert result.article_write_queue_run.attempted_page_ids == ("bad", "good")
    assert result.article_write_queue_run.accepted_page_ids == ("good",)
    assert "writer-failed" in {
        finding.finding_code for finding in result.article_write_queue_run.findings
    }


def test_article_queue_continues_after_soft_target_until_public_budget() -> None:
    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(
            _pack(page_id="first", title="First"),
            _pack(page_id="second", title="Second"),
        ),
        source_locator="sword.pdf",
        today="2026-07-07",
        article_writer=_PackCoherentWriter(),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="rpg-rules",
            target_accepted_articles=1,
            max_public_articles=2,
            max_attempted_packs=8,
            max_attempts_per_pack=1,
        ),
    )

    assert [page.page_id for page in result.pages] == ["first", "second"]
    assert result.article_write_queue_run.exhausted_reason == "pack-list-exhausted"
    assert result.article_write_queue_run.skipped_page_ids == ()


def test_article_queue_stops_after_max_attempted_packs() -> None:
    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(
            _pack(page_id="bad-a", title="Bad A"),
            _pack(page_id="bad-b", title="Bad B"),
        ),
        source_locator="sword.pdf",
        today="2026-07-07",
        article_writer=RejectingArticleWriter(),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="rpg-rules",
            target_accepted_articles=2,
            max_public_articles=2,
            max_attempted_packs=1,
            max_attempts_per_pack=1,
        ),
    )

    assert result.pages == ()
    assert result.article_write_queue_run.attempted_page_ids == ("bad-a",)
    assert result.article_write_queue_run.skipped_page_ids == ("bad-b",)
    assert result.article_write_queue_run.exhausted_reason == "attempt-budget-exhausted"
    assert "attempt-budget-exceeded" in {
        finding.finding_code for finding in result.article_write_queue_run.findings
    }
    assert "article-attempt-budget-exceeded" not in _finding_types(
        result.article_output.findings
    )


def test_article_queue_prefers_programming_recipe_then_topic() -> None:
    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(
            _pack(page_id="topic", title="Topic", family="topic-concept"),
            _pack(page_id="recipe", title="Recipe", family="recipe-pattern"),
            profile="programming-prose",
        ),
        source_locator="javascript.pdf",
        today="2026-07-07",
        article_writer=_PackCoherentWriter(),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="programming-prose",
            target_accepted_articles=2,
            max_public_articles=2,
            max_attempted_packs=2,
            max_attempts_per_pack=1,
            family_targets=(("recipe-pattern", 1), ("topic-concept", 1)),
        ),
    )

    assert result.article_write_queue_run.attempted_page_ids == ("recipe", "topic")
    assert result.article_write_queue_run.family_counts == (
        ("recipe-pattern", 1),
        ("topic-concept", 1),
    )


def test_article_queue_prefers_rpg_procedure_then_topic() -> None:
    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(
            _pack(page_id="topic", title="Topic", family="topic-concept"),
            _pack(page_id="procedure", title="Procedure", family="procedure-guide"),
            profile="rpg-rules",
        ),
        source_locator="sword.pdf",
        today="2026-07-07",
        article_writer=_PackCoherentWriter(),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="rpg-rules",
            target_accepted_articles=2,
            max_public_articles=2,
            max_attempted_packs=2,
            max_attempts_per_pack=1,
            family_targets=(("procedure-guide", 1), ("topic-concept", 1)),
        ),
    )

    assert result.article_write_queue_run.attempted_page_ids == ("procedure", "topic")


def test_article_queue_policy_scales_from_valid_pack_count() -> None:
    allonge = article_write_queue_policy_for_source("programming-prose", 14)
    sword = article_write_queue_policy_for_source("rpg-rules", 21)

    assert allonge.max_public_articles == 14
    assert allonge.max_attempted_packs == 14
    assert allonge.target_accepted_articles == 3
    assert dict(allonge.family_targets) == {"recipe-pattern": 6, "topic-concept": 4}
    assert sword.max_public_articles == 21
    assert sword.max_attempted_packs == 21
    assert dict(sword.family_targets) == {"procedure-guide": 8, "topic-concept": 8}


def test_rpg_scaled_policy_accepts_more_than_three_articles() -> None:
    packs = tuple(
        _pack(
            page_id=f"procedure-{index}",
            title=f"Procedure {index}",
            family="procedure-guide",
        )
        for index in range(5)
    )

    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(*packs),
        source_locator="sword.pdf",
        today="2026-07-07",
        article_writer=_PackCoherentWriter(),
    )

    assert len(result.pages) == 5
    assert result.article_write_queue_run.policy.max_public_articles == 5
    assert result.article_write_queue_run.acceptance_rate == 1.0


def test_article_queue_stops_after_public_article_budget() -> None:
    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(
            _pack(page_id="first", title="First"),
            _pack(page_id="second", title="Second"),
            _pack(page_id="third", title="Third"),
        ),
        source_locator="sword.pdf",
        today="2026-07-07",
        article_writer=_PackCoherentWriter(),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="rpg-rules",
            target_accepted_articles=1,
            max_public_articles=2,
            max_attempted_packs=8,
            max_attempts_per_pack=1,
        ),
    )

    assert [page.page_id for page in result.pages] == ["first", "second"]
    assert result.article_write_queue_run.skipped_page_ids == ("third",)
    assert result.article_write_queue_run.exhausted_reason == "source-page-budget-reached"
    assert "source-page-budget-reached" in {
        finding.finding_code for finding in result.article_write_queue_run.findings
    }


def test_article_queue_stops_after_low_acceptance_rate() -> None:
    packs = tuple(_pack(page_id=f"bad-{index}", title=f"Bad {index}") for index in range(9))

    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(*packs),
        source_locator="sword.pdf",
        today="2026-07-07",
        article_writer=RejectingArticleWriter(),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="rpg-rules",
            target_accepted_articles=3,
            max_public_articles=9,
            max_attempted_packs=9,
            max_attempts_per_pack=1,
            min_attempts_before_rate_gate=8,
            min_acceptance_rate=0.25,
            acceptance_rate_window=8,
        ),
    )

    assert len(result.article_write_queue_run.attempted_page_ids) == 8
    assert result.article_write_queue_run.skipped_page_ids == ("bad-8",)
    assert result.article_write_queue_run.exhausted_reason == "low-acceptance-rate"
    assert result.article_write_queue_run.rolling_acceptance_rate == 0.0


def test_article_queue_family_caps_limit_one_family() -> None:
    result = build_human_article_linked_pages(
        evidence_pack_set=_pack_set(
            _pack(page_id="recipe-a", title="Recipe A", family="recipe-pattern"),
            _pack(page_id="recipe-b", title="Recipe B", family="recipe-pattern"),
            _pack(page_id="topic", title="Topic", family="topic-concept"),
            profile="programming-prose",
        ),
        source_locator="javascript.pdf",
        today="2026-07-07",
        article_writer=_PackCoherentWriter(),
        queue_policy=ArticleWriteQueuePolicy(
            source_profile_kind="programming-prose",
            target_accepted_articles=3,
            max_public_articles=3,
            max_attempted_packs=3,
            max_attempts_per_pack=1,
            family_targets=(("recipe-pattern", 2), ("topic-concept", 1)),
            family_caps=(("recipe-pattern", 1), ("topic-concept", 2)),
        ),
    )

    assert result.article_write_queue_run.attempted_page_ids == ("recipe-a", "topic")
    assert result.article_write_queue_run.skipped_page_ids == ("recipe-b",)
    assert result.article_write_queue_run.family_counts == (
        ("recipe-pattern", 1),
        ("topic-concept", 1),
    )


def test_article_validator_rejects_contract_violations() -> None:
    pack = _pack()
    valid_sentence = "Shade creates darkness around the target."
    unknown = _article(valid_sentence, support=SupportRef("typed-evidence-record", "missing"))
    missing = _article(valid_sentence, support=None)
    unmapped = HumanArticle(
        "shade",
        "Shade",
        (ArticleSection("s1", "Overview", (ArticleBlock("b1", "paragraph", "Unmapped fact."),)),),
        (ArticleClaim("c1", valid_sentence, (_SUPPORT,)),),
    )
    placeholder = _article("Shade has TODO text.")
    raw_markdown = _article("# Shade\n\nShade creates darkness around the target.")

    assert _types(validate_human_article(pack, unknown)) >= {"unknown-support-ref"}
    assert _types(validate_human_article(pack, missing)) >= {"missing-support-ref"}
    assert _types(validate_human_article(pack, unmapped)) >= {"unmapped-factual-sentence"}
    assert _types(validate_human_article(pack, placeholder)) >= {"placeholder-text"}
    assert _types(validate_human_article(pack, raw_markdown)) >= {"raw-markdown-prose"}


def test_article_validator_rejects_clipped_fragments_copied_phrases_and_weak_labels() -> None:
    source = (
        "The shade is also very fragile and will easily disintegrate if exposed to "
        "strong light. Furthermore if an opponent destroys a shade with a weapon, "
        "the opponent will also suffer the same damage. If a shade itself comes "
        "into contact with a will-o-wisp's body or enters the area lit by it, the "
        "shade suffers damage."
    )
    pack = _pack(source_text=source)

    clipped = _article("The shade is also very fragile and will easily.")
    copied = _article("one two three four five six seven eight.", pack=_pack())
    weak = _article(
        "Alway uses source support.",
        pack=_pack(page_id="alway", title="Alway"),
    )

    assert _types(validate_human_article(pack, clipped)) >= {"clipped-evidence-fragment"}
    assert _types(validate_human_article(_pack(), copied)) >= {"copied-source-phrases"}
    assert _types(validate_human_article(_pack(page_id="alway", title="Alway"), weak)) >= {
        "weak-topic-identity"
    }


def test_article_renderer_adds_citations_source_trail_related_links_and_payload() -> None:
    pack = _pack(payload="Distance=20 meters", record_type="formula")
    article = _article(
        "Shade creates darkness around the target.",
        pack=pack,
        related=(
            ArticleRelatedLink(
                "will-o-wisp",
                "Will-o-wisp",
                "shared spell interaction",
                "Shows how light interacts with darkness.",
                (_SUPPORT,),
            ),
        ),
    )
    rendered = render_human_article(pack, article)
    page = render_page(
        write_human_article_page(
            pack,
            PageMetadata(
                "shade",
                "concept",
                "Shade summary.",
                page_family="topic-concept",
                sources=("raw/sword.pdf",),
            ),
            _Writer(article),
            max_attempts=1,
        ).page
    )

    assert (
        "Shade creates darkness around the target. _(raw/sword.pdf (p. 59))_"
        in rendered.page_body
    )
    assert "- Source manifest: [[source]]" in rendered.page_body
    assert "- raw/sword.pdf (p. 59) - Spirit Magic List / Shade" in rendered.page_body
    assert "`Distance=20 meters`" in rendered.page_body
    assert "[[will-o-wisp]] - shared spell interaction" in rendered.page_body
    assert "shared support: typed-evidence-record:record-shade" in rendered.page_body
    assert "projection_coverage: human-article-shade@" in page
    assert "page_family: topic-concept" in page
    entry = rendered.coverage.entries[0]
    assert entry.projection_coverage_unit_kind == "article-claim"
    assert entry.draft_support_refs == ("typed-evidence-record:record-shade",)


def test_rejecting_article_writer_publishes_no_fallback_page() -> None:
    attempt = write_human_article_page(
        _pack(),
        PageMetadata(
            "shade",
            "concept",
            "Shade summary.",
            page_family="topic-concept",
            sources=("raw/sword.pdf",),
        ),
        RejectingArticleWriter(),
        max_attempts=1,
    )

    assert attempt.page is None
    assert attempt.record is None
    assert _finding_types(attempt.findings) >= {"empty-article"}


def test_write_human_article_page_omits_page_when_lint_blocks() -> None:
    pack = _pack()
    article = _article("Shade creates darkness around the target.", pack=pack)
    attempt = write_human_article_page(
        pack,
        PageMetadata(
            "shade",
            "concept",
            "Shade summary.",
            page_family="topic-concept",
            sources=("raw/sword.pdf",),
        ),
        _Writer(article),
        max_attempts=1,
        title_findings=(
            PageTitleFinding(
                "finding-title",
                "blocking",
                "planning-title-failed",
                "Shade",
                "planner supplied a blocking title finding",
            ),
        ),
    )

    assert attempt.page is None
    assert attempt.record is None
    assert attempt.lint_run is not None
    assert attempt.lint_run.publication_gate.decision == "blocked"
    assert _finding_types(attempt.findings) >= {"title-lint-failed"}


def test_write_human_article_page_records_writer_errors_without_crashing() -> None:
    attempt = write_human_article_page(
        _pack(),
        PageMetadata(
            "shade",
            "concept",
            "Shade summary.",
            page_family="topic-concept",
            sources=("raw/sword.pdf",),
        ),
        _ExplodingWriter(),
        max_attempts=1,
    )

    assert attempt.page is None
    assert attempt.record is None
    assert _finding_types(attempt.findings) == {"article-writer-error"}


def test_forge_human_article_writer_uses_structured_tool_with_full_evidence() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [
                                    {
                                        "block_id": "b1",
                                        "block_kind": "paragraph",
                                        "text": "Shade creates darkness around the target.",
                                    }
                                ],
                                "article_claim_ids": ["c1"],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Shade creates darkness around the target.",
                                "support_refs": ["S1"],
                            }
                        ],
                    },
                )
            ]
        ]
    )
    writer = ForgeHumanArticleWriter(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="FULL WIKI SCHEMA SHOULD NOT BE SENT",
    )

    article = writer.write_article(_pack(source_text="Full Shade evidence text."))

    assert article.claims[0].support_refs[0].code == "typed-evidence-record:record-shade"
    sent = json.dumps(client.sent)
    assert "Full Shade evidence text." in sent
    assert "support_alias" in sent
    assert "S1" in sent
    assert "source_text" in sent
    assert "HumanArticle contract" in sent
    assert "FULL WIKI SCHEMA SHOULD NOT BE SENT" not in sent
    assert "typed-evidence-record:record-shade" not in sent
    assert '"summary"' not in sent


def test_forge_human_article_writer_rejects_unclaimed_block_prose() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [
                                    {
                                        "block_id": "b1",
                                        "block_kind": "paragraph",
                                        "text": (
                                            "Unsupported model prose. "
                                            "Shade creates darkness around the target."
                                        ),
                                    }
                                ],
                                "article_claim_ids": ["c1"],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Shade creates darkness around the target.",
                                "support_refs": ["S1"],
                            }
                        ],
                    },
                )
            ]
        ]
    )
    writer = ForgeHumanArticleWriter(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="schema",
        max_iterations=1,
    )

    attempt = write_human_article_page(
        _pack(source_text="Full Shade evidence text."),
        PageMetadata("shade", "concept", "Shade summary.", page_family="topic-concept"),
        writer,
        max_attempts=1,
    )

    assert attempt.page is None
    assert _finding_types(attempt.findings) == {"article-writer-error"}


def test_forge_human_article_writer_rejects_multi_sentence_claims() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [
                                    {
                                        "block_id": "b1",
                                        "block_kind": "paragraph",
                                        "text": "Shade can darken an area with magic.",
                                    }
                                ],
                                "article_claim_ids": ["c1"],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": (
                                    "Shade creates darkness around the target. "
                                    "Shade interacts with will-o-wisp light."
                                ),
                                "support_refs": ["S1"],
                            }
                        ],
                    },
                )
            ]
        ]
    )
    writer = ForgeHumanArticleWriter(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="schema",
        max_iterations=1,
    )
    pack = _pack(source_text="Full Shade evidence text.")

    attempt = write_human_article_page(
        pack,
        PageMetadata("shade", "concept", "Shade summary.", page_family="topic-concept"),
        writer,
        max_attempts=1,
    )

    assert attempt.page is None
    assert _finding_types(attempt.findings) == {"article-writer-error"}


def test_forge_human_article_writer_rejects_unrendered_claims() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [],
                                "article_claim_ids": ["c1", "c2"],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Bonus Damage +2",
                                "support_refs": ["S1"],
                            },
                            {
                                "claim_id": "c2",
                                "sentence": "Critical Target -1",
                                "support_refs": ["S1"],
                            },
                        ],
                    },
                )
            ]
        ]
    )
    writer = ForgeHumanArticleWriter(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="schema",
        max_iterations=1,
    )
    pack = _pack(source_text="Full combat option evidence text.")

    attempt = write_human_article_page(
        pack,
        PageMetadata("shade", "concept", "Shade summary.", page_family="topic-concept"),
        writer,
        max_attempts=1,
    )

    assert attempt.page is None
    assert _finding_types(attempt.findings) == {"article-writer-error"}


def test_forge_human_article_writer_rescues_json_string_blocks() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [
                                    (
                                        '{"block_id":"b1","block_kind":"paragraph",'
                                        '"text":"Shade creates darkness around the target."}'
                                    )
                                ],
                                "article_claim_ids": ["c1"],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Shade creates darkness around the target.",
                                "support_refs": ["S1"],
                            }
                        ],
                    },
                )
            ]
        ]
    )
    writer = ForgeHumanArticleWriter(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="schema",
    )
    pack = _pack(source_text="Full Shade evidence text.")

    article = writer.write_article(pack)

    assert article.sections[0].blocks[0].text == "Shade creates darkness around the target."
    assert validate_human_article(pack, article).accepted


def test_forge_human_article_writer_repairs_after_tool_validation_error() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [
                                    {
                                        "block_id": "b1",
                                        "block_kind": "paragraph",
                                        "text": "Shade can darken an area with magic.",
                                    }
                                ],
                                "article_claim_ids": ["c1"],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Shade creates a region of magical darkness.",
                                "support_refs": ["S1"],
                            }
                        ],
                    },
                )
            ],
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [
                                    {
                                        "block_id": "b1",
                                        "block_kind": "paragraph",
                                        "text": "Shade can darken an area with magic.",
                                    }
                                ],
                                "article_claim_ids": ["c1"],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Shade can darken an area with magic.",
                                "support_refs": ["S1"],
                            }
                        ],
                    },
                )
            ],
        ]
    )
    writer = ForgeHumanArticleWriter(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="schema",
    )
    pack = _pack(
        source_text=(
            "Shade creates a region of magical darkness that affects light in the area."
        )
    )

    article = writer.write_article(pack)

    assert article.claims[0].sentence == "Shade can darken an area with magic."
    assert len(client.sent) == 2


def test_forge_human_article_writer_rejects_unknown_support_alias() -> None:
    client = FakeClient(
        [
            [
                ToolCall(
                    tool="write_article",
                    args={
                        "page_id": "shade",
                        "title": "Shade",
                        "sections": [
                            {
                                "section_id": "overview",
                                "heading": "Overview",
                                "blocks": [
                                    {
                                        "block_id": "b1",
                                        "block_kind": "paragraph",
                                        "text": "Shade creates darkness around the target.",
                                    }
                                ],
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Shade creates darkness around the target.",
                                "support_refs": ["support-1"],
                            }
                        ],
                    },
                )
            ]
        ]
    )
    writer = ForgeHumanArticleWriter(
        client=client,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        schema_text="schema",
        max_iterations=1,
    )

    attempt = write_human_article_page(
        _pack(),
        PageMetadata(
            "shade",
            "concept",
            "Shade summary.",
            page_family="topic-concept",
            sources=("raw/sword.pdf",),
        ),
        writer,
        max_attempts=1,
    )

    assert attempt.page is None
    assert attempt.record is None
    assert _finding_types(attempt.findings) == {"article-writer-error"}


def test_write_human_article_page_includes_exception_type_for_blank_errors() -> None:
    attempt = write_human_article_page(
        _pack(),
        PageMetadata(
            "shade",
            "concept",
            "Shade summary.",
            page_family="topic-concept",
            sources=("raw/sword.pdf",),
        ),
        _BlankErrorWriter(),
        max_attempts=1,
    )

    assert attempt.page is None
    assert attempt.findings[0].message == "Article writer failed: TimeoutError"


def _article(
    sentence: str,
    *,
    pack: EvidencePack | None = None,
    support: SupportRef | None = _SUPPORT,
    related: tuple[ArticleRelatedLink, ...] = (),
) -> HumanArticle:
    selected = pack or _pack()
    support_refs = () if support is None else (support,)
    return HumanArticle(
        selected.page_id,
        selected.title,
        (
            ArticleSection(
                "s1",
                "Overview",
                (ArticleBlock("b1", "paragraph", sentence),),
                ("c1",),
            ),
        ),
        (ArticleClaim("c1", sentence, support_refs),),
        related,
    )


def _pack(
    *,
    page_id: str = "shade",
    title: str = "Shade",
    source_text: str = "one two three four five six seven eight nine ten",
    payload: str = "",
    record_type: str = "rule",
    family: str = "topic-concept",
    profile: str = "rpg-rules",
) -> EvidencePack:
    item = EvidencePackItem(
        support_ref=_SUPPORT,
        typed_evidence_record_id="record-shade",
        evidence_record_type=record_type,
        source_anchors=(_anchor(),),
        source_block_ids=("block-shade",),
        source_text=source_text,
        payload_text=payload,
        citation_label="raw/sword.pdf (p. 59)",
        section_path="Spirit Magic List / Shade",
    )
    return EvidencePack(
        page_id=page_id,
        source_id="source",
        source_hash=_HASH,
        source_profile_kind=profile,
        page_kind="concept",
        page_family=family,
        title=title,
        items=(item,),
        coverage=(
            EvidencePackCoverage(
                page_id,
                family,
                family,
                _SUPPORT,
                "page-purpose-support",
                "covered",
            ),
        ),
    )


def _pack_set(*packs: EvidencePack, profile: str = "rpg-rules") -> EvidencePackSet:
    return EvidencePackSet(
        evidence_pack_set_id="pack-set",
        evidence_pack_set_fingerprint="fingerprint",
        source_id="source",
        source_hash=_HASH,
        source_profile_kind=profile,
        packs=packs,
        findings=(),
    )


def _pack_with_two_items() -> EvidencePack:
    first = _pack().items[0]
    second = EvidencePackItem(
        support_ref=_SECOND_SUPPORT,
        typed_evidence_record_id="record-wisp",
        evidence_record_type="rule",
        source_anchors=(_anchor(),),
        source_block_ids=("block-wisp",),
        source_text="Will-o-wisp creates light.",
        payload_text="Will-o-wisp creates light.",
        citation_label="raw/sword.pdf (p. 59)",
        section_path="Spirit Magic List / Will-o-wisp",
    )
    return EvidencePack(
        page_id="shade",
        source_id="source",
        source_hash=_HASH,
        source_profile_kind="rpg-rules",
        page_kind="concept",
        page_family="topic-concept",
        title="Shade",
        items=(first, second),
        coverage=(
            EvidencePackCoverage(
                "shade",
                "topic-concept",
                "topic-concept",
                _SUPPORT,
                "page-purpose-support",
                "covered",
            ),
            EvidencePackCoverage(
                "shade",
                "topic-concept",
                "topic-concept",
                _SECOND_SUPPORT,
                "page-purpose-support",
                "covered",
            ),
        ),
    )


def _anchor() -> SourceAnchor:
    return SourceAnchor(
        source_locator="sword.pdf",
        source_hash=_HASH,
        page_span=(59, 59),
        element_path=("source", "shade"),
        text_fingerprint="shade",
    )


class _Writer:
    def __init__(self, article: HumanArticle) -> None:
        self.article = article

    def write_article(self, pack: EvidencePack, findings=()) -> HumanArticle:  # type: ignore[no-untyped-def]
        return self.article


class _PackCoherentWriter:
    def write_article(self, pack: EvidencePack, findings=()) -> HumanArticle:  # type: ignore[no-untyped-def]
        sentence = f"{pack.title} has source-backed evidence."
        claim = ArticleClaim("claim-1", sentence, (pack.items[0].support_ref,))
        block = ArticleBlock("block-1", "paragraph", sentence)
        section = ArticleSection("section-1", "Overview", (block,), ("claim-1",))
        return HumanArticle(pack.page_id, pack.title, (section,), (claim,))


class _FailsPageWriter:
    def __init__(self, page_id: str) -> None:
        self.page_id = page_id

    def write_article(self, pack: EvidencePack, findings=()) -> HumanArticle:  # type: ignore[no-untyped-def]
        if pack.page_id == self.page_id:
            raise ValueError("planned failure")
        return _PackCoherentWriter().write_article(pack, findings)


class _ExplodingWriter:
    def write_article(self, pack: EvidencePack, findings=()) -> HumanArticle:  # type: ignore[no-untyped-def]
        raise ValueError("Support ref must be formatted as kind:id, got 'support-1'.")


class _BlankErrorWriter:
    def write_article(self, pack: EvidencePack, findings=()) -> HumanArticle:  # type: ignore[no-untyped-def]
        raise TimeoutError()


def _types(result) -> set[str]:  # type: ignore[no-untyped-def]
    return {finding.finding_type for finding in result.findings}


def _finding_types(findings) -> set[str]:  # type: ignore[no-untyped-def]
    return {finding.finding_type for finding in findings}
