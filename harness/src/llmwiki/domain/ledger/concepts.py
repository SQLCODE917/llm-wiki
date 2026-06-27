"""Concept-topic extraction for claim-ledger entries.

Concept facets are source-derived defined terms, not arbitrary subject tokens.
This keeps cross-source topic planning from cleaning up bad subjects after the
fact: only entries with explicit, lexicalized concept facets can anchor topics.
"""

from __future__ import annotations

import re

_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9-]*")
_QUOTED = re.compile(r'"([^"]+)"|\'([^\']+)\'|`([^`]+)`')
_DEFINITION_CUE = re.compile(
    r"\b(is\s+defined\s+as|defined\s+as|refers\s+to|is\s+called|known\s+as|means(?!\s+of\b))\b",
    re.IGNORECASE,
)
_LEXICAL_FRAME = re.compile(
    r"\b(?:word|term|phrase|name|concept)\s+(?:called\s+|named\s+)?(.+)$",
    re.IGNORECASE,
)
_LEADING_GRAMMAR = re.compile(
    r"^(?:a|an|the|this|that|these|those|one|two|first|second|very)\s+",
    re.IGNORECASE,
)
_TRAILING_CLAUSE = re.compile(r"\s+(?:that|which|who|whose|with|from|in|on|for)\b.*$", re.I)
_TRAILING_DEFINITION_MODIFIER = re.compile(r"\s+(?:merely|simply|only|just)$", re.I)
_DEICTIC_OR_PRONOUN = frozenset(
    {
        "i",
        "you",
        "he",
        "she",
        "it",
        "we",
        "they",
        "this",
        "that",
        "these",
        "those",
        "here",
        "there",
        "what",
        "when",
        "where",
        "which",
        "who",
        "whom",
        "whose",
    }
)
_PREPOSITIONS = frozenset({"in", "on", "at", "by", "for", "from", "with", "without", "of"})


def concept_facets_for_definition(statement: str, subject: str) -> tuple[str, ...]:
    """Return exact concept facets when a definition has a defined term.

    The detector accepts source-neutral linguistic forms:
    - quoted/code-styled terms before the definition cue;
    - lexical frames such as "the term X" or "the word X";
    - concise noun phrases before a definition predicate.

    Deictic subjects such as "this means ..." do not define a portable concept.
    """

    prefix = _definition_prefix(statement)
    if not prefix:
        return ()
    candidates = (
        _quoted_term(prefix),
        _lexical_frame_term(prefix),
        _direct_defined_subject(prefix, subject),
    )
    for candidate in candidates:
        normalized = _normalize(candidate)
        if _is_defined_term(normalized):
            return (normalized,)
    return ()


def concept_topic_keys(facets: tuple[str, ...]) -> tuple[str, ...]:
    keys = []
    for facet in facets:
        key = "-".join(token.lower() for token in _TOKEN.findall(facet))
        if key:
            keys.append(key)
    return tuple(dict.fromkeys(keys))


def _definition_prefix(statement: str) -> str:
    match = _DEFINITION_CUE.search(statement)
    if match is None:
        return ""
    return statement[: match.start()].strip()


def _quoted_term(prefix: str) -> str:
    matches = tuple(_QUOTED.finditer(prefix))
    if not matches:
        return ""
    match = matches[-1]
    return next(group for group in match.groups() if group)


def _lexical_frame_term(subject: str) -> str:
    match = _LEXICAL_FRAME.search(subject)
    return match.group(1) if match else ""


def _direct_defined_subject(prefix: str, subject: str) -> str:
    return subject if _normalize(prefix) == _normalize(subject) else ""


def _normalize(text: str) -> str:
    normalized = " ".join(text.replace("_", " ").split())
    normalized = normalized.strip(" \t\n\r.,;:()[]{}")
    while True:
        stripped = _LEADING_GRAMMAR.sub("", normalized).strip()
        if stripped == normalized:
            break
        normalized = stripped
    normalized = _TRAILING_CLAUSE.sub("", normalized).strip(" \t\n\r.,;:()[]{}")
    normalized = _TRAILING_DEFINITION_MODIFIER.sub("", normalized).strip(" \t\n\r.,;:()[]{}")
    return normalized.lower()


def _is_defined_term(text: str) -> bool:
    tokens = [token.lower() for token in _TOKEN.findall(text)]
    if not tokens or len(tokens) > 5:
        return False
    if any(token in _DEICTIC_OR_PRONOUN for token in tokens):
        return False
    if tokens[0] in _PREPOSITIONS:
        return False
    return any(any(char.isalpha() for char in token) for token in tokens)
