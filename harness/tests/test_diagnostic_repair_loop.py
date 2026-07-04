"""Diagnostic question and repair-loop behavior."""

from __future__ import annotations

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswer,
    DiagnosticAnswerCorpus,
    DiagnosticFinding,
    DiagnosticQuestion,
)
from llmwiki.domain.diagnostics import diagnostic_finding
from llmwiki.domain.ledger.article_lint_artifacts import ArticleLintArtifact
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
    ArticleFinding,
    ArticleSection,
    HumanArticle,
)
from llmwiki.domain.ledger.page_publication import PageCandidate, PagePublicationPlan
from llmwiki.domain.source_map import SourceAnchor
from llmwiki.runtime.diagnostic_repair_loop import run_diagnostic_repair_loop
from llmwiki.runtime.ledger_human_article_pages import (
    HumanArticleLinkedPages,
    build_human_article_linked_pages,
)

TODAY = "2026-07-04"
_HASH = "abc123"


class RepairingWriter:
    def write_article(
        self, pack: EvidencePack, findings: tuple[ArticleFinding, ...] = ()
    ) -> HumanArticle:
        verb = "Repaired" if findings else "Initial"
        sentence = f"{verb} {pack.title} answer uses wiki evidence."
        return _article(pack, sentence)


class ClippedRepairWriter:
    def write_article(
        self, pack: EvidencePack, findings: tuple[ArticleFinding, ...] = ()
    ) -> HumanArticle:
        sentence = (
            "The shade is also very fragile and will easily."
            if findings
            else f"Initial {pack.title} answer uses wiki evidence."
        )
        return _article(pack, sentence)


class StaticAnswerer:
    def answer_diagnostic_question(
        self, question: DiagnosticQuestion, _corpus: DiagnosticAnswerCorpus
    ) -> DiagnosticAnswer:
        return DiagnosticAnswer(
            question.diagnostic_question_id,
            "Invented unsupported answer.",
            question.page_ids,
        )


class ShadeFindingJudge:
    def judge_diagnostic_answer(
        self,
        question: DiagnosticQuestion,
        _answer: DiagnosticAnswer,
        pack: EvidencePack | None,
    ) -> tuple[DiagnosticFinding, ...]:
        if pack is not None and "Shade" in pack.title:
            return (
                diagnostic_finding(
                    question,
                    "unsupported-answer",
                    "answer invented a Shade effect",
                ),
            )
        return ()


def test_repair_loop_rewrites_only_targeted_pages() -> None:
    shade = _pack(page_id="sword-shade", title="Shade")
    brownie = _pack(page_id="sword-brownie", title="Brownie")
    initial = build_human_article_linked_pages(
        evidence_pack_set=_pack_set((shade, brownie)),
        source_locator="sword.md",
        today=TODAY,
        article_writer=RepairingWriter(),
    )

    result = run_diagnostic_repair_loop(
        source_locator="sword.md",
        source_id="sword",
        source_hash=_HASH,
        today=TODAY,
        publication_plan=_publication_plan((shade, brownie)),
        pack_set=_pack_set((shade, brownie)),
        initial_human_articles=initial,
        initial_article_lint=initial_lint(initial),
        article_writer=RepairingWriter(),
        diagnostic_answerer=StaticAnswerer(),
        diagnostic_judge=ShadeFindingJudge(),
    )

    pages = {page.page_id: page.page_body for page in result.final_human_articles.pages}
    assert result.repair_run.changed_page_ids == ("sword-shade",)
    assert "Repaired Shade" in pages["sword-shade"]
    assert "Initial Brownie" in pages["sword-brownie"]


def test_clipped_repair_attempt_is_rejected_and_previous_page_is_kept() -> None:
    shade = _pack(
        page_id="sword-shade",
        title="Shade",
        source_text="The shade is also very fragile and will easily collapse in bright light.",
    )
    initial = build_human_article_linked_pages(
        evidence_pack_set=_pack_set((shade,)),
        source_locator="sword.md",
        today=TODAY,
        article_writer=ClippedRepairWriter(),
    )

    result = run_diagnostic_repair_loop(
        source_locator="sword.md",
        source_id="sword",
        source_hash=_HASH,
        today=TODAY,
        publication_plan=_publication_plan((shade,)),
        pack_set=_pack_set((shade,)),
        initial_human_articles=initial,
        initial_article_lint=initial_lint(initial),
        article_writer=ClippedRepairWriter(),
        diagnostic_answerer=StaticAnswerer(),
        diagnostic_judge=ShadeFindingJudge(),
    )

    page = result.final_human_articles.pages[0]
    assert result.repair_run.changed_page_ids == ()
    assert result.repair_run.rejected_page_ids == ("sword-shade",)
    assert "Initial Shade" in page.page_body
    assert "will easily" not in page.page_body


def initial_lint(initial: HumanArticleLinkedPages) -> ArticleLintArtifact:
    from llmwiki.domain.ledger.article_lint_artifacts import build_article_lint_artifact

    return build_article_lint_artifact(source_hash=_HASH, runs=initial.article_lint_runs)


def _article(pack: EvidencePack, sentence: str) -> HumanArticle:
    return HumanArticle(
        pack.page_id,
        pack.title,
        (ArticleSection("s1", "Overview", (ArticleBlock("b1", "paragraph", sentence),)),),
        (ArticleClaim("c1", sentence, (pack.items[0].support_ref,)),),
    )


def _pack_set(packs: tuple[EvidencePack, ...]) -> EvidencePackSet:
    return EvidencePackSet("packs", "fingerprint", "sword", _HASH, "rpg-rules", packs, ())


def _publication_plan(packs: tuple[EvidencePack, ...]) -> PagePublicationPlan:
    return PagePublicationPlan(
        "plan",
        "fingerprint",
        "sword",
        _HASH,
        "rpg-rules",
        "budget",
        tuple(_candidate_like(pack) for pack in packs),
        tuple(),
        tuple(),
    )


def _candidate_like(pack: EvidencePack) -> PageCandidate:
    return PageCandidate(
        f"candidate-{pack.page_id}",
        "sword",
        _HASH,
        "rpg-rules",
        pack.page_id,
        pack.title,
        pack.page_kind,
        pack.page_family,
        "test",
        1.0,
        1,
        tuple(item.typed_evidence_record_id for item in pack.items),
    )


def _pack(
    *,
    page_id: str = "sword-shade",
    title: str = "Shade",
    source_text: str = "Shade creates darkness around a target.",
) -> EvidencePack:
    support = SupportRef("typed-evidence-record", f"record-{page_id}")
    item = EvidencePackItem(
        support,
        support.support_id,
        "rule",
        (_anchor(page_id),),
        (f"block-{page_id}",),
        source_text,
        "",
        "raw/sword.md (p. 1)",
        title,
    )
    return EvidencePack(
        page_id,
        "sword",
        _HASH,
        "rpg-rules",
        "concept",
        "topic-concept",
        title,
        (item,),
        (
            EvidencePackCoverage(
                page_id,
                "topic-concept",
                "topic-concept",
                support,
                "support",
                "covered",
            ),
        ),
    )


def _anchor(page_id: str) -> SourceAnchor:
    return SourceAnchor("sword.md", _HASH, (1, 1), ("source", page_id), page_id)
