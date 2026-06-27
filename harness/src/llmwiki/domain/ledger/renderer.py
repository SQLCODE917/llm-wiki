"""WikiPageRenderer: render a SourceWikiPage body from a projection plan.

The page is a projection of the ledger: source-structure sections first (each
rendering its generated page claims as source-close lines and its technical
atoms as source-equivalent payload blocks), then a source review section
listing needs-review items and disposition counts. Every rendered unit gets one
projection coverage entry with its page text range. Visible citations use
source-facing labels; internal support ids never appear in the body.
"""

from __future__ import annotations

from llmwiki.domain.ledger.atom_context import TechnicalAtomContext, best_atom_context
from llmwiki.domain.ledger.atoms import AtomPayload, TablePayload, atom_raw_text
from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.coverage import (
    PageBodyBuilder,
    PageTextRange,
    ProjectionCoverage,
    ProjectionCoverageEntry,
    RenderedPage,
    clean_statement,
)
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection import LedgerProjectionPlan

_FENCE_KINDS = {"code-block"}


def render_source_page(plan: LedgerProjectionPlan, ledger: ClaimLedger) -> RenderedPage:
    body = PageBodyBuilder()
    entries: list[ProjectionCoverageEntry] = []
    body.add(f"# {plan.title}\n\n")
    for section in plan.sections:
        _render_heading(body, section.heading_text, section.depth)
        for claim in section.claims:
            span = body.add(f"- {claim.text} _({claim.citation_label})_\n")
            entries.append(
                _coverage(
                    plan, "generated-page-claim", span, selected=claim.selected_ledger_entry_ids
                )
            )
        if section.claims:
            body.add("\n")
        for block in section.atom_blocks:
            span = _render_atom(body, ledger, block.technical_atom_id, block.citation_label)
            entries.append(
                _coverage(
                    plan, "rendered-technical-atom-block", span, atom_id=block.technical_atom_id
                )
            )
    _render_review(body, plan, entries)
    text = body.text()
    return RenderedPage(text, short_digest(text, 32), ProjectionCoverage(tuple(entries)))


def _render_heading(body: PageBodyBuilder, heading: str, depth: int) -> None:
    level = "#" * min(max(depth + 1, 2), 5)
    body.add(f"{level} {heading}\n\n")


def _render_atom(
    body: PageBodyBuilder, ledger: ClaimLedger, atom_id: str, citation: str
) -> PageTextRange:
    atom = ledger.atom(atom_id)
    if atom is None:
        return body.add(f"> _(missing atom {atom_id})_\n\n")
    rendered = atom_block(atom.technical_atom_kind, atom.payload)
    context = _atom_context_line(ledger, atom_id, atom.source_locator)
    return body.add(f"{context}**Atom:** _({citation})_\n\n{rendered}\n\n")


def atom_block(kind: str, payload: AtomPayload) -> str:
    raw = atom_raw_text(payload)
    if kind in _FENCE_KINDS:
        language = getattr(payload, "language_tag", "") or ""
        return f"```{language}\n{raw}\n```"
    if kind == "table":
        return _table_block(payload) if isinstance(payload, TablePayload) else f"```\n{raw}\n```"
    return "\n".join(f"> {line}" for line in raw.splitlines()) or "> "


def _atom_context_line(ledger: ClaimLedger, atom_id: str, source_locator: str) -> str:
    context = best_atom_context(ledger.atom_contexts(atom_id))
    if context is None:
        return ""
    return atom_context_block(context, source_locator)


def atom_context_block(context: TechnicalAtomContext, source_locator: str) -> str:
    context_text = clean_statement(context.context_text)[:500]
    context_source = ", ".join(context.context_source_range_ids)
    return f"**Context:** _({source_locator} ({context_source}))_\n\n> {context_text}\n\n"


def _table_block(payload: TablePayload) -> str:
    logical = _markdown_table(payload)
    raw = payload.raw_table_text
    if not logical:
        return f"```\n{raw}\n```"
    raw_block = f"<details>\n<summary>Raw table text</summary>\n\n```\n{raw}\n```\n\n</details>"
    return f"{logical}\n\n{raw_block}"


def _markdown_table(payload: TablePayload) -> str:
    if not payload.columns or not payload.rows or not payload.cells:
        return ""
    headers = [
        _escape_table_cell(column.header_text or f"column {column.column_index + 1}")
        for column in payload.columns
    ]
    by_cell = {(cell.row_index, cell.column_index): cell.value for cell in payload.cells}
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in payload.rows:
        values = [
            _escape_table_cell(by_cell.get((row.row_index, column.column_index), ""))
            for column in payload.columns
        ]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def _escape_table_cell(value: str) -> str:
    return " ".join(value.replace("|", "\\|").split())


def _render_review(
    body: PageBodyBuilder, plan: LedgerProjectionPlan, entries: list[ProjectionCoverageEntry]
) -> None:
    if not plan.review_items and not plan.disposition_counts:
        return
    body.add("## Source review\n\n")
    if plan.review_items:
        body.add("### Needs review\n\n")
        for item in plan.review_items:
            span = body.add(
                f"- {item.text.strip()[:300]} — _{item.review_reason_kind}: "
                f"{item.review_reason_detail}_ _({item.citation_label})_\n"
            )
            entries.append(
                _coverage(plan, "source-review-item", span, ledger_entry_id=item.ledger_entry_id)
            )
        body.add("\n")
    if plan.disposition_counts:
        body.add("### Disposition counts\n\n")
        for count in plan.disposition_counts:
            span = body.add(f"- {count.disposition}: {count.count}\n")
            entries.append(
                _coverage(plan, "disposition-count", span, disposition=count.disposition)
            )


def _coverage(
    plan: LedgerProjectionPlan,
    unit_kind: str,
    span: PageTextRange,
    *,
    selected: tuple[str, ...] = (),
    atom_id: str = "",
    ledger_entry_id: str = "",
    disposition: str = "",
) -> ProjectionCoverageEntry:
    entry_id = deterministic_id(
        "projection-coverage-entry",
        plan.wiki_page_locator,
        unit_kind,
        f"{span.start}-{span.end}",
        "|".join(selected) or atom_id or ledger_entry_id or disposition,
    )
    return ProjectionCoverageEntry(
        projection_coverage_entry_id=entry_id,
        projection_coverage_unit_kind=unit_kind,
        page_text_range=span,
        selected_ledger_entry_ids=selected,
        technical_atom_id=atom_id,
        ledger_entry_id=ledger_entry_id,
        extracted_unit_disposition=disposition,
    )
