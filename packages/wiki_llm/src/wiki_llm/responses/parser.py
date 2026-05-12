"""Response parsing utilities for model outputs.

Parses model outputs to extract file contents and validate paths.

Usage:
    from wiki_llm.responses import parse_model_output, write_parsed_files
    
    files = parse_model_output(response.output)
    write_parsed_files(files, worktree)
"""
from __future__ import annotations

from pathlib import Path


def parse_model_output(output: str, expected_files: list[str] | None = None) -> dict[str, str]:
    """Parse model output into file contents.

    Expected format:
    ```wiki/path/to/file.md
    file contents here
    ```

    Args:
        output: Raw model output text
        expected_files: Optional list of expected file paths (for validation)

    Returns:
        Dictionary mapping file paths to their contents
    """
    files: dict[str, str] = {}
    current_file: str | None = None
    current_content: list[str] = []

    for line in output.split("\n"):
        # Start of a fenced code block with a path
        if line.startswith("```") and len(line) > 3 and not line.startswith("```\n"):
            # Save previous file if any
            if current_file:
                files[current_file] = "\n".join(current_content)

            path = line[3:].strip()
            # Check if it looks like a file path
            if path.endswith(".md") or path.endswith(".json") or path.endswith(".py"):
                current_file = path
                current_content = []
            elif expected_files and path in expected_files:
                current_file = path
                current_content = []
            else:
                current_file = None
                current_content = []

        # End of fenced code block
        elif line == "```" and current_file:
            files[current_file] = "\n".join(current_content)
            current_file = None
            current_content = []

        # Content within a file block
        elif current_file is not None:
            current_content.append(line)

    return files


def validate_file_paths(files: dict[str, str], worktree: Path) -> list[str]:
    """Validate that all file paths are within the worktree.

    Returns list of invalid paths (empty if all valid).
    """
    invalid = []
    worktree_resolved = worktree.resolve()

    for path in files.keys():
        try:
            full_path = (worktree / path).resolve()
            if not str(full_path).startswith(str(worktree_resolved)):
                invalid.append(path)
        except Exception:
            invalid.append(path)

    return invalid


def write_parsed_files(files: dict[str, str], worktree: Path, dry_run: bool = False) -> list[Path]:
    """Write parsed files to the worktree.

    Args:
        files: Dictionary mapping paths to contents
        worktree: Root directory for file writes
        dry_run: If True, only print what would be written

    Returns:
        List of paths that were written (or would be written)
    """
    written = []

    for path, content in files.items():
        full_path = worktree / path

        if dry_run:
            print(f"Would write: {full_path} ({len(content)} chars)")
        else:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content)
            print(f"Wrote: {full_path} ({len(content)} chars)")

        written.append(full_path)

    return written


def extract_markdown_blocks(output: str, language: str | None = None) -> list[str]:
    """Extract fenced code blocks from model output.

    Args:
        output: Raw model output text
        language: Optional language filter (e.g., "json", "markdown")

    Returns:
        List of code block contents
    """
    blocks: list[str] = []
    current_block: list[str] = []
    in_block = False
    block_language = ""

    for line in output.split("\n"):
        if line.startswith("```"):
            if in_block:
                # End of block
                if language is None or block_language == language:
                    blocks.append("\n".join(current_block))
                current_block = []
                in_block = False
            else:
                # Start of block
                block_language = line[3:].strip().lower()
                in_block = True
        elif in_block:
            current_block.append(line)

    return blocks


def extract_json_from_output(output: str) -> str | None:
    """Extract JSON content from model output.

    Handles both fenced code blocks and raw JSON.

    Returns:
        JSON string or None if not found
    """
    import json

    # Try extracting from code blocks first
    blocks = extract_markdown_blocks(output, "json")
    if blocks:
        return blocks[0]

    # Try finding raw JSON object/array
    output = output.strip()

    # Find first { or [
    start_obj = output.find("{")
    start_arr = output.find("[")

    if start_obj == -1 and start_arr == -1:
        return None

    if start_obj == -1:
        start = start_arr
        end_char = "]"
    elif start_arr == -1:
        start = start_obj
        end_char = "}"
    else:
        if start_obj < start_arr:
            start = start_obj
            end_char = "}"
        else:
            start = start_arr
            end_char = "]"

    # Find matching end
    depth = 0
    for i, c in enumerate(output[start:], start):
        if c in "{[":
            depth += 1
        elif c in "}]":
            depth -= 1
            if depth == 0:
                candidate = output[start:i + 1]
                # Validate it's valid JSON
                try:
                    json.loads(candidate)
                    return candidate
                except json.JSONDecodeError:
                    continue

    return None
