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

Evidence bank:

{{evidence_bank}}

- Use only evidence inside the selected page's allowed source range when one is shown in the evidence bank.
- If no allowed source range is shown, either declare `source_ranges` in the reference page frontmatter or stop and report that the source section cannot be range-gated.
- `source_ranges` values must look like `{{slug}}:normalized:L12-L34`.
- Do not pull evidence from unrelated sections just because a keyword matches the page title.

Reference-page rules:
- The selected page must have `type: reference`.
- The page should contain reusable lookup facts, not advice invented from general game knowledge.
- Do not split one generic evidence sentence into multiple specific rows unless the source explicitly names each item.
- Do not infer item categories, priority tiers, formulas, timings, costs, or upgrade names that the evidence does not state.
- If the evidence bank is thin, create a narrow reference page with fewer supported facts rather than a broad lookup table.
- If there are not at least 2 source-backed lookup rows, stop and report that the candidate lacks enough evidence.
- Each reference data row must be a source-backed fact, not a model-generated classification.

The selected page must include:
- YAML frontmatter with `type: reference`, `status: draft`, `last_updated: {{current_date}}`, and `sources` linking to `../sources/{{slug}}.md`.
- `# Title`
- One short summary paragraph.
- `## Reference data`
- `## Source-backed details`
- `## Source pages`

`## Reference data` must contain this exact table shape:

```md
| Item | Supported fact | Evidence | Locator | Source |
|---|---|---|---|---|
| Source-native item name. | Narrow fact supported by the quoted evidence. | "Short exact excerpt copied from the normalized source." | `normalized:L12` | [Source title](../sources/{{slug}}.md) |
```

`## Source-backed details` must contain this exact table shape:

```md
| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Concrete reusable claim in the agent's own words. | "Short exact excerpt copied from the normalized source." | `normalized:L12` | [Source title](../sources/{{slug}}.md) |
```

Evidence and locator rules:
- Include at least 2 data rows in `## Reference data`.
- Include at least 3 rows in `## Source-backed details`.
- Evidence cells must be short exact excerpts from `{{normalized_source}}`; do not paraphrase evidence cells.
- If a source line contains internal quotation marks, choose a shorter exact excerpt that avoids those internal quotes.
- Prefer exact snippets from the evidence bank above.
- Locator cells must use `normalized:L12` or `normalized:L12-L14`, and the evidence excerpt must appear inside that cited line range.
- Do not put pipe characters inside table cells.
- Evidence table data rows must start with `|`, not `+`, `-`, or diff-marker text.
- The claim and supported-fact cells must synthesize in your own words; do not copy the evidence sentence into those cells.
- Claim and supported-fact cells must not use weak generic words: important, crucial, fundamental, essential, success.
- If the source uses weak generic words, preserve the supported substance without those words. For example, use "should be prioritized highly" instead of "is important."

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
- Each body link back to the source page must use a relative Markdown link.
- Do not Markdown-link to candidate pages that remain uncreated.
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
