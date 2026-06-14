"""TextRecognizer port: the swappable OCR interface (design: one narrow
contract, engines are adapters; "no text found" is a normal result).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

# Filtering guards: keep photo noise (a slogan on a coffee bag) out of the
# intermediate. Tuned only against the decorative fixture so far — awaiting
# a text-bearing fixture (docs/open-questions.md).
OCR_MIN_CONFIDENCE = 0.5
OCR_MIN_TEXT_CHARS = 12


@dataclass(frozen=True)
class TextSpan:
    text: str
    confidence: float  # 0.0–1.0


class TextRecognizer(Protocol):
    """OCR engine port. Implementations must return [] for no text —
    raising is reserved for engine failure (fail loud)."""

    def recognize(self, image_path: Path) -> list[TextSpan]: ...


class NullRecognizer:
    """No-op engine: every image is decorative. Useful default and test double."""

    def recognize(self, image_path: Path) -> list[TextSpan]:
        return []


def usable_text(
    spans: list[TextSpan],
    min_confidence: float = OCR_MIN_CONFIDENCE,
    min_chars: int = OCR_MIN_TEXT_CHARS,
) -> str | None:
    """Reduce raw spans to figure text, or None if the image is decorative.

    None is the NORMAL case — callers must treat it silently.
    """
    kept = [s.text.strip() for s in spans if s.confidence >= min_confidence and s.text.strip()]
    joined = " ".join(kept)
    if len(joined) < min_chars:
        return None
    return joined
