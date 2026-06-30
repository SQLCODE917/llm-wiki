"""Universal structured evidence extraction for task packs."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from llmwiki.domain.pages import PageError, parse_page

_MAX_ARTIFACT_CHARS = 900
_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9'~-]{2,}")
_ARITHMETIC_RE = re.compile(r"\b\d+\s*(?:[+\-*/xX]|x)\s*\d+.*=")
_DICE_RE = re.compile(r"\b\d+d(?:\s*[+xX]\s*\d+)?\b", re.IGNORECASE)
_TABLE_RE = re.compile(r"\btable\b", re.IGNORECASE)
_EXAMPLE_RE = re.compile(
    r"\b(?:example|worked example|for example|this character|our|we(?:'ll|'ve|'re)?)\b",
    re.IGNORECASE,
)
_MARKDOWN_TABLE_RE = re.compile(r"^\s*\|.+\|\s*$", re.MULTILINE)
_TABLE_LABEL_RE = re.compile(
    r"\bTable\s+[A-Za-z0-9][A-Za-z0-9.-]*(?::\s*[^,.\n_`>()]+)?",
)
_STOP_TERMS = frozenset(
    {
        "about",
        "also",
        "and",
        "are",
        "can",
        "from",
        "has",
        "have",
        "into",
        "must",
        "not",
        "section",
        "source",
        "step",
        "that",
        "the",
        "their",
        "then",
        "this",
        "with",
        "you",
    }
)


@dataclass(frozen=True)
class StructuredEvidenceArtifact:
    """A compact structured fact block lifted from an already-projected page."""

    page_id: str
    category: str
    heading: str
    excerpt: str


def select_structured_evidence_artifacts(
    pages: Mapping[str, str],
    page_ids: Sequence[str],
    focus_texts: Sequence[str],
    *,
    max_artifacts: int = 24,
    max_total_chars: int = 12_000,
) -> tuple[StructuredEvidenceArtifact, ...]:
    """Select table, formula, and worked-example artifacts from candidate pages."""

    focus_terms = _terms("\n".join(focus_texts))
    scored: list[tuple[int, int, StructuredEvidenceArtifact]] = []
    for page_order, page_id in enumerate(page_ids):
        text = pages.get(page_id)
        if text is None:
            continue
        try:
            page = parse_page(text)
        except PageError:
            continue
        if page.page_metadata.page_family == "source-manifest":
            continue
        for artifact in _extract_artifacts(page.page_id, page.page_body):
            scored.append((_score(artifact, focus_terms, page_order), page_order, artifact))

    selected: list[StructuredEvidenceArtifact] = []
    seen: set[str] = set()
    total = 0
    index_artifact = _table_index_artifact(scored)
    if index_artifact is not None:
        selected.append(index_artifact)
        seen.add(_fingerprint(index_artifact))
        total += len(index_artifact.excerpt)
    for _score_value, _page_order, artifact in sorted(scored, key=_sort_key):
        if len(selected) >= max_artifacts:
            break
        key = _fingerprint(artifact)
        if key in seen:
            continue
        excerpt = _clip(artifact.excerpt, _MAX_ARTIFACT_CHARS)
        if total + len(excerpt) > max_total_chars:
            break
        seen.add(key)
        total += len(excerpt)
        selected.append(
            StructuredEvidenceArtifact(
                page_id=artifact.page_id,
                category=artifact.category,
                heading=artifact.heading,
                excerpt=excerpt,
            )
        )
    return tuple(selected)


def _table_index_artifact(
    scored: Sequence[tuple[int, int, StructuredEvidenceArtifact]],
) -> StructuredEvidenceArtifact | None:
    entries: list[str] = []
    seen: set[str] = set()
    page_id = ""
    for _score_value, _page_order, artifact in sorted(scored, key=_sort_key):
        for label in _table_labels(artifact.excerpt):
            key = label.lower()
            if key in seen:
                continue
            seen.add(key)
            page_id = page_id or artifact.page_id
            entries.append(f"- {label} ([[{artifact.page_id}]])")
            if len(entries) >= 28:
                break
        if len(entries) >= 28:
            break
    if not entries:
        return None
    return StructuredEvidenceArtifact(
        page_id=page_id,
        category="table-index",
        heading="Exact table references",
        excerpt="Exact table references found in candidate evidence:\n" + "\n".join(entries),
    )


def _table_labels(text: str) -> tuple[str, ...]:
    labels: list[str] = []
    for match in _TABLE_LABEL_RE.finditer(text):
        label = " ".join(match.group(0).split()).rstrip(" ,.;:")
        label = re.split(r"\s+(?:shows|is|must|does|determine|or|and)\b", label, maxsplit=1)[0]
        if label.lower() == "table":
            continue
        labels.append(label)
    return tuple(labels)


def _extract_artifacts(page_id: str, body: str) -> tuple[StructuredEvidenceArtifact, ...]:
    artifacts: list[StructuredEvidenceArtifact] = []
    artifacts.extend(_raw_table_artifacts(page_id, body))
    artifacts.extend(_markdown_table_artifacts(page_id, body))
    artifacts.extend(_technical_frame_artifacts(page_id, body))
    artifacts.extend(_statement_artifacts(page_id, body))
    return tuple(artifacts)


def _raw_table_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    lines = body.splitlines()
    artifacts: list[StructuredEvidenceArtifact] = []
    heading = ""
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("#"):
            heading = line.lstrip("# ").strip()
        if "<summary>Raw table text</summary>" not in line:
            index += 1
            continue
        start = max(0, index - 1)
        end = index + 1
        while end < len(lines) and "</details>" not in lines[end]:
            end += 1
        end = min(len(lines), end + 1)
        artifacts.append(
            StructuredEvidenceArtifact(
                page_id=page_id,
                category="raw-table-text",
                heading=heading,
                excerpt="\n".join(lines[start:end]).strip(),
            )
        )
        index = end
    return artifacts


def _markdown_table_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    lines = body.splitlines()
    artifacts: list[StructuredEvidenceArtifact] = []
    heading = ""
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("#"):
            heading = line.lstrip("# ").strip()
        if "|" not in line:
            index += 1
            continue
        start = index
        while index < len(lines) and "|" in lines[index]:
            index += 1
        block = "\n".join(lines[start:index]).strip()
        if len(block.splitlines()) >= 2 and _MARKDOWN_TABLE_RE.search(block):
            artifacts.append(
                StructuredEvidenceArtifact(
                    page_id=page_id,
                    category="markdown-table",
                    heading=heading,
                    excerpt=block,
                )
            )
    return artifacts


def _technical_frame_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    lines = body.splitlines()
    artifacts: list[StructuredEvidenceArtifact] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.startswith("### Technical frame"):
            index += 1
            continue
        heading = line.removeprefix("### ").strip()
        start = index
        index += 1
        while index < len(lines) and not lines[index].startswith(("## ", "### ")):
            index += 1
        block = "\n".join(lines[start:index]).strip()
        if _has_structured_signal(block):
            artifacts.append(
                StructuredEvidenceArtifact(
                    page_id=page_id,
                    category=_category(block),
                    heading=heading,
                    excerpt=block,
                )
            )
    return artifacts


def _statement_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    artifacts: list[StructuredEvidenceArtifact] = []
    heading = ""
    for line in body.splitlines():
        if line.startswith("### "):
            heading = line.removeprefix("### ").strip()
        if not line.startswith("- "):
            continue
        if not _has_structured_signal(line):
            continue
        artifacts.append(
            StructuredEvidenceArtifact(
                page_id=page_id,
                category=_category(line),
                heading=heading,
                excerpt=line,
            )
        )
    return artifacts


def _has_structured_signal(text: str) -> bool:
    return any(
        (
            _TABLE_RE.search(text),
            _ARITHMETIC_RE.search(text),
            _DICE_RE.search(text),
            _EXAMPLE_RE.search(text),
            "<summary>Raw table text</summary>" in text,
            _MARKDOWN_TABLE_RE.search(text),
        )
    )


def _category(text: str) -> str:
    if "<summary>Raw table text</summary>" in text:
        return "raw-table-text"
    if _MARKDOWN_TABLE_RE.search(text):
        return "markdown-table"
    if _TABLE_RE.search(text):
        return "table-reference"
    if _ARITHMETIC_RE.search(text) or _DICE_RE.search(text):
        return "formula"
    if _EXAMPLE_RE.search(text):
        return "procedure-example"
    return "structured-reference"


def _score(
    artifact: StructuredEvidenceArtifact,
    focus_terms: frozenset[str],
    page_order: int,
) -> int:
    haystack = f"{artifact.heading}\n{artifact.excerpt}".lower()
    overlap = len(focus_terms.intersection(_terms(haystack)))
    score = max(0, 12 - page_order)
    score += min(28, overlap * 2)
    score += {
        "raw-table-text": 22,
        "markdown-table": 20,
        "formula": 14,
        "procedure-example": 14,
        "table-reference": 9,
        "structured-reference": 8,
    }.get(artifact.category, 0)
    score += _signal_bonus(artifact.excerpt)
    if artifact.heading and focus_terms.intersection(_terms(artifact.heading)):
        score += 6
    if _is_sparse_table_label(artifact.excerpt):
        score -= 10
    return score


def _signal_bonus(text: str) -> int:
    score = 0
    if _EXAMPLE_RE.search(text):
        score += 14
    if _ARITHMETIC_RE.search(text):
        score += 12
    if _DICE_RE.search(text):
        score += 8
    if _TABLE_RE.search(text):
        score += 6
    return score


def _is_sparse_table_label(text: str) -> bool:
    terms = _terms(re.sub(r"_\([^)]*\)_", "", text))
    return bool(_TABLE_RE.search(text)) and len(terms) <= 8


def _sort_key(item: tuple[int, int, StructuredEvidenceArtifact]) -> tuple[int, int, str, str]:
    score, page_order, artifact = item
    return (-score, page_order, artifact.category, artifact.heading)


def _terms(text: str) -> frozenset[str]:
    return frozenset(
        term
        for term in _TOKEN_RE.findall(text.lower())
        if term not in _STOP_TERMS and not term.isdigit()
    )


def _fingerprint(artifact: StructuredEvidenceArtifact) -> str:
    return " ".join(_TOKEN_RE.findall(artifact.excerpt.lower()))[:500]


def _clip(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    clipped = text[:max_chars].rstrip()
    return f"{clipped}\n[TRUNCATED: structured evidence artifact]"
