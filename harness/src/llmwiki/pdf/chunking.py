"""TOC-aware semantic chunking (pure).

Sections come from the PDF's table of contents: each TOC entry spans from
its start page to the page before the next entry. Chunks pack whole
consecutive sections up to a token budget; a section that alone exceeds
the budget is split at paragraph boundaries, never mid-paragraph.
"""

from __future__ import annotations

from dataclasses import dataclass

# Per-map-run input budget from the design's 16K context table.
CHUNK_TOKEN_BUDGET = 6000

_CHARS_PER_TOKEN = 4  # same rough estimate forge uses


def estimate_tokens(text: str) -> int:
    return len(text) // _CHARS_PER_TOKEN


@dataclass(frozen=True)
class TocEntry:
    """One outline entry: 1-based start page, as PyMuPDF's get_toc gives."""

    level: int
    title: str
    start_page: int


@dataclass(frozen=True)
class Section:
    heading: str
    start_page: int  # 1-based, inclusive
    end_page: int  # 1-based, inclusive
    text: str


@dataclass(frozen=True)
class Chunk:
    chunk_id: int  # 1-based
    heading: str  # heading of the first section in the chunk
    start_page: int
    end_page: int
    text: str

    @property
    def token_estimate(self) -> int:
        return estimate_tokens(self.text)


def build_sections(toc: list[TocEntry], page_texts: list[str]) -> list[Section]:
    """Slice page texts into sections along TOC boundaries.

    Pages are the granularity: a section that starts mid-page includes the
    whole page, so adjacent sections may share a boundary page (small,
    accepted duplication). With no TOC, the whole document is one section.
    """
    n_pages = len(page_texts)
    if n_pages == 0:
        return []

    def page_span_text(start: int, end: int) -> str:
        return "\n\n".join(page_texts[start - 1 : end]).strip()

    entries = [e for e in toc if 1 <= e.start_page <= n_pages]
    if not entries:
        return [Section("Document", 1, n_pages, page_span_text(1, n_pages))]

    sections: list[Section] = []
    if entries[0].start_page > 1:
        sections.append(
            Section(
                "Front matter",
                1,
                entries[0].start_page - 1,
                page_span_text(1, entries[0].start_page - 1),
            )
        )
    for i, entry in enumerate(entries):
        next_start = entries[i + 1].start_page if i + 1 < len(entries) else n_pages + 1
        end_page = max(entry.start_page, next_start - 1)
        sections.append(
            Section(
                entry.title, entry.start_page, end_page, page_span_text(entry.start_page, end_page)
            )
        )
    return [s for s in sections if s.text]


def _split_oversized(section: Section, budget_tokens: int) -> list[Section]:
    """Split one over-budget section at paragraph boundaries."""
    paragraphs = [p for p in section.text.split("\n\n") if p.strip()]
    parts: list[Section] = []
    current: list[str] = []
    part_no = 1

    def flush() -> None:
        nonlocal current, part_no
        if current:
            parts.append(
                Section(
                    f"{section.heading} (part {part_no})",
                    section.start_page,
                    section.end_page,
                    "\n\n".join(current),
                )
            )
            part_no += 1
            current = []

    for paragraph in paragraphs:
        candidate = "\n\n".join([*current, paragraph])
        if current and estimate_tokens(candidate) > budget_tokens:
            flush()
        current.append(paragraph)
    flush()
    return parts


def pack_chunks(sections: list[Section], budget_tokens: int = CHUNK_TOKEN_BUDGET) -> list[Chunk]:
    """Pack consecutive sections into budget-sized chunks."""
    sized: list[Section] = []
    for section in sections:
        if estimate_tokens(section.text) > budget_tokens:
            sized.extend(_split_oversized(section, budget_tokens))
        else:
            sized.append(section)

    chunks: list[Chunk] = []
    group: list[Section] = []

    def flush() -> None:
        nonlocal group
        if group:
            chunks.append(
                Chunk(
                    chunk_id=len(chunks) + 1,
                    heading=group[0].heading,
                    start_page=group[0].start_page,
                    end_page=group[-1].end_page,
                    text="\n\n".join(s.text for s in group),
                )
            )
            group = []

    for section in sized:
        candidate = "\n\n".join(s.text for s in [*group, section])
        if group and estimate_tokens(candidate) > budget_tokens:
            flush()
        group.append(section)
    flush()
    return chunks
