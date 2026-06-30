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
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.projection_context_render import (
    atom_frame_markdown,
    evidence_block_line,
)
from llmwiki.domain.ledger.projection_policy import (
    TopicProjectionPolicy,
    entry_can_render_standalone,
    select_evidence_blocks_for_policy,
    topic_projection_policy,
)
from llmwiki.domain.ledger.renderer import atom_block, atom_context_block
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.ledger.topic_terms import topic_matcher
from llmwiki.domain.ledger.topics import SourceTopic
from llmwiki.domain.ledger.walkability import related_link_markdown


def render_topic_page(
    topic: SourceTopic,
    ledger: ClaimLedger,
    *,
    wiki_page_locator: str,
    source_page_id: str,
    related_pages: tuple[RelatedTopicLink, ...] = (),
    projection_context: ProjectionContext | None = None,
    projection_policy: TopicProjectionPolicy | None = None,
) -> RenderedPage:
    policy = projection_policy or topic_projection_policy(topic, ledger, projection_context)
    body = PageBodyBuilder()
    entries: list[ProjectionCoverageEntry] = []
    body.add(f"# {topic.label}\n\n")
    body.add(f"What [[{source_page_id}]] covers about {topic.label.lower()}:\n\n")

    related_pages_rendered = False
    if related_pages and policy.is_broad_topic:
        _render_related_pages(body, entries, wiki_page_locator, related_pages)
        related_pages_rendered = True

    heading = "## Statements by source section" if policy.is_broad_topic else "## Statements"
    body.add(f"{heading}\n\n")
    rendered_entry_ids: set[str] = set()
    if projection_context is not None:
        current_section_label = ""
        blocks = select_evidence_blocks_for_policy(
            projection_context.blocks_for_entries(topic.entry_ids), policy
        )
        for block in blocks:
            selected = tuple(
                entry_id for entry_id in block.entry_ids if entry_id in topic.entry_ids
            )
            if not selected:
                continue
            if block.section_label and block.section_label != current_section_label:
                body.add(f"### {block.section_label}\n\n")
                current_section_label = block.section_label
            span = body.add(f"{evidence_block_line(block)}\n\n")
            rendered_entry_ids.update(selected)
            entries.append(
                _coverage(wiki_page_locator, "projected-evidence-block", span, selected=selected)
            )
    if not policy.is_broad_topic:
        for entry_id in topic.entry_ids:
            if entry_id in rendered_entry_ids:
                continue
            entry = ledger.entry(entry_id)
            if entry is None or not (entry.normalized_text or entry.source_text).strip():
                continue
            if not entry_can_render_standalone(entry):
                continue
            text = clean_statement(entry.normalized_text or entry.source_text)
            citation = f"{entry.source_locator} ({entry.source_range_id})"
            span = body.add(f"- {text} _({citation})_\n")
            entries.append(
                _coverage(wiki_page_locator, "generated-page-claim", span, selected=(entry_id,))
            )

    rendered_atom_ids: set[str] = set()
    atom_frames = (
        projection_context.frames_for_atoms(topic.atom_ids)
        if projection_context is not None
        else ()
    )
    rendered_atoms = [
        atom
        for atom in (ledger.atom(a) for a in topic.atom_ids)
        if atom is not None and atom.technical_atom_id not in rendered_atom_ids
    ]
    if atom_frames or rendered_atoms:
        matcher = topic_matcher(topic.match_terms)
        body.add("\n## Technical atoms\n\n")
        for index, frame in enumerate(atom_frames, start=1):
            selected_atoms = tuple(
                atom_id for atom_id in frame.atom_ids if atom_id in topic.atom_ids
            )
            if not selected_atoms or projection_context is None:
                continue
            span = body.add(atom_frame_markdown(frame, ledger, projection_context, index))
            body.add("\n")
            rendered_atom_ids.update(selected_atoms)
            entries.append(
                _coverage(
                    wiki_page_locator,
                    "technical-atom-frame",
                    span,
                    atom_id=selected_atoms[0],
                )
            )
        rendered_atoms = [
            atom
            for atom in (ledger.atom(a) for a in topic.atom_ids)
            if atom is not None and atom.technical_atom_id not in rendered_atom_ids
        ]
        for index, atom in enumerate(rendered_atoms, start=len(atom_frames) + 1):
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

    if related_pages and not related_pages_rendered:
        _render_related_pages(body, entries, wiki_page_locator, related_pages)

    body.add(f"\n## Source\n\n- [[{source_page_id}]]\n")
    text = body.text()
    return RenderedPage(text, short_digest(text, 32), ProjectionCoverage(tuple(entries)))


def _render_related_pages(
    body: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    wiki_page_locator: str,
    related_pages: tuple[RelatedTopicLink, ...],
) -> None:
    body.add("\n## Related pages\n\n")
    for link in related_pages:
        span = body.add(f"{related_link_markdown(link)}\n")
        entries.append(
            _coverage(
                wiki_page_locator,
                "related-page-link",
                span,
                selected=link.shared_entry_ids,
                atom_id=link.shared_atom_ids[0] if link.shared_atom_ids else "",
            )
        )


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
