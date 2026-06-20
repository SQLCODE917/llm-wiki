"""Chunk manifest: the on-disk resume cursor for a PDF ingest (pure).

Chunk state lives here, not in the model's context — the design's
"control flow is not memory" applied at the orchestration level.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, replace

# Cap carried-forward notes so 20 chunks of digest fit the integrate run
# (~1.5K chars ≈ 375 tokens each). Awaiting experimentation.
NOTE_CAP_CHARS = 1500

_STATUSES = ("pending", "done")


@dataclass(frozen=True)
class ChunkRecord:
    chunk_id: int
    heading: str
    start_page: int
    end_page: int
    token_estimate: int
    status: str = "pending"
    notes: str = ""
    # Machine record of pages the chunk run actually wrote (captured at the
    # write_page tool) — ground truth where notes have over-claimed.
    pages_written: tuple[str, ...] = ()
    route_plan_pages: int = 0
    route_plan_gaps: int = 0
    route_gap_summaries: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in _STATUSES:
            raise ValueError(f"invalid chunk status {self.status!r}")


@dataclass(frozen=True)
class Manifest:
    source: str  # path relative to raw/
    sha256: str
    chunks: tuple[ChunkRecord, ...]
    integrated: bool = field(default=False)

    @property
    def pending(self) -> tuple[ChunkRecord, ...]:
        return tuple(c for c in self.chunks if c.status == "pending")

    @property
    def all_done(self) -> bool:
        return not self.pending

    def mark_done(
        self,
        chunk_id: int,
        notes: str,
        pages_written: tuple[str, ...] = (),
        route_plan_pages: int = 0,
        route_plan_gaps: int = 0,
        route_gap_summaries: tuple[str, ...] = (),
    ) -> Manifest:
        capped = notes if len(notes) <= NOTE_CAP_CHARS else notes[: NOTE_CAP_CHARS - 1] + "…"
        chunks = tuple(
            replace(
                c,
                status="done",
                notes=capped,
                pages_written=pages_written,
                route_plan_pages=route_plan_pages,
                route_plan_gaps=route_plan_gaps,
                route_gap_summaries=route_gap_summaries,
            )
            if c.chunk_id == chunk_id
            else c
            for c in self.chunks
        )
        if chunks == self.chunks:
            raise ValueError(f"no pending chunk with id {chunk_id}")
        return replace(self, chunks=chunks)

    def mark_integrated(self) -> Manifest:
        return replace(self, integrated=True)

    def requeue_missing_pages(
        self, existing_pages: frozenset[str], hub_page_id: str = ""
    ) -> Manifest:
        chunks = tuple(
            _requeue_if_missing_pages(chunk, existing_pages, hub_page_id) for chunk in self.chunks
        )
        if chunks == self.chunks:
            return self
        return replace(self, chunks=chunks, integrated=False)

    def requeue_mismatched_pages(
        self, expected_pages_by_chunk: dict[int, tuple[str, ...]]
    ) -> Manifest:
        chunks = tuple(
            _requeue_if_mismatched_pages(chunk, expected_pages_by_chunk.get(chunk.chunk_id, ()))
            for chunk in self.chunks
        )
        if chunks == self.chunks:
            return self
        return replace(self, chunks=chunks, integrated=False)

    def requeue_pages_with_wrong_source(
        self, sources_by_page: dict[str, tuple[str, ...]], source_locator: str
    ) -> Manifest:
        chunks = tuple(
            _requeue_if_wrong_source(chunk, sources_by_page, source_locator)
            for chunk in self.chunks
        )
        if chunks == self.chunks:
            return self
        return replace(self, chunks=chunks, integrated=False)

    def digest(self) -> str:
        """Concatenated per-chunk notes for the integrate run.

        The recorded pages_written line is the machine record; the notes
        above it are the model's own account.
        """
        parts = []
        for c in self.chunks:
            if c.status != "done" or not c.notes:
                continue
            entry = f"Chunk {c.chunk_id} — {c.heading} (p.{c.start_page}-{c.end_page}):\n{c.notes}"
            if c.pages_written:
                entry += "\nPages written (recorded): " + ", ".join(
                    f"[[{p}]]" for p in c.pages_written
                )
            if c.route_plan_pages or c.route_plan_gaps:
                entry += (
                    "\nIngest route plan: "
                    f"{c.route_plan_pages} planned page(s), {c.route_plan_gaps} route gap(s)"
                )
            parts.append(entry)
        return "\n\n".join(parts)

    def page_map(self) -> str:
        """Compact machine record for integration prompts."""
        parts = []
        for c in self.chunks:
            if c.status != "done":
                continue
            pages = ", ".join(f"[[{p}]]" for p in c.pages_written) or "(none recorded)"
            route_plan = ""
            if c.route_plan_pages or c.route_plan_gaps:
                route_plan = (
                    f"; route plan: {c.route_plan_pages} planned page(s), "
                    f"{c.route_plan_gaps} route gap(s)"
                )
            parts.append(
                f"Chunk {c.chunk_id} — {c.heading} "
                f"(p.{c.start_page}-{c.end_page}): {pages}{route_plan}"
            )
        return "\n".join(parts)

    def write_counts(self) -> dict[str, int]:
        """Per-page write totals across done chunks (salience input)."""
        counts: dict[str, int] = {}
        for c in self.chunks:
            for page in c.pages_written:
                counts[page] = counts.get(page, 0) + 1
        return counts


def _requeue_if_missing_pages(
    chunk: ChunkRecord, existing_pages: frozenset[str], hub_page_id: str
) -> ChunkRecord:
    if chunk.status != "done":
        return chunk
    if chunk.route_plan_pages and not chunk.pages_written:
        return _pending_chunk(chunk)
    if hub_page_id and set(chunk.pages_written) == {hub_page_id}:
        return _pending_chunk(chunk)
    if not chunk.pages_written:
        return chunk
    if all(page in existing_pages for page in chunk.pages_written):
        return chunk
    return _pending_chunk(chunk)


def _requeue_if_mismatched_pages(
    chunk: ChunkRecord, expected_pages: tuple[str, ...]
) -> ChunkRecord:
    if chunk.status != "done" or not chunk.route_plan_pages or not expected_pages:
        return chunk
    if set(chunk.pages_written) == set(expected_pages):
        return chunk
    return _pending_chunk(chunk)


def _requeue_if_wrong_source(
    chunk: ChunkRecord, sources_by_page: dict[str, tuple[str, ...]], source_locator: str
) -> ChunkRecord:
    if chunk.status != "done" or not chunk.pages_written:
        return chunk
    if all(
        _page_sources_cover_locator(sources_by_page.get(page_id, ()), source_locator)
        for page_id in chunk.pages_written
    ):
        return chunk
    return _pending_chunk(chunk)


def _page_sources_cover_locator(sources: tuple[str, ...], source_locator: str) -> bool:
    target = _normalize_source_locator(source_locator)
    return any(_normalize_source_locator(source) == target for source in sources)


def _normalize_source_locator(source: str) -> str:
    normalized = source.strip().removeprefix("raw/").strip()
    return normalized.split(" p.", maxsplit=1)[0].strip()


def _pending_chunk(chunk: ChunkRecord) -> ChunkRecord:
    return replace(
        chunk,
        status="pending",
        notes="",
        pages_written=(),
        route_plan_pages=0,
        route_plan_gaps=0,
        route_gap_summaries=(),
    )


def to_json(manifest: Manifest) -> str:
    return json.dumps(
        {
            "source": manifest.source,
            "sha256": manifest.sha256,
            "integrated": manifest.integrated,
            "chunks": [
                {
                    "id": c.chunk_id,
                    "heading": c.heading,
                    "pages": [c.start_page, c.end_page],
                    "tokens": c.token_estimate,
                    "status": c.status,
                    "notes": c.notes,
                    "pages_written": list(c.pages_written),
                    "route_plan_pages": c.route_plan_pages,
                    "route_plan_gaps": c.route_plan_gaps,
                    "route_gap_summaries": list(c.route_gap_summaries),
                }
                for c in manifest.chunks
            ],
        },
        indent=2,
        ensure_ascii=False,
    )


def from_json(text: str) -> Manifest:
    data = json.loads(text)
    return Manifest(
        source=data["source"],
        sha256=data["sha256"],
        integrated=data["integrated"],
        chunks=tuple(
            ChunkRecord(
                chunk_id=c["id"],
                heading=c["heading"],
                start_page=c["pages"][0],
                end_page=c["pages"][1],
                token_estimate=c["tokens"],
                status=c["status"],
                notes=c["notes"],
                # absent in manifests written before the salience design
                pages_written=tuple(c.get("pages_written", [])),
                route_plan_pages=c.get("route_plan_pages", 0),
                route_plan_gaps=c.get("route_plan_gaps", 0),
                route_gap_summaries=tuple(c.get("route_gap_summaries", [])),
            )
            for c in data["chunks"]
        ),
    )
