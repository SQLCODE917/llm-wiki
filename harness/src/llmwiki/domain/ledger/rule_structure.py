"""Source-neutral rule-shape parsing for prose technical atoms."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import RulePayload

_DEONTIC_FORCE = (
    (("must", "shall", "required", "have to"), "required"),
    (("cannot", "can not", "forbidden", "prohibited", "never", "may not"), "forbidden"),
    (("may", "allowed", "permitted", "can"), "permitted"),
    (("should", "recommended", "ought"), "recommended"),
)
_MODAL = (
    r"must|shall|should|may|can|cannot|can not|required|have to|allowed|"
    r"permitted|prohibited|forbidden|never|always"
)
_MAX_RULE_WORDS = 60
_EPISTEMIC_MODAL = re.compile(
    r"\b(?:may|might|could|should|would)\s+(?:\w+\s+){0,3}?"
    r"(?:be|have|seem|appear|prove|turn|mean|ask|say|think|suppose)\b",
    re.IGNORECASE,
)
_AUTHORIAL_MODAL = re.compile(
    r"\b(?:i|we)\b[^.!?]{0,120}\b(?:may|might|could|should|would|shall|must|can)\b",
    re.IGNORECASE,
)
_META_MODAL = re.compile(
    rf"\b(?:{_MODAL}|might|could|would)\b(?:\s+\w+){{0,3}}\s+be\s+"
    r"(?:realized|conceived|considered|understood|remembered|noted|urged|"
    r"supposed|regarded|treated|seen|thought|imagined|explained)\b",
    re.IGNORECASE,
)
_CONDITION = re.compile(
    r"\b(?P<cue>if|when|whenever|unless|except|only if|only when)\b"
    r"(?P<trigger>[^,.;]*)",
    re.IGNORECASE,
)
_ACTOR_MODAL = re.compile(
    rf"^(?P<scope>(?!(?:it|this|that|there|for|thus|therefore|however)\b)"
    rf"[A-Za-z][^.!?]{{0,100}}?)\s+(?P<modal>{_MODAL})\s+(?P<effect>.+)$",
    re.IGNORECASE,
)
_DIRECT_ACTOR_MODAL = re.compile(
    rf"\b(?P<scope>you|your)\s+(?P<modal>{_MODAL})\s+(?P<effect>[^.!?]+)",
    re.IGNORECASE,
)
_ACTION_START = re.compile(
    r"^(?:not\s+|also\s+|always\s+|only\s+|then\s+|still\s+|try\s+to\s+)*"
    r"(?:add|adjust|apply|attack|call|cast|check|choose|compile|crawl|create|"
    r"deal|declare|determine|drop|equip|gain|get|hide|initialize|lose|make|"
    r"move|perform|provide|reduce|return|roll|select|set|spend|squeeze|"
    r"subtract|take|use|validate|wear)\b",
    re.IGNORECASE,
)
_CONDITIONAL_EFFECT = re.compile(
    r"^(?:[A-Za-z][^.!?]{0,60}\s+)?"
    r"(?:add|adjust|apply|deal|gain|get|increase|lose|reduce|roll|subtract|take)\w*\b",
    re.IGNORECASE,
)


def materialize_rule_payload(sentence: str, source_locator: str) -> RulePayload | None:
    text = sentence.strip()
    if len(text.split()) > _MAX_RULE_WORDS or _is_epistemic_or_meta(text):
        return None
    force = _rule_force(text)
    if force is None:
        return None
    scope, trigger, effect, exception = _rule_structure(text)
    if not any((scope, trigger, effect, exception)):
        return None
    return RulePayload(
        rule_text=text,
        rule_force=force,
        source_locator=source_locator,
        scope=scope,
        trigger=trigger,
        effect=effect,
        exception=exception,
    )


def _rule_force(sentence: str) -> str | None:
    lowered = sentence.lower()
    for cues, force in _DEONTIC_FORCE:
        if any(re.search(rf"\b{re.escape(cue)}\b", lowered) for cue in cues):
            return force
    if re.search(r"\b(always|except|if|unless|when|whenever|never)\b", lowered):
        return "asserted-constraint"
    if re.search(
        r"\b(?:must|shall|should|may|can|cannot|can not)\s+only\b"
        r"|\bonly\s+(?:if|when|while|after|before)\b",
        lowered,
    ):
        return "asserted-constraint"
    return None


def _is_epistemic_or_meta(sentence: str) -> bool:
    return bool(
        _EPISTEMIC_MODAL.search(sentence)
        or _AUTHORIAL_MODAL.search(sentence)
        or _META_MODAL.search(sentence)
    )


def _rule_structure(sentence: str) -> tuple[str, str, str, str]:
    condition = _CONDITION.search(sentence)
    if condition is not None:
        trigger = condition.group(0).strip(" ,")
        exception = trigger if condition.group("cue").lower() in {"unless", "except"} else ""
        scope = _scope(sentence)
        effect = _effect_after(sentence, condition.end())
        if not scope and not _CONDITIONAL_EFFECT.search(effect):
            return ("", "", "", "")
        return (scope, trigger, effect, exception)
    actor = _ACTOR_MODAL.match(sentence) or _DIRECT_ACTOR_MODAL.search(sentence)
    if actor is None:
        return ("", "", "", "")
    effect = actor.group("effect").strip()
    if not _ACTION_START.search(effect):
        return ("", "", "", "")
    return (actor.group("scope").strip(" ,"), "", effect, "")


def _scope(sentence: str) -> str:
    actor = _ACTOR_MODAL.match(sentence) or _DIRECT_ACTOR_MODAL.search(sentence)
    return actor.group("scope").strip(" ,") if actor is not None else ""


def _effect_after(sentence: str, index: int) -> str:
    suffix = sentence[index:].lstrip(" ,;")
    return suffix if suffix else sentence
