"""Source-neutral prose-flow repair for extracted text.

PDF extractors often turn layout breaks into paragraph breaks. This module
repairs only structural continuations before source ranges are minted; it does
not use source-, book-, code-, or domain-specific vocabulary.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

_HARD_BLOCK = re.compile(r"^\s{0,3}(?:#{1,6}\s|```|~~~|\|.*\||\[Figure\b)", re.IGNORECASE)
_TRAILING_CONNECTIVE = re.compile(
    r"\b(?:and|or|but|nor|yet|so|for|if|when|whenever|unless|because|although|"
    r"while|where|which|that|who|whom|whose|with|of|to|as|than|then|also|only|"
    r"even|in|on|at|by|from|into|through|after|before|under|over|between|"
    r"without)\s*$",
    re.IGNORECASE,
)
_LEADING_CONTINUATION = re.compile(
    r"^(?:and|or|but|nor|yet|so|because|although|while|where|which|that|who|"
    r"whom|whose|then|also|again|therefore|however|unless|until|than|as)\b",
    re.IGNORECASE,
)
_LEADING_VERB_FRAGMENT = re.compile(
    r"^(?:again|also|then|therefore|however),?\s+"
    r"(?:is|are|was|were|be|been|being|has|have|had|do|does|did|must|shall|"
    r"should|may|might|can|could|will|would|ought|cannot|can not)\b",
    re.IGNORECASE,
)
_TERMINAL = frozenset(".!?")
_OPENERS = {"(": ")", "[": "]", "{": "}", "“": "”", '"': '"'}
_CLOSING_MARKS = "\"'”’)]}*_`~"
_OPENING_MARKS = "\"'“‘([{*_`~"


def normalize_prose_paragraphs(
    paragraphs: Iterable[str], *, max_chars: int | None = None
) -> tuple[str, ...]:
    """Merge adjacent prose paragraphs when the boundary is a continuation."""

    merged: list[str] = []
    for paragraph in paragraphs:
        text = _clean(paragraph)
        if not text:
            continue
        if merged and should_merge_prose(merged[-1], text, max_chars=max_chars):
            merged[-1] = f"{merged[-1].rstrip()} {text.lstrip()}"
        else:
            merged.append(text)
    return tuple(merged)


def normalize_prose_text(text: str, *, max_chars: int | None = None) -> str:
    """Repair prose flow inside one markdown-ish text block."""

    blocks = tuple(_paragraph_blocks(text))
    merged = merge_prose_blocks(blocks, prose_kinds=("paragraph",), max_chars=max_chars)
    return "\n\n".join(block for _kind, block in merged)


def merge_prose_blocks(
    blocks: Iterable[tuple[str, str]],
    *,
    prose_kinds: tuple[str, ...] = ("paragraph",),
    max_chars: int | None = None,
) -> tuple[tuple[str, str], ...]:
    """Merge adjacent blocks only when both are prose of the same kind."""

    prose = set(prose_kinds)
    merged: list[tuple[str, str]] = []
    for kind, text in blocks:
        if (
            kind in prose
            and merged
            and merged[-1][0] == kind
            and should_merge_prose(merged[-1][1], text, max_chars=max_chars)
        ):
            merged[-1] = (kind, f"{merged[-1][1].rstrip()} {_clean(text)}")
        else:
            merged.append((kind, text))
    return tuple(merged)


def should_merge_prose(left: str, right: str, *, max_chars: int | None = None) -> bool:
    """Return true when two adjacent prose blocks form one textual unit."""

    left_text = _clean(left)
    right_text = _clean(right)
    if not left_text or not right_text or _HARD_BLOCK.match(right_text):
        return False
    if max_chars is not None and len(left_text) + len(right_text) + 1 > max_chars:
        return False
    if _strong_left_continuation(left_text):
        return True
    return _weak_left_continuation(left_text) and _right_continuation(right_text)


def structural_incompleteness_reason(text: str) -> str | None:
    """Classify source text that should not be asserted as a standalone unit."""

    cleaned = _clean(text)
    if not cleaned:
        return "empty text"
    if _strong_left_continuation(cleaned):
        return "text ends with an unfinished clause"
    if _LEADING_VERB_FRAGMENT.match(_strip_opening_marks(cleaned)):
        return "text starts with a continuation cue before a verb"
    if _has_unclosed_delimiter(cleaned):
        return "text has an unclosed delimiter"
    return None


def _paragraph_blocks(text: str) -> tuple[tuple[str, str], ...]:
    blocks: list[tuple[str, str]] = []
    current: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            _append_text_block(blocks, current)
            current = []
            continue
        if _HARD_BLOCK.match(stripped):
            _append_text_block(blocks, current)
            blocks.append(("hard", stripped))
            current = []
            continue
        current.append(stripped)
    _append_text_block(blocks, current)
    return tuple(blocks)


def _append_text_block(blocks: list[tuple[str, str]], lines: list[str]) -> None:
    if lines:
        blocks.append(("paragraph", _clean(" ".join(lines))))


def _strong_left_continuation(text: str) -> bool:
    tail = _strip_closing_marks(text)
    return (
        tail.endswith(",")
        or _TRAILING_CONNECTIVE.search(tail) is not None
        or _has_unclosed_delimiter(tail)
    )


def _weak_left_continuation(text: str) -> bool:
    tail = _strip_closing_marks(text)
    return bool(tail) and tail[-1] not in _TERMINAL


def _right_continuation(text: str) -> bool:
    stripped = _strip_opening_marks(text)
    if not stripped:
        return False
    return (
        stripped[0].islower()
        or stripped[0] in ",;:)]}”’"
        or _LEADING_CONTINUATION.match(stripped) is not None
    )


def _has_unclosed_delimiter(text: str) -> bool:
    counts = {opener: 0 for opener in _OPENERS}
    for character in text:
        if character in counts:
            counts[character] += 1
        for opener, closer in _OPENERS.items():
            if character == closer and counts[opener] > 0:
                counts[opener] -= 1
    return any(count > 0 for opener, count in counts.items() if opener != '"')


def _strip_closing_marks(text: str) -> str:
    return text.rstrip().rstrip(_CLOSING_MARKS).rstrip()


def _strip_opening_marks(text: str) -> str:
    return text.lstrip().lstrip(_OPENING_MARKS).lstrip()


def _clean(text: str) -> str:
    return " ".join(text.split()).strip()
