#!/usr/bin/env python3
"""Tests for wiki_core parsing utilities."""
from wiki_core.parsing import (
    # Markdown
    strip_markdown,
    normalize_for_search,
    # Tables
    split_table_row,
    table_rows,
    is_separator_row,
    code_cell_target,
    link_cell_target,
    first_markdown_target,
    # Evidence
    clean_evidence_excerpt,
)


def test_strip_markdown():
    """Test strip_markdown removes formatting."""
    # Links
    assert strip_markdown("[text](url)") == "text"
    assert strip_markdown(
        "See [link](http://example.com) here") == "See link here"

    # Inline code
    assert strip_markdown("`code`") == "code"

    # Bold/italic
    assert strip_markdown("**bold**") == "bold"
    assert strip_markdown("*italic*") == "italic"
    assert strip_markdown("_underscored_") == "underscored"

    # Combined
    assert strip_markdown(
        "**[bold link](url)** and `code`") == "bold link and code"

    print("✓ test_strip_markdown passed")


def test_normalize_for_search():
    """Test normalize_for_search handles various normalizations."""
    # Basic lowercasing and whitespace
    assert normalize_for_search("  Hello   World  ") == "hello world"

    # Unicode dashes get converted to ASCII, then may be joined if followed by lowercase
    # This is intended for fuzzy matching, not exact preservation
    assert "dash" in normalize_for_search("en\u2013dash")  # en dash
    assert "dash" in normalize_for_search("em\u2014dash")  # em dash

    # Unicode quotes
    assert normalize_for_search("\u201csmart quotes\u201d") == '"smart quotes"'
    assert normalize_for_search(
        "\u2018single quotes\u2019") == "'single quotes'"

    # PDF hyphenation (this is the main use case)
    assert normalize_for_search("subprob-\nlems") == "subproblems"
    assert normalize_for_search("subprob- lems") == "subproblems"

    # Parentheticals removed
    assert normalize_for_search("text (with parens) here") == "text here"

    # Trailing ellipsis
    assert normalize_for_search("truncated...") == "truncated"

    # Trailing punctuation
    assert normalize_for_search("sentence:") == "sentence"
    assert normalize_for_search("question?") == "question"

    print("✓ test_normalize_for_search passed")


def test_split_table_row():
    """Test split_table_row handles various cases."""
    # Basic row
    assert split_table_row("| A | B | C |") == ["A", "B", "C"]

    # With whitespace
    assert split_table_row("|  A  |  B  |") == ["A", "B"]

    # Empty cells
    assert split_table_row("| | B | |") == ["", "B", ""]

    # Code with pipes (should not split)
    assert split_table_row("| `code|pipe` | normal |") == [
        "`code|pipe`", "normal"]

    # Escaped pipes
    assert split_table_row("| A \\| B | C |") == ["A \\| B", "C"]

    # Not a table row
    assert split_table_row("not a table row") is None
    assert split_table_row("| missing end") is None
    assert split_table_row("missing start |") is None

    print("✓ test_split_table_row passed")


def test_table_rows():
    """Test table_rows extracts all rows from markdown."""
    markdown = """
| Header | Header |
|--------|--------|
| A      | B      |
| C      | D      |

Not a table line.
"""
    rows = table_rows(markdown)
    assert len(rows) == 4
    assert rows[0] == ["Header", "Header"]
    assert rows[1] == ["--------", "--------"]
    assert rows[2] == ["A", "B"]
    assert rows[3] == ["C", "D"]

    print("✓ test_table_rows passed")


def test_is_separator_row():
    """Test is_separator_row identifies separator rows."""
    # Valid separators
    assert is_separator_row(["---", "---", "---"]) is True
    assert is_separator_row([":---:", "---:", ":---"]) is True
    assert is_separator_row(["- - -", "---"]) is True

    # Not separators
    assert is_separator_row(["Header", "Row"]) is False
    assert is_separator_row(["123", "456"]) is False
    assert is_separator_row([""]) is False  # Empty cell

    print("✓ test_is_separator_row passed")


def test_code_cell_target():
    """Test code_cell_target extracts .md paths."""
    assert code_cell_target(
        "`../concepts/example.md`") == "../concepts/example.md"
    assert code_cell_target("  `path.md`  ") == "path.md"

    # Not matching
    assert code_cell_target("plain text") is None
    assert code_cell_target("`not-md-file`") is None
    assert code_cell_target("[link](path.md)") is None

    print("✓ test_code_cell_target passed")


def test_link_cell_target():
    """Test link_cell_target extracts .md paths from links."""
    assert link_cell_target("[Title](path.md)") == "path.md"
    assert link_cell_target(
        "[Example Page](../concepts/example.md)") == "../concepts/example.md"

    # Not matching
    assert link_cell_target("plain text") is None
    assert link_cell_target("`path.md`") is None
    assert link_cell_target("[link](http://example.com)") is None

    print("✓ test_link_cell_target passed")


def test_first_markdown_target():
    """Test first_markdown_target finds first .md link."""
    assert first_markdown_target(
        "See [Page](page.md) and [Other](other.md)") == "page.md"
    assert first_markdown_target(
        "Text [Link](../path.md) more") == "../path.md"

    # Not matching
    assert first_markdown_target("No links here") is None
    assert first_markdown_target("[link](http://example.com)") is None

    print("✓ test_first_markdown_target passed")


def test_clean_evidence_excerpt():
    """Test clean_evidence_excerpt normalizes evidence text."""
    # Surrounding quotes
    assert clean_evidence_excerpt('"quoted text"') == "quoted text"
    assert clean_evidence_excerpt("'single quoted'") == "single quoted"
    assert clean_evidence_excerpt("\"'nested'\"") == "nested"

    # Escaped quotes
    assert clean_evidence_excerpt(
        'text with \\" inside') == 'text with " inside'

    # Whitespace
    assert clean_evidence_excerpt("  extra   spaces  ") == "extra spaces"
    assert clean_evidence_excerpt("  \"  quoted  \"  ") == "quoted"

    print("✓ test_clean_evidence_excerpt passed")


if __name__ == "__main__":
    test_strip_markdown()
    test_normalize_for_search()
    test_split_table_row()
    test_table_rows()
    test_is_separator_row()
    test_code_cell_target()
    test_link_cell_target()
    test_first_markdown_target()
    test_clean_evidence_excerpt()

    print()
    print("All parsing tests passed! ✓")
