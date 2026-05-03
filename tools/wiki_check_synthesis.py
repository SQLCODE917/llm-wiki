#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

from wiki_common import (
    bullet_count,
    code_paths,
    content_tokens,
    h2_headings,
    markdown_links,
    parse_frontmatter,
    section,
)


SYNTH_TYPES = {"concept", "entity", "procedure", "reference"}
REQUIRED_KEYS = ["title", "type", "tags", "status", "last_updated", "sources"]
RELATED_CREATED = "created"
RELATED_NOT_CREATED = "not created yet"
RELATED_PRIORITIES = {"must create", "should create", "could create", "defer"}
WEAK_EVIDENCE_PATTERNS = [
    r"\bwe'll get back\b",
    r"\bas referred to in the guide\b",
    r"\bthis chapter is\b",
    r"\bsummary: this document\b",
    r"\bthe guide (?:covers|mentions|discusses)\b",
]
WEAK_CLAIM_PATTERNS = [
    r"\bimportant\b",
    r"\bcrucial\b",
    r"\bfundamental\b",
    r"\bessential\b",
    r"\bsuccess\b",
]
LOCATOR_RE = re.compile(r"^(?:p\.\s*\d+\s*;\s*)?normalized:L(?P<start>\d+)(?:-L?(?P<end>\d+))?$", re.IGNORECASE)


@dataclass(frozen=True)
class EvidenceSource:
    lines: list[str]


@dataclass(frozen=True)
class RelatedScope:
    title: str
    path: str
    group: str | None
    evidence_basis: str | None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Phase 2 synthesized pages for one source.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--min-pages", type=int, default=3)
    parser.add_argument("--max-pages", type=int, default=15)
    parser.add_argument("--min-evidence-rows", type=int, default=3)
    parser.add_argument("--normalized-source", help="normalized source markdown for evidence excerpt checks")
    parser.add_argument(
        "--skip-evidence-text-check",
        action="store_true",
        help="require evidence table structure but do not verify excerpts against normalized source text",
    )
    parser.add_argument(
        "--allowed-page",
        action="append",
        default=[],
        help="repo-relative synthesized page path allowed for this phase; repeatable",
    )
    parser.add_argument(
        "--require-allowed-pages",
        action="store_true",
        help="fail if any --allowed-page path is not created and linked for this source",
    )
    args = parser.parse_args()

    failures = check_synthesis(
        args.slug,
        args.min_pages,
        args.max_pages,
        args.allowed_page,
        min_evidence_rows=args.min_evidence_rows,
        normalized_source=args.normalized_source,
        check_evidence_text=not args.skip_evidence_text_check,
        require_allowed_pages=args.require_allowed_pages,
    )
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print(f"PASS: synthesis for {args.slug}")
    return 0


def check_synthesis(
    slug: str,
    min_pages: int,
    max_pages: int,
    allowed_pages: list[str] | None = None,
    *,
    min_evidence_rows: int = 3,
    normalized_source: str | None = None,
    check_evidence_text: bool = True,
    require_allowed_pages: bool = False,
) -> list[str]:
    source_path = Path("wiki/sources") / f"{slug}.md"
    failures: list[str] = []
    if not source_path.exists():
        return [f"missing source page {source_path}"]

    evidence_source = load_evidence_source(source_path, normalized_source) if check_evidence_text else None

    linked_pages = linked_synthesized_pages(source_path)
    sourced_pages = sourced_synthesized_pages(source_path)
    created_pages = sorted(set(linked_pages) | set(sourced_pages))
    if len(created_pages) < min_pages:
        failures.append(f"{source_path}: only {len(created_pages)} synthesized pages; expected at least {min_pages}")
    if len(created_pages) > max_pages:
        failures.append(f"{source_path}: {len(created_pages)} synthesized pages; expected at most {max_pages}")

    allowed = {Path(path).as_posix() for path in allowed_pages or []}
    if allowed:
        for page in created_pages:
            if page.as_posix() not in allowed:
                failures.append(f"{page}: page was not selected for this Phase 2 run")
        if require_allowed_pages:
            created = {page.as_posix() for page in created_pages}
            for page in sorted(allowed - created):
                failures.append(f"{page}: selected page was not created and linked")

    for page in sorted(set(sourced_pages) - set(linked_pages)):
        failures.append(f"{source_path}: synthesized page {page.as_posix()} is not linked from Related pages")
    for page in sorted(set(linked_pages) - set(sourced_pages)):
        failures.append(f"{page}: page is linked from source but does not cite that source in frontmatter")

    related = section(parse_frontmatter(source_path).body, "## Related pages")
    scopes = related_scopes(source_path, related)
    for page in created_pages:
        failures.extend(
            check_synthesized_page(
                page,
                source_path,
                min_evidence_rows,
                evidence_source,
                scopes.get(page.as_posix()),
            )
        )

    failures.extend(check_related_table(source_path, related))
    for code_path in code_paths(related):
        candidate = (source_path.parent / code_path).resolve()
        if candidate.exists():
            failures.append(
                f"{source_path}: existing page {code_path!r} is still listed as a candidate instead of a Markdown link"
            )
    return failures


