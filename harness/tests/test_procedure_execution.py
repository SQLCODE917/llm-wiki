from llmwiki.domain.chat_grounding import ChatTaskMode
from llmwiki.domain.procedure_execution import (
    ProcedureExecution,
    ProcedureOutput,
    ProcedureStepResult,
    validate_procedure_execution,
)
from llmwiki.domain.search import SearchHit
from llmwiki.domain.task_evidence import build_task_evidence_pack


def test_task_evidence_pack_follows_procedure_step_links() -> None:
    pack = build_task_evidence_pack(
        _pages(),
        (SearchHit("book-procedure-create-character", 500, "procedure"),),
        task_mode=ChatTaskMode.EXECUTE_PROCEDURE,
    )

    assert pack is not None
    assert pack.procedure_id == "book-procedure-create-character"
    assert [step.title for step in pack.steps] == ["Choose Race", "Record Name"]
    assert pack.page_ids >= {
        "book-procedure-create-character",
        "book-choose-race",
        "book-record-name",
    }
    assert "Deterministic task evidence pack" in pack.render()


def test_task_evidence_pack_lifts_structured_artifacts_from_linked_pages() -> None:
    pack = build_task_evidence_pack(
        _pages(),
        (SearchHit("book-procedure-create-character", 500, "procedure"),),
        task_mode=ChatTaskMode.EXECUTE_PROCEDURE,
    )

    assert pack is not None
    rendered = pack.render()
    assert "Deterministic structured evidence artifacts" in rendered
    assert "Table A: Example Outcomes" in rendered
    assert "roll 8 gives trained operator" in rendered
    assert "calibration-table" in pack.evidence_texts["book-source-section"]


def test_task_evidence_pack_excludes_source_manifest_artifacts() -> None:
    pack = build_task_evidence_pack(
        _pages(),
        (SearchHit("book-procedure-create-character", 500, "procedure"),),
        task_mode=ChatTaskMode.EXECUTE_PROCEDURE,
    )

    assert pack is not None
    rendered = pack.render()
    assert "irrelevant global formula" not in rendered
    assert "book-source-manifest" not in pack.page_ids


def test_task_evidence_pack_supports_explanation_without_execution_tool() -> None:
    pack = build_task_evidence_pack(
        _pages(),
        (SearchHit("book-procedure-create-character", 500, "procedure"),),
        task_mode=ChatTaskMode.EXPLAIN_PROCEDURE,
    )

    assert pack is not None
    rendered = pack.render(require_procedure_execution=False)
    assert "Procedure explanation checklist" in rendered
    assert "submit_procedure_execution" not in rendered


def test_procedure_execution_rejects_missing_step() -> None:
    pack = _pack()
    execution = ProcedureExecution(
        procedure_id=pack.procedure_id,
        step_results=(
            ProcedureStepResult(
                sequence=1,
                title="Choose Race",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="race",
                        value="human",
                        support="evidence",
                        evidence_page_ids=("book-choose-race",),
                    ),
                ),
            ),
        ),
    )

    decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

    assert not decision.allowed
    assert "Missing ProcedureExecution step" in decision.message


def test_procedure_execution_rejects_unsupported_evidence_value() -> None:
    pack = _pack()
    execution = ProcedureExecution(
        procedure_id=pack.procedure_id,
        step_results=(
            ProcedureStepResult(
                sequence=1,
                title="Choose Race",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="race",
                        value="dragon",
                        support="evidence",
                        evidence_page_ids=("book-choose-race",),
                    ),
                ),
            ),
            ProcedureStepResult(
                sequence=2,
                title="Record Name",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="name",
                        value="Aldis",
                        support="assumption",
                    ),
                ),
            ),
        ),
        assumptions=("Aldis is the chosen name.",),
    )

    decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

    assert not decision.allowed
    assert "does not appear" in decision.message


def test_procedure_execution_rejects_derived_terms_absent_from_evidence() -> None:
    pack = _pack()
    execution = ProcedureExecution(
        procedure_id=pack.procedure_id,
        step_results=(
            ProcedureStepResult(
                sequence=1,
                title="Choose Race",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="race",
                        value="human",
                        support="evidence",
                        evidence_page_ids=("book-choose-race",),
                    ),
                ),
            ),
            ProcedureStepResult(
                sequence=2,
                title="Record Name",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="derived-name",
                        value="Druid",
                        support="derived",
                        evidence_page_ids=("book-record-name",),
                        derivation="Use a fantasy class name.",
                    ),
                ),
            ),
        ),
    )

    decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

    assert not decision.allowed
    assert "derives terms absent" in decision.message


