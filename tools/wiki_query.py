#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import content_tokens, iter_content_pages, one_line, parse_frontmatter, section


@dataclass(frozen=True)
class PageHit:
    path: Path
    title: str
    page_type: str
    score: int
    summary: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Answer a query from the wiki using a bounded local-model context.")
    parser.add_argument("question")
    parser.add_argument("--candidate", help="local Codex candidate, e.g. local-4090 or local-4090:model")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--max-pages", type=int, default=6)
    parser.add_argument("--output", help="write answer to this path instead of stdout")
    parser.add_argument("--save-analysis", action="store_true", help="file the answer under wiki/analyses/")
    parser.add_argument("--slug", help="analysis slug; default is derived from the question")
    parser.add_argument("--plan-only", action="store_true", help="only print selected pages and prompt preview")
    args = parser.parse_args()

    index_path = Path("wiki/index.md")
    if not index_path.exists():
        print("FAIL: missing wiki/index.md", file=sys.stderr)
        return 2

    hits = select_pages(args.question, args.max_pages)
    if not hits:
        print("FAIL: no relevant wiki pages found", file=sys.stderr)
        return 1

    prompt = render_prompt(args.question, hits)
    if args.plan_only or not args.candidate:
        print(render_plan(args.question, hits, prompt))
        return 0

    answer, returncode = run_codex_answer(args.codex_bin, args.candidate, prompt, args.timeout)
    if returncode != 0:
        print(answer)
        return returncode

    if args.output:
        Path(args.output).write_text(answer)
        print(f"wrote {args.output}")
    elif not args.save_analysis:
        print(answer)

    if args.save_analysis:
        analysis_path = save_analysis(args.question, args.slug, answer, hits)
        finalize_analysis(analysis_path, args.question, hits)
        print(f"wrote {analysis_path}")

    return 0


def select_pages(question: str, max_pages: int) -> list[PageHit]:
    query_tokens = set(content_tokens(question))
    hits: list[PageHit] = []
    for path in iter_content_pages():
        fm = parse_frontmatter(path)
        title = str(fm.data.get("title") or path.stem.replace("-", " ").title())
        page_type = str(fm.data.get("type") or "")
        summary = section(fm.body, "## Summary") or first_paragraph(fm.body)
        text = " ".join([title, page_type, summary, path.read_text(errors="ignore")])
        tokens = set(content_tokens(text))
        score = len(query_tokens & tokens)
        if score == 0:
            continue
        if page_type == "source":
            score += 1
        hits.append(PageHit(path, title, page_type, score, one_line(summary, 180)))
    return sorted(hits, key=lambda hit: (-hit.score, hit.page_type != "source", hit.path.as_posix()))[:max_pages]


def render_plan(question: str, hits: list[PageHit], prompt: str) -> str:
    lines = [
        "# Query Plan",
        "",
        f"Question: {question}",
        "",
        "## Selected Pages",
        "",
    ]
    for hit in hits:
        lines.append(f"- {hit.path.as_posix()} ({hit.page_type}, score {hit.score}) - {hit.summary}")
    lines.extend(["", "## Prompt Preview", "", "```text", one_line(prompt, 3000), "```"])
    return "\n".join(lines) + "\n"


def render_prompt(question: str, hits: list[PageHit]) -> str:
    page_blocks = []
    for hit in hits:
        text = hit.path.read_text(errors="ignore")
        page_blocks.append(
            "\n".join(
                [
                    f"PAGE: {hit.path.as_posix()}",
                    f"TITLE: {hit.title}",
                    f"TYPE: {hit.page_type}",
                    "CONTENT:",
                    trim_page(text),
                ]
            )
        )
    return f"""You are answering a query from the existing LLM-Wiki. Do not edit files.

Question:
{question}

Use only the supplied wiki pages. If the supplied pages do not cover something, say `not covered in sources`.
Answer concisely and cite the wiki pages you used with relative Markdown links.

Supplied pages:

{chr(10).join(page_blocks)}
"""


def trim_page(text: str, limit: int = 7000) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n\n[trimmed]"


