"""Text-shape heuristics for source claim classification."""

from __future__ import annotations

import re

from llmwiki.domain.planning_analysis import tokens

_FURNITURE_PHRASES = (
    "©",
    "(c)",
    "copyright",
    "isbn",
    "table of contents",
    "http://",
    "https://",
    "for sale at",
    "leanpub",
    "also by",
    "original words in this book",
    "author and publisher",
    "authors and publishers",
    "lean publishing",
    "creativecommons",
    "some rights reserved",
    "all rights reserved",
    "flickr",
    "acknowledgment",
    "acknowledgement",
    "acknowledgments",
    "acknowledgements",
    "about the author",
    "download",
    "published by",
    "everything is explained",
)
_SHORT_BYLINE_PREFIXES = (
    "by ",
    "written by ",
    "edited by ",
    "translated by ",
    "illustrated by ",
    "authored by ",
)
_SHORT_BYLINE_PHRASES = (
    "written by",
    "edited by",
    "translated by",
    "illustrated by",
    "authored by",
    "published by",
)
_RHETORICAL_REGEXES = tuple(
    re.compile(pattern)
    for pattern in (r"\bwhy\?\b", r"\bwhat if\b", r"\bhow would\b", r"\bwouldn'?t it\b")
)
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
_MAX_CODE_FRAGMENT_INPUT_CHARS = 20_000
_SPACE_STRIPPED_PUNCTUATION = frozenset(",;:)]")


def is_source_furniture(lowered: str) -> bool:
    lowered = lowered[:4_000]
    if ("to the left of" in lowered or "to the right of" in lowered) and "field" in lowered:
        return True
    if "field to write" in lowered or "field labeled" in lowered:
        return True
    if _has_any_phrase(lowered, _FURNITURE_PHRASES) or _has_page_number(lowered):
        return True
    statement_tokens = _ascii_words(lowered)
    if len(statement_tokens) <= 14 and _is_short_byline_furniture(lowered):
        return True
    return len(statement_tokens) <= 8 and not lowered.endswith((".", "?", "!"))


def _is_short_byline_furniture(lowered: str) -> bool:
    return lowered.startswith(_SHORT_BYLINE_PREFIXES) or _has_any_phrase(
        lowered, _SHORT_BYLINE_PHRASES
    )


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


def code_fragment_payload(statement: object) -> str:
    text = _bounded_text(statement)
    text = _strip_balanced_marker_spans(text, "**")
    text = _strip_balanced_marker_spans(text, "_")
    text = text.replace("\\ ", " ")
    return _collapse_space_before_punctuation(text)


def _bounded_text(value: object) -> str:
    text = value if isinstance(value, str) else str(value)
    return text[:_MAX_CODE_FRAGMENT_INPUT_CHARS]


def _strip_balanced_marker_spans(text: str, marker: str) -> str:
    if marker not in text:
        return text
    parts: list[str] = []
    index = 0
    marker_length = len(marker)
    while index < len(text):
        start = text.find(marker, index)
        if start < 0:
            parts.append(text[index:])
            break
        end = text.find(marker, start + marker_length)
        if end < 0:
            parts.append(text[index:])
            break
        inner = text[start + marker_length : end]
        if _markdown_span_is_plain(text, marker, start, end, inner):
            parts.append(text[index:start])
            parts.append(inner)
            index = end + marker_length
        else:
            parts.append(text[index : start + marker_length])
            index = start + marker_length
    return "".join(parts)


def _markdown_span_is_plain(text: str, marker: str, start: int, end: int, inner: str) -> bool:
    if not inner or "\n" in inner or marker in inner:
        return False
    before = text[start - 1] if start > 0 else " "
    after_index = end + len(marker)
    after = text[after_index] if after_index < len(text) else " "
    return not (_is_identifier_char(before) or _is_identifier_char(after))


def _is_identifier_char(char: str) -> bool:
    return char.isalnum() or char in "_$"


def _collapse_space_before_punctuation(text: str) -> str:
    chars: list[str] = []
    for char in text:
        if char in _SPACE_STRIPPED_PUNCTUATION:
            while chars and chars[-1].isspace():
                chars.pop()
        chars.append(char)
    return "".join(chars)


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


def _has_any_phrase(text: str, phrases: tuple[str, ...]) -> bool:
    return any(phrase in text for phrase in phrases)


def _has_page_number(text: str) -> bool:
    words = _ascii_words(text)
    for index, word in enumerate(words[:-1]):
        if word == "page" and _ascii_digits(words[index + 1]):
            return True
    return False


def _ascii_words(text: str) -> tuple[str, ...]:
    words: list[str] = []
    current: list[str] = []
    for char in text[:4_000]:
        if len(char) != 1:
            continue
        codepoint = ord(char)
        if 48 <= codepoint <= 57 or 97 <= codepoint <= 122:
            current.append(char)
        elif 65 <= codepoint <= 90:
            current.append(chr(codepoint + 32))
        elif current:
            words.append("".join(current))
            current = []
    if current:
        words.append("".join(current))
    return tuple(words)


def _ascii_digits(text: str) -> bool:
    return bool(text) and all(48 <= ord(char) <= 57 for char in text)
