#!/usr/bin/env python3
"""Cloud-native wiki ingest using model backend abstraction.

This is a simplified ingest pipeline that works with cloud backends
(Bedrock, OpenAI, Anthropic) without requiring local Codex.

Usage:
    pnpm wiki:ingest:cloud raw/inbox/example.pdf --slug example
    pnpm wiki:ingest:cloud --slug example --skip-phase0  # Resume from Phase 1
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import log_context_stats, parse_frontmatter, section
from wiki_model_backend import get_backend, ModelConfig, ModelResponse


@dataclass
class IngestState:
    """Track ingest progress."""
    slug: str
    source_path: Path | None
    normalized_source: Path | None
    source_page: Path | None
    synthesized_pages: list[Path]
    backend_name: str
    timeout: int
    max_phase2_pages: int


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cloud-native wiki ingest pipeline")
    parser.add_argument("source", nargs="?",
                        help="source file under raw/inbox/")
    parser.add_argument("--slug", required=True, help="source slug")
    parser.add_argument(
        "--backend", default=os.environ.get("WIKI_MODEL_BACKEND", "bedrock"))
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--max-phase2-pages", type=int, default=5)
    parser.add_argument("--skip-phase0", action="store_true")
    parser.add_argument("--skip-phase1", action="store_true")
    parser.add_argument("--skip-phase2", action="store_true")
    parser.add_argument("--skip-phase3", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--reuse-imported", action="store_true")
    parser.add_argument("--overwrite-normalized", action="store_true")
    args = parser.parse_args()

    state = IngestState(
        slug=args.slug,
        source_path=Path(args.source) if args.source else None,
        normalized_source=None,
        source_page=None,
        synthesized_pages=[],
        backend_name=args.backend,
        timeout=args.timeout,
        max_phase2_pages=args.max_phase2_pages,
    )

    # Phase 0: Normalize
    if not args.skip_phase0:
        if not state.source_path:
            print("FAIL: source required for Phase 0", file=sys.stderr)
            return 2
        print(f"\n{'='*60}")
        print("PHASE 0: Normalize PDF")
        print(f"{'='*60}")
        if args.dry_run:
            print(f"[dry-run] Would normalize {state.source_path}")
        else:
            code = run_phase0(state, args.reuse_imported,
                              args.overwrite_normalized)
            if code != 0:
                return code

    # Find normalized source
    state.normalized_source = find_normalized_source(state.slug)
    if not state.normalized_source:
        print(
            f"FAIL: no normalized source found for {state.slug}", file=sys.stderr)
        return 2
    print(f"Normalized source: {state.normalized_source}")

    # Phase 1: Create source page
    if not args.skip_phase1:
        print(f"\n{'='*60}")
        print("PHASE 1: Create Source Page")
        print(f"{'='*60}")
        if args.dry_run:
            print(f"[dry-run] Would create wiki/sources/{state.slug}.md")
        else:
            code = run_phase1(state)
            if code != 0:
                return code

    # Verify source page exists
    state.source_page = Path(f"wiki/sources/{state.slug}.md")
    if not state.source_page.exists():
        print(
            f"FAIL: source page does not exist: {state.source_page}", file=sys.stderr)
        return 2

    # Phase 2: Synthesize pages
    if not args.skip_phase2:
        print(f"\n{'='*60}")
        print("PHASE 2: Synthesize Pages")
        print(f"{'='*60}")
        if args.dry_run:
            print(
                f"[dry-run] Would synthesize up to {args.max_phase2_pages} pages")
        else:
            code = run_phase2(state)
            if code != 0:
                return code

    # Phase 3: Finalize
    if not args.skip_phase3:
        print(f"\n{'='*60}")
        print("PHASE 3: Finalize")
        print(f"{'='*60}")
        if args.dry_run:
            print("[dry-run] Would update index, graph, and log")
        else:
            code = run_phase3(state)
            if code != 0:
                return code

    print(f"\n{'='*60}")
    print("INGEST COMPLETE")
    print(f"{'='*60}")
    print(f"Source page: {state.source_page}")
    print(f"Synthesized pages: {len(state.synthesized_pages)}")
    return 0


def run_phase0(state: IngestState, reuse_imported: bool, overwrite_normalized: bool) -> int:
    """Run Phase 0: PDF normalization."""
    import subprocess

    cmd = ["python3", "tools/wiki_phase0_import.py",
           str(state.source_path), state.slug]
    if reuse_imported:
        cmd.append("--reuse-imported")
    if overwrite_normalized:
        cmd.append("--overwrite-normalized")

    result = subprocess.run(cmd)
    return result.returncode


def find_normalized_source(slug: str) -> Path | None:
    """Find the normalized source markdown file."""
    normalized_dir = Path(f"raw/normalized/{slug}")
    if not normalized_dir.exists():
        return None

    # Look for source.md first
    source_md = normalized_dir / "source.md"
    if source_md.exists():
        return source_md

    # Fall back to any .md file
    md_files = list(normalized_dir.glob("*.md"))
    if md_files:
        return md_files[0]

    return None


def run_phase1(state: IngestState) -> int:
    """Run Phase 1: Create source page using cloud backend."""
    print(f"Using backend: {state.backend_name}")

    try:
        backend = get_backend(state.backend_name)
    except Exception as e:
        print(f"FAIL: could not initialize backend: {e}", file=sys.stderr)
        return 1

    # Read normalized source and extract outline
    source_text = state.normalized_source.read_text()
    source_lines = len(source_text.splitlines())
    print(f"Source: {source_lines} lines, {len(source_text):,} chars")

    # Extract outline for context efficiency
    outline = extract_outline(source_text)
    print(f"Outline: {len(outline.splitlines())} headings/markers")

    # Sample content from different sections
    samples = extract_samples(source_text, max_samples=10, sample_lines=30)
    samples_text = "\n\n---\n\n".join(samples)

    # Build prompt
    prompt = build_phase1_prompt(
        state.slug, outline, samples_text, source_lines)
    log_context_stats(prompt, label="Phase 1 prompt")

    # Run model
    print("Generating source page...")
    config = ModelConfig(
        worktree=Path.cwd(),
        prefix="phase1",
        timeout=state.timeout,
    )

    response = backend.run(prompt, config)
    if not response.success:
        print(f"FAIL: model error: {response.error}", file=sys.stderr)
        return 1

    if response.truncated:
        print("WARNING: Model output was truncated - page may be incomplete")

    # Parse and save source page
    source_page_content = extract_markdown_from_response(response.output)
    if not source_page_content:
        print("FAIL: model did not produce valid markdown", file=sys.stderr)
        print("Response preview:", response.output[:500])
        return 1

    # Post-process to fix common issues
    source_page_content = postprocess_source_page(
        source_page_content, state.slug)

    # Save source page
    source_page_path = Path(f"wiki/sources/{state.slug}.md")
    source_page_path.parent.mkdir(parents=True, exist_ok=True)
    source_page_path.write_text(source_page_content)
    print(f"Created: {source_page_path}")

    # Validate
    return validate_source_page(state.slug)


def extract_outline(source_text: str) -> str:
    """Extract headings and page markers from source."""
    lines = []
    for i, line in enumerate(source_text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith('#'):
            lines.append(f"L{i}: {stripped}")
        elif '<!-- page' in stripped.lower():
            lines.append(f"L{i}: {stripped}")
    return "\n".join(lines)


def extract_samples(source_text: str, max_samples: int = 10, sample_lines: int = 30) -> list[str]:
    """Extract representative samples from different parts of the source."""
    lines = source_text.splitlines()
    total_lines = len(lines)

    if total_lines <= sample_lines * max_samples:
        # Source is small enough to include entirely
        return [source_text]

    samples = []
    # Sample evenly distributed sections
    step = total_lines // max_samples

    for i in range(max_samples):
        start = i * step
        end = min(start + sample_lines, total_lines)
        sample = "\n".join(lines[start:end])
        samples.append(f"[Lines {start+1}-{end}]\n{sample}")

    return samples


def build_phase1_prompt(slug: str, outline: str, samples: str, total_lines: int) -> str:
    """Build the Phase 1 source page generation prompt."""
    today = date.today().isoformat()

    return f"""You are creating a source page for the LLM-Wiki.