def run_codex_answer(codex_bin: str, candidate: str, prompt: str, timeout: int) -> tuple[str, int]:
    profile, model = parse_candidate(candidate)
    with tempfile.TemporaryDirectory(prefix="llm-wiki-query.") as tmp:
        last_message = Path(tmp) / "last-message.md"
        command = [
            codex_bin,
            "exec",
            "--profile",
            profile,
            "--cd",
            str(Path(tmp)),
            "--dangerously-bypass-approvals-and-sandbox",
            "--skip-git-repo-check",
            "--ephemeral",
            "--output-last-message",
            str(last_message),
        ]
        if model:
            command.extend(["--model", model])
        command.append("-")
        completed = subprocess.run(
            command,
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        output = last_message.read_text() if last_message.exists() else completed.stdout
        return output, completed.returncode


def parse_candidate(raw: str) -> tuple[str, str | None]:
    if ":" not in raw:
        return raw, None
    profile, model = raw.split(":", 1)
    if not profile or not model:
        raise SystemExit(f"invalid candidate {raw!r}; use PROFILE or PROFILE:MODEL")
    return profile, model


def save_analysis(question: str, slug: str | None, answer: str, hits: list[PageHit]) -> Path:
    analysis_slug = slug or slugify(question)
    path = Path("wiki/analyses") / f"{date.today().isoformat()}-{analysis_slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    source_pages = source_pages_for_hits(hits)
    if not source_pages:
        raise SystemExit("FAIL: cannot save analysis without at least one source page")
    sources = "\n".join(f"  - ../{source.relative_to('wiki').as_posix()}" for source in source_pages)
    source_links = "\n".join(f"- [{page_title(source)}](../{source.relative_to('wiki').as_posix()})" for source in source_pages)
    related_hits = [hit for hit in hits if hit.path not in source_pages]
    related = "\n".join(f"- [{hit.title}](../{hit.path.relative_to('wiki').as_posix()})" for hit in related_hits)
    path.write_text(
        "\n".join(
            [
                "---",
                f"title: {yaml_string(analysis_title(question))}",
                "type: analysis",
                "tags: []",
                "status: draft",
                f"last_updated: {date.today().isoformat()}",
                "sources:",
                sources,
                "---",
                "",
                f"# {analysis_title(question)}",
                "",
                answer.strip(),
                "",
                "## Source pages",
                "",
                source_links,
                "",
                "## Related pages",
                "",
                related or "None.",
                "",
            ]
        )
    )
    return path


def source_pages_for_hits(hits: list[PageHit]) -> list[Path]:
    source_pages: set[Path] = set()
    cwd = Path.cwd().resolve()
    for hit in hits:
        if hit.page_type == "source":
            source_pages.add(hit.path)
        fm = parse_frontmatter(hit.path)
        for source in fm.data.get("sources") or []:
            if not isinstance(source, str):
                continue
            resolved = (hit.path.parent / source).resolve()
            try:
                rel = resolved.relative_to(cwd)
            except ValueError:
                continue
            if len(rel.parts) >= 3 and rel.parts[0] == "wiki" and rel.parts[1] == "sources" and rel.suffix == ".md":
                source_pages.add(rel)
    return sorted(source_pages)


def page_title(path: Path) -> str:
    fm = parse_frontmatter(path)
    return str(fm.data.get("title") or path.stem.replace("-", " ").title())


def finalize_analysis(path: Path, question: str, hits: list[PageHit]) -> None:
    run(["python3", "tools/wiki_check_analysis.py", path.as_posix()])
    run(["python3", "tools/wiki_index.py"])
    run(["python3", "tools/wiki_graph.py"])
    details = [
        f"Question: {question}",
        f"Analysis page: {path.as_posix()}",
        "Pages used: " + ", ".join(hit.path.as_posix() for hit in hits),
    ]
    command = ["python3", "tools/wiki_log.py", "query", f"filed {path.stem}"]
    for detail in details:
        command.extend(["--detail", detail])
    run(command)


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def first_paragraph(body: str) -> str:
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("|"):
            if lines:
                break
            continue
        if stripped.startswith("- ") or stripped.startswith("```"):
            continue
        lines.append(stripped)
    return " ".join(lines)


def analysis_title(question: str) -> str:
    cleaned = question.strip().rstrip("?")
    if len(cleaned) > 80:
        cleaned = cleaned[:77].rstrip() + "..."
    return cleaned[:1].upper() + cleaned[1:]


def yaml_string(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60].strip("-") or "query"


if __name__ == "__main__":
    sys.exit(main())
