"""Source-neutral notation detectors for formulas and rules-like expressions."""

from __future__ import annotations

import re

_URLISH = re.compile(r"https?://|\bwww\.|/[A-Za-z0-9_.-]+/")
_ARITHMETIC = re.compile(r"(?<![/\w])\d+\s*[-+*x×÷]\s*\d+(?![/\w])")
_DICE = re.compile(r"\b\d*d\d+(?:\s*[-+]\s*\d+)?\b", re.IGNORECASE)
_LATEX_OR_SYMBOL = re.compile(r"\\frac|\\sum|≤|≥|∑|√")
_SYMBOLIC = re.compile(r"[+\-*/^]|∑|√|×|÷|\\frac|\\sum")
_WORD = re.compile(r"[A-Za-z][A-Za-z0-9_-]*")
_MAX_FORMULA_WORDS = 24
_MAX_EQUATION_LHS_WORDS = 5
_ARITHMETIC_EXPRESSION = re.compile(
    r"^[A-Za-z0-9_(). \t+\-*/×÷^]+=[A-Za-z0-9_(). \t+\-*/×÷^]+$|"
    r"^\d+(?:\.\d+)?(?:\s*[-+*×÷]\s*\d+(?:\.\d+)?)+$"
)
_DICE_EXPRESSION = re.compile(r"^\d*d\d+(?:\s*[-+]\s*\d+)?$", re.IGNORECASE)


def formula_candidate_line(text: str) -> str | None:
    for line in text.splitlines():
        if is_formula_line(line):
            return line
    return None


def standalone_formula_candidate_line(text: str) -> str | None:
    for line in text.splitlines():
        if is_standalone_formula_line(line):
            return line
    return None


def is_formula_line(line: str) -> bool:
    stripped = " ".join(line.split())
    if not stripped or _URLISH.search(stripped):
        return False
    if _LATEX_OR_SYMBOL.search(stripped):
        return True
    if len(stripped.split()) > _MAX_FORMULA_WORDS:
        return False
    return bool(_equation_like(stripped) or _ARITHMETIC.search(stripped) or _DICE.search(stripped))


def is_standalone_formula_line(line: str) -> bool:
    stripped = " ".join(line.split())
    if not is_formula_line(stripped):
        return False
    if _LATEX_OR_SYMBOL.search(stripped):
        return True
    if len(stripped.split()) > 12:
        return False
    if _DICE_EXPRESSION.fullmatch(stripped):
        return True
    if _ARITHMETIC_EXPRESSION.fullmatch(stripped):
        return True
    return bool(_equation_like(stripped) and _SYMBOLIC.search(stripped))


def _equation_like(stripped: str) -> bool:
    if "=" not in stripped:
        return False
    left, _separator, right = stripped.partition("=")
    if not left.strip() or not right.strip():
        return False
    left_words = _WORD.findall(left)
    if not left_words or len(left_words) > _MAX_EQUATION_LHS_WORDS:
        return False
    return bool(_WORD.search(right) or re.search(r"\d", right))
