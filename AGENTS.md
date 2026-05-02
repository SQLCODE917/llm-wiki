# LLM-Wiki operating rules

## Mission
Maintain the wiki in `/wiki` as the compiled knowledge layer for `/raw`.
Never modify files under `/raw/imported`.

## Repository map
- `raw/inbox/`: user drops new PDFs or markdown files here
- `raw/imported/`: immutable originals
- `raw/normalized/`: extracted or normalized markdown
- `raw/assets/`: extracted images and media
- `wiki/sources/`: one page per source
- `wiki/concepts/`: canonical concept pages
- `wiki/entities/`: people, orgs, projects, libraries
- `wiki/analyses/`: durable analyses generated from questions
- `packages/concepts/src/`: executable TypeScript implementations
- `packages/concepts/tests/`: tests for implementations

## Ingest workflow
1. If the source is a PDF, convert it to markdown from `raw/inbox/` into `raw/normalized/`.
2. If the source is markdown, preserve the original in `raw/imported/` and work from `raw/normalized/`.
3. Create or update `wiki/sources/<slug>.md`.
4. Update affected pages in `wiki/concepts/` and `wiki/entities/`.
5. Update `wiki/index.md`.
6. Append one entry to `wiki/log.md`.
7. If the source implies an executable concept, add or update TypeScript code and tests.
8. Before finishing any code change, run:
   - `pnpm code:typecheck`
   - `pnpm code:test`
9. Every source page must include:
   - YAML frontmatter with `source_id`, `source_type`, `raw_path`, `normalized_path`, and `status`
   - Summary
   - Key claims
   - Concepts
   - Entities
   - Open questions
   - Related pages

## Query workflow
1. Read `wiki/index.md` first.
2. Prefer existing wiki pages over re-reading raw sources.
3. If the answer is durable, save it to `wiki/analyses/YYYY-MM-DD-<slug>.md`.
4. Add links between the new analysis and related concept/entity pages.

## Writing rules
- Prefer updating an existing page over creating duplicates.
- Keep pages small, specific, and heavily linked.
- Every concept page should link to its source pages.
- Every executable concept page should link to its TypeScript implementation and tests.

## Safety rails
- Never edit `raw/imported/`.
- Never delete a wiki page unless it is clearly duplicated and the replacement is linked.
- Do not leave code changes untested if tests exist.
