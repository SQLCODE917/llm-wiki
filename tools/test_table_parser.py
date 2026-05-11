#!/usr/bin/env python3
"""Regression tests for table parsing.

These tests ensure the table parser handles:
- Escaped pipes \|
- Escaped backslashes \\|
- Pipes inside inline code `a | b`
- Normal table rows
"""
from wiki_check_synthesis import split_table_row
import pytest
import sys
sys.path.insert(0, '/workspaces/llm-wiki/tools')


class TestSplitTableRow:
    """Test table row splitting with edge cases."""

    def test_normal_row_four_cells(self):
        line = "| Claim | Evidence | Locator | Source |"
        result = split_table_row(line)
        assert result == ["Claim", "Evidence", "Locator", "Source"]

    def test_escaped_pipe_in_evidence(self):
        """Escaped pipes \| should not be treated as delimiters."""
        line = r"| JavaScript's \|\| operator | Evidence text | `L123` | Source |"
        result = split_table_row(line)
        assert len(result) == 4
        assert r"\|\|" in result[0]  # The escaped pipe stays in the cell

    def test_multiple_escaped_pipes(self):
        """Multiple escaped pipes in same cell."""
        line = r"| The \|\| and && operators | Short-circuit for \|\| | `L456` | Link |"
        result = split_table_row(line)
        assert len(result) == 4

    def test_pipe_inside_inline_code(self):
        """Pipes inside backticks should not be treated as delimiters."""
        line = "| Claim | `a | b` is code | `L789` | Source |"
        result = split_table_row(line)
        assert len(result) == 4
        assert "`a | b`" in result[1]

    def test_escaped_backslash_then_pipe(self):
        """Escaped backslash followed by pipe: \\| means literal backslash + delimiter."""
        line = r"| path\\| more | `L1` | Source |"
        result = split_table_row(line)
        # After \\, the next | is a delimiter, not escaped
        assert len(result) == 4

    def test_empty_cells(self):
        line = "| | Evidence | | Source |"
        result = split_table_row(line)
        assert result == ["", "Evidence", "", "Source"]

    def test_separator_row(self):
        line = "| --- | --- | --- | --- |"
        result = split_table_row(line)
        assert result == ["---", "---", "---", "---"]

    def test_no_leading_pipe(self):
        line = "Claim | Evidence | Locator | Source |"
        result = split_table_row(line)
        assert result is None

    def test_no_trailing_pipe(self):
        line = "| Claim | Evidence | Locator | Source"
        result = split_table_row(line)
        assert result is None

    def test_complex_evidence_with_code_and_escapes(self):
        """Real-world case from js-allonge Control Flow page."""
        line = r'| JavaScript\'s logical operators (\|\| and &&) exhibit short-circuit evaluation | "The ternary operator (?:), \|\|, and && are control flow operators" | `normalized:L3077-L3078` | [Source](../sources/js-allonge.md) |'
        result = split_table_row(line)
        assert len(result) == 4
        assert "Claim" not in str(result)  # Not the header row
        assert "normalized:L3077-L3078" in result[2]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
