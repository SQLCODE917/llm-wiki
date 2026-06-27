"""Source-structure reference pages.

Topic pages are selective. These pages follow the source's own headings and are
therefore better for authoritative lookup inside a chapter or section.
"""

from __future__ import annotations

from llmwiki.domain.ledger.atom_context import best_atom_context
from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.renderer import atom_block, atom_context_block
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.table_identity import (
    has_matching_table_name,
    normalize_table_name,
    table_identity_names_by_atom_id,
)
from llmwiki.domain.pages import PageError, PageMetadata, WikiPage, slugify

_SECTION_NODE_KINDS = {"chapter", "section", "heading"}


def build_section_pages(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
) -> tuple[WikiPage, ...]:
    pages: list[WikiPage] = []
    for node in sorted(structure.structure_nodes, key=lambda item: item.source_order):
        if node.structure_node_kind not in _SECTION_NODE_KINDS:
            continue
        entries = _entries_for_node(ledger, node.structure_node_id)
        atoms = _atoms_for_entries(ledger, entries, structure, node)
        if not entries and not atoms:
            continue
        page_id = _page_id(source_page_id, node)
        body = _body(ledger, node, entries, atoms, source_page_id)
        metadata = PageMetadata(
            page_id=page_id,
            page_kind="source",
            summary=(
                f"{node.heading_text}: {len(entries)} source-backed entries and "
                f"{len(atoms)} atom(s) from raw/{source_locator}."
            ),
            sources=(f"raw/{source_locator}",),
            updated=today,
            domain=source_page_id,
            category_path=f"sources/{source_page_id}/sections",
            source_id=source_locator,
            projection_coverage_pointer=f"section-{page_id}@{short_digest(body, 32)}",
        )
        pages.append(WikiPage.from_metadata(metadata, body))
    return tuple(pages)


def _body(
    ledger: ClaimLedger,
    node: StructureNode,
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    source_page_id: str,
) -> str:
    lines = [f"# {node.heading_text}", "", f"From [[{source_page_id}]].", ""]
    claim_entries = tuple(entry for entry in entries if entry.ledger_entry_kind != "technical-atom")
    if claim_entries:
        lines.extend(("## Statements", ""))
        for entry in claim_entries:
            text = entry.normalized_text or entry.source_text
            citation = f"{entry.source_locator} ({entry.source_range_id})"
            lines.append(f"- {text.strip()} _({citation})_")
        lines.append("")
    if atoms:
        lines.extend(("## Technical atoms", ""))
        for index, atom in enumerate(atoms, start=1):
            lines.extend((f"### Technical atom {index}", ""))
            context = best_atom_context(ledger.atom_contexts(atom.technical_atom_id))
            if context is not None:
                lines.extend(atom_context_block(context, atom.source_locator).strip().splitlines())
                lines.append("")
            rendered = atom_block(atom.technical_atom_kind, atom.payload)
            citation = f"{atom.source_locator} ({atom.source_range_id})"
            lines.extend((f"**Atom:** _({citation})_", "", rendered, ""))
    return "\n".join(lines).strip() + "\n"


def _entries_for_node(ledger: ClaimLedger, node_id: str) -> tuple[LedgerEntry, ...]:
    return tuple(
        entry
        for entry in ledger.usable_entries
        if node_id in entry.structure_node_ids
        and (entry.normalized_text or entry.source_text or entry.technical_atom_id)
    )


def _atoms_for_entries(
    ledger: ClaimLedger,
    entries: tuple[LedgerEntry, ...],
    structure: DocumentStructure,
    node: StructureNode,
) -> tuple[TechnicalAtom, ...]:
    atom_ids = {
        entry.technical_atom_id
        for entry in entries
        if entry.ledger_entry_kind == "technical-atom" and entry.technical_atom_id
    }
    section_name = normalize_table_name(node.heading_text)
    if section_name:
        for atom_id, names in table_identity_names_by_atom_id(ledger, structure).items():
            if has_matching_table_name(section_name, names):
                atom_ids.add(atom_id)
    return tuple(
        atom
        for atom in ledger.technical_atoms
        if atom.technical_atom_id in atom_ids and atom_raw_text(atom.payload).strip()
    )


def _page_id(source_page_id: str, node: StructureNode) -> str:
    label = _safe_slug(node.heading_text)[:72]
    suffix = short_digest(node.structure_node_id, 8)
    return slugify(f"{source_page_id}-section-{label}-{suffix}")


def _safe_slug(text: str) -> str:
    try:
        return slugify(text)
    except PageError:
        return "section"