TASK: Create wiki/sources/{slug}.md

SOURCE OVERVIEW:
- Slug: {slug}
- Total lines: {total_lines}
- Normalized path: raw/normalized/{slug}/source.md
- Imported original: ../../raw/imported/{slug}/original.pdf

OUTLINE (headings and page markers):
{outline}

CONTENT SAMPLES:
{samples}

CRITICAL TABLE FORMAT RULES:
- Key claims table MUST have exactly 3 columns: | Claim | Evidence | Locator |
- NEVER use || or && in evidence cells - write "OR" or "AND" instead to avoid breaking table parsing
- Natural groupings table MUST have exactly 4 columns: | Group | Scope | Evidence basis | Candidate page types |
- Candidate page types MUST ONLY be: concept, entity, procedure, reference (NOT analysis)
- Related pages table MUST have exactly 6 columns: | Candidate page | Intended path | Group | Priority | Evidence basis | Status |
- Group names in Related pages MUST match exactly a group name from Natural groupings
- Every row must have the same number of pipe characters

REQUIREMENTS:
1. Create a source page with this EXACT structure:

```markdown
---
title: <Descriptive title based on content>
type: source
source_id: {slug}
source_type: pdf
raw_path: ../../raw/imported/{slug}/
normalized_path: ../../raw/normalized/{slug}/
status: draft
last_updated: {today}
tags: []
sources: []
---

# <Title>

## Summary

<2-3 paragraph summary of the source content>

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| <Concrete reusable claim> | "<Short exact excerpt>" | `normalized:L<line>` |

## Major concepts

<List the major concepts/topics covered>

### Natural groupings

| Group | Scope | Evidence basis | Candidate page types |
|---|---|---|---|
| <Group name> | <Scope description> | <Concrete sections or claims> | concept |

## Entities

<List named entities: people, libraries, tools, etc. or write "None.">

## Procedures

<List any step-by-step procedures or write "None.">

## References

<List any reference material or write "None.">

## Open questions

<List any gaps or unclear areas or write "None.">

## Related pages

| Candidate page | Intended path | Group | Priority | Evidence basis | Status |
|---|---|---|---|---|---|
| <Page title> | `../concepts/<slug>.md` | <EXACT group name from above> | must create | <Evidence> | not created yet |
```

