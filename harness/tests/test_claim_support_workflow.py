"""Tests for Claim Support Audit workflow filing and verdict validation."""

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall
from helpers import wiki_page

from llmwiki.cli import _curator_report
from llmwiki.config import WikiPaths
from llmwiki.domain.claim_support import (
    ClaimSupportCandidate,
    ClaimSupportFinding,
    ClaimSupportSelection,
)
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.claim_support_tools import record_claim_support_verdict_tool

TODAY = "2026-06-22"


def test_verdict_tool_rejects_supported_with_deterministic_findings(
    store: WikiStore,
) -> None:
    store.write_page(
        wiki_page(name="alpha", category="source", summary="A.", body="Body.")
    )
    candidate = _candidate()
    finding = ClaimSupportFinding(
        finding_id="finding-alpha",
        candidate_id=candidate.candidate_id,
        page_id="alpha",
        severity="blocker",
        category="missing-evidence",
        message="No evidence.",
    )
    verdicts = []
    tool = record_claim_support_verdict_tool(store, verdicts, (candidate,), (finding,))

    with pytest.raises(WikiStoreError, match="cannot be recorded as supported"):
        tool.callable(
            candidate_id=candidate.candidate_id,
            verdict="supported",
            rationale="Looks fine.",
            recommended_action="None.",
        )

    assert verdicts == []


def test_candidate_render_uses_bounded_excerpt_evidence_ids() -> None:
    candidate = ClaimSupportCandidate(
        candidate_id="claim-support-summary-alpha-1",
        page_id="alpha",
        claim_text="Alpha is supported.",
        page_context="Alpha is supported. (raw/alpha.md)",
        citation_texts=("raw/alpha.md",),
        source_claim_ids=("source-claim-alpha",),
        evidence_ids=tuple(f"evidence-{index}" for index in range(12)),
        evidence_excerpts=("evidence-7: Alpha is supported.",),
        candidate_kind="source-summary",
    )

    rendered = candidate.render(1)

    assert "### Candidate 1: claim-support-summary-alpha-1" in rendered
    assert "Evidence excerpt ids: evidence-7" in rendered
    assert "evidence-11" not in rendered


def test_candidate_render_limits_evidence_ids_when_excerpts_are_missing() -> None:
    candidate = ClaimSupportCandidate(
        candidate_id="claim-support-summary-alpha-1",
        page_id="alpha",
        claim_text="Alpha is supported.",
        page_context="Alpha is supported. (raw/alpha.md)",
        citation_texts=("raw/alpha.md",),
        source_claim_ids=("source-claim-alpha",),
        evidence_ids=tuple(f"evidence-{index}" for index in range(10)),
        evidence_excerpts=(),
        candidate_kind="source-summary",
    )

    rendered = candidate.render(1)

    assert "Evidence excerpt ids: evidence-0" in rendered
    assert "(2 more not shown)" in rendered
    assert "evidence-9" not in rendered


async def test_session_files_claim_support_report_and_log(
    store: WikiStore, paths: WikiPaths
) -> None:
    store.write_page(
        wiki_page(
            name="alpha",
            category="source",
            summary="A.",
            body="Alpha is supported. (raw/alpha.md)",
        )
    )
    selection = ClaimSupportSelection(
        candidates=(_candidate(),),
        blocked_candidates=(),
        deterministic_findings=(),
        candidate_count=1,
        max_claims=1,
    )
    script = [
        [
            ToolCall(
                tool="record_claim_support_verdict",
                args={
                    "candidate_id": "claim-support-summary-alpha-1",
                    "verdict": "supported",
                    "rationale": "The evidence excerpt states the same claim.",
                    "recommended_action": "No action.",
                },
            )
        ],
        [ToolCall(tool="finish_claim_support", args={"report": "One claim supported."})],
    ]

    result = await _session(store, script, paths).claim_support(selection)

    assert result.op == "claim-support"
    assert "Verdict 1: INFO - supported" in result.output
    assert "- supported: 1" in result.output
    assert "wiki-claim-support" in store.list_pages()
    assert "Claim Support Audit" in store.read_page("wiki-claim-support")
    assert "claim-support | claim support audit" in paths.log_path.read_text()