def test_procedure_execution_rejects_assumption_terms_absent_from_step_evidence() -> None:
    pack = _pack()
    execution = ProcedureExecution(
        procedure_id=pack.procedure_id,
        step_results=(
            ProcedureStepResult(
                sequence=1,
                title="Choose Race",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="race",
                        value="wizard",
                        support="assumption",
                    ),
                ),
            ),
            ProcedureStepResult(
                sequence=2,
                title="Record Name",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="name",
                        value="Aldis",
                        support="assumption",
                    ),
                ),
            ),
        ),
        assumptions=("Choose a wizard race and the name Aldis.",),
    )

    decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

    assert not decision.allowed
    assert "assumes terms absent" in decision.message


def test_procedure_execution_accepts_evidence_and_declared_assumptions() -> None:
    pack = _pack()
    execution = ProcedureExecution(
        procedure_id=pack.procedure_id,
        step_results=(
            ProcedureStepResult(
                sequence=1,
                title="Choose Race",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="race",
                        value="human",
                        support="evidence",
                        evidence_page_ids=("book-choose-race",),
                    ),
                ),
            ),
            ProcedureStepResult(
                sequence=2,
                title="Record Name",
                status="completed",
                outputs=(
                    ProcedureOutput(
                        name="name",
                        value="Aldis",
                        support="assumption",
                    ),
                ),
            ),
        ),
        assumptions=("Aldis is the chosen character name.",),
    )

    decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

    assert decision.allowed


def test_procedure_execution_accepts_partial_step_note_without_outputs() -> None:
    pack = _pack()
    execution = ProcedureExecution(
        procedure_id=pack.procedure_id,
        step_results=(
            ProcedureStepResult(
                sequence=1,
                title="Choose Race",
                status="partial",
                note="The worked example chooses a human.",
            ),
            ProcedureStepResult(
                sequence=2,
                title="Record Name",
                status="partial",
                note="Name is a free character choice.",
            ),
        ),
    )

    decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

    assert decision.allowed


def _pack():
    pack = build_task_evidence_pack(
        _pages(),
        (SearchHit("book-procedure-create-character", 500, "procedure"),),
        task_mode=ChatTaskMode.EXECUTE_PROCEDURE,
    )
    assert pack is not None
    return pack


def _pages() -> dict[str, str]:
    return {
        "book-procedure-create-character": _page(
            "book-procedure-create-character",
            "procedure",
            "procedure-guide",
            "Create Character.",
            "# Create Character\n\n"
            "From [[book-source-manifest]].\n\n"
            "## Procedure Steps\n\n"
            "1. **Choose Race** (`choose`) - evidence section [[book-choose-race]].\n"
            "2. **Record Name** (`record`) - evidence section [[book-record-name]].\n"
            "\n## Source Trail\n\n- Source section: [[book-source-section]]\n",
        ),
        "book-choose-race": _page(
            "book-choose-race",
            "source",
            "section-reference",
            "Race choices.",
            "# Choose Race\n\nThe race chosen in the worked example is human.",
        ),
        "book-record-name": _page(
            "book-record-name",
            "source",
            "section-reference",
            "Name choice.",
            "# Record Name\n\nNames are a free character choice.",
        ),
        "book-source-manifest": _page(
            "book-source-manifest",
            "source",
            "source-manifest",
            "Aggregate source page.",
            "# Aggregate Source\n\n- For example, an irrelevant global formula is 10 x 10 = 100.\n",
        ),
        "book-source-section": _page(
            "book-source-section",
            "source",
            "section-reference",
            "Structured procedure evidence.",
            "# Source Section\n\n"
            "## Statements\n\n"
            "- For example, roll 8 gives trained operator and 200 starting credits.\n\n"
            "## Technical atoms\n\n"
            "### Technical frame 1: Generic Procedure / Outcomes\n\n"
            "**Context:** _(Manual.pdf (source-range-0001))_\n\n"
            "> Table A: Example Outcomes\n\n"
            "<details><summary>Raw table text</summary>\n\n"
            "```text\n"
            "calibration-table\n"
            "Roll | Outcome | Credits\n"
            "8 | trained operator | 200\n"
            "```\n\n"
            "</details>\n",
        ),
    }


def _page(page_id: str, kind: str, family: str, summary: str, body: str) -> str:
    return (
        "---\n"
        f"page_id: {page_id}\n"
        f"page_kind: {kind}\n"
        f"page_family: {family}\n"
        f"summary: {summary}\n"
        "---\n\n"
        f"{body}\n"
    )
