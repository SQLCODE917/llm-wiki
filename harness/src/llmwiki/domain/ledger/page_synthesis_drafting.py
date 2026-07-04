"""Draft production contracts for page synthesis."""

from __future__ import annotations

from typing import Protocol

from llmwiki.domain.ledger.page_synthesis import (
    PageDraft,
    PageSynthesisFinding,
    PageSynthesisPlan,
)


class PageDraftProducer(Protocol):
    def draft_page(
        self,
        plan: PageSynthesisPlan,
        findings: tuple[PageSynthesisFinding, ...] = (),
    ) -> PageDraft: ...


class RejectingPageDraftProducer:
    """Producer used when no model-backed synthesis implementation is installed.

    The wiki must not publish generated factual prose from evidence labels or
    summaries. Returning an empty draft keeps the pipeline deterministic while
    recording normal validation findings for the rejected page.
    """

    def draft_page(
        self,
        plan: PageSynthesisPlan,
        findings: tuple[PageSynthesisFinding, ...] = (),
    ) -> PageDraft:
        return PageDraft(plan.page_id, plan.title, (), ())
