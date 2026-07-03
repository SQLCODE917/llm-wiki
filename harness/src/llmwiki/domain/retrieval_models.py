"""Domain records for deterministic wiki retrieval."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalSignal:
    name: str
    score: int
    detail: str


@dataclass(frozen=True)
class RetrievalCandidate:
    page_id: str
    page_kind: str
    summary: str
    score: int
    snippet: str
    signals: tuple[RetrievalSignal, ...]
    related_page_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class WikiContextPack:
    query: str
    candidates: tuple[RetrievalCandidate, ...]
    source_scope: tuple[str, ...] = ()
