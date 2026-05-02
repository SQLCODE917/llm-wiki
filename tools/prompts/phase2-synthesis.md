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
- Use the strongest candidate rows in `wiki/sources/{{slug}}.md`.
- Create or update {{min_pages}} to {{max_pages}} synthesized pages total.
- Prefer small, specific pages over broad duplicates.
- Do not create pages whose substance is not covered by the source.
- Each synthesized page must be one of: concept, entity, procedure, reference.
- Each synthesized page must include YAML frontmatter, an H1, source-backed details, cross-links if useful, and a source-page link.
- Each synthesized page frontmatter `sources` must include a relative link to `../sources/{{slug}}.md` or equivalent correct relative path.
- Each synthesized page body must include a Markdown link back to `wiki/sources/{{slug}}.md` using a relative path.
- Replace only the candidate rows in `wiki/sources/{{slug}}.md` whose pages you actually created with real Markdown links.
- Keep not-yet-created candidate pages as candidate table rows with code-formatted paths.

After writing, run exactly:

```bash
python3 tools/wiki_check_synthesis.py {{slug}} --min-pages {{min_pages}} --max-pages {{max_pages}}
pnpm wiki:grounding
```

If validation fails, repair only the allowed files and rerun the same commands.

Stop only when both commands pass, or when you cannot proceed. If you cannot proceed, report the exact failing validation output.
