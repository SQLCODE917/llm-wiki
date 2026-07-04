"""Diagnostic domain behavior."""

from __future__ import annotations

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswer,
    DiagnosticFinding,
    DiagnosticFindingSet,
    DiagnosticQuestion,
    DiagnosticQuestionSet,
)
from llmwiki.domain.diagnostic_defaults import CorpusDiagnosticAnswerer, EvidenceDiagnosticJudge
from llmwiki.domain.diagnostics import (
    answer_diagnostic_questions,
    build_diagnostic_question_set,
    build_repair_task_set,
    diagnostic_answer_corpus_from_pages,
    diagnostic_finding,
)
from llmwiki.domain.ledger.evidence_pack import (
    EvidencePack,
    EvidencePackCoverage,
    EvidencePackItem,
    EvidencePackSet,
    SupportRef,
)
from llmwiki.domain.ledger.page_publication import PageCandidate, PagePublicationPlan
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.source_map import SourceAnchor

_HASH = "abc123"


def test_diagnostic_builder_creates_pack_questions_and_shade_interaction() -> None:
    pack = _pack(
        page_id="sword-shade",
        title="Shade",
        source_text="If a shade comes into contact with a will-o-wisp, their effects interact.",
    )
    question_set = build_diagnostic_question_set(
        source_id="sword",
        source_hash=_HASH,
        pack_set=_pack_set((pack,)),
        publication_plan=_publication_plan((pack,)),
    )

    assert len(question_set.questions) == 1
    assert question_set.questions[0].question_text == "How does Shade interact with will-o-wisp?"
    assert question_set.questions[0].expected_support_refs == (pack.items[0].support_ref.code,)


def test_answerer_uses_wiki_corpus_only() -> None:
    question = _question()
    page = WikiPage.from_metadata(
        PageMetadata("sword-shade", "concept", "Shade page.", page_family="topic-concept"),
        "# Shade\n\nWiki-only answer text.\n",
    )

    answer_set = answer_diagnostic_questions(
        _question_set((question,)),
        diagnostic_answer_corpus_from_pages((page,)),
        CorpusDiagnosticAnswerer(),
    )

    assert answer_set.answers[0].answer_text == "Wiki-only answer text."
    assert "raw source" not in answer_set.answers[0].answer_text


def test_default_judge_records_missing_and_unsupported_answers() -> None:
    judge = EvidenceDiagnosticJudge()
    question = _question()
    pack = _pack()

    missing = judge.judge_diagnostic_answer(
        question,
        DiagnosticAnswer(question.diagnostic_question_id, "", ()),
        pack,
    )
    unsupported = judge.judge_diagnostic_answer(
        question,
        DiagnosticAnswer(
            question.diagnostic_question_id,
            "Invented unsupported answer.",
            ("sword-shade",),
        ),
        pack,
    )

    assert missing[0].finding_code == "missing-answer"
    assert unsupported[0].finding_code == "unsupported-answer"


def test_repair_planner_creates_tasks_from_blocking_findings() -> None:
    question = _question()
    finding_set = _finding_set((diagnostic_finding(question, "unsupported-answer", "unsupported"),))

    task_set = build_repair_task_set(finding_set)

    assert len(task_set.tasks) == 1
    assert task_set.tasks[0].repair_kind == "rewrite-human-article"
    assert task_set.tasks[0].target_page_id == "sword-shade"


def _question() -> DiagnosticQuestion:
    pack = _pack()
    return build_diagnostic_question_set(
        source_id="sword",
        source_hash=_HASH,
        pack_set=_pack_set((pack,)),
        publication_plan=_publication_plan((pack,)),
    ).questions[0]


def _question_set(questions: tuple[DiagnosticQuestion, ...]) -> DiagnosticQuestionSet:
    return DiagnosticQuestionSet(
        "questions", "fingerprint", ARTIFACT_FORMAT, "sword", _HASH, questions
    )


def _finding_set(findings: tuple[DiagnosticFinding, ...]) -> DiagnosticFindingSet:
    return DiagnosticFindingSet(
        "findings", "fingerprint", ARTIFACT_FORMAT, "sword", _HASH, findings
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
        (SourceAnchor("sword.md", _HASH, (1, 1), ("source", page_id), page_id),),
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
