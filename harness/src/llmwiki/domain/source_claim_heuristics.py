"""Text-shape heuristics for source claim classification."""

from __future__ import annotations

import re

from llmwiki.domain.planning_analysis import tokens


def is_source_furniture(lowered: str) -> bool:
    if ("to the left of" in lowered or "to the right of" in lowered) and "field" in lowered:
        return True
    if "field to write" in lowered or "field labeled" in lowered:
        return True
    furniture_patterns = (
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
    if any(re.search(pattern, lowered) for pattern in furniture_patterns):
        return True
    statement_tokens = tokens(lowered)
    if len(statement_tokens) <= 14 and _is_short_byline_furniture(lowered):
        return True
    return len(statement_tokens) <= 8 and not lowered.endswith((".", "?", "!"))


def _is_short_byline_furniture(lowered: str) -> bool:
    return bool(
        re.search(
            r"^(?:by|written by|edited by|translated by|illustrated by|authored by)\b",
            lowered,
        )
        or re.search(
            r"\b(?:written|edited|translated|illustrated|authored|published)\s+by\b",
            lowered,
        )
    )


def is_code_fragment(statement: str) -> bool:
    stripped = statement.strip()
    if stripped.startswith(("```", "~~~", "const ", "let ", "var ", "function ")):
        return True
    code_markers = sum(
        marker in stripped for marker in ("=>", "===", "!==", "{", "}", "();", "return ")
    )
    return code_markers >= 2 and len(tokens(stripped)) <= 18


def is_rhetorical_example(lowered: str) -> bool:
    if lowered.endswith("?"):
        return True
    return any(
        re.search(pattern, lowered)
        for pattern in (r"\bwhy\?\b", r"\bwhat if\b", r"\bhow would\b", r"\bwouldn'?t it\b")
    )


def is_narrative_frame(lowered: str) -> bool:
    if lowered.startswith(("'", '"')):
        return True
    narrative_patterns = (
        r"\bdear reader\b",
        r"\blet us\b",
        r"\blet's\b",
        r"\bwe will\b",
        r"\bwe'?ll\b.+\blook\b",
        r"\bwe are going to\b",
        r"\bimagine\b",
        r"\bthe story\b",
        r"\bonce upon\b",
        r"\bthere are\b.+\bways to make it\b",
        r"\binterview(er|s|ing)?\b",
        r"\brecruiter\b",
        r"\bconference room\b",
        r"\barrived early\b",
        r"\byou (desire|tolerate|express your order)\b",
        r"\bi (came across|went|pondered|told|think|thought|asked|couldn'?t)\b",
        r"\bsomeone asked me\b",
        r"\bespresso\b",
        r"\bristretto\b",
        r"\blong pull\b.+\bcoffee\b",
        r"\bcoffee\b.+\bflavou?r complexity\b",
        r"\bcoffee enthusiasts everywhere\b",
        r"\bbob was well-known\b",
        r"\bblind dating\b",
        r"\bclients often needed experience\b",
        r"\basks (?:us|you) to\b",
    )
    return any(re.search(pattern, lowered) for pattern in narrative_patterns)
