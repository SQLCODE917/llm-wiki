"""Pure chat-turn planning from wiki search inputs."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from llmwiki.domain.chat_evidence_scope import ChatEvidenceScope
from llmwiki.domain.chat_grounding import (
    ChatGroundingPlan,
    ChatTaskMode,
    plan_chat_grounding,
    render_grounded_user_message,
)
from llmwiki.domain.search import render_hits, search_pages
from llmwiki.domain.task_evidence import TaskEvidencePack, build_task_evidence_pack


@dataclass(frozen=True)
class ChatTurnContext:
    grounding_plan: ChatGroundingPlan
    index_text: str = ""
    search_results: str = ""
    evidence_scope: ChatEvidenceScope | None = None
    task_evidence_pack: TaskEvidencePack | None = None
    task_evidence_pack_text: str = ""
    require_procedure_execution: bool = False

    @property
    def allow_index_response(self) -> bool:
        return self.grounding_plan.allow_index_response

    @property
    def require_wiki_read(self) -> bool:
        return self.grounding_plan.require_wiki_read

    def render_user_message(self, question: str) -> str:
        return render_grounded_user_message(
            question,
            self.grounding_plan,
            index_text=self.index_text,
            search_results=self.search_results,
            task_evidence_pack=self.task_evidence_pack_text,
        )


def build_chat_turn_context(
    question: str,
    *,
    page_texts: Mapping[str, str],
    index_text: str,
    grounded: bool,
    has_window: bool,
) -> ChatTurnContext:
    plan = plan_chat_grounding(question, grounded=grounded, has_window=has_window)
    if plan.include_index:
        return ChatTurnContext(grounding_plan=plan, index_text=index_text)
    if not plan.include_search_results:
        return ChatTurnContext(grounding_plan=plan)

    hits = search_pages(page_texts, question)
    evidence_scope = ChatEvidenceScope.from_search_hits(page_texts, hits)
    task_pack = build_task_evidence_pack(
        page_texts,
        hits,
        task_mode=plan.task_mode,
    )
    require_execution = task_pack is not None and plan.task_mode is ChatTaskMode.EXECUTE_PROCEDURE
    task_pack_text = (
        task_pack.render(require_procedure_execution=require_execution)
        if task_pack is not None
        else ""
    )
    return ChatTurnContext(
        grounding_plan=plan,
        search_results=render_hits(hits),
        evidence_scope=evidence_scope,
        task_evidence_pack=task_pack,
        task_evidence_pack_text=task_pack_text,
        require_procedure_execution=require_execution,
    )
