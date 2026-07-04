"""Render validated human articles to wiki markdown and coverage."""

from __future__ import annotations

from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.coverage import (
    PageBodyBuilder,
    PageTextRange,
    ProjectionCoverage,
    ProjectionCoverageEntry,
    RenderedPage,
)
from llmwiki.domain.ledger.evidence_pack import EvidencePack, EvidencePackItem
from llmwiki.domain.ledger.human_article import ArticleClaim, HumanArticle
from llmwiki.domain.ledger.page_synthesis_text import split_sentences


def render_human_article(pack: EvidencePack, article: HumanArticle) -> RenderedPage:
    body = PageBodyBuilder()
    entries: list[ProjectionCoverageEntry] = []
    claims = {_normalize(claim.sentence): claim for claim in article.claims}
    items = {item.support_ref.code: item for item in pack.items}

    body.add(f"# {article.title}\n\n")
    for section in article.sections:
        body.add(f"## {section.heading}\n\n")
        for block in section.blocks:
            if block.block_kind == "paragraph":
                _render_paragraph(body, entries, pack, block.text, claims, items)
            elif block.block_kind == "bullet-list":
                _render_list(body, entries, pack, block.items, claims, items, ordered=False)
            elif block.block_kind in {"numbered-list", "ordered-list"}:
                _render_list(body, entries, pack, block.items, claims, items, ordered=True)
            elif block.block_kind == "table" and block.table_rows:
                _render_table(body, block.table_rows)
            elif block.block_kind == "code" and block.text.strip():
                _render_code(body, block.text)
    _render_payload_context(body, pack)
    _render_related_links(body, entries, pack, article, items)
    _render_source_trail(body, pack, article)
    text = body.text()
    return RenderedPage(text, short_digest(text, 32), ProjectionCoverage(tuple(entries)))


def _render_paragraph(
    body: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    pack: EvidencePack,
    text: str,
    claims: dict[str, ArticleClaim],
    items: dict[str, EvidencePackItem],
) -> None:
    for sentence in split_sentences(text):
        span = body.add(_render_claim_text(sentence, claims, items) + " ")
        _append_coverage(entries, pack, sentence, claims, span)
    body.add("\n\n")


def _render_list(
    body: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    pack: EvidencePack,
    item_texts: tuple[str, ...],
    claims: dict[str, ArticleClaim],
    items: dict[str, EvidencePackItem],
    *,
    ordered: bool,
) -> None:
    for index, item_text in enumerate(item_texts, start=1):
        prefix = f"{index}. " if ordered else "- "
        rendered = " ".join(
            _render_claim_text(sentence, claims, items)
            for sentence in split_sentences(item_text)
        )
        span = body.add(f"{prefix}{rendered}\n")
        for sentence in split_sentences(item_text):
            _append_coverage(entries, pack, sentence, claims, span)
    body.add("\n")


def _render_claim_text(
    sentence: str,
    claims: dict[str, ArticleClaim],
    items: dict[str, EvidencePackItem],
) -> str:
    claim = claims.get(_normalize(sentence))
    if claim is None:
        return sentence.strip()
    citations = _claim_citations(claim, items)
    if not citations:
        return claim.sentence.strip()
    return f"{claim.sentence.strip()} _({'; '.join(citations)})_"


def _claim_citations(
    claim: ArticleClaim, items: dict[str, EvidencePackItem]
) -> tuple[str, ...]:
    citations: list[str] = []
    for support_ref in claim.support_refs:
        item = items.get(support_ref.code)
        if item is None:
            continue
        citation = item.citation_label
        if citation and citation not in citations:
            citations.append(citation)
    return tuple(citations)


def _render_payload_context(body: PageBodyBuilder, pack: EvidencePack) -> None:
    payload_items = tuple(item for item in pack.items if item.payload_text.strip())
    if not payload_items:
        return
    body.add("## Evidence Details\n\n")
    for item in payload_items:
        label = item.citation_label or item.support_ref.code
        if item.evidence_record_type == "code_example":
            body.add(f"### {label}\n\n")
            _render_code(body, item.payload_text)
        else:
            body.add(f"- {label}: `{item.payload_text.strip()}`\n")
    body.add("\n")


def _render_related_links(
    body: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    pack: EvidencePack,
    article: HumanArticle,
    items: dict[str, EvidencePackItem],
) -> None:
    if not article.related_links:
        return
    body.add("## Related pages\n\n")
    for link in article.related_links:
        reason = link.relation.strip() or "related article"
        preview = f": {link.preview_text.strip()}" if link.preview_text.strip() else ""
        shared = tuple(ref.code for ref in link.shared_support_refs)
        support_note = f" _(shared support: {', '.join(shared)})_" if shared else ""
        span = body.add(f"- [[{link.page_id}]] - {reason}{preview}{support_note}\n")
        entries.append(_coverage_entry(pack, "related-page-link", span, "", shared, items))
    body.add("\n")


def _render_source_trail(body: PageBodyBuilder, pack: EvidencePack, article: HumanArticle) -> None:
    body.add("## Source Trail\n\n")
    body.add(f"- Source manifest: [[{pack.source_id}]]\n")
    extra = tuple(dict.fromkeys(article.source_trail_items))
    for trail_item in extra:
        body.add(f"- {trail_item}\n")
    for item in tuple(dict.fromkeys(pack.items)):
        section = f" - {item.section_path}" if item.section_path else ""
        body.add(f"- {item.citation_label}{section}\n")


def _render_table(body: PageBodyBuilder, rows: tuple[tuple[str, ...], ...]) -> None:
    header = rows[0]
    body.add("| " + " | ".join(header) + " |\n")
    body.add("| " + " | ".join("---" for _ in header) + " |\n")
    for row in rows[1:]:
        body.add("| " + " | ".join(row) + " |\n")
    body.add("\n")


def _render_code(body: PageBodyBuilder, code: str) -> None:
    body.add("```text\n")
    body.add(code.strip() + "\n")
    body.add("```\n\n")


def _append_coverage(
    entries: list[ProjectionCoverageEntry],
    pack: EvidencePack,
    sentence: str,
    claims: dict[str, ArticleClaim],
    span: PageTextRange,
) -> None:
    claim = claims.get(_normalize(sentence))
    if claim is None:
        return
    support_refs = tuple(ref.code for ref in claim.support_refs)
    entries.append(_coverage_entry(pack, "article-claim", span, claim.claim_id, support_refs, {}))


def _coverage_entry(
    pack: EvidencePack,
    unit_kind: str,
    span: PageTextRange,
    article_claim_id: str,
    support_refs: tuple[str, ...],
    items: dict[str, EvidencePackItem],
) -> ProjectionCoverageEntry:
    entry_id = deterministic_id(
        "projection-coverage-entry",
        pack.page_id,
        unit_kind,
        f"{span.start}-{span.end}",
        article_claim_id,
        "|".join(support_refs),
    )
    technical_atom_id = _technical_atom_id(support_refs, items)
    return ProjectionCoverageEntry(
        projection_coverage_entry_id=entry_id,
        projection_coverage_unit_kind=unit_kind,
        page_text_range=span,
        technical_atom_id=technical_atom_id,
        draft_claim_id=article_claim_id,
        draft_support_refs=support_refs,
    )


def _technical_atom_id(
    support_refs: tuple[str, ...], items: dict[str, EvidencePackItem]
) -> str:
    for support_ref in support_refs:
        item = items.get(support_ref)
        if item and item.evidence_record_type in {"formula", "table_fact", "code_example"}:
            return item.typed_evidence_record_id
    return ""


def _normalize(text: str) -> str:
    return " ".join(text.split()).strip()
