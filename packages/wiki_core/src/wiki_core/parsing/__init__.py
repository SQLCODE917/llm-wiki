"""Parsing utilities for the wiki ingestion pipeline.

This module contains pure parsing functions for:
- Markdown text processing (strip_markdown, normalize_for_search)
- Table parsing (split_table_row, table_rows, is_separator_row)
- Evidence text processing (clean_evidence_excerpt)

All functions are pure (no I/O or external dependencies).

Usage:
    from wiki_core.parsing import (
        strip_markdown,
        normalize_for_search,
        split_table_row,
        table_rows,
        is_separator_row,
        clean_evidence_excerpt,
    )
"""
from wiki_core.parsing.markdown import (
    strip_markdown,
    normalize_for_search,
)
from wiki_core.parsing.tables import (
    split_table_row,
    table_rows,
    is_separator_row,
    code_cell_target,
    link_cell_target,
    first_markdown_target,
)
from wiki_core.parsing.evidence import (
    clean_evidence_excerpt,
)

__all__ = [
    # Markdown processing
    "strip_markdown",
    "normalize_for_search",
    # Table parsing
    "split_table_row",
    "table_rows",
    "is_separator_row",
    "code_cell_target",
    "link_cell_target",
    "first_markdown_target",
    # Evidence processing
    "clean_evidence_excerpt",
]