2. Key claims MUST have:
   - Concrete, reusable claims (not vague statements)
   - Exact quotes from the source as evidence in double quotes
   - Line number locators like `normalized:L123`
   - Exactly 3 columns per row

3. Include 8-15 key claims covering the main ideas

4. Natural groupings:
   - 4-6 groups based on the source's structure
   - Each row MUST have exactly 4 columns
   - Candidate page types: ONLY concept, entity, procedure, or reference

5. Related pages:
   - 6-8 candidate synthesized pages (keep it concise)
   - Each row MUST have exactly 6 columns
   - Group column MUST match a group name from Natural groupings exactly
   - Keep evidence basis short (under 20 words)

OUTPUT: Produce ONLY the markdown content for the source page. No explanations or preamble."""


def extract_markdown_from_response(response: str) -> str | None:
    """Extract markdown content from model response."""
    if not response:
        return None

    # Try to find fenced code block with markdown
    match = re.search(r'```(?:markdown|md)?\s*\n(.*?)```', response, re.DOTALL)
    if match:
        content = match.group(1).strip()
        if content and '---' in content:
            return content

    # Try to find YAML frontmatter start
    if response.strip().startswith('---'):
        return response.strip()

    # Look for frontmatter anywhere in response
    match = re.search(r'(---\n.*?---\n.*)', response, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fall back to looking for # heading
    match = re.search(r'(# [^\n]+\n.*)', response, re.DOTALL)
    if match:
        return match.group(1).strip()

    # If all else fails, return the raw response if it's substantial
    if len(response) > 200:
        return response.strip()

    return None


def postprocess_source_page(content: str, slug: str) -> str:
    """Fix common issues in generated source pages."""
    # Fix the sources: [] to include original.pdf for PDF sources
    original_pdf = f"../../raw/imported/{slug}/original.pdf"

    # Replace empty sources list with one containing original.pdf
    content = re.sub(
        r'sources:\s*\[\]',
        f'sources:\n  - {original_pdf}',
        content
    )

    # Also handle if sources is a list but doesn't have original.pdf
    if 'sources:' in content and original_pdf not in content:
        # Find and update the sources section
        content = re.sub(
            r'sources:\s*\n(\s+-.*\n)*',
            f'sources:\n  - {original_pdf}\n',
            content
        )

    # Fix pipe characters in table evidence cells
    # This handles || and && which get parsed as table delimiters
    content = fix_table_pipes(content)

    return content


def fix_table_pipes(content: str) -> str:
    """Fix pipe characters in markdown table cells that break parsing."""
    lines = content.splitlines()
    result = []
    in_table = False
    expected_cols = 0

    for line in lines:
        if '|' in line and line.strip().startswith('|'):
            # This is a table row
            if not in_table:
                in_table = True
                # Count columns from header
                expected_cols = line.count('|')

            actual_cols = line.count('|')
            if actual_cols > expected_cols and expected_cols > 0:
                # Too many pipes - need to escape some
                # Find evidence cells (usually contain || or &&)
                line = escape_inner_pipes(line, expected_cols)
        else:
            if in_table and line.strip() and not line.strip().startswith('|'):
                in_table = False
                expected_cols = 0

        result.append(line)

    return '\n'.join(result)


def escape_inner_pipes(line: str, expected_cols: int) -> str:
    """Escape pipe characters inside table cells."""
    # Split by | but keep track of positions
    parts = line.split('|')

    if len(parts) <= expected_cols:
        return line  # Already correct

    # Replace || with "OR" and && with "AND" in table cells
    # These operators break markdown tables
    line = re.sub(r'\|\|', ' OR ', line)
    line = re.sub(r'&&', ' AND ', line)

    return line


def validate_source_page(slug: str) -> int:
    """Run deterministic validation on the source page."""
    import subprocess

    result = subprocess.run(
        ["python3", "tools/wiki_check_source.py", slug],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("Source page validation issues:")
        print(result.stdout)
        print(result.stderr)
        # Don't fail on validation - just warn
        print("WARNING: Source page has validation issues (continuing anyway)")
    else:
        print("Source page validation: PASS")

    return 0  # Continue even with warnings


def run_phase2(state: IngestState) -> int:
    """Run Phase 2: Synthesize concept/entity/procedure/reference pages."""
    # Get candidates from source page
    candidates = get_phase2_candidates(state.source_page)
    if not candidates:
        print("No Phase 2 candidates found in source page")
        return 0

    print(
        f"Found {len(candidates)} candidates, processing up to {state.max_phase2_pages}")

    try:
        backend = get_backend(state.backend_name)
    except Exception as e:
        print(f"FAIL: could not initialize backend: {e}", file=sys.stderr)
        return 1

    source_text = state.normalized_source.read_text()

    for i, candidate in enumerate(candidates[:state.max_phase2_pages]):
        print(
            f"\n[{i+1}/{min(len(candidates), state.max_phase2_pages)}] {candidate['title']}")

        page_path = synthesize_page(backend, state, candidate, source_text)
        if page_path:
            state.synthesized_pages.append(page_path)
            print(f"  Created: {page_path}")

            # Post-process the synthesized page
            postprocess_synthesized_page(page_path, state.normalized_source)
        else:
            print(f"  WARN: Failed to create page")

    # Update source page to link to created pages
    if state.synthesized_pages:
        update_source_page_links(state.source_page, state.synthesized_pages)

    return 0


def postprocess_synthesized_page(page_path: Path, normalized_source: Path) -> None:
    """Fix common issues in synthesized pages."""
    content = page_path.read_text()
    original = content

    # Normalize ASCII characters
    content = normalize_ascii(content)

    # Fix table pipes
    content = fix_table_pipes(content)

    # Fix locator format - convert single quotes to backticks
    # 'normalized:L123' -> `normalized:L123`
    content = re.sub(r"'(normalized:L\d+(?:-L\d+)?)'", r'`\1`', content)

    # Remove empty sections
    content = remove_empty_sections(content)

    if content != original:
        page_path.write_text(content)
        print(f"  Post-processed: fixed formatting issues")


def remove_empty_sections(text: str) -> str:
    """Remove sections with no content."""
    lines = text.splitlines()
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('## ') and i + 1 < len(lines):
            # Check if next line is empty or another heading
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ''
            next_next = lines[i + 2].strip() if i + 2 < len(lines) else ''

            # Skip empty sections (## Heading followed by blank line and another ##)
            if (not next_line or next_line.startswith('##')) or \
               (not next_line and (not next_next or next_next.startswith('##'))):
                i += 1  # Skip this heading
                while i < len(lines) and not lines[i].strip():
                    i += 1
                continue

        result.append(line)
        i += 1

    return '\n'.join(result)


def normalize_ascii(text: str) -> str:
    """Replace common non-ASCII characters with ASCII equivalents."""
    replacements = {
        '"': '"', '"': '"',  # Smart quotes
        ''': "'", ''': "'",  # Smart apostrophes
        '`': "'",  # Backticks (when used as apostrophes)
        '—': '--', '–': '-',  # Dashes
        '…': '...',  # Ellipsis
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',  # Accented e
        'à': 'a', 'â': 'a', 'á': 'a', 'ä': 'a',  # Accented a
        'ù': 'u', 'û': 'u', 'ú': 'u', 'ü': 'u',  # Accented u
        'î': 'i', 'ï': 'i', 'í': 'i', 'ì': 'i',  # Accented i
        'ô': 'o', 'ö': 'o', 'ó': 'o', 'ò': 'o',  # Accented o
        '×': 'x',  # Multiplication
        '→': '->',  # Arrow
        '←': '<-',  # Arrow
        '≈': '~=',  # Approximately
        '≠': '!=',  # Not equal
        '≤': '<=', '≥': '>=',  # Comparisons
        '•': '-',  # Bullet
        '©': '(c)', '®': '(R)', '™': '(TM)',  # Symbols
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def update_source_page_links(source_page: Path, created_pages: list[Path]) -> None:
    """Update source page to link to created synthesized pages."""
    content = source_page.read_text()

    for page_path in created_pages:
        # Convert page path to relative path from source page
        page_name = page_path.stem
        page_type = page_path.parent.name
        rel_path = f"../{page_type}/{page_name}.md"

        # Convert candidate reference to markdown link
        # Pattern: `../concepts/foo.md` | ... | not created yet
        # To: [../concepts/foo.md](../concepts/foo.md) | ... | created
        old_pattern = f'`{rel_path}`'
        new_link = f'[{rel_path}]({rel_path})'
        content = content.replace(old_pattern, new_link)

        # Also update status column
        content = re.sub(
            rf'{re.escape(new_link)}([^|]*\|[^|]*\|[^|]*\|[^|]*\|)\s*not created yet',
            f'{new_link}\\1 created',
            content
        )

    source_page.write_text(content)


def get_phase2_candidates(source_page: Path) -> list[dict]:
    """Extract candidate pages from source page's Related pages section."""
    content = source_page.read_text()
    related_section = section(content, "## Related pages")

    if not related_section:
        return []

    candidates = []
    # Parse table rows
    for line in related_section.splitlines():
        if '|' not in line or line.strip().startswith('|---'):
            continue

        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 5:
            # | Title | Path | Group | Priority | Evidence | Status |
            title = parts[1] if len(parts) > 1 else ""
            path = parts[2] if len(parts) > 2 else ""
            group = parts[3] if len(parts) > 3 else ""
            priority = parts[4] if len(parts) > 4 else ""
            evidence = parts[5] if len(parts) > 5 else ""

            # Extract path from backticks or markdown link
            path_match = re.search(r'`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)', path)
            if path_match:
                actual_path = path_match.group(1) or path_match.group(3)
                if actual_path and 'not created' not in line.lower():
                    continue  # Skip already created
                if actual_path:
                    candidates.append({
                        'title': title,
                        'path': actual_path,
                        'group': group,
                        'priority': priority,
                        'evidence': evidence,
                    })

    # Sort by priority
    priority_order = {'must create': 0,
                      'should create': 1, 'could create': 2, 'defer': 3}
    candidates.sort(key=lambda c: priority_order.get(
        c.get('priority', '').lower(), 99))

    return candidates


