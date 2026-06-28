"""Render a per-source topic page from an aggregated SourceTopic.

The page answers "what does this source say about X": the source-close claims
that mention the topic, the relevant technical atoms (code/rules/examples), and
a link back to the source. Every rendered unit gets one projection coverage
entry; internal ids never appear in the body.
"""

from __future__ import annotations

from llmwiki.domain.ledger.atom_context import best_atom_context
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
from llmwiki.domain.ledger.renderer import atom_block, atom_context_block
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.ledger.topic_terms import topic_matcher
from llmwiki.domain.ledger.topics import SourceTopic


def render_topic_page(
    topic: SourceTopic,
    ledger: ClaimLedger,
    *,
    wiki_page_locator: str,
    source_page_id: str,
    related_pages: tuple[RelatedTopicLink, ...] = (),
) -> RenderedPage:
    body = PageBodyBuilder()
    entries: list[ProjectionCoverageEntry] = []
    body.add(f"# {topic.label}\n\n")
    body.add(f"What [[{source_page_id}]] covers about {topic.label.lower()}:\n\n")

    body.add("## Statements\n\n")
    for entry_id in topic.entry_ids:
        entry = ledger.entry(entry_id)
        if entry is None or not (entry.normalized_text or entry.source_text).strip():
            continue
        text = clean_statement(entry.normalized_text or entry.source_text)
        citation = f"{entry.source_locator} ({entry.source_range_id})"
        span = body.add(f"- {text} _({citation})_\n")
        entries.append(
            _coverage(wiki_page_locator, "generated-page-claim", span, selected=(entry_id,))
        )

    rendered_atoms = [atom for atom in (ledger.atom(a) for a in topic.atom_ids) if atom is not None]
    if rendered_atoms:
        matcher = topic_matcher(topic.match_terms)
        body.add("\n## Technical atoms\n\n")
        for index, atom in enumerate(rendered_atoms, start=1):
            body.add(f"### Technical atom {index}\n\n")
            context = best_atom_context(ledger.atom_contexts(atom.technical_atom_id), matcher)
            if context is not None:
                span = body.add(atom_context_block(context, atom.source_locator))
                entries.append(
                    _coverage(
                        wiki_page_locator,
                        "technical-atom-context",
                        span,
                        atom_id=atom.technical_atom_id,
                    )
                )
            rendered = atom_block(atom.technical_atom_kind, atom.payload)
            citation = f"{atom.source_locator} ({atom.source_range_id})"
            span = body.add(f"**Atom:** _({citation})_\n\n{rendered}\n\n")
            entries.append(
                _coverage(
                    wiki_page_locator,
                    "rendered-technical-atom-block",
                    span,
                    atom_id=atom.technical_atom_id,
                )
            )

    if related_pages:
        body.add("\n## Related pages\n\n")
        for link in related_pages:
            span = body.add(f"- [[{link.page_id}]] - {link.relation}{_evidence_note(link)}\n")
            entries.append(
                _coverage(
                    wiki_page_locator,
                    "related-page-link",
                    span,
                    selected=link.shared_entry_ids,
                    atom_id=link.shared_atom_ids[0] if link.shared_atom_ids else "",
                )
            )

    body.add(f"\n## Source\n\n- [[{source_page_id}]]\n")
    text = body.text()
    return RenderedPage(text, short_digest(text, 32), ProjectionCoverage(tuple(entries)))


def _evidence_note(link: RelatedTopicLink) -> str:
    parts: list[str] = []
    if link.shared_entry_count:
        parts.append(f"{link.shared_entry_count} shared statement(s)")
    if link.shared_atom_count:
        parts.append(f"{link.shared_atom_count} shared atom(s)")
    return f" ({', '.join(parts)})" if parts else ""


def _coverage(
    wiki_page_locator: str,
    unit_kind: str,
    span: PageTextRange,
    *,
    selected: tuple[str, ...] = (),
    atom_id: str = "",
) -> ProjectionCoverageEntry:
    entry_id = deterministic_id(
        "projection-coverage-entry",
        wiki_page_locator,
        unit_kind,
        f"{span.start}-{span.end}",
        "|".join(selected) or atom_id,
    )
    return ProjectionCoverageEntry(
        projection_coverage_entry_id=entry_id,
        projection_coverage_unit_kind=unit_kind,
        page_text_range=span,
        selected_ledger_entry_ids=selected,
        technical_atom_id=atom_id,
    )
