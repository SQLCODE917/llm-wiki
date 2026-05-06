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

Locators available (evidence will be filled automatically):

{{evidence_bank}}

CRITICAL FORMAT REQUIREMENTS:

1. **Write claims, NOT evidence**: You write a **3-column table**. Evidence cells are filled automatically by deterministic post-processing. Do NOT write evidence text.

   ```md
   | Claim | Locator | Source |
   | ----- | ------- | ------ |
   | Your synthesized insight in your own words. | `normalized:L123` | [Source](../sources/{{slug}}.md) |
   ```

2. **Synthesize claims**: Claims must be YOUR interpretation of what the source teaches. Do not copy source text into claims.

   BAD: `| JavaScript uses function declarations to bind... |` (copying source)
   GOOD: `| Function declarations create named bindings in scope. |` (your synthesis)

3. **Use exact locators**: Copy locators exactly as provided in the evidence bank. Use `normalized:L123` format.

4. **Complete frontmatter**: Every synthesized page MUST have this exact structure:

   ```yaml
   ---
   title: Page Title
   type: concept
   tags: []
   status: draft
   last_updated: {{current_date}}
   sources:
     - ../sources/{{slug}}.md
   source_ranges:
     - {{slug}}:normalized:L787
     - {{slug}}:normalized:L937
   ---
   ```

   List EVERY line number you cite as a separate source_ranges entry.

5. **Required sections**: Every synthesized page MUST have:
   - `## Source-backed details` with 3-column evidence table
   - `## Source pages` with link to ../sources/{{slug}}.md

Additional rules:

- Use only locators inside each selected page's allowed source range when one is shown.
- Do not create pages for any other candidate rows.
- Do not create backup files.
- After this run, the source should have {{expected_total_pages}} synthesized pages total.
- Prefer small, specific pages over broad duplicates.
- Each synthesized page must be one of: concept, entity, procedure, reference.
- Each synthesized page must include YAML frontmatter, an H1, a short definition, `## Source-backed details`, and `## Source pages`.
- `## Source-backed details` must contain a **3-column** Markdown table:

```md
| Claim | Locator | Source |
| ----- | ------- | ------ |
| Concrete reusable insight in your own words. | `normalized:L12` | [Source title](../sources/{{slug}}.md) |
```

- Include at least 3 rows per synthesized page.
- Use locators from the evidence bank provided above.
- Do NOT write an Evidence column - it is filled automatically from locators.
- Do not make a claim just because it sounds appropriate for the page title; every claim must be directly supported by its own Evidence cell.
- If the evidence bank does not contain exact support for a likely-sounding claim, omit that claim.
- Locator cells must use `normalized:L12` or `normalized:L12-L14` from the evidence bank, and the evidence excerpt must appear inside that cited line range.
- Do not put pipe characters inside table cells.
- Evidence table data rows must start with `|`, not `+`, `-`, or diff-marker text.
- The claim cell must synthesize in your own words; do not copy the evidence sentence into the claim cell.
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
- Cross-links may point only to pages that already exist or pages created in this phase. Do not Markdown-link to candidate pages that remain uncreated.
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
