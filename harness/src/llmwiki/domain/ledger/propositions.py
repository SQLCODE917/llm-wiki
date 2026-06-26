"""Decompose a source-close statement into structured proposition fields.

This is best-effort and source-neutral. It splits a statement into subject /
predicate / object around a verb region, and classifies polarity, claim force,
condition scope, and temporal/spatial scope from reusable linguistic
categories (negation, deontic modals, conditionals, time/place cues). When no
verb region is found the proposition is marked incomplete, and the builder
routes the entry to review rather than asserting it as prose.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.common import SpatialScope, TemporalScope

_MODAL_FORCE = (
    (("must not", "shall not", "may not"), "negative", "required"),
    (("cannot", "can not", "must never"), "affirmative", "forbidden"),
    (("must", "shall", "have to", "required to"), "affirmative", "required"),
    (("should", "ought to", "recommended"), "affirmative", "recommended"),
    (("may", "can", "could", "allowed to", "permitted to"), "affirmative", "permitted"),
    (("might", "possibly", "perhaps"), "affirmative", "possible"),
)
# Linking/auxiliary/modal verbs, a closed set of high-frequency descriptive
# verbs, and a past-tense suffix. This is general English, not source-specific;
# it splits most sentences into subject/predicate/object. A statement with no
# recognizable verb stays fragmentary and is routed to review.
_VERB_PIVOT = re.compile(
    r"\b(is|are|was|were|be|been|being|has|have|had|do|does|did|must not|shall not|may not"
    r"|cannot|can not|must|shall|should|may|might|can|could|will|would|ought"
    r"|contains?|consists?|includes?|requires?|provides?|represents?|describes?|defines?"
    r"|refers?|shows?|means|allows?|causes?|uses?|makes?|gives?|holds?|forms?|becomes?"
    r"|remains?|begins?|ends?|occurs?|appears?|seems?|gains?|loses?|adds?|rolls?"
    r"|\w{2,}ed)\b",
    re.IGNORECASE,
)
_NEGATION = re.compile(r"\b(not|never|no|none|without|cannot|can not|n't)\b", re.IGNORECASE)
_YEAR = re.compile(
    r"\b\d{3,4}\b|\bBCE?\b|\bAD\b|\b\d{1,2}(?:st|nd|rd|th)\s+centur\w+", re.IGNORECASE
)
_RELATIVE_TIME = re.compile(
    r"\b(before|after|later|earlier|then|next|subsequently|once)\b", re.IGNORECASE
)
_PLACE = re.compile(
    r"\b(?:in|at|near|within|across|throughout)\s+([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)"
)
_RELATIVE_PLACE = re.compile(r"\b(here|there|nearby|above|below|beyond|elsewhere)\b", re.IGNORECASE)
_CONDITION = re.compile(r"\b(if|when|whenever|provided that|in case)\b", re.IGNORECASE)
_EXCEPTION = re.compile(r"\b(unless|except|but not|other than)\b", re.IGNORECASE)


@dataclass(frozen=True)
class Proposition:
    subject: str
    predicate: str
    object_value: str
    polarity: str
    claim_force: str
    condition_scope: str
    condition_text: str
    exception_text: str
    temporal_scope: TemporalScope | None
    spatial_scope: SpatialScope | None
    complete: bool


def decompose(statement: str) -> Proposition:
    text = " ".join(statement.split())
    pivot = _VERB_PIVOT.search(text)
    subject, predicate, object_value, complete = _split(text, pivot)
    polarity, claim_force = _polarity_force(text)
    condition_scope, condition_text, exception_text = _condition(text)
    return Proposition(
        subject=subject,
        predicate=predicate,
        object_value=object_value,
        polarity=polarity,
        claim_force=claim_force,
        condition_scope=condition_scope,
        condition_text=condition_text,
        exception_text=exception_text,
        temporal_scope=_temporal(text),
        spatial_scope=_spatial(text),
        complete=complete,
    )


def _split(text: str, pivot: re.Match[str] | None) -> tuple[str, str, str, bool]:
    if pivot is None:
        return text, "", "", False
    subject = text[: pivot.start()].strip()
    predicate = pivot.group(0)
    object_value = text[pivot.end() :].strip()
    complete = bool(subject) and bool(object_value)
    return subject, predicate, object_value, complete


def _polarity_force(text: str) -> tuple[str, str]:
    lowered = text.lower()
    for cues, polarity, force in _MODAL_FORCE:
        if any(cue in lowered for cue in cues):
            return polarity, force
    negated = bool(_NEGATION.search(lowered))
    return ("negative" if negated else "affirmative"), "asserted"


def _condition(text: str) -> tuple[str, str, str]:
    exception = _EXCEPTION.search(text)
    if exception is not None:
        return "exception", "", text[exception.start() :].strip()
    condition = _CONDITION.search(text)
    if condition is not None:
        return "conditional", text[condition.start() :].strip(), ""
    return "unconditional", "", ""


def _temporal(text: str) -> TemporalScope | None:
    explicit = _YEAR.search(text)
    if explicit is not None:
        return TemporalScope(explicit.group(0), "date", "resolved")
    relative = _RELATIVE_TIME.search(text)
    if relative is not None:
        return TemporalScope(relative.group(0), "sequence", "unresolved")
    return None


def _spatial(text: str) -> SpatialScope | None:
    place = _PLACE.search(text)
    if place is not None:
        return SpatialScope(place.group(1), "place", "resolved")
    relative = _RELATIVE_PLACE.search(text)
    if relative is not None:
        return SpatialScope(relative.group(0), "relative-location", "unresolved")
    return None
