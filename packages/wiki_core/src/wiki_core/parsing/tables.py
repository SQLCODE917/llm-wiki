"""Markdown table parsing utilities.

Pure parsing functions for extracting data from Markdown tables.
No I/O or external dependencies.

Usage:
    from wiki_core.parsing import split_table_row, table_rows, is_separator_row
    
    # Parse a single row
    cells = split_table_row("| A | B | C |")  # ["A", "B", "C"]
    
    # Parse all rows from markdown
    rows = table_rows(markdown_text)
    
    # Check if row is a separator (|---|---|)
    is_separator_row(["---", "---"])  # True
"""
from __future__ import annotations

import re


def split_table_row(line: str) -> list[str] | None:
    """Split a Markdown table row into cells.

    Handles:
    - Escaped pipes (\\|)
    - Inline code containing pipes (`code|with|pipes`)
    - Leading/trailing whitespace in cells

    Args:
        line: A single line that may be a table row

    Returns:
        List of cell contents (stripped), or None if not a valid table row

    Examples:
        >>> split_table_row("| A | B | C |")
        ['A', 'B', 'C']
        >>> split_table_row("| `code|pipe` | normal |")
        ['`code|pipe`', 'normal']
        >>> split_table_row("not a table row")
        None
    """
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None

    cells: list[str] = []
    buf: list[str] = []
    escaped = False
    in_code = False

    # Remove leading and trailing pipes
    s = stripped[1:-1]

    for ch in s:
        if escaped:
            buf.append(ch)
            escaped = False
            continue

        if ch == "\\":
            escaped = True
            buf.append(ch)
            continue

        if ch == "`":
            in_code = not in_code
            buf.append(ch)
            continue

        if ch == "|" and not in_code:
            cells.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)

    cells.append("".join(buf).strip())
    return cells


def table_rows(markdown: str) -> list[list[str]]:
    """Extract all table rows from Markdown text.

    Parses each line and returns rows that are valid table rows.
    Does not filter separator rows - use is_separator_row() for that.

    Args:
        markdown: Markdown text potentially containing tables

    Returns:
        List of rows, where each row is a list of cell contents
    """
    rows: list[list[str]] = []
    for line in markdown.splitlines():
        row = split_table_row(line)
        if row is not None:
            rows.append(row)
    return rows


def is_separator_row(cells: list[str]) -> bool:
    """Check if a table row is a separator row.

    Separator rows contain only dashes, colons, and spaces.
    Used to separate header from body in Markdown tables.

    Args:
        cells: List of cell contents from split_table_row()

    Returns:
        True if this is a separator row (e.g., |---|:---:|)

    Examples:
        >>> is_separator_row(["---", "---", "---"])
        True
        >>> is_separator_row([":---:", "---:", ":---"])
        True
        >>> is_separator_row(["Header", "Row"])
        False
    """
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def code_cell_target(cell: str) -> str | None:
    """Extract a .md path from a backtick-wrapped cell.

    Matches cells like `../path/to/file.md` and returns the path.

    Args:
        cell: Table cell content

    Returns:
        The path if cell matches `path.md` pattern, else None

    Examples:
        >>> code_cell_target("`../concepts/example.md`")
        '../concepts/example.md'
        >>> code_cell_target("plain text")
        None
    """
    match = re.fullmatch(r"`([^`]+\.md)`", cell.strip())
    return match.group(1) if match else None


def link_cell_target(cell: str) -> str | None:
    """Extract a .md path from a Markdown link cell.

    Matches cells like [Title](../path/to/file.md) and returns the path.

    Args:
        cell: Table cell content

    Returns:
        The path if cell matches [text](path.md) pattern, else None

    Examples:
        >>> link_cell_target("[Example Page](../concepts/example.md)")
        '../concepts/example.md'
        >>> link_cell_target("plain text")
        None
    """
    match = re.fullmatch(r"\[([^\]]+)\]\(([^)]+\.md)\)", cell.strip())
    return match.group(2) if match else None


def first_markdown_target(text: str) -> str | None:
    """Find the first .md link target in text.

    Searches for the first Markdown link to a .md file and returns
    the target path.

    Args:
        text: Text that may contain Markdown links

    Returns:
        The first .md path found, or None

    Examples:
        >>> first_markdown_target("See [Page](page.md) and [Other](other.md)")
        'page.md'
        >>> first_markdown_target("No links here")
        None
    """
    match = re.search(r"\[[^\]]+\]\(([^)]+\.md)\)", text)
    return match.group(1) if match else None
