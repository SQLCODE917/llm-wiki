from __future__ import annotations

from llmwiki.domain.ledger.article_lint import lint_human_article
from llmwiki.domain.ledger.coverage import ProjectionCoverage, RenderedPage
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
)
from llmwiki.domain.ledger.human_article_rendering import render_human_article
from llmwiki.domain.ledger.page_title_lint import lint_page_title
from llmwiki.domain.source_map import SourceAnchor

_HASH = "d" * 64
_SUPPORT = SupportRef("typed-evidence-record", "record-shade")


def test_article_lint_blocks_sentence_without_claim() -> None:
    pack = _pack()
    article = HumanArticle(
        "shade",
        "Shade",
        (
            ArticleSection(
                "s1",
                "Overview",
                (ArticleBlock("b1", "paragraph", "Shade creates darkness."),),
            ),
        ),
        (ArticleClaim("c1", "Different sentence.", (_SUPPORT,)),),
    )

    run = lint_human_article(
        article=article,
        rendered=render_human_article(pack, article),
        pack=pack,
    )

    assert run.publication_gate.decision == "blocked"
    assert _codes(run) >= {"unmapped-factual-sentence"}


def test_article_lint_blocks_unknown_support_ref() -> None:
    missing = SupportRef("typed-evidence-record", "missing")
    pack = _pack()
    article = _article("Shade creates darkness.", support=missing)

    run = lint_human_article(
        article=article,
        rendered=render_human_article(pack, article),
        pack=pack,
    )

    assert run.publication_gate.decision == "blocked"
    assert _codes(run) >= {"unknown-support-ref"}
    assert run.authority_metrics.unknown_support_ref_count == 1


def test_article_lint_blocks_shade_clipped_fragments_and_records_metrics() -> None:
    source = (
        "The shade is also very fragile and will easily disintegrate if exposed "
        "to strong light. Furthermore if an opponent destroys a shade with a "
        "weapon, the opponent will also suffer the same damage. If a shade "
        "itself comes into contact with a will-o-wisp's body or enters the "
        "area lit by it, the shade suffers damage."
    )
    pack = _pack(source_text=source)

    for sentence in (
        "The shade is also very fragile and will easily.",
        "Furthermore if an opponent destroys a will also suffer the same damage.",
        "If a shade itself comes into will -o-wisp's body or enters the area.",
    ):
        article = _article(sentence, pack=pack)
        run = lint_human_article(
            article=article,
            rendered=render_human_article(pack, article),
            pack=pack,
        )

        assert run.publication_gate.decision == "blocked"
        assert "clipped-evidence-fragment" in _codes(run)
        assert run.coherence_metrics.clipped_sentence_count == 1


def test_article_lint_blocks_unreadable_technical_evidence_ids() -> None:
    pack = _pack(payload="Distance=20 meters", record_type="formula")
    article = _article("Shade reaches targets up to twenty meters away.", pack=pack)
    rendered = RenderedPage(
        page_body=(
            "# Shade\n\n"
            "Shade reaches targets up to twenty meters away. _(raw/sword.pdf (p. 59))_\n\n"
            "## Evidence Details\n\n"
            "- typed-evidence-record:record-shade\n"
        ),
        page_body_hash="hash",
        coverage=ProjectionCoverage(()),
    )

    run = lint_human_article(article=article, rendered=rendered, pack=pack)

    assert run.publication_gate.decision == "blocked"
    assert "unreadable-technical-evidence" in _codes(run)
    assert run.coherence_metrics.unreadable_technical_evidence_count == 1


def test_article_lint_blocks_title_findings() -> None:
    pack = _pack(page_id="alway", title="Alway")
    article = _article("Alway has source support.", pack=pack)
    title_findings = lint_page_title("Alway", "alway", "topic-concept")

    run = lint_human_article(
        article=article,
        rendered=render_human_article(pack, article),
        pack=pack,
        title_findings=title_findings,
    )

    assert run.publication_gate.decision == "blocked"
    assert "title-lint-failed" in _codes(run)


def test_article_lint_records_authority_coverage_for_clean_article() -> None:
    pack = _pack()
    article = _article("Shade creates darkness around the target.", pack=pack)

    run = lint_human_article(
        article=article,
        rendered=render_human_article(pack, article),
        pack=pack,
    )

    assert run.publication_gate.decision == "accepted"
    assert run.authority_metrics.factual_sentence_count == 1
    assert run.authority_metrics.cited_factual_sentence_count == 1
    assert run.authority_metrics.authority_coverage_ratio == 1.0


def test_article_lint_blocks_related_links_without_navigation_context() -> None:
    pack = _pack()
    article = _article(
        "Shade creates darkness around the target.",
        pack=pack,
        related=(
            ArticleRelatedLink(
                "will-o-wisp",
                "Will-o-wisp",
                "interaction",
                "",
                (SupportRef("typed-evidence-record", "missing"),),
            ),
        ),
    )

    run = lint_human_article(
        article=article,
        rendered=render_human_article(pack, article),
        pack=pack,
    )

    assert run.publication_gate.decision == "blocked"
    assert _codes(run) >= {
        "missing-related-link-preview",
        "unknown-related-link-support-ref",
    }
    assert run.coherence_metrics.missing_related_preview_count == 1


def test_article_lint_recomputes_after_article_repair() -> None:
    pack = _pack()
    bad = _article("Shade has TODO text.", pack=pack)
    repaired = _article("Shade creates darkness around the target.", pack=pack)

    bad_run = lint_human_article(
        article=bad,
        rendered=render_human_article(pack, bad),
        pack=pack,
    )
    repaired_run = lint_human_article(
        article=repaired,
        rendered=render_human_article(pack, repaired),
        pack=pack,
    )

    assert bad_run.publication_gate.decision == "blocked"
    assert repaired_run.publication_gate.decision == "accepted"


def _article(
    sentence: str,
    *,
    pack: EvidencePack | None = None,
    support: SupportRef = _SUPPORT,
    related: tuple[ArticleRelatedLink, ...] = (),
) -> HumanArticle:
    selected = pack or _pack()
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
        (ArticleClaim("c1", sentence, (support,)),),
        related,
    )


def _pack(
    *,
    page_id: str = "shade",
    title: str = "Shade",
    source_text: str = "Shade creates darkness around the target.",
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


def _codes(run) -> set[str]:  # type: ignore[no-untyped-def]
    return {finding.finding_code for finding in run.findings}
