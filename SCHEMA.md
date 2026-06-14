# LLM-Wiki Schema

This document defines how the wiki is structured and how the maintainer model
operates on it. It is rendered into the model's system prompt by the harness.
The index and log formats below are also enforced in harness code
(`harness/src/llmwiki/domain/`) — keep them in sync when revising this file.

## Layers

- `raw/` — immutable source documents. Read-only. Never edit, never delete.
- `wiki/` — the knowledge base: interlinked markdown pages. The model writes
  this layer exclusively through the `write_page` tool.
- `SCHEMA.md` — this file. Conventions and workflows. Revisions are logged.

## Page conventions

- Page names are kebab-case slugs, unique across the wiki: `bronze-age-collapse`.
- Every page belongs to one category:
  - `source` — summary of one raw source; named after the source.
  - `entity` — a person, place, organization, system, or thing.
  - `concept` — an idea, theme, claim, or recurring pattern.
  - `synthesis` — cross-source analysis, comparisons, answers worth keeping.
- Link to other pages inline with `[[page-name]]`. Link liberally — links to
  pages that do not exist yet mark pages worth creating.
- Cite evidence by raw source path, e.g. `(raw/some-article.md)`. For paged
  sources (PDFs), include the page range: `(raw/book.pdf p.28-41)`.
- Book-scale sources get a hub `source` page named after the file (e.g.
  `javascriptallonge`) that summarizes the whole source and links
  per-chapter source pages named `<hub>-<chapter-slug>`.
- Text marked `[figure text (OCR, unverified)]` was machine-recognized from
  an image: usable as evidence with that caveat, never as a verbatim quote.
- When a new source contradicts an existing claim, do not overwrite silently:
  state both claims, mark the conflict with `**Contradiction:**`, and cite
  both sources.
- Frontmatter (category, summary, sources, updated date) is composed by the
  harness from `write_page` arguments — do not write it in page content.
- `write_page` replaces the entire page. When updating an existing page,
  `read_page` it first and carry forward the content you are not changing.
- On hub source pages, the `Key concepts:` / `Key entities:` lines are
  derived navigation maintained by the harness — like index.md entries,
  never write or edit key-entity/key-concept lists yourself; they are
  replaced from computed evidence after every ingest.

## index.md

One entry per page, grouped by category. Maintained deterministically by the
harness on every `write_page` — never edited by hand or by the model directly,
but readable via the `read_index` tool: it is the catalog to consult for
questions about the wiki itself or its overall coverage.
Entry format: `- [[page-name]] — one-line summary`.

## log.md

Append-only chronology, written by the harness when an operation completes.
Entry prefix: `## [YYYY-MM-DD] <op> | <subject>` so that
`grep "^## \[" wiki/log.md | tail -5` lists recent activity.

## Workflows

### ingest

1. Read the source with `read_source`.
2. Search the wiki for related pages (`search_wiki`, `read_page`).
3. Write or update a `source` page summarizing the key information.
4. Update every affected `entity`/`concept`/`synthesis` page: integrate new
   facts, add cross-references, flag contradictions. Create pages for
   important entities or concepts that lack one.
5. Call `finish_ingest` with a short report of what changed.

### query

1. Search the wiki (`search_wiki`), then read the relevant pages.
2. Answer from wiki content with page and source citations.
3. If the answer is a new synthesis worth keeping (a comparison, an analysis,
   a connection not yet recorded), file it with `write_page` (category
   `synthesis`) before responding.
4. Call `respond` with the answer.

### lint

1. The harness reports deterministic findings first: broken `[[links]]`,
   orphan pages, index drift, and citation evidence findings when enabled.
2. Review flagged pages: resolve or document contradictions, add missing
   cross-references, propose pages for concepts mentioned often but never
   given a page.
   - For orphan-only repairs, use `link_orphan(from_page, orphan_page)` to add
     the inbound `[[orphan-page]]` link from a related existing page. Do not
     rewrite a whole page merely to add one graph edge.
3. Call `finish_lint` with the health report. The harness recomputes
   deterministic findings after the model pass and files a verified report:
   model report, deterministic delta, and before/after deterministic state. The
   harness files that verified report as the `wiki-health` synthesis page
   (rewritten each lint pass; history is in log.md). `wiki-health` is exempt
   from orphan checks.