def linked_synthesized_pages(source_path: Path) -> list[Path]:
    heading_line = line_number_of_heading(source_path.read_text(), "## Related pages")
    pages: list[Path] = []
    for link in markdown_links(source_path):
        if link.line <= heading_line or not link.resolved or not link.resolved.exists():
            continue
        try:
            rel = link.resolved.relative_to(Path.cwd().resolve())
        except ValueError:
            continue
        if len(rel.parts) >= 3 and rel.parts[0] == "wiki" and rel.parts[1] in {"concepts", "entities", "procedures", "references"}:
            pages.append(rel)
    return sorted(set(pages))


def check_related_table(source_path: Path, related: str) -> list[str]:
    failures: list[str] = []
    for row_number, line in enumerate(related.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.lower() in {"none.", "not covered in sources"}:
            continue
        if not stripped.startswith("|"):
            continue
        cells = split_table_row(stripped)
        if cells is None or len(cells) not in {3, 5, 6}:
            failures.append(f"{source_path}: Related pages row {row_number} must have three, five, or six table cells")
            continue

        title = cells[0]
        path_cell = cells[1]
        status_cell = cells[-1]
        if title.lower() in {"candidate page", "page"} or is_separator_row(cells):
            continue
        if title.strip().lower() == "page title":
            failures.append(f"{source_path}: Related pages row {row_number} uses placeholder title 'Page title'")
        group = None
        priority = None
        evidence_basis = None
        if len(cells) == 5:
            priority = cells[2].strip().lower()
            evidence_basis = cells[3].strip()
        elif len(cells) == 6:
            group = cells[2].strip()
            priority = cells[3].strip().lower()
            evidence_basis = cells[4].strip()
            if not group:
                failures.append(f"{source_path}: Related pages row {row_number} group must not be empty")
        if priority is not None:
            if priority not in RELATED_PRIORITIES:
                failures.append(
                    f"{source_path}: Related pages row {row_number} priority must be one of {sorted(RELATED_PRIORITIES)}"
                )
            if not evidence_basis:
                failures.append(f"{source_path}: Related pages row {row_number} evidence basis must not be empty")
        if not title:
            failures.append(f"{source_path}: Related pages row {row_number} has an empty title")
        if "](" in title or "`" in title:
            failures.append(f"{source_path}: Related pages row {row_number} title cell must be plain text")

        status = status_cell.strip().lower()
        code_target = code_cell_target(path_cell)
        link_target = link_cell_target(path_cell)
        if code_target:
            if status != RELATED_NOT_CREATED:
                failures.append(
                    f"{source_path}: Related pages candidate row {row_number} status must be {RELATED_NOT_CREATED!r}"
                )
            if (source_path.parent / code_target).resolve().exists():
                failures.append(
                    f"{source_path}: Related pages row {row_number} points to an existing page but is still a candidate"
                )
            continue

        if "](" in path_cell:
            if path_cell.count("](") != 1 or not link_target:
                failures.append(f"{source_path}: Related pages row {row_number} has a non-canonical Markdown link")
                continue
            label = path_cell[1 : path_cell.index("](")].strip()
            if label != link_target:
                failures.append(
                    f"{source_path}: Related pages row {row_number} link text must exactly equal its path"
                )
            if status != RELATED_CREATED:
                failures.append(
                    f"{source_path}: Related pages linked row {row_number} status must be {RELATED_CREATED!r}"
                )
            if not (source_path.parent / link_target).resolve().exists():
                failures.append(f"{source_path}: Related pages row {row_number} links to a missing page")
            continue

        failures.append(
            f"{source_path}: Related pages row {row_number} path cell must be a code-formatted candidate path or canonical Markdown link"
        )
    return failures


def related_scopes(source_path: Path, related: str) -> dict[str, RelatedScope]:
    scopes: dict[str, RelatedScope] = {}
    for line in related.splitlines():
        cells = split_table_row(line)
        if cells is None or is_separator_row(cells) or cells[0].lower() in {"candidate page", "page"}:
            continue
        if len(cells) not in {3, 5, 6}:
            continue
        if cells[-1].strip().lower() != RELATED_CREATED:
            continue
        target = link_cell_target(cells[1])
        if target is None:
            continue
        try:
            rel = (source_path.parent / target).resolve().relative_to(Path.cwd().resolve()).as_posix()
        except ValueError:
            continue
        group = cells[2].strip() if len(cells) == 6 else None
        evidence_basis = cells[4].strip() if len(cells) == 6 else cells[3].strip() if len(cells) == 5 else None
        scopes[rel] = RelatedScope(
            title=strip_markdown(cells[0]).strip(),
            path=rel,
            group=group,
            evidence_basis=evidence_basis,
        )
    return scopes


def sourced_synthesized_pages(source_path: Path) -> list[Path]:
    pages: list[Path] = []
    for directory in ("wiki/concepts", "wiki/entities", "wiki/procedures", "wiki/references"):
        root = Path(directory)
        if not root.exists():
            continue
        for page in sorted(root.glob("*.md")):
            fm = parse_frontmatter(page)
            sources = fm.data.get("sources")
            if not isinstance(sources, list):
                continue
            for source in sources:
                if not isinstance(source, str):
                    continue
                if (page.parent / source).resolve() == source_path.resolve():
                    pages.append(page)
                    break
    return sorted(set(pages))


def check_synthesized_page(
    page: Path,
    source_path: Path,
    min_evidence_rows: int,
    evidence_source: EvidenceSource | None,
    related_scope: RelatedScope | None,
) -> list[str]:
    failures: list[str] = []
    text = page.read_text()
    non_ascii = sorted({char for char in text if ord(char) > 127})
    if non_ascii:
        sample = "".join(non_ascii[:8])
        failures.append(f"{page}: contains non-ASCII characters {sample!r}; use ASCII unless the source requires them")

    fm = parse_frontmatter(page)
    for error in fm.errors:
        failures.append(f"{page}: {error}")
    for key in REQUIRED_KEYS:
        if key not in fm.data:
            failures.append(f"{page}: missing frontmatter key {key!r}")

    page_type = fm.data.get("type")
    if page_type not in SYNTH_TYPES:
        failures.append(f"{page}: type must be one of {sorted(SYNTH_TYPES)}")

    first_body_line = first_nonblank_line(fm.body)
    if not re.search(r"^# .+", fm.body, re.MULTILINE):
        failures.append(f"{page}: missing H1 title")
    elif first_body_line is not None and not first_body_line.startswith("# "):
        failures.append(f"{page}: first nonblank body line must be the H1 title")
    failures.extend(body_metadata_failures(page, fm.body))

    source_rel = relative_link(page, source_path)
    sources = fm.data.get("sources")
    if not isinstance(sources, list) or source_rel not in sources:
        failures.append(f"{page}: frontmatter sources must include {source_rel}")

    body_links = []
    for link in markdown_links(page):
        if not link.resolved:
            continue
        if not link.resolved.exists():
            failures.append(f"{page}:{link.line}: broken Markdown link {link.target!r}")
            continue
        body_links.append(link.resolved)
    if source_path.resolve() not in body_links:
        failures.append(f"{page}: body must link back to {source_rel}")

    body_headings = h2_headings(fm.body)
    duplicate_headings = sorted({heading for heading in body_headings if body_headings.count(heading) > 1})
    for heading in duplicate_headings:
        failures.append(f"{page}: duplicate heading {heading!r}")

    for heading in body_headings:
        if not section(fm.body, heading).strip():
            failures.append(f"{page}: empty section {heading!r}")

    if "## Source-backed details" not in body_headings:
        failures.append(f"{page}: missing source-backed details section")
    else:
        details = section(fm.body, "## Source-backed details")
        detail_tokens = content_tokens(details)
        if len(detail_tokens) < 25:
            failures.append(f"{page}: source-backed details section is too thin")
        failures.extend(check_evidence_table(page, source_path, details, min_evidence_rows, evidence_source, related_scope))

    if "## Source pages" not in body_headings and "## Sources" not in body_headings:
        failures.append(f"{page}: missing source page section")

    failures.extend(check_type_specific_sections(page, fm.body, page_type, evidence_source, related_scope))
    return failures


def relative_link(page: Path, target: Path) -> str:
    return Path("../" * (len(page.parent.relative_to("wiki").parts)) + target.relative_to("wiki").as_posix()).as_posix()


def first_nonblank_line(markdown: str) -> str | None:
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return None


def body_metadata_failures(page: Path, body: str) -> list[str]:
    failures: list[str] = []
    in_code = False
    for line_number, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if re.match(r"^(?:title|type|tags|status|last_updated|sources|source_id|source_type):\s*", stripped):
            failures.append(f"{page}: body line {line_number} looks like stray frontmatter: {stripped}")
    return failures


def check_evidence_table(
    page: Path,
    source_path: Path,
    details: str,
    min_evidence_rows: int,
    evidence_source: EvidenceSource | None,
    related_scope: RelatedScope | None,
) -> list[str]:
    failures: list[str] = []
    rows = table_rows(details)
    if len(rows) < 2:
        failures.append(f"{page}: Source-backed details must include a Claim/Evidence/Locator/Source table")
        failures.extend(diff_marker_failures(page, details))
        return failures

    header_index: int | None = None
    for index, cells in enumerate(rows):
        normalized = [cell.strip().lower() for cell in cells]
        if normalized == ["claim", "evidence", "locator", "source"]:
            header_index = index
            break
    if header_index is None:
        return [f"{page}: evidence table header must be exactly | Claim | Evidence | Locator | Source |"]

    data_rows: list[tuple[str, str, str, str]] = []
    for cells in rows[header_index + 1 :]:
        if is_separator_row(cells):
            continue
        if len(cells) != 4:
            failures.append(f"{page}: evidence table row must have exactly four cells")
            continue
        claim, evidence, locator, source = (cell.strip() for cell in cells)
        if claim or evidence or locator or source:
            data_rows.append((claim, evidence, locator, source))

    if len(data_rows) < min_evidence_rows:
        failures.append(f"{page}: evidence table has {len(data_rows)} rows; expected at least {min_evidence_rows}")
        failures.extend(diff_marker_failures(page, details))

    for index, (claim, evidence, locator, source) in enumerate(data_rows, start=1):
        claim_words = re.findall(r"[A-Za-z0-9']+", strip_markdown(claim))
        if len(claim_words) < 5:
            failures.append(f"{page}: evidence row {index} claim is too short")
        if any(re.search(pattern, claim, flags=re.IGNORECASE) for pattern in WEAK_CLAIM_PATTERNS):
            failures.append(f"{page}: evidence row {index} uses weak generic claim language")
        repeated = repeated_phrase(strip_markdown(claim))
        if repeated:
            failures.append(f"{page}: evidence row {index} repeats phrase {repeated!r}")

        excerpt = clean_evidence_excerpt(evidence)
        failures.extend(scope_failures(page, f"evidence row {index}", claim + " " + excerpt, related_scope))
        claim_norm = normalize_for_search(strip_markdown(claim))
        excerpt_norm = normalize_for_search(excerpt)
        if claim_norm == excerpt_norm or SequenceMatcher(None, claim_norm, excerpt_norm).ratio() > 0.88:
            failures.append(f"{page}: evidence row {index} claim repeats the evidence instead of synthesizing it")

        excerpt_words = re.findall(r"[A-Za-z0-9']+", excerpt)
        if len(excerpt_words) < 4 or len(excerpt) < 24:
            failures.append(f"{page}: evidence row {index} excerpt is too short")
        if any(re.search(pattern, excerpt, flags=re.IGNORECASE) for pattern in WEAK_EVIDENCE_PATTERNS):
            failures.append(f"{page}: evidence row {index} excerpt is document navigation or metadata, not evidence")

        parsed_locator = parse_locator(locator)
        if parsed_locator is None:
            failures.append(
                f"{page}: evidence row {index} locator must look like `normalized:L12` or `normalized:L12-L14`"
            )
        elif evidence_source is not None:
            start, end = parsed_locator
            if start < 1 or end < start or end > len(evidence_source.lines):
                failures.append(
                    f"{page}: evidence row {index} locator {clean_locator(locator)!r} is outside normalized source line range"
                )
            else:
                locator_text = "\n".join(evidence_source.lines[start - 1 : end])
                if excerpt_norm not in normalize_for_search(locator_text):
                    failures.append(
                        f"{page}: evidence row {index} excerpt is not found in locator range {clean_locator(locator)!r}"
                    )

        source_target = first_markdown_target(source)
        if source_target is None:
            failures.append(f"{page}: evidence row {index} source cell must link to the source page")
        elif (page.parent / source_target).resolve() != source_path.resolve():
            failures.append(f"{page}: evidence row {index} source link must resolve to {source_path.as_posix()}")

    return failures


def diff_marker_failures(page: Path, markdown: str) -> list[str]:
    failures: list[str] = []
    for line_number, line in enumerate(markdown.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith(("+", "-")) and "|" in stripped and not stripped.startswith("|"):
            failures.append(f"{page}: Source-backed details line {line_number} looks like a diff marker, not a table row")
    return failures


def check_type_specific_sections(
    page: Path,
    body: str,
    page_type: object,
    evidence_source: EvidenceSource | None,
    related_scope: RelatedScope | None,
) -> list[str]:
    failures: list[str] = []
    if page_type == "procedure":
        steps = section(body, "## Steps") or section(body, "## Procedure")
        if not steps:
            failures.append(f"{page}: procedure pages must include a ## Steps or ## Procedure section")
        elif bullet_count(steps) < 3:
            failures.append(f"{page}: procedure steps section has {bullet_count(steps)} steps; expected at least 3")
    elif page_type == "reference":
        reference_data = section(body, "## Reference data")
        if not reference_data:
            failures.append(f"{page}: reference pages must include a ## Reference data section")
        elif table_data_row_count(reference_data) < 2:
            failures.append(f"{page}: Reference data table has fewer than 2 data rows")
        else:
            failures.extend(check_reference_data_table(page, reference_data, evidence_source, related_scope))
    return failures


def check_reference_data_table(
    page: Path,
    markdown: str,
    evidence_source: EvidenceSource | None,
    related_scope: RelatedScope | None,
) -> list[str]:
    failures: list[str] = []
    rows = table_rows(markdown)
    if len(rows) < 2:
        return failures
    header_index = next((index for index, row in enumerate(rows) if not is_separator_row(row)), None)
    if header_index is None:
        return failures
    header = [cell.strip().lower() for cell in rows[header_index]]
    if "evidence" not in header or "locator" not in header:
        failures.append(f"{page}: Reference data table must include Evidence and Locator columns")
        return failures
    evidence_index = header.index("evidence")
    locator_index = header.index("locator")
    source_index = header.index("source") if "source" in header else None
    seen_facts: dict[str, int] = {}
    for row_number, row in enumerate(rows[header_index + 1 :], start=1):
        if is_separator_row(row):
            continue
        if len(row) != len(header):
            failures.append(f"{page}: Reference data row {row_number} must have {len(header)} cells")
            continue
        fact_text = " ".join(
            strip_markdown(cell).strip()
            for index, cell in enumerate(row)
            if index not in {evidence_index, locator_index, source_index}
        )
        supported_fact_text = supported_fact_cell_text(header, row, evidence_index, locator_index, source_index)
        evidence = clean_evidence_excerpt(row[evidence_index])
        locator = row[locator_index]
        if any(re.search(pattern, fact_text, flags=re.IGNORECASE) for pattern in WEAK_CLAIM_PATTERNS):
            failures.append(f"{page}: Reference data row {row_number} uses weak generic fact language")
        repeated = repeated_phrase(fact_text)
        if repeated:
            failures.append(f"{page}: Reference data row {row_number} repeats phrase {repeated!r}")
        failures.extend(scope_failures(page, f"Reference data row {row_number}", fact_text + " " + evidence, related_scope))
        fact_norm = normalize_for_search(supported_fact_text or fact_text)
        evidence_norm = normalize_for_search(evidence)
        if fact_norm in seen_facts:
            failures.append(
                f"{page}: Reference data row {row_number} duplicates the supported fact from row {seen_facts[fact_norm]}"
            )
        elif fact_norm:
            seen_facts[fact_norm] = row_number
        if fact_norm == evidence_norm or SequenceMatcher(None, fact_norm, evidence_norm).ratio() > 0.88:
            failures.append(f"{page}: Reference data row {row_number} fact repeats the evidence instead of synthesizing it")
        if len(re.findall(r"[A-Za-z0-9']+", evidence)) < 4 or len(evidence) < 24:
            failures.append(f"{page}: Reference data row {row_number} evidence excerpt is too short")
        parsed_locator = parse_locator(locator)
        if parsed_locator is None:
            failures.append(
                f"{page}: Reference data row {row_number} locator must look like `normalized:L12` or `normalized:L12-L14`"
            )
            continue
        if evidence_source is None:
            continue
        start, end = parsed_locator
        if start < 1 or end < start or end > len(evidence_source.lines):
            failures.append(f"{page}: Reference data row {row_number} locator {clean_locator(locator)!r} is outside normalized source line range")
            continue
        locator_text = "\n".join(evidence_source.lines[start - 1 : end])
        if normalize_for_search(evidence) not in normalize_for_search(locator_text):
            failures.append(f"{page}: Reference data row {row_number} evidence is not found in locator range {clean_locator(locator)!r}")
        unsupported = sorted(set(content_tokens(fact_text)) - set(content_tokens(evidence + " " + locator_text)))
        if len(unsupported) >= 8:
            failures.append(
                f"{page}: Reference data row {row_number} likely overreaches evidence; unsupported terms: {', '.join(unsupported[:10])}"
            )
    return failures


def scope_failures(page: Path, row_label: str, row_text: str, related_scope: RelatedScope | None) -> list[str]:
    if related_scope is None or page.parts[1] != "references":
        return []
    scope = scope_tokens(related_scope)
    if len(scope) < 3:
        return []
    row = lexical_tokens(row_text)
    if scope & row:
        return []
    return [
        f"{page}: {row_label} appears outside Related-pages scope; expected one of {sorted(scope)[:12]}"
    ]


def scope_tokens(scope: RelatedScope) -> set[str]:
    return lexical_tokens(" ".join(part for part in [scope.title, scope.path, scope.evidence_basis or ""] if part))


def lexical_tokens(text: str) -> set[str]:
    ignored = {
        "aoe2",
        "page",
        "pages",
        "source",
        "sources",
        "reference",
        "references",
        "concept",
        "concepts",
        "procedure",
        "procedures",
        "entity",
        "entities",
        "wiki",
        "common",
        "edge",
        "edges",
        "upgrade",
        "upgrades",
        "fact",
        "facts",
        "supported",
        "guide",
        "basics",
        "noobs",
        "and",
        "or",
    }
    tokens = set(content_tokens(text.replace("-", " ")))
    for raw in re.findall(r"[A-Za-z][A-Za-z0-9']*", text.replace("-", " ").lower()):
        token = raw.strip("'")
        if token.endswith("'s"):
            token = token[:-2]
        if len(token) > 4 and token.endswith("s"):
            token = token[:-1]
        if len(token) >= 3 and token not in ignored and "aoe2" not in token:
            tokens.add(token)
    return {token for token in tokens - ignored if "aoe2" not in token}


def supported_fact_cell_text(
    header: list[str],
    row: list[str],
    evidence_index: int,
    locator_index: int,
    source_index: int | None,
) -> str:
    preferred = {"supported fact", "fact", "claim", "value", "description"}
    ignored = {evidence_index, locator_index}
    if source_index is not None:
        ignored.add(source_index)
    for index, name in enumerate(header):
        if index not in ignored and name in preferred:
            return strip_markdown(row[index]).strip()
    return " ".join(strip_markdown(cell).strip() for index, cell in enumerate(row) if index not in ignored)


def repeated_phrase(text: str) -> str | None:
    words = [word.lower() for word in re.findall(r"[A-Za-z0-9']+", text)]
    if len(words) < 6:
        return None
    for size in range(6, 1, -1):
        counts: dict[tuple[str, ...], int] = {}
        for index in range(0, len(words) - size + 1):
            phrase = tuple(words[index : index + size])
            counts[phrase] = counts.get(phrase, 0) + 1
            if counts[phrase] >= 3:
                return " ".join(phrase)
    comma_parts = [normalize_for_search(part) for part in re.split(r"[,;]", text) if len(content_tokens(part)) >= 2]
    for part in comma_parts:
        if comma_parts.count(part) >= 3:
            return part
    return None


def table_data_row_count(markdown: str) -> int:
    count = 0
    header_seen = False
    for row in table_rows(markdown):
        normalized = [cell.strip().lower() for cell in row]
        if is_separator_row(row):
            continue
        if not header_seen:
            header_seen = True
            continue
        if any(cell for cell in normalized):
            count += 1
    return count


def load_evidence_source(source_path: Path, normalized_source: str | None) -> EvidenceSource | None:
    if normalized_source:
        path = Path(normalized_source)
    else:
        path = normalized_markdown_from_source_page(source_path)
        if path is None:
            return None
    if path.is_file():
        text = path.read_text(errors="ignore")
        return EvidenceSource(lines=text.splitlines())
    if path.is_dir():
        markdown_files = sorted(path.rglob("*.md"), key=lambda candidate: candidate.stat().st_size, reverse=True)
        if markdown_files:
            text = markdown_files[0].read_text(errors="ignore")
            return EvidenceSource(lines=text.splitlines())
    return None


def parse_locator(locator: str) -> tuple[int, int] | None:
    cleaned = clean_locator(locator)
    match = LOCATOR_RE.fullmatch(cleaned)
    if not match:
        return None
    start = int(match.group("start"))
    end = int(match.group("end") or start)
    return start, end


def clean_locator(locator: str) -> str:
    return strip_markdown(locator).strip()


def normalized_markdown_from_source_page(source_path: Path) -> Path | None:
    fm = parse_frontmatter(source_path)
    normalized_path = fm.data.get("normalized_path")
    if not isinstance(normalized_path, str):
        return None
    return (source_path.parent / normalized_path).resolve()


def line_number_of_heading(text: str, heading: str) -> int:
    for i, line in enumerate(text.splitlines(), start=1):
        if line.strip() == heading:
            return i
    return 0


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def table_rows(markdown: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in markdown.splitlines():
        row = split_table_row(line)
        if row is not None:
            rows.append(row)
    return rows


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def code_cell_target(cell: str) -> str | None:
    match = re.fullmatch(r"`([^`]+\.md)`", cell.strip())
    return match.group(1) if match else None


def link_cell_target(cell: str) -> str | None:
    match = re.fullmatch(r"\[([^\]]+)\]\(([^)]+\.md)\)", cell.strip())
    return match.group(2) if match else None


def first_markdown_target(text: str) -> str | None:
    match = re.search(r"\[[^\]]+\]\(([^)]+\.md)\)", text)
    return match.group(1) if match else None


def clean_evidence_excerpt(text: str) -> str:
    cleaned = text.strip().replace('\\"', '"')
    while (cleaned.startswith('"') and cleaned.endswith('"')) or (cleaned.startswith("'") and cleaned.endswith("'")):
        cleaned = cleaned[1:-1].strip()
    return " ".join(cleaned.split())


def strip_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("`", "").replace("*", "").replace("_", "")


def normalize_for_search(text: str) -> str:
    replacements = {
        "\u00a0": " ",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2015": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return " ".join(text.lower().split())


if __name__ == "__main__":
    sys.exit(main())
