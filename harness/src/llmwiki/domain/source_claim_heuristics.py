"""Text-shape heuristics for source claim classification."""

from __future__ import annotations

import re

from llmwiki.domain.planning_analysis import tokens

_FURNITURE_REGEXES = tuple(
    re.compile(pattern)
    for pattern in (
        r"©",
        r"\(c\)",
        r"\bcopyright\b",
        r"\bisbn\b",
        r"\btable of contents\b",
        r"\bhttp(s)?://\b",
        r"\bfor sale at\b",
        r"\bleanpub\b",
        r"\balso by\b",
        r"\boriginal words in this book\b",
        r"\bauthors? and publishers?\b",
        r"\blean publishing\b",
        r"\bcreativecommons\b",
        r"\bsome rights reserved\b",
        r"\ball rights reserved\b",
        r"\bflickr\b",
        r"\backnowledg(e)?ments?\b",
        r"\babout the author\b",
        r"\bdownload\b",
        r"\bpublished by\b",
        r"\beverything is explained\b",
        r"\bpage \d+\b",
    )
)
_SHORT_BYLINE_REGEXES = (
    re.compile(r"^(?:by|written by|edited by|translated by|illustrated by|authored by)\b"),
    re.compile(r"\b(?:written|edited|translated|illustrated|authored|published)\s+by\b"),
)
_RHETORICAL_REGEXES = tuple(
    re.compile(pattern)
    for pattern in (r"\bwhy\?\b", r"\bwhat if\b", r"\bhow would\b", r"\bwouldn'?t it\b")
)
_BOLD_SPAN_RE = re.compile(r"(?<![A-Za-z0-9_)])\*\*([^*\n]+?)\*\*(?![A-Za-z0-9_(])")
_ITALIC_SPAN_RE = re.compile(r"(?<![A-Za-z0-9_])_([^_\n]+?)_(?![A-Za-z0-9_])")
_DECLARATION_RE = re.compile(
    r"^\s*(?:const|let|var|class)\s+[A-Za-z_$][\w$]*(?:\s*[,=]|\s+extends\b)"
)
_FUNCTION_EXPRESSION_RE = re.compile(r"^\s*\(?\s*(?:async\s+)?function\b")
_ARROW_EXPRESSION_RE = re.compile(r"^\s*(?:async\s+)?(?:\([^)]*\)|[A-Za-z_$][\w$]*)\s*=>")
_NARRATIVE_PHRASES = (
    "dear reader",
    "let us",
    "let's",
    "we will",
    "we are going to",
    "imagine",
    "the story",
    "once upon",
    "they are given",
    "they are led",
    "they are told",
    "they find",
    "after a bit",
    "interview",
    "recruiter",
    "conference room",
    "arrived early",
    "someone asked me",
    "espresso",
    "ristretto",
    "coffee enthusiasts everywhere",
    "bob was well-known",
    "blind dating",
    "clients often needed experience",
    "asks us to",
    "asks you to",
)
_FIRST_PERSON_NARRATIVE_MARKERS = (
    "i came across",
    "i went",
    "i pondered",
    "i told",
    "i think",
    "i thought",
    "i asked",
    "i couldn't",
    "i couldnt",
)


def is_source_furniture(lowered: str) -> bool:
    if ("to the left of" in lowered or "to the right of" in lowered) and "field" in lowered:
        return True
    if "field to write" in lowered or "field labeled" in lowered:
        return True
    if _matches_any(_FURNITURE_REGEXES, lowered):
        return True
    statement_tokens = tokens(lowered)
    if len(statement_tokens) <= 14 and _is_short_byline_furniture(lowered):
        return True
    return len(statement_tokens) <= 8 and not lowered.endswith((".", "?", "!"))


def _is_short_byline_furniture(lowered: str) -> bool:
    return _matches_any(_SHORT_BYLINE_REGEXES, lowered)


def is_code_fragment(statement: str) -> bool:
    stripped = code_fragment_payload(statement).strip()
    lowered = stripped.lower()
    if stripped.startswith(("```", "~~~", "const ", "let ", "var ", "function ")):
        return True
    if (
        _DECLARATION_RE.match(stripped)
        or _FUNCTION_EXPRESSION_RE.match(stripped)
        or _ARROW_EXPRESSION_RE.match(stripped)
    ):
        return True
    code_markers = sum(
        marker in lowered
        for marker in (
            "=>",
            "===",
            "!==",
            "{",
            "}",
            "();",
            "return ",
            "function ",
            "yield ",
            ";",
        )
    )
    return code_markers >= 2 and len(tokens(stripped)) <= 48


def code_fragment_payload(statement: str) -> str:
    text = _BOLD_SPAN_RE.sub(r"\1", statement)
    text = _ITALIC_SPAN_RE.sub(r"\1", text)
    text = text.replace("\\ ", " ")
    text = re.sub(r"\s+([,;:)\]])", r"\1", text)
    return text


def is_rhetorical_example(lowered: str) -> bool:
    if lowered.endswith("?"):
        return True
    return _matches_any(_RHETORICAL_REGEXES, lowered)


def is_narrative_frame(lowered: str) -> bool:
    if lowered.startswith(("'", '"')):
        return True
    if any(phrase in lowered for phrase in _NARRATIVE_PHRASES):
        return True
    if any(marker in lowered for marker in _FIRST_PERSON_NARRATIVE_MARKERS):
        return True
    if "we'll" in lowered and "look" in lowered:
        return True
    if "when" in lowered and "trying to choose" in lowered and _mentions_people(lowered):
        return True
    if "of course," in lowered and "students" in lowered:
        return True
    if "once again" in lowered and "card" in lowered:
        return True
    if "whereas the" in lowered and ("mathematicians" in lowered or "engineers" in lowered):
        return True
    if "there are" in lowered and "ways to make it" in lowered:
        return True
    if "you desire" in lowered or "you tolerate" in lowered:
        return True
    return "express your order" in lowered


def _mentions_people(lowered: str) -> bool:
    return any(group in lowered for group in ("students", "people", "customers", "programmers"))


def _matches_any(patterns: tuple[re.Pattern[str], ...], text: str) -> bool:
    for pattern in patterns:  # noqa: SIM110 - avoid generator churn in claim hot path.
        if pattern.search(text):
            return True
    return False
