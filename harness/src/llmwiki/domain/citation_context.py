"""Local context extraction for raw-source citations."""

from __future__ import annotations

import re

_OCR_CAVEAT_RE = re.compile(r"\[figure text \(OCR, unverified\)(?::[^\]]*)?\]")


def evidence_text_near_citation(body: str, start: int, end: int) -> str | None:
    line_start = body.rfind("\n", 0, start) + 1
    line_end = body.find("\n", end)
    if line_end == -1:
        line_end = len(body)
    line = body[line_start:line_end]
    before = line[: start - line_start]
    if line.strip().startswith("|") and "|" in line:
        return _table_evidence_text(before)
    quoted = list(re.finditer(r'"([^"]{6,})"|“([^”]{6,})”', before))
    if quoted:
        match = quoted[-1]
        return (match.group(1) or match.group(2) or "").strip()
    return None


def citation_caveats(body: str, start: int, end: int) -> tuple[str, ...]:
    line_start = body.rfind("\n", 0, start) + 1
    line_end = body.find("\n", end)
    if line_end == -1:
        line_end = len(body)
    if _OCR_CAVEAT_RE.search(body[line_start:line_end]):
        return ("ocr-unverified",)
    return ()


def ocr_caveat_texts(body: str) -> tuple[str, ...]:
    return tuple(match.group(0) for match in _OCR_CAVEAT_RE.finditer(body))


def _table_evidence_text(before: str) -> str | None:
    cells = [cell.strip() for cell in before.strip().strip("|").split("|")]
    candidates = [cell for cell in cells if cell and not set(cell) <= {"-", ":"}]
    return candidates[-1] if candidates else None
