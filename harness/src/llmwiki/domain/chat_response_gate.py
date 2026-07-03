"""Pure response-gating policy for grounded chat turns."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.chat_citations import ChatResponseCitationPolicy

_WIKI_LINK_RE = re.compile(r"\[\[[a-z0-9][a-z0-9-]*\]\]")
_SOURCE_CITATION_RE = re.compile(r"\braw/[a-zA-Z0-9_./-]+|source-range-[a-z0-9]+-\d+")


@dataclass(frozen=True)
class ChatResponseGateConfig:
    allow_index_response: bool = True
    require_wiki_read: bool = True
    require_read_page_citation: bool = False
    require_procedure_execution: bool = False


@dataclass(frozen=True)
class ChatResponseEvidenceState:
    missing_focus_reports: frozenset[str] = frozenset()
    read_page_ids: frozenset[str] | None = None
    index_was_read: bool = False
    procedure_execution_satisfied: bool = True


@dataclass(frozen=True)
class ChatResponseGateDecision:
    allowed: bool
    message: str = ""


def decide_chat_response(
    message: str,
    *,
    config: ChatResponseGateConfig,
    evidence: ChatResponseEvidenceState,
) -> ChatResponseGateDecision:
    if config.require_procedure_execution and not evidence.procedure_execution_satisfied:
        return ChatResponseGateDecision(
            allowed=False,
            message=(
                "Call submit_procedure_execution with a valid ProcedureExecution "
                "before respond. A procedure execution answer must be validated "
                "against the deterministic task evidence pack first."
            ),
        )
    if evidence.missing_focus_reports:
        findings = _chat_response_findings(message)
        if findings:
            return ChatResponseGateDecision(
                allowed=False,
                message=(
                    "Chat answer violates missing-coverage grounding:\n"
                    + "\n".join(f"- {finding}" for finding in findings)
                    + "\nReplace the answer with a cited limitation. Include the inspected "
                    "[[PageId]], raw source locator or source-range id, and do not ask "
                    "the user to continue outside the wiki."
                ),
            )
    if not config.require_wiki_read or evidence.read_page_ids is None:
        return ChatResponseGateDecision(allowed=True)
    if evidence.read_page_ids:
        if config.require_read_page_citation:
            citation = ChatResponseCitationPolicy(
                evidence.read_page_ids
            ).response_decision(message)
            if not citation.allowed:
                return ChatResponseGateDecision(False, citation.message)
        return ChatResponseGateDecision(allowed=True)
    if config.allow_index_response and evidence.index_was_read:
        return ChatResponseGateDecision(allowed=True)
    if config.allow_index_response:
        return ChatResponseGateDecision(
            allowed=False,
            message=(
                "Call read_page for a relevant wiki page, or read_index for a "
                "wiki coverage/catalog question, before respond. Search snippets "
                "alone are not enough evidence for an answer."
            ),
        )
    return ChatResponseGateDecision(
        allowed=False,
        message=(
            "Call read_page for a relevant wiki page before respond. The index "
            "and search snippets are discovery aids, not enough evidence for a "
            "substantive content answer."
        ),
    )


def _chat_response_findings(message: str) -> tuple[str, ...]:
    findings: list[str] = []
    if _WIKI_LINK_RE.search(message) is None:
        findings.append("missing inspected wiki page citation like [[page-id]]")
    if _SOURCE_CITATION_RE.search(message) is None:
        findings.append("missing raw source locator or source-range id")
    if message.rstrip().endswith("?"):
        findings.append("ends with a follow-up question after reporting missing coverage")
    return tuple(findings)
