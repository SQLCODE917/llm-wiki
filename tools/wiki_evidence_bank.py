#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from wiki_common import content_tokens


WEAK_SNIPPET_PATTERNS = [
    r"\bwe'll get back\b",
    r"\bas referred to in the guide\b",
    r"\bthis chapter is\b",
    r"\bsummary: this document\b",
    r"\bthe guide (?:covers|mentions|discusses)\b",
]


@dataclass(frozen=True)
class SourceChunk:
    text: str
    locator: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract exact normalized-source evidence snippets for candidate pages.")
    parser.add_argument("normalized_source", help="normalized markdown source file")
    parser.add_argument("candidate", nargs="+", help="candidate path or title to retrieve evidence for")
    parser.add_argument("--per-candidate", type=int, default=8)
    args = parser.parse_args()

    source_path = Path(args.normalized_source)
    if not source_path.exists():
        print(f"FAIL: missing normalized source {source_path}", file=sys.stderr)
        return 1

    text = source_path.read_text(errors="ignore")
    print(render_evidence_bank(text, args.candidate, args.per_candidate))
    return 0


def render_evidence_bank(source_text: str, candidates: list[str], per_candidate: int = 8) -> str:
    chunks = source_chunks(source_text)
    sections: list[str] = []
    for candidate in candidates:
        snippets = snippets_for_candidate(candidate, chunks, per_candidate)
        sections.append(f"### {candidate}")
        if snippets:
            sections.extend(f"- `{snippet.locator}` - {snippet.text}" for snippet in snippets)
        else:
            sections.append("- not covered in sources")
        sections.append("")
    return "\n".join(sections).rstrip()


def snippets_for_candidate(candidate: str, chunks: list[SourceChunk], limit: int) -> list[SourceChunk]:
    candidate_key = Path(candidate).stem if candidate.endswith(".md") else candidate
    query_tokens = candidate_tokens(candidate_key)
    if not query_tokens:
        query_tokens = set(content_tokens(candidate))

    scored: list[tuple[int, int, int, SourceChunk]] = []
    for index, chunk in enumerate(chunks):
        tokens = evidence_tokens(chunk.text)
        score = len(query_tokens & tokens)
        if score == 0:
            continue
        if any(re.search(pattern, chunk.text, flags=re.IGNORECASE) for pattern in WEAK_SNIPPET_PATTERNS):
            continue
        if any(token in tokens for token in query_tokens):
            snippet = SourceChunk(text=trim_chunk(chunk.text, query_tokens), locator=chunk.locator)
            scored.append((score, -len(snippet.text), -index, snippet))

    seen: set[str] = set()
    snippets: list[SourceChunk] = []
    for _score, _neg_len, _neg_index, snippet in sorted(scored, reverse=True):
        key = f"{snippet.locator}:{snippet.text}"
        if key in seen:
            continue
        seen.add(key)
        snippets.append(snippet)
        if len(snippets) >= limit:
            break
    return snippets


def candidate_tokens(candidate: str) -> set[str]:
    ignored = {
        "aoe2",
        "wiki",
        "concept",
        "concepts",
        "entity",
        "entities",
        "procedure",
        "procedures",
        "reference",
        "references",
        "upgrade",
        "upgrades",
        "page",
        "pages",
        "md",
    }
    tokens: set[str] = set()
    for raw in re.findall(r"[A-Za-z][A-Za-z0-9']*", candidate.replace("-", " ").lower()):
        token = raw.strip("'")
        if token.endswith("'s"):
            token = token[:-2]
        if len(token) > 4 and token.endswith("s"):
            token = token[:-1]
        if len(token) >= 3 and token not in ignored:
            tokens.add(token)
    return tokens


def evidence_tokens(text: str) -> set[str]:
    tokens = set(content_tokens(text))
    for raw in re.findall(r"[A-Za-z][A-Za-z0-9']*", text.lower()):
        token = raw.strip("'")
        if token.endswith("'s"):
            token = token[:-2]
        if len(token) > 4 and token.endswith("s"):
            token = token[:-1]
        if len(token) >= 3:
            tokens.add(token)
    return tokens


def source_chunks(text: str) -> list[SourceChunk]:
    chunks: list[SourceChunk] = []
    for line_number, raw in enumerate(text.splitlines(), start=1):
        line = " ".join(raw.strip().split())
        if not line or line.startswith("#") or line.startswith("|") or set(line) <= {"-", " "}:
            continue
        if len(line) < 40:
            continue
        for sentence in split_sentences(line):
            if len(sentence) >= 40:
                chunks.append(SourceChunk(text=sentence, locator=f"normalized:L{line_number}"))
    return chunks


def split_sentences(line: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", line)
    if len(parts) == 1:
        return [line]
    out: list[str] = []
    buffer = ""
    for part in parts:
        candidate = f"{buffer} {part}".strip()
        if len(candidate) < 80:
            buffer = candidate
            continue
        out.append(candidate)
        buffer = ""
    if buffer:
        out.append(buffer)
    return out


def trim_chunk(chunk: str, query_tokens: set[str], limit: int = 240) -> str:
    if len(chunk) <= limit:
        return chunk.replace("|", "/")

    lowered = chunk.lower()
    positions = [lowered.find(token) for token in query_tokens if lowered.find(token) != -1]
    center = min(positions) if positions else 0
    start = max(0, center - limit // 3)
    end = min(len(chunk), start + limit)
    start = max(0, end - limit)

    while start > 0 and not chunk[start].isspace():
        start += 1
    while end < len(chunk) and not chunk[end - 1].isspace():
        end -= 1
    return chunk[start:end].strip().replace("|", "/")


if __name__ == "__main__":
    sys.exit(main())
