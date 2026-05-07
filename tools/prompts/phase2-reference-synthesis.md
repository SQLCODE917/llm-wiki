Read `AGENTS.md` fully before acting.

You are performing LLM-Wiki ingest Phase 2 only: create or update exactly one synthesized reference page from an existing source page.

Current date: {{current_date}}
Source slug: `{{slug}}`
Source page to read and update: `wiki/sources/{{slug}}.md`
Normalized source to consult: `{{normalized_source}}`

Allowed writes:

- `wiki/sources/{{slug}}.md`
- the single selected reference page listed below

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
- `wiki/concepts/**`
- `wiki/entities/**`
- `wiki/procedures/**`
- `packages/**`
- `tools/**`
- any synthesized page other than the selected reference page
- backup files such as `*.bak`, `*.orig`, `*.tmp`, or `*~`

Do not update index, graph, or log. This is Phase 2 only.

Task:

- Existing synthesized pages for this source that should remain linked:

{{existing_pages}}

- Create or update exactly this selected page in this run and no others:

{{selected_candidates}}

Locators available (evidence will be filled automatically):

{{evidence_bank}}

- Use only locators inside the selected page's allowed source range when one is shown.
- `source_ranges` values must look like `{{slug}}:normalized:L<start>-L<end>` (single line: `L123-L123`).
- Do not use locators from unrelated sections.

Reference-page rules:

- The selected page must have `type: reference`.
- The page should contain reusable lookup facts, not advice invented from general game knowledge.
- Do not infer item categories, priority tiers, formulas, timings, costs, or upgrade names that the evidence does not state.
- If there are not at least 2 source-backed lookup rows, stop and report that the candidate lacks enough evidence.
- Each reference data row must be a source-backed fact, not a model-generated classification.

The selected page must include:

- YAML frontmatter with `type: reference`, `status: draft`, `last_updated: {{current_date}}`, and `sources` linking to `../sources/{{slug}}.md`.
- `# Title`
- One short summary paragraph.
- `## Reference data`
- `## Source-backed details`
- `## Source pages`

CRITICAL: Write **4-column** tables for reference data and **3-column** tables for source-backed details. Evidence is filled automatically - do NOT write evidence text.

`## Reference data` must contain this exact table shape:

```md
| Item                     | Supported fact                             | Locator              | Source                                 |
| ------------------------ | ------------------------------------------ | -------------------- | -------------------------------------- |
| Source-native item name. | Narrow fact synthesized in your own words. | `normalized:L12-L12` | [Source title](../sources/{{slug}}.md) |
```

`## Source-backed details` must contain this exact table shape:

```md
| Claim                                      | Locator              | Source                                 |
| ------------------------------------------ | -------------------- | -------------------------------------- |
| Concrete reusable claim in your own words. | `normalized:L12-L12` | [Source title](../sources/{{slug}}.md) |
```

Rules:

- Include at least 2 data rows in `## Reference data`.
- Include at least 3 rows in `## Source-backed details`.
- Do NOT write Evidence columns - they are filled automatically from locators.
- Locator cells must use range format `normalized:L<start>-L<end>` (single line: `L123-L123`).
- The claim and supported-fact cells must synthesize in your own words; do not copy source text.
- Claim and supported-fact cells must not use weak generic words: important, crucial, fundamental, essential, success.

Source-page update rules:

- After this run, the source should have {{expected_total_pages}} synthesized pages total: existing pages plus this selected page.
- Replace only the candidate row for the page you actually created.
- Keep not-yet-created candidate pages as code-formatted paths.
- Preserve any Group, Priority, and Evidence basis cells already present in `## Related pages`.
- Keep `wiki/sources/{{slug}}.md` `## Related pages` in this exact table shape:

```md
| Page title | [../references/example.md](../references/example.md) | Source-native group name | must create | concrete evidence basis | created |
| Page title | `../references/example.md` | Source-native group name | should create | concrete evidence basis | not created yet |
```

Cross-link rules:

- Cross-links may point only to pages that already exist or pages created in this phase.
- Synthesized pages must use TWO separate sections for page references:
  - `## Related pages` — Only Markdown links to pages that exist. Example: `- [Functions](../concepts/functions.md)`
  - `## Candidate pages` — Plain text names (no links) for concepts worth exploring later. Example: `- Scope`
- Do NOT use phrases like "(not created yet)" or similar annotations. If a page doesn't exist, put its name in `## Candidate pages` without a link.
- Each body link back to the source page must use a relative Markdown link.
- Do not add empty headings.
- Do not duplicate headings.
- Do not put YAML/frontmatter keys such as `tags:`, `sources:`, `status:`, or `last_updated:` in the Markdown body.
- Do not add `## Executable implementation`.
- Use ASCII punctuation unless the source requires otherwise.
- Do not create backup files.
- Do not create scratch files such as `.fixed` files or `temp_file.md`.

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
