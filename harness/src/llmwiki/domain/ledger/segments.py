"""SourceSegment: one extracted source segment before atom/claim classification.

A ``SourceSegment`` is the domain's ``ExtractedUnit`` — a finer-grained span
than an ingest chunk (a fenced code block, a tabular block, a heading, a
paragraph, ...). Profiling, extractor decisions, and dispositions all happen at
this granularity, so every segment is accounted for with exactly one
disposition and a code block can become its own technical atom.
"""

from __future__ import annotations

from dataclasses import dataclass

SEGMENT_KINDS = (
    "heading",
    "code-fence",
    "table-block",
    "figure",
    "list",
    "paragraph",
    "blank",
)


@dataclass(frozen=True)
class SourceSegment:
    segment_id: str
    source_range_id: str
    source_locator: str
    source_hash: str
    heading_path: str
    structure_node_id: str
    source_order: int
    text: str
    segment_kind: str
    evidence_ids: tuple[str, ...] = ()
    source_element_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class SegmentClaim:
    """One candidate factual statement extracted from a segment.

    ``eligibility`` and ``role_tags`` come from the adapter's source-neutral
    claim classifier; the builder turns eligible, decomposable claims into
    claim-like ledger entries and routes fragmentary ones to review.
    """

    claim_id: str
    statement: str
    role_tags: tuple[str, ...] = ()
    eligibility: str = "eligible"
    certainty: str = "supported"
    evidence_ids: tuple[str, ...] = ()
