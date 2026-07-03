"""Evidence-page selection policy for grounded chat reads."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from llmwiki.domain.pages import PageError, PageMetadata, parse_page
from llmwiki.domain.search import SearchHit

_AGGREGATE_PAGE_FAMILIES = frozenset({"source-manifest", "broad-topic"})
_FOCUSED_PAGE_FAMILIES = frozenset(
    {
        "source-summary",
        "section-reference",
        "topic-concept",
        "procedure-guide",
        "recipe-pattern",
        "entity-profile",
        "cross-source-synthesis",
    }
)
_SUGGESTED_FOCUSED_PAGES = 4


@dataclass(frozen=True)
class ChatEvidenceCandidate:
    page_id: str
    score: int
    page_family: str

    @property
    def is_aggregate(self) -> bool:
        return self.page_family in _AGGREGATE_PAGE_FAMILIES

    @property
    def is_focused(self) -> bool:
        if not self.page_family:
            return True
        return self.page_family in _FOCUSED_PAGE_FAMILIES


@dataclass(frozen=True)
class ChatEvidenceReadDecision:
    allowed: bool
    message: str = ""


@dataclass(frozen=True)
class ChatEvidenceScope:
    """The evidence pages a content chat turn discovered before tool use."""

    candidates: tuple[ChatEvidenceCandidate, ...] = ()

    @classmethod
    def from_search_hits(
        cls, pages: Mapping[str, str], hits: Sequence[SearchHit]
    ) -> ChatEvidenceScope:
        candidates: list[ChatEvidenceCandidate] = []
        for hit in hits:
            text = pages.get(hit.page_id)
            if text is None:
                continue
            try:
                page = parse_page(text)
            except PageError:
                continue
            candidates.append(
                ChatEvidenceCandidate(
                    page_id=hit.page_id,
                    score=hit.score,
                    page_family=page.page_metadata.page_family,
                )
            )
        return cls(tuple(candidates))

    def read_decision(self, metadata: PageMetadata) -> ChatEvidenceReadDecision:
        if metadata.page_family not in _AGGREGATE_PAGE_FAMILIES:
            return ChatEvidenceReadDecision(allowed=True)
        focused = self._focused_candidates()
        if not focused:
            return ChatEvidenceReadDecision(allowed=True)
        aggregate_score = self._candidate_score(metadata.page_id)
        best_focused_score = max(candidate.score for candidate in focused)
        if aggregate_score > best_focused_score:
            return ChatEvidenceReadDecision(allowed=True)
        suggestions = ", ".join(f"[[{candidate.page_id}]]" for candidate in focused[:4])
        return ChatEvidenceReadDecision(
            allowed=False,
            message=(
                f"Do not use [[{metadata.page_id}]] as evidence for this focused "
                f"lookup: it is a broad {metadata.page_family} page, and the "
                "current search scope has more focused pages with at least as "
                f"much relevance. Read one of these instead: {suggestions}."
            ),
        )

    def _focused_candidates(self) -> tuple[ChatEvidenceCandidate, ...]:
        focused = tuple(candidate for candidate in self.candidates if candidate.is_focused)
        return tuple(
            sorted(
                focused,
                key=lambda candidate: (-candidate.score, candidate.page_id),
            )[:_SUGGESTED_FOCUSED_PAGES]
        )

    def _candidate_score(self, page_id: str) -> int:
        for candidate in self.candidates:
            if candidate.page_id == page_id:
                return candidate.score
        return 0
