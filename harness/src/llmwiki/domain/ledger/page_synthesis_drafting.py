"""Draft production contracts for page synthesis."""

from __future__ import annotations

from typing import Protocol

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.page_synthesis import (
    DraftBlock,
    DraftClaim,
    DraftEvidenceCard,
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


class DeterministicPageDraftProducer:
    """Local structured producer used for batch projection and tests.

    Forge/Ollama-backed producers can implement the same protocol. This producer
    keeps ingest deterministic by drafting only from plan evidence cards.
    """

    def draft_page(
        self,
        plan: PageSynthesisPlan,
        findings: tuple[PageSynthesisFinding, ...] = (),
    ) -> PageDraft:
        blocks: list[DraftBlock] = []
        claims: list[DraftClaim] = []
        cards = {card.evidence_ref.code: card for card in plan.selected_evidence}
        seen_sentences: set[str] = set()
        for index, section in enumerate(plan.outline, start=1):
            section_cards = tuple(
                card for ref in section.support_refs if (card := cards.get(ref.code)) is not None
            )
            sentence_cards = []
            for card in section_cards:
                sentence = _card_sentence(plan, card)
                if not sentence or sentence in seen_sentences:
                    continue
                sentence_cards.append((sentence, card))
                seen_sentences.add(sentence)
            if not sentence_cards:
                continue
            sentences = tuple(sentence for sentence, _ in sentence_cards)
            block = _draft_block(
                plan.page_id,
                index,
                section.heading,
                section.block_kind,
                sentences,
            )
            blocks.append(block)
            for offset, (sentence, card) in enumerate(sentence_cards, start=1):
                claims.append(
                    DraftClaim(
                        claim_id=deterministic_id(
                            "draft-claim",
                            plan.page_id,
                            str(index),
                            str(offset),
                            card.evidence_ref.code,
                            sentence,
                        ),
                        sentence=sentence,
                        support_refs=(card.evidence_ref,),
                    )
                )
        return PageDraft(
            page_id=plan.page_id,
            title=plan.title,
            blocks=tuple(blocks),
            claims=tuple(claims),
        )


def _draft_block(
    page_id: str,
    index: int,
    heading: str,
    block_kind: str,
    sentences: tuple[str, ...],
) -> DraftBlock:
    block_id = deterministic_id("draft-block", page_id, str(index), heading)
    if block_kind == "paragraph":
        return DraftBlock(
            block_id=block_id,
            block_kind="paragraph",
            heading=heading,
            text=sentences[0],
        )
    if block_kind == "numbered-list":
        return DraftBlock(
            block_id=block_id,
            block_kind="numbered-list",
            heading=heading,
            items=sentences,
        )
    return DraftBlock(block_id=block_id, block_kind="bullet-list", heading=heading, items=sentences)


def _card_sentence(plan: PageSynthesisPlan, card: DraftEvidenceCard) -> str:
    summary = _sentence(card.summary)
    if summary:
        return summary
    section = f" in {card.section_label}" if card.section_label else ""
    return _sentence(f"{plan.title} has selected source support{section}")


def _sentence(text: str) -> str:
    cleaned = " ".join(text.split()).strip(" -")
    if not cleaned:
        return ""
    cleaned = cleaned[0].upper() + cleaned[1:]
    if cleaned[-1] not in ".!?":
        cleaned += "."
    return cleaned
