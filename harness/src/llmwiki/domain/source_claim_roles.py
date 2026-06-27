"""Deterministic role tags for source claims."""

from __future__ import annotations

SOURCE_FRAMING_PREFIXES = (
    "the source discusses",
    "the source describes",
    "the source mentions",
    "the source notes",
    "the source lists",
    "the source provides",
    "this source discusses",
    "this source describes",
    "the text discusses",
    "the text describes",
    "the text mentions",
    "the text notes",
    "the section discusses",
    "the section describes",
    "the book discusses",
    "the book describes",
)

CLAIM_ROLE_ORDER = (
    "source-uncertainty",
    "ordinary-modality",
    "source-framing",
    "analogy",
    "worked-example",
    "negative-evidence",
    "limitation",
    "method",
    "evidence",
    "provenance",
    "temporal",
    "quantitative",
    "function",
    "mechanism",
    "comparison",
    "relationship",
    "requirement",
    "procedure",
    "definition",
    "identity",
    "attribute",
    "open-question",
)

CLAIM_ROLE_WEIGHTS = {
    "source-uncertainty": 0.30,
    "ordinary-modality": 0.08,
    "negative-evidence": 0.34,
    "limitation": 0.31,
    "method": 0.27,
    "function": 0.30,
    "mechanism": 0.25,
    "provenance": 0.22,
    "temporal": 0.18,
    "identity": 0.22,
    "definition": 0.22,
    "comparison": 0.20,
    "evidence": 0.20,
    "quantitative": 0.16,
    "analogy": 0.05,
    "worked-example": 0.10,
    "source-framing": 0.03,
}

_ROLE_SCAN_CHAR_LIMIT = 4096
_UNCERTAINTY_VERBS = (
    "specify",
    "state",
    "identify",
    "confirm",
    "establish",
    "explain",
    "include",
)
_UNCERTAINTY_WORDS = (
    "specified",
    "stated",
    "identified",
    "confirmed",
    "established",
    "known",
    "resolved",
)
_UNCERTAINTY_PHRASES = (
    "not fully confirm",
    "not confirmed",
    "not ingested",
    "unknown",
    "unclear",
    "unresolved",
    "unconfirmed",
    "open question",
    "[verify]",
)
_MODALITY_WORDS = ("may", "might", "possibly", "possible", "could", "should")
_MODALITY_PHRASES = ("more to",)
_SOURCE_FRAMING_PHRASES = (
    "when discussing",
    "delight in explaining",
    "this is exactly how",
)
_ANALOGY_PHRASES = (
    "analogy",
    "metaphor",
    "similar to",
    "akin to",
    "as if",
    "like a",
    "like an",
    "like most",
    "compared to",
    "just as",
    "much like",
)


def claim_role_tags(statement: str) -> tuple[str, ...]:
    lowered = statement.lower()[:_ROLE_SCAN_CHAR_LIMIT]
    roles: list[str] = []
    words = _normalized_words(lowered)
    word_set = frozenset(words)
    for role in CLAIM_ROLE_ORDER:
        if _role_matches(role, lowered, words, word_set):
            roles.append(role)
    return tuple(roles)


