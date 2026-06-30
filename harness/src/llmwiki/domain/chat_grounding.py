"""Grounding policy for conversational wiki turns."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from enum import StrEnum

from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, PageMetadata, parse_page
from llmwiki.domain.search import SearchHit

_AGGREGATE_PAGE_FAMILIES = frozenset({"source-manifest", "broad-topic"})
_FOCUSED_PAGE_FAMILIES = frozenset(
    {
        "source-summary",
        "section-reference",
        "topic-concept",
        "procedure-guide",
        "entity-profile",
        "cross-source-synthesis",
    }
)
_SUGGESTED_FOCUSED_PAGES = 4


class ChatEvidenceMode(StrEnum):
    PAGE = "page"
    CATALOG_OR_PAGE = "catalog-or-page"
    CONVERSATION = "conversation"


class ChatTaskMode(StrEnum):
    NONE = "none"
    EXPLAIN_PROCEDURE = "explain-procedure"
    EXECUTE_PROCEDURE = "execute-procedure"
    SOURCE_AUDIT = "source-audit"


@dataclass(frozen=True)
class ChatGroundingPlan:
    evidence_mode: ChatEvidenceMode
    include_index: bool
    include_search_results: bool
    task_mode: ChatTaskMode = ChatTaskMode.NONE

    @property
    def allow_index_response(self) -> bool:
        return self.evidence_mode in {
            ChatEvidenceMode.CATALOG_OR_PAGE,
            ChatEvidenceMode.CONVERSATION,
        }

    @property
    def require_wiki_read(self) -> bool:
        return self.evidence_mode is not ChatEvidenceMode.CONVERSATION


@dataclass(frozen=True)
class ChatEvidenceCandidate:
    page_id: str
    score: int
    page_family: str

    @property
    def is_aggregate(self) -> bool:
        return self.page_family in _AGGREGATE_PAGE_FAMILIES

    @property
    def is_focused(self) -> bool:
        if not self.page_family:
            return True
        return self.page_family in _FOCUSED_PAGE_FAMILIES


@dataclass(frozen=True)
class ChatEvidenceReadDecision:
    allowed: bool
    message: str = ""


@dataclass(frozen=True)
class ChatResponseCitationDecision:
    allowed: bool
    message: str = ""


@dataclass(frozen=True)
class ChatResponseCitationPolicy:
    """Citation contract for a chat answer grounded in read wiki pages."""

    read_page_ids: frozenset[str]

    def response_decision(self, message: str) -> ChatResponseCitationDecision:
        if not self.read_page_ids:
            return ChatResponseCitationDecision(allowed=True)
        cited_read_pages = extract_links(message) & self.read_page_ids
        if cited_read_pages:
            return ChatResponseCitationDecision(allowed=True)
        suggestions = ", ".join(f"[[{page_id}]]" for page_id in sorted(self.read_page_ids)[:3])
        return ChatResponseCitationDecision(
            allowed=False,
            message=(
                "Cite at least one wiki page read for this answer with a [[page-id]] "
                f"link, such as {suggestions}. Raw source citations alone are not "
                "enough because the chat answer must identify the wiki evidence page."
            ),
        )


@dataclass(frozen=True)
class ChatEvidenceScope:
    """The evidence pages a content chat turn discovered before tool use."""

    candidates: tuple[ChatEvidenceCandidate, ...] = ()

    @classmethod
    def from_search_hits(
        cls, pages: Mapping[str, str], hits: Sequence[SearchHit]
    ) -> ChatEvidenceScope:
        candidates: list[ChatEvidenceCandidate] = []
        for hit in hits:
            text = pages.get(hit.name)
            if text is None:
                continue
            try:
                page = parse_page(text)
            except PageError:
                continue
            candidates.append(
                ChatEvidenceCandidate(
                    page_id=hit.name,
                    score=hit.score,
                    page_family=page.page_metadata.page_family,
                )
            )
        return cls(tuple(candidates))

    def read_decision(self, metadata: PageMetadata) -> ChatEvidenceReadDecision:
        if metadata.page_family not in _AGGREGATE_PAGE_FAMILIES:
            return ChatEvidenceReadDecision(allowed=True)
        focused = self._focused_candidates()
        if not focused:
            return ChatEvidenceReadDecision(allowed=True)
        aggregate_score = self._candidate_score(metadata.page_id)
        best_focused_score = max(candidate.score for candidate in focused)
        if aggregate_score > best_focused_score:
            return ChatEvidenceReadDecision(allowed=True)
        suggestions = ", ".join(f"[[{candidate.page_id}]]" for candidate in focused[:4])
        return ChatEvidenceReadDecision(
            allowed=False,
            message=(
                f"Do not use [[{metadata.page_id}]] as evidence for this focused "
                f"lookup: it is a broad {metadata.page_family} page, and the "
                "current search scope has more focused pages with at least as "
                f"much relevance. Read one of these instead: {suggestions}."
            ),
        )

    def _focused_candidates(self) -> tuple[ChatEvidenceCandidate, ...]:
        focused = tuple(candidate for candidate in self.candidates if candidate.is_focused)
        return tuple(
            sorted(
                focused,
                key=lambda candidate: (-candidate.score, candidate.page_id),
            )[:_SUGGESTED_FOCUSED_PAGES]
        )

    def _candidate_score(self, page_id: str) -> int:
        for candidate in self.candidates:
            if candidate.page_id == page_id:
                return candidate.score
        return 0


_CATALOG_TERMS = re.compile(
    r"\b("
    r"catalog|coverage|cover|covers|covered|index|pages?|sources?|"
    r"what\s+is\s+this\s+wiki\s+about|what\s+does\s+this\s+wiki"
    r")\b",
    re.IGNORECASE,
)

_CONVERSATION_FOLLOWUP = re.compile(
    r"^\s*("
    r"shorter(?:\s+please)?|"
    r"say\s+that\s+shorter|"
    r"make\s+(?:that|it)\s+shorter|"
    r"more\s+concise|"
    r"summarize\s+(?:that|it)|"
    r"rephrase\s+(?:that|it)|"
    r"rewrite\s+(?:that|it)|"
    r"clean\s+(?:that|it)\s+up|"
    r"tl;?dr|"
    r"go\s+on|"
    r"continue(?:\s+(?:that|it))?"
    r")\s*[.!?]?\s*$",
    re.IGNORECASE,
)

_PROCEDURE_EXPLANATION = re.compile(
    r"\b(how\s+do\s+i|how\s+to|steps?|procedure|workflow|process)\b",
    re.IGNORECASE,
)

_PROCEDURE_EXECUTION = re.compile(
    r"\b("
    r"actually\s+(create|make|build|generate|run|do)|"
    r"(create|make|build|generate)\s+(?:a|an|the|new)\b|"
    r"run\s+(?:the\s+)?(procedure|workflow|process)|"
    r"walk\s+through\s+(creating|making|building|generating)"
    r")\b",
    re.IGNORECASE,
)

_SOURCE_AUDIT = re.compile(
    r"\b(compare|check|verify|validate|audit|match)\b.*\b("
    r"source\s+material|source|sources|evidence|wiki\s+evidence"
    r")\b",
    re.IGNORECASE,
)


def plan_chat_grounding(question: str, *, grounded: bool, has_window: bool) -> ChatGroundingPlan:
    if _is_catalog_question(question):
        return ChatGroundingPlan(
            evidence_mode=ChatEvidenceMode.CATALOG_OR_PAGE,
            include_index=True,
            include_search_results=False,
            task_mode=_task_mode(question),
        )
    if has_window and _is_conversation_followup(question):
        return ChatGroundingPlan(
            evidence_mode=ChatEvidenceMode.CONVERSATION,
            include_index=False,
            include_search_results=False,
        )
    return ChatGroundingPlan(
        evidence_mode=ChatEvidenceMode.PAGE,
        include_index=False,
        include_search_results=True,
        task_mode=_task_mode(question),
    )


def render_grounded_user_message(
    question: str,
    plan: ChatGroundingPlan,
    *,
    index_text: str = "",
    search_results: str = "",
) -> str:
    if plan.include_index:
        return (
            f"The wiki's index - the catalog of every page:\n\n{index_text}\n\nQuestion: {question}"
        )
    if plan.include_search_results:
        task_guidance = _task_guidance(plan.task_mode)
        return (
            "Initial wiki search results for the question. These are discovery "
            "hints, not enough evidence for a substantive answer; read a "
            "relevant page before responding.\n\n"
            f"{search_results}\n\n"
            f"{task_guidance}"
            f"Question: {question}"
        )
    return question


def _is_catalog_question(question: str) -> bool:
    normalized = " ".join(question.lower().split())
    if _is_source_audit(normalized):
        return False
    return _CATALOG_TERMS.search(normalized) is not None


def _is_conversation_followup(question: str) -> bool:
    normalized = " ".join(question.lower().split())
    return _CONVERSATION_FOLLOWUP.search(normalized) is not None


def _task_mode(question: str) -> ChatTaskMode:
    normalized = " ".join(question.lower().split())
    if _is_source_audit(normalized):
        return ChatTaskMode.SOURCE_AUDIT
    asks_for_explanation = _PROCEDURE_EXPLANATION.search(normalized) is not None
    if _PROCEDURE_EXECUTION.search(normalized) and not asks_for_explanation:
        return ChatTaskMode.EXECUTE_PROCEDURE
    if asks_for_explanation:
        return ChatTaskMode.EXPLAIN_PROCEDURE
    return ChatTaskMode.NONE


def _task_guidance(task_mode: ChatTaskMode) -> str:
    if task_mode is ChatTaskMode.EXECUTE_PROCEDURE:
        return (
            "Task intent: execute the relevant procedure, not merely summarize it. "
            "Read the best procedure page and any linked evidence pages needed for "
            "specific choices, tables, formulas, or constraints. If the user did not "
            "provide choices or random results, make explicit assumptions or use "
            "source-provided worked examples; label those assumptions in the answer. "
            "Do not fill missing table or formula details from memory; when the "
            "needed rule detail is not available in the read wiki pages, mark that "
            "field unresolved instead of inventing it. Return a completed procedure "
            "output, not a future-tense plan: include one concrete result or "
            "explicit unresolved note for each procedure step. Cite the wiki pages "
            "read.\n\n"
        )
    if task_mode is ChatTaskMode.SOURCE_AUDIT:
        return (
            "Task intent: audit a previous answer against source material. Use the "
            "conversation history to identify the answer being checked, then read "
            "the procedure or evidence pages cited in that answer before responding. "
            "Report matches, mismatches, unsupported fields, and corrections with "
            "wiki page citations.\n\n"
        )
    if task_mode is ChatTaskMode.EXPLAIN_PROCEDURE:
        return (
            "Task intent: explain the relevant procedure. Prefer procedure pages "
            "when present, and cite the wiki pages read.\n\n"
        )
    return ""


def _is_source_audit(normalized_question: str) -> bool:
    return _SOURCE_AUDIT.search(normalized_question) is not None
