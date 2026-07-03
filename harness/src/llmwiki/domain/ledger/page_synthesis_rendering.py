"""Render accepted page drafts to markdown and projection coverage."""

from __future__ import annotations

from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.coverage import (
    PageBodyBuilder,
    PageTextRange,
    ProjectionCoverage,
    ProjectionCoverageEntry,
    RenderedPage,
)
from llmwiki.domain.ledger.page_synthesis import (
    DraftBlock,
    DraftClaim,
    DraftEvidenceCard,
    PageDraft,
    PageSynthesisPlan,
)


def render_page_draft(plan: PageSynthesisPlan, draft: PageDraft) -> RenderedPage:
    body = PageBodyBuilder()
    entries: list[ProjectionCoverageEntry] = []
    claims = {_normalize(claim.sentence): claim for claim in draft.claims}
    cards = {card.evidence_ref.code: card for card in plan.selected_evidence}

    body.add(f"# {draft.title}\n\n")
    for block in draft.blocks:
        if block.heading:
            body.add(f"## {block.heading}\n\n")
        _render_block(body, entries, plan, block, claims, cards)
    _render_related_links(body, entries, plan)
    _render_source_trail(body, plan)
    text = body.text()
    return RenderedPage(text, short_digest(text, 32), ProjectionCoverage(tuple(entries)))


def _render_block(
    body: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    plan: PageSynthesisPlan,
    block: DraftBlock,
    claims: dict[str, DraftClaim],
    cards: dict[str, DraftEvidenceCard],
) -> None:
    if block.block_kind == "paragraph":
        span = body.add(_render_claim_text(block.text, claims, cards) + "\n\n")
        _append_coverage(entries, plan, block.text, claims, span)
        return
    if block.block_kind == "bullet-list":
        for item in block.items:
            span = body.add(f"- {_render_claim_text(item, claims, cards)}\n")
            _append_coverage(entries, plan, item, claims, span)
        body.add("\n")
        return
    if block.block_kind == "numbered-list":
        for index, item in enumerate(block.items, start=1):
            span = body.add(f"{index}. {_render_claim_text(item, claims, cards)}\n")
            _append_coverage(entries, plan, item, claims, span)
        body.add("\n")
        return
    if block.block_kind == "table" and block.table_rows:
        _render_table(body, block.table_rows)


def _render_claim_text(
    text: str, claims: dict[str, DraftClaim], cards: dict[str, DraftEvidenceCard]
) -> str:
    claim = claims.get(_normalize(text))
    if claim is None:
        return text.strip()
    citations = _claim_citations(claim, cards)
    if not citations:
        return claim.sentence.strip()
    return f"{claim.sentence.strip()} _({'; '.join(citations)})_"


def _claim_citations(claim: DraftClaim, cards: dict[str, DraftEvidenceCard]) -> tuple[str, ...]:
    citations: list[str] = []
    for support_ref in claim.support_refs:
        card = cards.get(support_ref.code)
        if card is None:
            continue
        citation = card.citation or _citation(card)
        if citation not in citations:
            citations.append(citation)
    return tuple(citations)


def _citation(card: DraftEvidenceCard) -> str:
    if card.source_range_id:
        return f"raw/{card.source_locator} ({card.source_range_id})"
    return f"raw/{card.source_locator}"


def _render_table(body: PageBodyBuilder, rows: tuple[tuple[str, ...], ...]) -> None:
    header = rows[0]
    body.add("| " + " | ".join(header) + " |\n")
    body.add("| " + " | ".join("---" for _ in header) + " |\n")
    for row in rows[1:]:
        body.add("| " + " | ".join(row) + " |\n")
    body.add("\n")


def _render_related_links(
    body: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    plan: PageSynthesisPlan,
) -> None:
    if not plan.related_links:
        return
    body.add("## Related pages\n\n")
    for link in plan.related_links:
        reason = link.relation.strip() or "source-backed relation"
        span = body.add(f"- [[{link.page_id}]] - {reason}\n")
        entries.append(
            _coverage_entry(
                plan,
                "related-page-link",
                span,
                draft_claim_id="",
                support_refs=tuple(ref.code for ref in link.support_refs),
            )
        )
    body.add("\n")


def _render_source_trail(body: PageBodyBuilder, plan: PageSynthesisPlan) -> None:
    body.add("## Source Trail\n\n")
    body.add(f"- Source manifest: [[{plan.source_page_id}]]\n")
    for section_page_id in plan.source_section_page_ids:
        body.add(f"- Source section: [[{section_page_id}]]\n")


def _append_coverage(
    entries: list[ProjectionCoverageEntry],
    plan: PageSynthesisPlan,
    sentence: str,
    claims: dict[str, DraftClaim],
    span: PageTextRange,
) -> None:
    claim = claims.get(_normalize(sentence))
    if claim is None:
        return
    support_codes = tuple(ref.code for ref in claim.support_refs)
    entries.append(
        _coverage_entry(
            plan,
            "draft-claim",
            span,
            draft_claim_id=claim.claim_id,
            support_refs=support_codes,
        )
    )


def _coverage_entry(
    plan: PageSynthesisPlan,
    unit_kind: str,
    span: PageTextRange,
    *,
    draft_claim_id: str,
    support_refs: tuple[str, ...],
) -> ProjectionCoverageEntry:
    ledger_ids = tuple(
        ref.removeprefix("ledger:") for ref in support_refs if ref.startswith("ledger:")
    )
    atom_ids = tuple(ref.removeprefix("atom:") for ref in support_refs if ref.startswith("atom:"))
    entry_id = deterministic_id(
        "projection-coverage-entry",
        plan.page_id,
        unit_kind,
        f"{span.start}-{span.end}",
        draft_claim_id,
        "|".join(support_refs),
    )
    return ProjectionCoverageEntry(
        projection_coverage_entry_id=entry_id,
        projection_coverage_unit_kind=unit_kind,
        page_text_range=span,
        selected_ledger_entry_ids=ledger_ids,
        technical_atom_id=atom_ids[0] if atom_ids else "",
        draft_claim_id=draft_claim_id,
        draft_support_refs=support_refs,
    )


def _normalize(text: str) -> str:
    return " ".join(text.split()).strip()