def synthesize_page(backend, state: IngestState, candidate: dict, source_text: str) -> Path | None:
    """Synthesize a single concept/entity/procedure/reference page."""
    # Determine page type from path
    path_str = candidate['path']
    if '../concepts/' in path_str:
        page_type = 'concept'
    elif '../entities/' in path_str:
        page_type = 'entity'
    elif '../procedures/' in path_str:
        page_type = 'procedure'
    elif '../references/' in path_str:
        page_type = 'reference'
    else:
        page_type = 'concept'  # Default

    # Build path
    page_slug = Path(path_str).stem
    page_path = Path(f"wiki/{page_type}s/{page_slug}.md")

    if page_path.exists():
        print(f"  Skipping (exists): {page_path}")
        return page_path

    # Extract relevant evidence from source
    relevant_lines = find_relevant_lines(
        source_text, candidate['title'], candidate.get('evidence', ''))

    prompt = build_phase2_prompt(
        state.slug,
        candidate['title'],
        page_type,
        page_slug,
        candidate.get('group', ''),
        relevant_lines,
    )
    log_context_stats(prompt, label=f"Phase 2 prompt ({candidate['title']})")

    config = ModelConfig(
        worktree=Path.cwd(),
        prefix=f"phase2-{page_slug}",
        timeout=state.timeout,
    )

    response = backend.run(prompt, config)
    if not response.success:
        print(f"  Model error: {response.error}")
        return None

    # Debug: show response length
    print(f"  Response: {len(response.output)} chars")

    content = extract_markdown_from_response(response.output)
    if not content:
        print(f"  No valid markdown in response")
        print(f"  First 500 chars: {response.output[:500]}")
        return None

    # Debug: show extracted content length
    print(f"  Extracted: {len(content)} chars")

    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(content)
    return page_path