def _role_matches(
    role: str, lowered: str, words: tuple[str, ...], word_set: frozenset[str]
) -> bool:
    if role == "source-uncertainty":
        return (
            ("does not" in lowered and _has_any_word(word_set, _UNCERTAINTY_VERBS))
            or ("not" in word_set and _has_any_word(word_set, _UNCERTAINTY_WORDS))
            or _has_any_phrase(lowered, _UNCERTAINTY_PHRASES)
        )
    if role == "ordinary-modality":
        return (
            _has_any_word(word_set, _MODALITY_WORDS)
            or _has_stem(words, "suggest")
            or _has_any_phrase(lowered, _MODALITY_PHRASES)
        )
    if role == "source-framing":
        return _has_any_phrase(lowered, SOURCE_FRAMING_PREFIXES + _SOURCE_FRAMING_PHRASES) or (
            "this is exactly how" in lowered and "works" in lowered
        )
    if role == "analogy":
        return _has_any_phrase(lowered, _ANALOGY_PHRASES)
    if role == "worked-example":
        return _has_any_phrase(lowered, ("for example", "example", "suppose", "consider"))
    if role == "negative-evidence":
        return (
            ("no" in word_set and "found" in word_set)
            or ("not" in word_set and "found" in word_set)
            or "does not" in lowered
            or "without" in word_set
        )
    if role == "limitation":
        return _has_any_word(word_set, ("unless", "except", "only", "cannot")) or _has_stem(
            words, "limit"
        )
    if role == "method":
        return _has_any_word(word_set, ("used", "using", "study")) or _has_any_stem(
            words, ("analys", "test", "explor")
        )
    if role == "evidence":
        return _has_any_word(word_set, ("evidence", "citation", "record")) or _has_stem(
            words, "inscription"
        )
    if role == "provenance":
        return "from" in word_set or "retrieved" in word_set or _has_stem(words, "origin")
    if role == "temporal":
        return (
            _has_year(words)
            or _has_any_word(word_set, ("bc", "ad", "year"))
            or _has_stem(words, "centur")
        )
    if role == "quantitative":
        return _has_digit(words) or _has_any_phrase(lowered, ("at least", "more than", "roughly"))
    if role == "function":
        return (
            _has_any_stem(
                words,
                (
                    "track",
                    "predict",
                    "show",
                    "represent",
                    "encode",
                    "return",
                    "combine",
                    "call",
                    "transform",
                ),
            )
            or "advance" in word_set
        )
    if role == "mechanism":
        return _has_any_word(word_set, ("consists", "case", "crank", "through")) or _has_stem(
            words, "gear"
        )
    if role == "comparison":
        return (
            "matched" in word_set
            or "compared" in word_set
            or "than" in word_set
            or _has_stem(words, "surpass")
        )
    if role == "relationship":
        return _has_any_word(word_set, ("between", "with")) or _has_any_stem(
            words, ("link", "connect")
        )
    if role == "requirement":
        return _has_any_word(word_set, ("must", "shall", "should")) or _has_stem(words, "require")
    if role == "procedure":
        return (
            _has_any_word(word_set, ("process", "workflow", "then", "next", "finally"))
            or _has_stem(words, "turn")
            or "step" in word_set
            or "first," in lowered
        )
    if role == "definition":
        return _has_any_phrase(lowered, ("defined as", "means", "refers to"))
    if role == "identity":
        return _has_any_word(word_set, ("is", "are")) or _has_any_phrase(
            lowered, ("known as", "described as")
        )
    if role == "attribute":
        return _has_any_word(word_set, ("has", "have", "contains", "housed", "size"))
    if role == "open-question":
        return _has_any_phrase(lowered, ("open question", "unclear", "unresolved"))
    return False


def _normalized_words(text: str) -> tuple[str, ...]:
    chars = [character if character.isalnum() or character == "-" else " " for character in text]
    return tuple(word for word in "".join(chars).split() if word)


def _has_any_word(word_set: frozenset[str], words: tuple[str, ...]) -> bool:
    index = 0
    while index < len(words):
        if words[index] in word_set:
            return True
        index += 1
    return False


def _has_any_phrase(text: str, phrases: tuple[str, ...]) -> bool:
    index = 0
    while index < len(phrases):
        if phrases[index] in text:
            return True
        index += 1
    return False


def _has_stem(words: tuple[str, ...], stem: str) -> bool:
    index = 0
    while index < len(words):
        if words[index].startswith(stem):
            return True
        index += 1
    return False


def _has_any_stem(words: tuple[str, ...], stems: tuple[str, ...]) -> bool:
    index = 0
    while index < len(stems):
        if _has_stem(words, stems[index]):
            return True
        index += 1
    return False


def _has_year(words: tuple[str, ...]) -> bool:
    index = 0
    while index < len(words):
        word = words[index]
        if word.isdigit() and len(word) in {3, 4}:
            return True
        index += 1
    return False


def _has_digit(words: tuple[str, ...]) -> bool:
    word_index = 0
    while word_index < len(words):
        character_index = 0
        word = words[word_index]
        while character_index < len(word):
            if word[character_index].isdigit():
                return True
            character_index += 1
        word_index += 1
    return False
