"""Tests for wiki_llm.responses module."""
import pytest
from pathlib import Path
import tempfile

from wiki_llm.responses import (
    parse_model_output,
    validate_file_paths,
    write_parsed_files,
    extract_markdown_blocks,
    extract_json_from_output,
)


class TestParseModelOutput:
    """Tests for parse_model_output()."""

    def test_single_file(self):
        output = """Here's the file:

```wiki/concepts/test.md
---
title: Test
---
# Test

Content here.
```
"""
        files = parse_model_output(output)
        assert "wiki/concepts/test.md" in files
        assert "# Test" in files["wiki/concepts/test.md"]

    def test_multiple_files(self):
        output = """
```wiki/file1.md
Content 1
```

```wiki/file2.md
Content 2
```
"""
        files = parse_model_output(output)
        assert len(files) == 2
        assert "wiki/file1.md" in files
        assert "wiki/file2.md" in files

    def test_json_file(self):
        output = """
```wiki/_graph.json
{"nodes": {}}
```
"""
        files = parse_model_output(output)
        assert "wiki/_graph.json" in files

    def test_ignores_non_file_blocks(self):
        output = """
```python
def foo():
    pass
```

```wiki/real.md
Real content
```
"""
        files = parse_model_output(output)
        assert len(files) == 1
        assert "wiki/real.md" in files


class TestValidateFilePaths:
    """Tests for validate_file_paths()."""

    def test_valid_paths(self):
        files = {
            "wiki/test.md": "content",
            "wiki/concepts/foo.md": "content",
        }
        invalid = validate_file_paths(files, Path("/tmp/worktree"))
        assert invalid == []

    def test_path_escape(self):
        files = {
            "../outside.md": "content",
        }
        invalid = validate_file_paths(files, Path("/tmp/worktree"))
        assert "../outside.md" in invalid


class TestWriteParsedFiles:
    """Tests for write_parsed_files()."""

    def test_writes_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            worktree = Path(tmpdir)
            files = {"test.md": "# Test\n\nContent"}

            written = write_parsed_files(files, worktree)

            assert len(written) == 1
            assert (worktree / "test.md").exists()
            assert (worktree / "test.md").read_text() == "# Test\n\nContent"

    def test_dry_run(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            worktree = Path(tmpdir)
            files = {"test.md": "Content"}

            written = write_parsed_files(files, worktree, dry_run=True)

            assert len(written) == 1
            assert not (worktree / "test.md").exists()


class TestExtractMarkdownBlocks:
    """Tests for extract_markdown_blocks()."""

    def test_extracts_all_blocks(self):
        output = """
```python
code1
```

```json
{"key": "value"}
```
"""
        blocks = extract_markdown_blocks(output)
        assert len(blocks) == 2

    def test_filter_by_language(self):
        output = """
```python
code
```

```json
{"key": "value"}
```
"""
        blocks = extract_markdown_blocks(output, "json")
        assert len(blocks) == 1
        assert '{"key": "value"}' in blocks[0]


class TestExtractJsonFromOutput:
    """Tests for extract_json_from_output()."""

    def test_from_code_block(self):
        output = """
Here's the JSON:

```json
{"status": "ok"}
```
"""
        json_str = extract_json_from_output(output)
        assert json_str == '{"status": "ok"}'

    def test_raw_json(self):
        output = """The result is {"status": "ok"} which indicates success."""
        json_str = extract_json_from_output(output)
        assert json_str == '{"status": "ok"}'

    def test_array(self):
        output = '[1, 2, 3]'
        json_str = extract_json_from_output(output)
        assert json_str == '[1, 2, 3]'

    def test_no_json(self):
        output = "No JSON here"
        json_str = extract_json_from_output(output)
        assert json_str is None