def find_relevant_lines(source_text: str, title: str, evidence_hint: str) -> str:
    """Find lines relevant to the topic using simple keyword matching."""
    keywords = set()
    for word in (title + " " + evidence_hint).lower().split():
        if len(word) > 3:
            keywords.add(word)

    relevant = []
    lines = source_text.splitlines()

    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(kw in line_lower for kw in keywords):
            # Include context
            start = max(0, i - 2)
            end = min(len(lines), i + 3)
            context = "\n".join(
                f"L{start+j+1}: {lines[start+j]}" for j in range(end - start))
            relevant.append(context)

            if len(relevant) >= 20:  # Limit context
                break

    return "\n\n".join(relevant) if relevant else "[No specific lines matched]"


def build_phase2_prompt(slug: str, title: str, page_type: str, page_slug: str, group: str, relevant_lines: str) -> str:
    """Build prompt for synthesizing a page."""
    today = date.today().isoformat()

    type_guidance = {
        'concept': "Explain the concept clearly. Include definition, why it matters, examples, and common mistakes.",
        'entity': "Describe the entity (person, tool, library, etc.). Include key facts and relationships.",
        'procedure': "Document the step-by-step process. Include prerequisites, steps (at least 3), and expected outcomes.",
        'reference': "Create a reference table or lookup resource. Include structured data with evidence.",
    }

    return f"""Create a {page_type} page for the LLM-Wiki.

TASK: Create wiki/{page_type}s/{page_slug}.md

TOPIC: {title}
GROUP: {group}
SOURCE: {slug}

RELEVANT SOURCE CONTENT:
{relevant_lines}

{type_guidance.get(page_type, '')}

REQUIREMENTS:
1. Use this structure:

```markdown
---
title: {title}
type: {page_type}
tags: []
status: draft
last_updated: {today}
sources:
  - ../sources/{slug}.md
---

# {title}

<Brief definition or summary>

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| <Claim> | "<Exact quote>" | `normalized:L<line>` | [Source](../sources/{slug}.md) |

## Why it matters

<Explain significance>

## Source pages

- [Source title](../sources/{slug}.md)
```

2. Every claim must have:
   - Concrete statement in your own words
   - Exact quote from source as evidence (use quotes from RELEVANT SOURCE CONTENT above)
   - Line number locator - USE THE LINE NUMBERS PROVIDED (L5609, L389, etc.)

3. Include 3-8 evidence-backed claims

4. IMPORTANT:
   - Do NOT include empty sections or sections with no content
   - Do NOT include "## Examples" unless you have actual examples
   - Always end with "## Source pages" linking back to the source
   - Use ASCII characters only (no smart quotes)

OUTPUT: Produce ONLY the markdown content. No explanations."""


def run_phase3(state: IngestState) -> int:
    """Run Phase 3: Update index, graph, and log."""
    import subprocess

    # Update index
    print("Updating index...")
    subprocess.run(["python3", "tools/wiki_index.py"])

    # Update graph
    print("Updating graph...")
    subprocess.run(["python3", "tools/wiki_graph.py"])

    # Add log entry
    print("Adding log entry...")
    details = [
        f"Source: {state.slug}",
        f"Backend: {state.backend_name}",
        f"Synthesized pages: {len(state.synthesized_pages)}",
    ]
    cmd = ["python3", "tools/wiki_log.py",
           "ingest", f"Cloud ingest of {state.slug}"]
    for d in details:
        cmd.extend(["--detail", d])
    subprocess.run(cmd)

    return 0


if __name__ == "__main__":
    sys.exit(main())
