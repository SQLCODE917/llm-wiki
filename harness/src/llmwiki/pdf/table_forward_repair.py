"""Recover numbered tables introduced by generic forward table cues."""

from __future__ import annotations

import re
from statistics import median

from llmwiki.pdf.layout_lines import TextLine, WordBox, join_words

_FORWARD_TABLE_CUE = re.compile(
    r"\b(?:table\s+(?:below|following|that follows)|following\s+[^.]{0,80}\s+table)\b",
    re.IGNORECASE,
)
_ROW_MARKER = re.compile(r"^\d{1,3}(?:[-–]\d{1,3})?$")


def is_forward_table_cue(text: str) -> bool:
    return bool(_FORWARD_TABLE_CUE.search(" ".join(text.split())))


def forward_table_text(lines: tuple[TextLine, ...], cue_index: int) -> str:
    body = _collect_forward_lines(lines, cue_index)
    return numbered_table_text(body)


def numbered_table_text(lines: tuple[TextLine, ...], include_leading_text: bool = True) -> str:
    rows = _row_texts(lines, include_leading_text)
    return "\n".join(rows)


def is_numbered_row_marker_line(line: TextLine) -> bool:
    return _row_marker_line(line)


def _collect_forward_lines(lines: tuple[TextLine, ...], cue_index: int) -> tuple[TextLine, ...]:
    selected: list[TextLine] = []
    marker_count = 0
    for line in lines[cue_index + 1 :]:
        if marker_count >= 2 and _looks_like_section_heading(line):
            break
        selected.append(line)
        if _row_marker_line(line):
            marker_count += 1
        if len(selected) >= 42:
            break
    return tuple(selected) if marker_count >= 2 else ()


def _row_texts(lines: tuple[TextLine, ...], include_leading_text: bool) -> tuple[str, ...]:
    markers = tuple((index, line) for index, line in enumerate(lines) if _row_marker_line(line))
    if len(markers) < 2:
        return ()
    marker_x = median(line.words[0].x0 for _index, line in markers)
    label_x = median(line.words[1].x0 for _index, line in markers if len(line.words) >= 2)
    description_x = _description_x(lines, markers, label_x)
    starts = tuple(
        _row_start(lines, markers, index, include_leading_text) for index in range(len(markers))
    )
    rows: list[str] = []
    for marker_position, (_line_index, _marker_line) in enumerate(markers):
        top = starts[marker_position]
        bottom = (
            starts[marker_position + 1] if marker_position + 1 < len(starts) else _row_end(lines)
        )
        words = tuple(word for line in lines for word in line.words if top <= word.cy < bottom)
        number = tuple(word for word in words if word.x0 < marker_x + 12.0)
        label = tuple(word for word in words if marker_x + 12.0 <= word.x0 < description_x - 8.0)
        description = tuple(word for word in words if word.x0 >= description_x - 8.0)
        row = " ".join(
            part
            for part in (
                join_words(number),
                join_words(label),
                join_words(description),
            )
            if part
        )
        if row:
            rows.append(row)
    return tuple(rows)


def _row_start(
    lines: tuple[TextLine, ...],
    markers: tuple[tuple[int, TextLine], ...],
    marker_index: int,
    include_leading_text: bool,
) -> float:
    if marker_index == 0:
        if not include_leading_text:
            return markers[marker_index][1].y0 - 0.1
        return min(line.y0 for line in lines)
    start_index = markers[marker_index][0]
    previous_marker_index = markers[marker_index - 1][0]
    threshold = _line_delta_threshold(lines)
    for index in range(markers[marker_index][0], previous_marker_index, -1):
        if lines[index].y0 - lines[index - 1].y0 > threshold:
            start_index = index
            break
        start_index = index - 1
    return lines[start_index].y0 - 0.1


def _row_end(lines: tuple[TextLine, ...]) -> float:
    return max(line.y1 for line in lines) + 0.1


def _line_delta_threshold(lines: tuple[TextLine, ...]) -> float:
    heights = [line.y1 - line.y0 for line in lines if line.y1 > line.y0]
    if not heights:
        return 13.0
    return median(heights) + 3.0


def _description_x(
    lines: tuple[TextLine, ...], markers: tuple[tuple[int, TextLine], ...], label_x: float
) -> float:
    marker_indices = {index for index, _line in markers}
    candidates: list[float] = []
    for index, line in enumerate(lines):
        if index not in marker_indices and line.words and line.words[0].x0 > label_x + 30.0:
            candidates.append(line.words[0].x0)
            continue
        candidates.extend(_description_starts_on_marker_line(line, label_x))
    if candidates:
        return min(candidates)
    return label_x + 90.0


def _description_starts_on_marker_line(line: TextLine, label_x: float) -> tuple[float, ...]:
    if not _row_marker_line(line) or len(line.words) < 3:
        return ()
    starts: list[float] = []
    previous: WordBox | None = None
    for word in line.words[2:]:
        if previous is not None and word.x0 - previous.x1 > 18.0 and word.x0 > label_x + 30.0:
            starts.append(word.x0)
        previous = word
    return tuple(starts)


def _row_marker_line(line: TextLine) -> bool:
    return len(line.words) >= 2 and bool(_ROW_MARKER.fullmatch(line.words[0].text.strip()))


def _looks_like_section_heading(line: TextLine) -> bool:
    if not 1 <= len(line.words) <= 6:
        return False
    text = line.text.strip()
    if any(char.isdigit() for char in text) or text.endswith((".", ",", ";", ":")):
        return False
    return all(word.text[:1].isupper() for word in line.words if word.text)
