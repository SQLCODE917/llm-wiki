"""Canonical concept pages assembled from per-source topic evidence."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from llmwiki.domain.ledger.atom_addressing import technical_atom_anchor
from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.coverage import (
    PageBodyBuilder,
    PageTextRange,
    ProjectionCoverage,
    ProjectionCoverageEntry,
    RenderedPage,
    clean_statement,
)


@dataclass(frozen=True)
class ConceptEvidenceItem:
    ledger_entry_id: str
    text: str
    citation_label: str


@dataclass(frozen=True)
class ConceptAtomBlock:
    technical_atom_id: str
    technical_atom_kind: str
    payload: dict[str, Any]
    source_locator: str
    source_range_id: str
    context_text: str = ""
    context_source_range_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class ConceptSourceSection:
    source_locator: str
    source_page_id: str
    topic_page_id: str
    label: str
    evidence_items: tuple[ConceptEvidenceItem, ...]
    atom_blocks: tuple[ConceptAtomBlock, ...]


@dataclass(frozen=True)
class ConceptRelationship:
    cross_source_relationship_id: str
    relationship_kind: str
    source_page_ids: tuple[str, ...]
    texts: tuple[str, ...]


@dataclass(frozen=True)
class CanonicalConceptPage:
    topic_key: str
    label: str
    page_kind: str
    source_sections: tuple[ConceptSourceSection, ...]
    relationships: tuple[ConceptRelationship, ...]
    support_ids: tuple[str, ...]

    @property
    def statement_count(self) -> int:
        return sum(len(section.evidence_items) for section in self.source_sections)

    @property
    def atom_count(self) -> int:
        return sum(len(section.atom_blocks) for section in self.source_sections)


def render_canonical_concept_page(
    page: CanonicalConceptPage, wiki_page_locator: str
) -> RenderedPage:
    body = PageBodyBuilder()
    entries: list[ProjectionCoverageEntry] = []
    body.add(f"# {page.label}\n\n")
    body.add(
        f"Compiled concept page from {len(page.source_sections)} source(s), "
        f"{page.statement_count} statement(s), and {page.atom_count} technical atom(s).\n\n"
    )
    body.add("## Source Evidence\n\n")
    for section in page.source_sections:
        body.add(f"### [[{section.source_page_id}]]\n\n")
        body.add(f"Source topic: [[{section.topic_page_id}]]\n\n")
        if section.evidence_items:
            body.add("#### Statements\n\n")
        for item in section.evidence_items:
            text = clean_statement(item.text)
            span = body.add(f"- {text} _({item.citation_label})_\n")
            entries.append(
                _coverage(
                    wiki_page_locator,
                    "generated-page-claim",
                    span,
                    selected=(item.ledger_entry_id,),
                )
            )
        if section.atom_blocks:
            body.add("\n#### Technical atoms\n\n")
        for index, atom in enumerate(section.atom_blocks, start=1):
            body.add(f"##### Technical atom {index}\n\n")
            if atom.context_text:
                context_source = ", ".join(atom.context_source_range_ids)
                span = body.add(
                    f"**Context:** _({atom.source_locator} ({context_source}))_\n\n"
                    f"> {clean_statement(atom.context_text)}\n\n"
                )
                entries.append(
                    _coverage(
                        wiki_page_locator,
                        "technical-atom-context",
                        span,
                        atom_id=atom.technical_atom_id,
                    )
                )
            rendered = _atom_block(atom.technical_atom_kind, atom.payload)
            citation = f"{atom.source_locator} ({atom.source_range_id})"
            span = body.add(
                f"{technical_atom_anchor(atom.technical_atom_id)}\n\n"
                f"**Atom:** _({citation})_\n\n{rendered}\n\n"
            )
            entries.append(
                _coverage(
                    wiki_page_locator,
                    "rendered-technical-atom-block",
                    span,
                    atom_id=atom.technical_atom_id,
                )
            )
        body.add("\n")
    body.add("## Cross-Source Comparison\n\n")
    if page.relationships:
        for relationship in page.relationships:
            labels = " / ".join(f"[[{page_id}]]" for page_id in relationship.source_page_ids)
            span = body.add(f"- {relationship.relationship_kind}: {labels}\n")
            entries.append(
                _coverage(
                    wiki_page_locator,
                    "cross-source-relationship",
                    span,
                    cross_source_relationship_id=relationship.cross_source_relationship_id,
                )
            )
    else:
        body.add("- No typed cross-source relationships detected yet.\n")
    text = body.text()
    return RenderedPage(text, short_digest(text, 32), ProjectionCoverage(tuple(entries)))


def _coverage(
    wiki_page_locator: str,
    unit_kind: str,
    span: PageTextRange,
    *,
    selected: tuple[str, ...] = (),
    atom_id: str = "",
    cross_source_relationship_id: str = "",
) -> ProjectionCoverageEntry:
    entry_id = deterministic_id(
        "projection-coverage-entry",
        wiki_page_locator,
        unit_kind,
        f"{span.start}-{span.end}",
        "|".join(selected) or atom_id or cross_source_relationship_id,
    )
    return ProjectionCoverageEntry(
        projection_coverage_entry_id=entry_id,
        projection_coverage_unit_kind=unit_kind,
        page_text_range=span,
        selected_ledger_entry_ids=selected,
        technical_atom_id=atom_id,
        cross_source_relationship_id=cross_source_relationship_id,
    )


def _atom_block(kind: str, payload: dict[str, Any]) -> str:
    raw = _raw_text(payload)
    if kind == "code-block":
        language = str(payload.get("language_tag") or "")
        return f"```{language}\n{raw}\n```"
    if kind == "table":
        table = _markdown_table(payload)
        if table:
            raw_block = (
                f"<details>\n<summary>Raw table text</summary>\n\n```\n{raw}\n```\n\n</details>"
            )
            return f"{table}\n\n{raw_block}"
        return f"```\n{raw}\n```"
    return "\n".join(f"> {line}" for line in raw.splitlines()) or "> "


def _raw_text(payload: dict[str, Any]) -> str:
    for key in (
        "raw_table_text",
        "raw_code_text",
        "raw_formula_text",
        "raw_figure_text",
        "rule_text",
        "procedure_text",
        "example_text",
    ):
        value = payload.get(key)
        if isinstance(value, str):
            return value
    return ""


def _markdown_table(payload: dict[str, Any]) -> str:
    columns = [item for item in payload.get("columns", ()) if isinstance(item, dict)]
    rows = [item for item in payload.get("rows", ()) if isinstance(item, dict)]
    cells = [item for item in payload.get("cells", ()) if isinstance(item, dict)]
    if not columns or not rows or not cells:
        return ""
    headers = [
        _escape_table_cell(str(column.get("header_text") or f"column {index + 1}"))
        for index, column in enumerate(columns)
    ]
    by_cell = {
        (cell.get("row_index"), cell.get("column_index")): str(cell.get("value") or "")
        for cell in cells
    }
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        row_index = row.get("row_index")
        values = [
            _escape_table_cell(by_cell.get((row_index, column.get("column_index")), ""))
            for column in columns
        ]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def _escape_table_cell(value: str) -> str:
    return " ".join(value.replace("|", "\\|").split())
