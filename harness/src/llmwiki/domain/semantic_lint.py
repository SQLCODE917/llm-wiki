"""Deterministic scaffolding for model-assisted semantic lint."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from itertools import combinations
from typing import Literal

from llmwiki.domain.candidates import CandidateBacklog
from llmwiki.domain.citations import parse_citations
from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.system_pages import SYSTEM_PAGES

DEFAULT_MAX_ITEMS = 5
SemanticFindingKind = Literal["stale_claim", "possible_supersession", "data_gap"]
_EXCERPT_CHARS = 420
_TOKEN_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
_STOPWORDS = frozenset({"and", "are", "for", "from", "page", "raw", "see", "the", "with"})


@dataclass(frozen=True)
class SemanticLintCandidate:
    reason: str
    page_names: tuple[str, ...]
    missing_concept: str
    excerpt: str
    score: int

    def render(self, index: int) -> str:
        pages = ", ".join(f"[[{name}]]" for name in self.page_names) or "(none)"
        missing = f"\nMissing concept: {self.missing_concept}" if self.missing_concept else ""
        return (
            f"### Item {index}\n"
            f"Reason: {self.reason}\n"
            f"Pages: {pages}{missing}\n\n"
            f"Context:\n{self.excerpt}"
        )


@dataclass(frozen=True)
class SemanticLintSelection:
    candidates: tuple[SemanticLintCandidate, ...]
    candidate_count: int
    max_items: int

    @property
    def audited_count(self) -> int:
        return len(self.candidates)

    @property
    def skipped_count(self) -> int:
        return max(0, self.candidate_count - self.audited_count)

    def render_for_prompt(self) -> str:
        if not self.candidates:
            return "No semantic lint candidates were selected."
        return "\n\n".join(
            candidate.render(index) for index, candidate in enumerate(self.candidates, 1)
        )


@dataclass(frozen=True)
class SemanticFinding:
    kind: SemanticFindingKind
    affected_pages: tuple[str, ...]
    rationale: str
    evidence_consulted: str
    recommended_action: str

    def render(self, index: int) -> str:
        pages = ", ".join(f"[[{page}]]" for page in self.affected_pages)
        return (
            f"### Finding {index}: {self.kind}\n\n"
            f"- Pages: {pages}\n"
            f"- Rationale: {self.rationale}\n"
            f"- Evidence consulted: {self.evidence_consulted}\n"
            f"- Recommended action: {self.recommended_action}"
        )


@dataclass(frozen=True)
class SemanticLintReport:
    selection: SemanticLintSelection
    findings: tuple[SemanticFinding, ...]
    model_report: str

    def render(self) -> str:
        return "\n\n".join(
            [
                "# Semantic Lint",
                "## Audit Scope\n\n" + self._scope(),
                "## Findings\n\n" + self._findings(),
                "## Model Report\n\n" + (self.model_report.strip() or "No model report."),
                "## Uncertainty\n\n"
                "This is a bounded semantic lint pass over selected leads, not proof "
                "that the wiki has no stale claims or data gaps.",
            ]
        )

    def summary(self) -> str:
        return (
            f"Semantic lint: {len(self.findings)} finding(s); "
            f"audited {self.selection.audited_count} of "
            f"{self.selection.candidate_count} candidate item(s)."
        )

    def _scope(self) -> str:
        return (
            f"Candidate items discovered: {self.selection.candidate_count}\n"
            f"Audited items: {self.selection.audited_count}\n"
            f"Skipped by cap: {self.selection.skipped_count}\n"
            f"Max items: {self.selection.max_items}"
        )

    def _findings(self) -> str:
        if not self.findings:
            return "No semantic lint findings were recorded in the audited set."
        return "\n\n".join(finding.render(index) for index, finding in enumerate(self.findings, 1))


def select_semantic_lint_candidates(
    page_texts: Mapping[str, str],
    candidate_backlog: CandidateBacklog,
    *,
    max_items: int = DEFAULT_MAX_ITEMS,
) -> SemanticLintSelection:
    if max_items < 1:
        raise ValueError("max_items must be at least 1.")
    pages = {
        name: _page_signals(name, text)
        for name, text in page_texts.items()
        if name not in SYSTEM_PAGES
    }
    candidates = [*_data_gap_candidates(candidate_backlog, pages), *_overlap_candidates(pages)]
    ordered = tuple(
        sorted(candidates, key=lambda item: (-item.score, item.reason, item.page_names))
    )
    return SemanticLintSelection(
        candidates=ordered[:max_items],
        candidate_count=len(ordered),
        max_items=max_items,
    )


@dataclass(frozen=True)
class _PageSignals:
    body: str
    sources: frozenset[str]
    citations: frozenset[str]
    links: frozenset[str]
    keywords: frozenset[str]
    updated: str


def _data_gap_candidates(
    backlog: CandidateBacklog, pages: Mapping[str, _PageSignals]
) -> tuple[SemanticLintCandidate, ...]:
    selected: list[SemanticLintCandidate] = []
    for record in backlog.top():
        related = tuple(page for page in record.source_pages if page in pages)
        if not related:
            continue
        excerpts = "\n\n".join(f"[[{page}]]: {_excerpt(pages[page].body)}" for page in related[:2])
        selected.append(
            SemanticLintCandidate(
                reason=f"data gap candidate: {record.slug} ({record.status})",
                page_names=related,
                missing_concept=record.slug,
                excerpt=excerpts,
                score=5 + record.mention_count,
            )
        )
    return tuple(selected)


def _overlap_candidates(pages: Mapping[str, _PageSignals]) -> tuple[SemanticLintCandidate, ...]:
    selected: list[SemanticLintCandidate] = []
    for left, right in combinations(sorted(pages), 2):
        candidate = _overlap_candidate(left, pages[left], right, pages[right])
        if candidate is not None:
            selected.append(candidate)
    return tuple(selected)


def _overlap_candidate(
    left: str, left_signals: _PageSignals, right: str, right_signals: _PageSignals
) -> SemanticLintCandidate | None:
    reasons: list[str] = []
    score = 0
    if shared_sources := sorted(_specific_sources(left_signals.sources & right_signals.sources)):
        reasons.append("shared sources: " + ", ".join(shared_sources[:3]))
        score += 4
    if shared_citations := sorted(left_signals.citations & right_signals.citations):
        reasons.append("shared raw citations: " + ", ".join(shared_citations[:3]))
        score += 4
    if right in left_signals.links or left in right_signals.links:
        reasons.append("direct wiki link")
        score += 3
    if (right in left_signals.links or left in right_signals.links) and len(
        left_signals.keywords & right_signals.keywords
    ) >= 4:
        reasons.append("repeated topic keywords")
        score += 1
    if (
        left_signals.updated
        and right_signals.updated
        and left_signals.updated != right_signals.updated
    ):
        reasons.append(f"updated dates differ: {left_signals.updated} vs {right_signals.updated}")
        score += 1
    if score < 5:
        return None
    excerpt = (
        f"[[{left}]]: {_excerpt(left_signals.body)}\n\n[[{right}]]: {_excerpt(right_signals.body)}"
    )
    return SemanticLintCandidate(
        reason="; ".join(reasons),
        page_names=(left, right),
        missing_concept="",
        excerpt=excerpt,
        score=score,
    )


def _page_signals(name: str, text: str) -> _PageSignals:
    try:
        page = parse_page(name, text)
        body = page.body
        sources = frozenset(page.sources)
        updated = page.updated
    except PageError:
        body = text
        sources = frozenset()
        updated = ""
    return _PageSignals(
        body=body,
        sources=sources,
        citations=frozenset(c.raw_text for c in parse_citations(name, body).citations),
        links=frozenset(extract_links(body)),
        keywords=_keywords(name + "\n" + body),
        updated=updated,
    )


def _keywords(text: str) -> frozenset[str]:
    tokens = {part for token in _TOKEN_RE.findall(text.lower()) for part in token.split("-")}
    return frozenset(token for token in tokens if token and token not in _STOPWORDS)


def _specific_sources(sources: frozenset[str]) -> frozenset[str]:
    return frozenset(source for source in sources if " p." in source or "normalized:" in source)


def _excerpt(text: str) -> str:
    cleaned = " ".join(line.strip() for line in text.splitlines() if line.strip())
    if not cleaned:
        return "(empty page body)"
    if len(cleaned) <= _EXCERPT_CHARS:
        return cleaned
    return cleaned[: _EXCERPT_CHARS - 15].rstrip() + " ... [truncated]"
