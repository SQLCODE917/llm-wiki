"""Shared page-title lint for generated public page candidates."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.page_synthesis_text import words
from llmwiki.domain.pages import PageError, validate_page_id

_MALFORMED_TOPIC_LABELS = frozenset({"alway", "bonuse", "needn", "sixe"})
_MALFORMED_PHRASES = ("double sixe",)
_TOPIC_FAMILIES = {"topic-concept", "broad-topic"}


@dataclass(frozen=True)
class PageTitleFinding:
    finding_id: str
    severity: str
    finding_code: str
    title: str
    message: str


def lint_page_title(title: str, page_id: str, page_family: str) -> tuple[PageTitleFinding, ...]:
    findings: list[PageTitleFinding] = []
    cleaned_title = " ".join(title.split()).strip()
    if not cleaned_title:
        findings.append(_finding("blank-page-title", title, "candidate title is blank"))
    try:
        validate_page_id(page_id)
    except PageError as exc:
        findings.append(_finding("invalid-page-id", title, str(exc)))
    if _has_malformed_identity(cleaned_title) or _has_malformed_identity(page_id):
        findings.append(
            _finding(
                "malformed-topic-identity",
                title,
                "candidate title or page id contains a malformed extracted topic label",
            )
        )
    if page_family in _TOPIC_FAMILIES and is_weak_topic_identity(cleaned_title):
        findings.append(
            _finding(
                "weak-topic-identity",
                title,
                "topic label is malformed or too weak for a public synthesized page",
            )
        )
    return tuple(findings)


def is_weak_topic_identity(label: str) -> bool:
    tokens = _identity_tokens(label)
    if not tokens:
        return True
    return any(token in _MALFORMED_TOPIC_LABELS for token in tokens)


def _has_malformed_identity(label: str) -> bool:
    lowered = " ".join(label.casefold().replace("-", " ").split())
    return any(phrase in lowered for phrase in _MALFORMED_PHRASES) or is_weak_topic_identity(label)


def _identity_tokens(label: str) -> tuple[str, ...]:
    return tuple(part for token in words(label) for part in token.split("-") if part)


def _finding(code: str, title: str, message: str) -> PageTitleFinding:
    return PageTitleFinding(
        finding_id=deterministic_id("page-title-finding", code, title),
        severity="blocking",
        finding_code=code,
        title=title,
        message=message,
    )
