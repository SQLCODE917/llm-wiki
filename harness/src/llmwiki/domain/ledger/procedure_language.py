"""Source-agnostic language classifiers for procedural content."""

from __future__ import annotations

import re

_ACTION_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("choose", re.compile(r"\b(choose|choosing|select|selecting|decide|pick)\b", re.I)),
    ("generate", re.compile(r"\b(roll|rolling|generate|determine|determining)\b", re.I)),
    ("lookup", re.compile(r"\b(consult|reference|look\s+up|looking\s+up|find)\b", re.I)),
    ("calculate", re.compile(r"\b(calculate|compute|add|subtract|divide|multiply)\b", re.I)),
    ("allocate", re.compile(r"\b(spend|spending|allocate|increase|assign)\b", re.I)),
    ("acquire", re.compile(r"\b(purchase|purchasing|buy|acquire|get|obtain)\b", re.I)),
    ("record", re.compile(r"\b(write|record|fill|filling|note)\b", re.I)),
    ("validate", re.compile(r"\b(check|verify|confirm|ensure|restrict|restriction)\b", re.I)),
    ("apply", re.compile(r"\b(apply|use|using)\b", re.I)),
    ("finalize", re.compile(r"\b(finalize|finish|complete)\b", re.I)),
)
_TASK_NOUN = re.compile(
    r"\b(creation|setup|installation|configuration|procedure|workflow|process|"
    r"guide|tutorial|filling|purchasing|building|making)\b",
    re.I,
)
_CONDITION = re.compile(r"\b(if|when|unless|except|whether|depending on whether)\b", re.I)
_LEADING_NUMBER = re.compile(r"^\s*\d+(?:\.\d+)*\.?\s*")
_ORDERED_HEADING = re.compile(r"^\s*\d+(?:\.\d+){1,}\s+")


def has_task_noun(text: str) -> bool:
    return bool(_TASK_NOUN.search(text))


def has_condition(text: str) -> bool:
    return bool(_CONDITION.search(text))


def action_type(text: str) -> str:
    for action, pattern in _ACTION_PATTERNS:
        if pattern.search(text):
            return action
    return ""


def is_step_heading(text: str) -> bool:
    return bool(_ORDERED_HEADING.search(text) or action_type(text))


def goal_title(heading: str) -> str:
    title = clean_title(heading)
    lower = title.lower()
    if lower.endswith(" creation"):
        return f"Create {title[:-9].strip()}"
    for prefix, replacement in (
        ("purchasing ", "Purchase "),
        ("filling ", "Fill "),
        ("determining ", "Determine "),
        ("using ", "Use "),
    ):
        if lower.startswith(prefix):
            return replacement + title[len(prefix) :]
    return title


def goal_sentence(heading: str) -> str:
    title = goal_title(heading)
    if title.lower().startswith(("create ", "purchase ", "fill ", "determine ", "use ")):
        return title[0].upper() + title[1:]
    return f"Complete {title}"


def step_title(heading: str) -> str:
    return clean_title(heading).rstrip(".")


def clean_title(text: str) -> str:
    cleaned = _LEADING_NUMBER.sub("", " ".join(text.replace("/", " ").split()))
    return cleaned.strip(" :-")
