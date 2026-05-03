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
- `wiki/_grounding-report.md`
- `wiki/analyses/**`
- `packages/**`
- `tools/**`

Do not update index, graph, or log. This is Phase 2 only.

Task:
- Existing synthesized pages for this source that should remain linked:

{{existing_pages}}

- Create or update exactly these {{selected_count}} selected synthesized pages in this run and no others:

{{selected_candidates}}

Evidence bank:

{{evidence_bank}}

- Do not create pages for any other candidate rows.
- After this run, the source should have {{expected_total_pages}} synthesized pages total: existing pages plus selected pages.
- Prefer small, specific pages over broad duplicates.
- Use the source page's Group column as a page-boundary signal. Preserve source-native group names, but do not create new wiki directories from them.
- Do not create pages whose substance is not covered by the source.
- Each synthesized page must be one of: concept, entity, procedure, reference.
- Each synthesized page must include YAML frontmatter, an H1, a short definition, `## Source-backed details`, and `## Source pages`.
- `## Source-backed details` must contain a Markdown evidence table with this exact header:

```md
| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Concrete reusable claim. | "Short exact excerpt copied from the normalized source." | `normalized:L12` | [Source title](../sources/{{slug}}.md) |
```

- Include at least 3 evidence rows per synthesized page.
- Evidence cells must be short exact excerpts from `{{normalized_source}}`; do not paraphrase evidence cells.
- Prefer using exact snippets from the evidence bank above.
- Locator cells must use `normalized:L12` or `normalized:L12-L14` from the evidence bank, and the evidence excerpt must appear inside that cited line range.
- Do not put pipe characters inside table cells.
- Evidence table data rows must start with `|`, not `+`, `-`, or diff-marker text.
- The claim cell must synthesize in your own words; do not copy the evidence sentence into the claim cell.
- The evidence cell must quote the source text exactly.
- Do not add empty headings.
- Do not duplicate headings.
- Do not add `## Executable implementation` unless a real implementation file exists and is linked.
- Procedure pages must include `## Steps` with at least 3 concrete numbered or bulleted steps.
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
python3 tools/wiki_check_synthesis.py {{slug}} --min-pages {{expected_total_pages}} --max-pages {{expected_total_pages}}{{allowed_page_args}} --require-allowed-pages --normalized-source {{normalized_source}}
pnpm wiki:grounding:check
```

If validation fails, repair only the allowed files and rerun the same commands.

Stop only when all validation commands pass, or when you cannot proceed. If you cannot proceed, report the exact failing validation output.
