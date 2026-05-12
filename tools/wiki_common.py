from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import frontmatter as fm


CONTENT_DIRS = {
    "sources",
    "concepts",
    "entities",
    "procedures",
    "references",
    "analyses",
}

SOURCE_HEADINGS = [
    "## Summary",
    "## Key claims",
    "## Major concepts",
    "## Entities",
    "## Procedures",
    "## References",
    "## Open questions",
    "## Related pages",
]


@dataclass(frozen=True)
class Frontmatter:
    data: dict[str, object]
    body: str
    errors: list[str]


@dataclass(frozen=True)
class MarkdownLink:
    target: str
    line: int
    resolved: Path | None


def wiki_root() -> Path:
    return Path("wiki")


def is_content_page(path: Path) -> bool:
    parts = path.parts
    return len(parts) >= 3 and parts[0] == "wiki" and parts[1] in CONTENT_DIRS and path.suffix == ".md"


def iter_content_pages(root: Path = Path("wiki")) -> Iterable[Path]:
    for child in sorted(root.rglob("*.md")):
        if is_content_page(child):
            yield child


def page_node_id(path: Path) -> str:
    rel = path.relative_to("wiki").with_suffix("")
    return "wiki:" + rel.as_posix()


def parse_frontmatter(path: Path) -> Frontmatter:
    """Parse YAML frontmatter from a markdown file.

    Uses python-frontmatter for robust YAML parsing.
    Returns a Frontmatter dataclass with data, body, and errors.
    """
    text = path.read_text()
    if not text.startswith("---\n"):
        return Frontmatter({}, text, ["missing YAML frontmatter"])

    try:
        post = fm.loads(text)
        return Frontmatter(dict(post.metadata), post.content, [])
    except Exception as e:
        # Fall back to returning the text as body if parsing fails
        return Frontmatter({}, text, [f"YAML parse error: {e}"])


def section(body: str, heading: str) -> str:
    lines = body.splitlines()
    start: int | None = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i + 1
            break
    if start is None:
        return ""
    out: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        out.append(line)
    return "\n".join(out).strip()


def h2_headings(body: str) -> list[str]:
    return [line.strip() for line in body.splitlines() if line.startswith("## ")]


def first_h1(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line.strip()
    return None


def bullet_count(markdown: str) -> int:
    count = 0
    for line in markdown.splitlines():
        if re.match(r"^\s*(?:[-*]\s+|\d+[.]\s+)", line):
            count += 1
    return count


def markdown_links(path: Path) -> list[MarkdownLink]:
    links: list[MarkdownLink] = []
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for line_no, line in enumerate(path.read_text().splitlines(), start=1):
        for match in pattern.finditer(line):
            target = match.group(1).strip()
            clean = target.split("#", 1)[0]
            if not clean or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", clean):
                links.append(MarkdownLink(target, line_no, None))
                continue
            if clean.endswith(".md"):
                links.append(MarkdownLink(target, line_no,
                             (path.parent / clean).resolve()))
            else:
                links.append(MarkdownLink(target, line_no, None))
    return links


def code_paths(markdown: str) -> list[str]:
    return re.findall(r"`([^`]+\.md)`", markdown)


def one_line(text: str, limit: int = 180) -> str:
    collapsed = " ".join(text.strip().split())
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 1].rstrip() + "…"


STOPWORDS = {
    "about",
    "after",
    "against",
    "allows",
    "also",
    "because",
    "been",
    "being",
    "between",
    "both",
    "could",
    "different",
    "does",
    "doing",
    "done",
    "each",
    "from",
    "game",
    "games",
    "have",
    "having",
    "helps",
    "into",
    "like",
    "more",
    "most",
    "must",
    "need",
    "needs",
    "other",
    "players",
    "player",
    "should",
    "that",
    "their",
    "there",
    "these",
    "they",
    "this",
    "through",
    "using",
    "when",
    "where",
    "while",
    "with",
    "without",
    "would",
}


def content_tokens(text: str) -> list[str]:
    tokens: list[str] = []
    for raw in re.findall(r"[A-Za-z][A-Za-z0-9'-]*", text.lower()):
        token = raw.strip("-'")
        if len(token) < 4 or token in STOPWORDS:
            continue
        if token.endswith("'s"):
            token = token[:-2]
        if len(token) > 5 and token.endswith("s"):
            token = token[:-1]
        if token and token not in STOPWORDS:
            tokens.append(token)
    return tokens


# --- Context measurement utilities for local model debugging ---


def estimate_tokens(text: str, chars_per_token: float = 3.7) -> int:
    """Rough token estimate for mixed markdown/code content.

    Default of 3.7 chars/token is calibrated for markdown with code blocks.
    Use 4.0 for pure English prose, 3.5 for dense code.
    """
    return int(len(text) / chars_per_token)


def context_stats(text: str, label: str = "prompt") -> dict[str, int | str]:
    """Return context statistics for a prompt or text block."""
    chars = len(text)
    tokens = estimate_tokens(text)
    lines = text.count("\n") + 1
    return {
        "label": label,
        "chars": chars,
        "tokens": tokens,
        "lines": lines,
    }


def log_context_stats(text: str, label: str = "prompt", warn_threshold: int = 10000) -> None:
    """Print context statistics. Warn if estimated tokens exceed threshold.

    Default threshold of 10000 tokens is conservative for 30B models with 32K context.
    Qwen3-Coder-30B practical budget: 8k-12k input tokens.
    Adjust based on your model's effective context window.
    """
    stats = context_stats(text, label)
    print(
        f"Context [{stats['label']}]: {stats['chars']:,} chars, ~{stats['tokens']:,} tokens, {stats['lines']:,} lines")
    if stats["tokens"] > warn_threshold:
        print(
            f"  WARNING: {stats['label']} exceeds {warn_threshold:,} token threshold - may degrade model performance")


def truncate_to_tokens(text: str, max_tokens: int, suffix: str = "\n\n[truncated]") -> str:
    """Truncate text to approximately max_tokens, preserving line boundaries."""
    target_chars = int(max_tokens * 3.7)
    if len(text) <= target_chars:
        return text
    truncated = text[:target_chars].rsplit("\n", 1)[0]
    return truncated + suffix


def extract_failure_lines(validation_output: str, context_lines: int = 2) -> str:
    """Extract only lines containing FAIL/error with minimal context.

    Useful for reducing validation output size in repair prompts.
    """
    lines = validation_output.splitlines()
    relevant_indices: set[int] = set()
    for i, line in enumerate(lines):
        lower = line.lower()
        if "fail" in lower or "error" in lower or line.startswith("FAIL"):
            for j in range(max(0, i - context_lines), min(len(lines), i + context_lines + 1)):
                relevant_indices.add(j)
    if not relevant_indices:
        return validation_output[:2000] + "\n[no FAIL/error lines found, showing first 2000 chars]"
    result = [lines[i] for i in sorted(relevant_indices)]
    omitted = len(lines) - len(result)
    if omitted > 0:
        result.append(f"\n[{omitted} additional lines omitted]")
    return "\n".join(result)
