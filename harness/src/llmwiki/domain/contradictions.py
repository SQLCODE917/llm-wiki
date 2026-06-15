"""Deterministic scaffolding for model-assisted contradiction audits."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import combinations
from typing import Literal

from llmwiki.domain.citations import parse_citations
from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.system_pages import SYSTEM_PAGES

ContradictionSeverity = Literal["low", "medium", "high"]

DEFAULT_MAX_PAIRS = 5
_EXCERPT_CHARS = 450
_TOKEN_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
_STOPWORDS = frozenset(
    {
        "about",
        "also",
        "and",
        "are",
        "because",
        "between",
        "but",
        "can",
        "claim",
        "concept",
        "from",
        "has",
        "into",
        "its",
        "not",
        "page",
        "raw",
        "see",
        "source",
        "that",
        "the",
        "this",
        "with",
    }
)


@dataclass(frozen=True)
class ContradictionCandidatePair:
    page_a: str
    page_b: str
    reasons: tuple[str, ...]
    excerpt_a: str
    excerpt_b: str
    score: int

    def render(self, index: int) -> str:
        reasons = ", ".join(self.reasons)
        return (
            f"### Pair {index}: [[{self.page_a}]] vs [[{self.page_b}]]\n"
            f"Reasons: {reasons}\n\n"
            f"Excerpt from [[{self.page_a}]]:\n{self.excerpt_a}\n\n"
            f"Excerpt from [[{self.page_b}]]:\n{self.excerpt_b}"
        )


@dataclass(frozen=True)
class ContradictionSelection:
    candidates: tuple[ContradictionCandidatePair, ...]
    candidate_count: int
    max_pairs: int

    @property
    def audited_count(self) -> int:
        return len(self.candidates)

    @property
    def skipped_count(self) -> int:
        return max(0, self.candidate_count - self.audited_count)

    def render_for_prompt(self) -> str:
        if not self.candidates:
            return "No deterministic contradiction candidate pairs were selected."
        return "\n\n".join(
            pair.render(index) for index, pair in enumerate(self.candidates, start=1)
        )


@dataclass(frozen=True)
class ContradictionFinding:
    page_a: str
    claim_a: str
    page_b: str
    claim_b: str
    severity: ContradictionSeverity
    rationale: str
    recommended_action: str

    def render(self, index: int) -> str:
        return (
            f"### Finding {index}: {self.severity.upper()} - "
            f"[[{self.page_a}]] vs [[{self.page_b}]]\n\n"
            f"- [[{self.page_a}]] claim: {self.claim_a}\n"
            f"- [[{self.page_b}]] claim: {self.claim_b}\n"
            f"- Rationale: {self.rationale}\n"
            f"- Recommended action: {self.recommended_action}"
        )


@dataclass(frozen=True)
class ContradictionAuditReport:
    selection: ContradictionSelection
    findings: tuple[ContradictionFinding, ...]
    model_report: str

    def render(self) -> str:
        findings = collapse_findings(self.findings)
        return "\n\n".join(
            [
                "# Contradiction Audit",
                "## Audit Scope\n\n" + self._scope(),
                "## Findings\n\n" + self._findings(findings),
                "## Model Report\n\n" + (self.model_report.strip() or "No model report."),
                "## Caveat\n\n"
                "This is a bounded audit over selected candidate pairs, not proof "
                "that the wiki has no contradictions.",
            ]
        )

    def _scope(self) -> str:
        return (
            f"Candidate pairs discovered: {self.selection.candidate_count}\n"
            f"Audited pairs: {self.selection.audited_count}\n"
            f"Skipped by cap: {self.selection.skipped_count}\n"
            f"Max pairs: {self.selection.max_pairs}"
        )

    def _findings(self, findings: tuple[ContradictionFinding, ...]) -> str:
        if not findings:
            return "No contradictions were recorded in the audited candidate set."
        return "\n\n".join(finding.render(index) for index, finding in enumerate(findings, 1))


def select_contradiction_candidates(
    page_texts: Mapping[str, str],
    *,
    max_pairs: int = DEFAULT_MAX_PAIRS,
) -> ContradictionSelection:
    if max_pairs < 1:
        raise ValueError("max_pairs must be at least 1.")
    pages = {
        name: _page_signals(name, text)
        for name, text in page_texts.items()
        if name not in SYSTEM_PAGES
    }
    candidates = [
        pair
        for left, right in combinations(sorted(pages), 2)
        if (pair := _candidate_pair(left, pages[left], right, pages[right])) is not None
    ]
    ordered = tuple(sorted(candidates, key=lambda pair: (-pair.score, pair.page_a, pair.page_b)))
    return ContradictionSelection(
        candidates=ordered[:max_pairs],
        candidate_count=len(ordered),
        max_pairs=max_pairs,
    )


def collapse_findings(
    findings: Sequence[ContradictionFinding],
) -> tuple[ContradictionFinding, ...]:
    seen: set[tuple[str, str, str, str]] = set()
    collapsed: list[ContradictionFinding] = []
    for finding in findings:
        pages = tuple(sorted((finding.page_a, finding.page_b)))
        claims = tuple(sorted((_normalize(finding.claim_a), _normalize(finding.claim_b))))
        key = (pages[0], pages[1], claims[0], claims[1])
        if key in seen:
            continue
        seen.add(key)
        collapsed.append(finding)
    return tuple(collapsed)


@dataclass(frozen=True)
class _PageSignals:
    body: str
    sources: frozenset[str]
    citations: frozenset[str]
    links: frozenset[str]
    keywords: frozenset[str]


def _page_signals(name: str, text: str) -> _PageSignals:
    try:
        page = parse_page(name, text)
        body = page.body
        sources = frozenset(page.sources)
    except PageError:
        body = text
        sources = frozenset()
    return _PageSignals(
        body=body,
        sources=sources,
        citations=frozenset(c.source_path for c in parse_citations(name, body).citations),
        links=frozenset(extract_links(body)),
        keywords=_keywords(name + "\n" + body),
    )


def _candidate_pair(
    page_a: str,
    signals_a: _PageSignals,
    page_b: str,
    signals_b: _PageSignals,
) -> ContradictionCandidatePair | None:
    reasons: list[str] = []
    score = 0
    if shared_sources := sorted(signals_a.sources & signals_b.sources):
        reasons.append("shared sources: " + ", ".join(shared_sources[:3]))
        score += 4
    if shared_citations := sorted(signals_a.citations & signals_b.citations):
        reasons.append("shared raw citations: " + ", ".join(shared_citations[:3]))
        score += 4
    if page_b in signals_a.links or page_a in signals_b.links:
        reasons.append("direct wiki link")
        score += 3
    shared_keywords = sorted(signals_a.keywords & signals_b.keywords)
    if len(shared_keywords) >= 3:
        reasons.append("keyword overlap: " + ", ".join(shared_keywords[:5]))
        score += 1
    if not reasons:
        return None
    return ContradictionCandidatePair(
        page_a=page_a,
        page_b=page_b,
        reasons=tuple(reasons),
        excerpt_a=_excerpt(signals_a.body),
        excerpt_b=_excerpt(signals_b.body),
        score=score,
    )


def _keywords(text: str) -> frozenset[str]:
    tokens = {part for token in _TOKEN_RE.findall(text.lower()) for part in token.split("-")}
    return frozenset(token for token in tokens if token and token not in _STOPWORDS)


def _excerpt(text: str) -> str:
    cleaned = " ".join(line.strip() for line in text.splitlines() if line.strip())
    if not cleaned:
        return "(empty page body)"
    if len(cleaned) <= _EXCERPT_CHARS:
        return cleaned
    return cleaned[: _EXCERPT_CHARS - 15].rstrip() + " ... [truncated]"


def _normalize(text: str) -> str:
    return " ".join(text.lower().split())
