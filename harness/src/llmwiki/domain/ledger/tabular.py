"""Source-neutral tabular row-sequence detectors."""

from __future__ import annotations

import re

_LINE_ROW_MARKER = re.compile(r"^\s*(?:[-*]\s*)?(\d{1,3})[.)\s]+(?=\S)")
_INLINE_ROW_MARKER = re.compile(r"(?:^|\s)(\d{1,3})[.)]?\s+(?=[A-Za-z])")
_RANGE_VALUE_MARKER = re.compile(r"(?:^|\s)(\d{1,3}(?:\s*[-–]\s*\d{1,3})?)\s+([+-]\d+)\b")
_MAX_FLAT_SCAN_CHARS = 250_000
_RANGE_SCAN_WINDOW_CHARS = 50_000
_RANGE_SCAN_OVERLAP_CHARS = 64


def row_marker_count(text: str) -> int:
    """Count reusable ordered row markers, rejecting isolated prose numbers."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    line_markers = _line_markers(lines)
    if len(line_markers) >= 2 and sequence_like(line_markers):
        return len(line_markers)
    flat_text = _bounded_flat_text(lines)
    range_entries = range_value_entries(flat_text)
    if len(range_entries) >= 3:
        return len(range_entries)
    inline_markers = inline_row_marker_spans(flat_text)
    if len(inline_markers) >= 3:
        return len(inline_markers)
    return 1 if len(line_markers) == 1 else 0


def inline_row_marker_spans(text: str) -> tuple[tuple[int, int, int], ...]:
    """Increasing inline row markers with source spans."""
    markers: list[tuple[int, int, int]] = []
    last = 0
    for match in _INLINE_ROW_MARKER.finditer(text):
        value = int(match.group(1))
        if markers and value <= last:
            continue
        markers.append((value, match.start(1), match.end()))
        last = value
    values = tuple(value for value, _start, _end in markers)
    return tuple(markers) if sequence_like(values) else ()


def range_value_entries(text: str) -> tuple[tuple[str, str], ...]:
    entries: list[tuple[str, str]] = []
    starts: list[int] = []
    seen_starts: set[int] = set()
    for offset, chunk in _range_scan_windows(text):
        for match in _RANGE_VALUE_MARKER.finditer(chunk):
            absolute_start = offset + match.start(1)
            if absolute_start in seen_starts:
                continue
            seen_starts.add(absolute_start)
            key = " ".join(match.group(1).replace("–", "-").split())
            value = match.group(2)
            entries.append((key, value))
            starts.append(_range_start(key))
    if len(entries) < 3 or not _range_sequence_like(tuple(starts)):
        return ()
    return tuple(entries)


def _bounded_flat_text(lines: list[str]) -> str:
    parts: list[str] = []
    remaining = _MAX_FLAT_SCAN_CHARS
    for line in lines:
        if remaining <= 0:
            break
        piece = line[:remaining]
        parts.append(piece)
        remaining -= len(piece) + 1
    return " ".join(parts)


def _range_scan_windows(text: str) -> tuple[tuple[int, str], ...]:
    if len(text) <= _RANGE_SCAN_WINDOW_CHARS:
        return ((0, text),)
    windows: list[tuple[int, str]] = []
    step = _RANGE_SCAN_WINDOW_CHARS - _RANGE_SCAN_OVERLAP_CHARS
    start = 0
    while start < len(text):
        end = min(start + _RANGE_SCAN_WINDOW_CHARS, len(text))
        windows.append((start, text[start:end]))
        if end == len(text):
            break
        start += step
    return tuple(windows)


def sequence_like(markers: tuple[int, ...]) -> bool:
    """True when numeric markers form an ordered row sequence."""
    if len(markers) < 2:
        return False
    adjacent = sum(
        1 for left, right in zip(markers, markers[1:], strict=False) if right - left == 1
    )
    required = 2 if len(markers) == 3 else max(1, len(markers) - 2)
    return adjacent >= required


def _line_markers(lines: list[str]) -> tuple[int, ...]:
    markers: list[int] = []
    for line in lines:
        match = _LINE_ROW_MARKER.match(line)
        if match is not None:
            markers.append(int(match.group(1)))
    return tuple(markers)


def _range_start(key: str) -> int:
    start, _separator, _end = key.partition("-")
    return int(start.strip())


def _range_sequence_like(starts: tuple[int, ...]) -> bool:
    if len(starts) < 3:
        return False
    deltas = [right - left for left, right in zip(starts, starts[1:], strict=False)]
    if not deltas or any(delta <= 0 for delta in deltas):
        return False
    return max(deltas.count(delta) for delta in set(deltas)) >= len(deltas) - 1
