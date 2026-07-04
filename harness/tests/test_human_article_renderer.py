from __future__ import annotations

import json

from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.domain.ledger.evidence_pack import (
    EvidencePack,
    EvidencePackCoverage,
    EvidencePackItem,
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
from llmwiki.runtime.ledger_human_article_pages import write_human_article_page

_HASH = "d" * 64
_SUPPORT = SupportRef("typed-evidence-record", "record-shade")


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
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "c1",
                                "sentence": "Shade creates darkness around the target.",
                                "support_refs": ["typed-evidence-record:record-shade"],
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

    article = writer.write_article(_pack(source_text="Full Shade evidence text."))

    assert article.claims[0].support_refs[0].code == "typed-evidence-record:record-shade"
    sent = json.dumps(client.sent)
    assert "Full Shade evidence text." in sent
    assert "source_text" in sent
    assert '"summary"' not in sent


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
        (ArticleSection("s1", "Overview", (ArticleBlock("b1", "paragraph", sentence),)),),
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
        source_profile_kind="rpg-rules",
        page_kind="concept",
        page_family="topic-concept",
        title=title,
        items=(item,),
        coverage=(
            EvidencePackCoverage(
                page_id,
                "topic-concept",
                "topic-concept",
                _SUPPORT,
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


def _types(result) -> set[str]:  # type: ignore[no-untyped-def]
    return {finding.finding_type for finding in result.findings}


def _finding_types(findings) -> set[str]:  # type: ignore[no-untyped-def]
    return {finding.finding_type for finding in findings}