async def test_session_batches_claim_support_candidates(
    store: WikiStore, paths: WikiPaths
) -> None:
    store.write_page(
        wiki_page(
            name="alpha",
            category="source",
            summary="A.",
            body="Alpha is supported. (raw/alpha.md)",
        )
    )
    candidates = tuple(_candidate(f"claim-support-summary-alpha-{index}") for index in range(6))
    selection = ClaimSupportSelection(
        candidates=candidates,
        blocked_candidates=(),
        deterministic_findings=(),
        candidate_count=6,
        max_claims=6,
    )
    script = [
        *_verdict_calls(candidates[:5]),
        [ToolCall(tool="finish_claim_support", args={"report": "First batch."})],
        *_verdict_calls(candidates[5:]),
        [ToolCall(tool="finish_claim_support", args={"report": "Second batch."})],
    ]

    result = await _session(store, script, paths).claim_support(selection)

    assert "Selected for model judgment: 6" in result.output
    assert "- supported: 6" in result.output
    assert "Verdict 6: INFO - supported" in result.output


async def test_invalid_verdict_label_recovers(store: WikiStore, paths: WikiPaths) -> None:
    store.write_page(wiki_page(name="alpha", category="source", summary="A.", body="Body."))
    selection = ClaimSupportSelection(
        candidates=(_candidate(),),
        blocked_candidates=(),
        deterministic_findings=(),
        candidate_count=1,
        max_claims=1,
    )
    script = [
        [
            ToolCall(
                tool="record_claim_support_verdict",
                args={
                    "candidate_id": "claim-support-summary-alpha-1",
                    "verdict": "maybe",
                    "rationale": "Invalid.",
                    "recommended_action": "None.",
                },
            )
        ],
        [
            ToolCall(
                tool="record_claim_support_verdict",
                args={
                    "candidate_id": "claim-support-summary-alpha-1",
                    "verdict": "unclear",
                    "rationale": "Recovered with valid enum.",
                    "recommended_action": "Review.",
                },
            )
        ],
        [ToolCall(tool="finish_claim_support", args={"report": "Recovered."})],
    ]

    result = await _session(store, script, paths).claim_support(selection)

    assert "maybe" not in result.output
    assert "Verdict 1: WARNING - unclear" in result.output


async def test_curator_status_summarizes_latest_claim_support(
    store: WikiStore, paths: WikiPaths
) -> None:
    store.write_page(
        wiki_page(
            name="wiki-claim-support",
            category="synthesis",
            summary="Claim support.",
            body="# Claim Support Audit\n\nSelected for model judgment: 1",
        )
    )

    report = _curator_report(store, paths, "off")

    assert "Latest Claim Support Audit" in report
    assert "Selected for model judgment: 1" in report


def _session(store: WikiStore, script: list, paths: WikiPaths) -> Session:
    return Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="test-run",
    )


def _candidate(candidate_id: str = "claim-support-summary-alpha-1") -> ClaimSupportCandidate:
    return ClaimSupportCandidate(
        candidate_id=candidate_id,
        page_id="alpha",
        claim_text="Alpha is supported.",
        page_context="Alpha is supported. (raw/alpha.md)",
        citation_texts=("raw/alpha.md",),
        source_claim_ids=("claim-alpha",),
        evidence_ids=("evidence-alpha",),
        evidence_excerpts=("evidence-alpha: Alpha is supported.",),
        candidate_kind="source-summary",
    )


def _verdict_calls(candidates: tuple[ClaimSupportCandidate, ...]) -> list[list[ToolCall]]:
    return [
        [
            ToolCall(
                tool="record_claim_support_verdict",
                args={
                    "candidate_id": candidate.candidate_id,
                    "verdict": "supported",
                    "rationale": "The evidence excerpt states the same claim.",
                    "recommended_action": "No action.",
                },
            )
        ]
        for candidate in candidates
    ]
