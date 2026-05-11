Read `AGENTS.md` fully before acting.

You are performing LLM-Wiki ingest Phase 2 only: synthesized pages from an existing source page.

Current date: {{current_date}}
Source slug: `{{slug}}`
Source page to read and update: `wiki/sources/{{slug}}.md`
Normalized source to consult if needed: `{{normalized_source}}`

Allowed writes:

- `wiki/sources/{{slug}}.md`
- `wiki/concepts/**`
- `wiki/entities/**`
- `wiki/procedures/**`
- `wiki/references/**`

Forbidden writes:

- `raw/imported/**`
- `raw/normalized/**`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_graph.json`
- `wiki/_linter-report.md`
- `wiki/_claim-judge-report.md`
- `wiki/_grounding-report.md`
- `wiki/analyses/**`
- `packages/**`
- `tools/**`
- backup files such as `*.bak`, `*.orig`, `*.tmp`, or `*~`

Do not update index, graph, or log. This is Phase 2 only.

Task:

- Existing synthesized pages for this source that should remain linked:

{{existing_pages}}

- Create or update exactly these {{selected_count}} selected synthesized pages in this run and no others:

{{selected_candidates}}

Evidence bank (cite by ID):

{{evidence_bank}}

CRITICAL FORMAT REQUIREMENTS:

1. **Cite evidence by ID**: You write a **2-column table**. Cite evidence by ID (e.g., `[E01]`). The full table with evidence text, locators, and source links is rendered automatically.

   ```md
   | Claim                                       | Evidence |
   | ------------------------------------------- | -------- |
   | Your synthesized insight in your own words. | [E01]    |
   | Another insight you synthesized.            | [E02]    |
   ```

2. **Synthesize claims**: Claims must be YOUR interpretation of what the source teaches. Do not copy the evidence text into claims.

   BAD: `| JavaScript uses function declarations to bind... |` (copying evidence)
   GOOD: `| Function declarations create named bindings in scope. |` (your synthesis)

3. **Use evidence IDs exactly**: Copy the ID from the evidence bank exactly as shown (e.g., `[E01]`, `[E07]`).

4. **Complete frontmatter**: Every synthesized page MUST have this exact structure:

   ```yaml
   ---
   title: Page Title
   type: concept
   tags: []
   status: draft
   last_updated: { { current_date } }
   sources:
     - ../sources/{{slug}}.md
   ---
   ```

5. **Required sections**: Every synthesized page MUST have:
   - `## Source-backed details` with 2-column evidence table
   - `## Source pages` with link to ../sources/{{slug}}.md

Additional rules:

- Only cite evidence IDs shown in the evidence bank for your page's topic.
- Do not create pages for any other candidate rows.
- Do not create backup files.
- After this run, the source should have {{expected_total_pages}} synthesized pages total.
- Prefer small, specific pages over broad duplicates.
- Each synthesized page must be one of: concept, entity, procedure, reference.
- Each synthesized page must include YAML frontmatter, an H1, a short definition, `## Source-backed details`, and `## Source pages`.
- `## Source-backed details` must contain a **2-column** Markdown table:

```md
| Claim                                        | Evidence |
| -------------------------------------------- | -------- |
| Concrete reusable insight in your own words. | [E01]    |
```

- Include at least 3 rows per synthesized page.
- Only use evidence IDs from the evidence bank provided above.
- Do NOT write evidence text, locators, or source links - they are filled automatically.
- Do not make a claim just because it sounds appropriate for the page title; every claim must cite a specific evidence ID.
- If the evidence bank does not contain support for a likely-sounding claim, omit that claim.
- Locator cells must use range format `normalized:L<start>-L<end>` from the evidence bank (single line: `L123-L123`).
- Do not put pipe characters inside table cells.
- Evidence table data rows must start with `|`, not `+`, `-`, or diff-marker text.
- The claim cell must synthesize in your own words; do not copy the evidence sentence into the claim cell.
- SYNTHESIS means expressing the SAME MEANING as the evidence using DIFFERENT WORDS. Example:
  - Evidence: "Linear recursion is a basic building block of algorithms."
  - BAD claim (copies): "Linear recursion is a basic building block of algorithms."
  - BAD claim (adds facts): "Linear recursion is a pattern where functions repeatedly call themselves."
  - GOOD claim: "Linear recursion serves as a core component for constructing algorithms."
- CONSERVATIVE CLAIMS: Each claim must be fully entailed by the cited evidence. Do NOT add details, qualifications, or explanations not present in the evidence.
- Claim cells must not use weak generic words: important, crucial, fundamental, essential, success.
- The evidence cell must quote the source text exactly.
- Do not add empty headings.
- Do not duplicate headings.
- Do not add `## Executable implementation` unless a real implementation file exists and is linked.
- Procedure pages must include `## Steps` with at least 3 concrete numbered or bulleted steps.
- Procedure steps must be traceable to the page's own evidence rows; do not add generic how-to advice from outside the cited excerpts.
- Reference pages must include `## Reference data` with a Markdown lookup table containing at least 2 data rows.
- Reference data tables must include `Evidence` and `Locator` columns, and those cells must follow the same exact-quote and normalized-line rules as `## Source-backed details`.
- Use bullets or short paragraphs under `## Source-backed details`; make the section substantial enough to preserve reusable source knowledge.
- Cross-links may point only to pages that already exist or pages created in this phase.
- Synthesized pages must use TWO separate sections for page references:
  - `## Related pages` — Only Markdown links to pages that exist. Example: `- [Functions](../concepts/functions.md)`
  - `## Candidate pages` — Plain text names (no links) for concepts worth exploring later. Example: `- Scope`
- Do NOT use phrases like "(not created yet)" or similar annotations. If a page doesn't exist, put its name in `## Candidate pages` without a link.
- Each synthesized page frontmatter `sources` must include a relative link to `../sources/{{slug}}.md` or equivalent correct relative path.
- Each synthesized page body must include a Markdown link back to `wiki/sources/{{slug}}.md` using a relative path.
- Each synthesized page must include a `## Source pages` section.
- Keep `wiki/sources/{{slug}}.md` `## Related pages` in this exact table shape:

```md
| Page title | [../concepts/example.md](../concepts/example.md) | Source-native group name | must create | concrete evidence basis | created |
| Page title | `../concepts/example.md` | Source-native group name | should create | concrete evidence basis | not created yet |
```

- Replace only the candidate rows whose pages you actually created.
- Do not use placeholder text such as `Page title`; keep the real page titles in the first column.
- Keep not-yet-created candidate pages as code-formatted paths.
- Preserve any Group, Priority, and Evidence basis cells already present in `## Related pages`.

After writing, run exactly:

```bash
python3 tools/wiki_link_related.py {{slug}}
python3 tools/wiki_fix_broken_links.py {{slug}}
python3 tools/wiki_normalize_ascii.py {{slug}}
python3 tools/wiki_normalize_tables.py {{slug}}
python3 tools/wiki_check_synthesis.py {{slug}} --min-pages {{expected_total_pages}} --max-pages {{expected_total_pages}}{{allowed_page_args}} --require-allowed-pages --normalized-source {{normalized_source}}{{range_page_args}}
pnpm wiki:grounding:check
```

If validation fails, repair only the allowed files and rerun the same commands.

Stop only when all validation commands pass, or when you cannot proceed. If you cannot proceed, report the exact failing validation output.
