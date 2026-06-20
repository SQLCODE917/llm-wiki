# LLM-Wiki Schema

This document defines how the wiki is structured and how the maintainer model
operates on it. It is rendered into the model's system prompt by the harness.
The index and log formats below are also enforced in harness code
(`harness/src/llmwiki/domain/`) — keep them in sync when revising this file.

## Layers

- `raw/` — immutable source documents. Read-only. Never edit, never delete.
- `wiki/` — the knowledge base: interlinked markdown pages. The model writes
  this layer exclusively through the `write_page` tool.
- `wiki/wiki-candidates.json` — harness-owned bookkeeping for missing page
  candidates. It is not wiki knowledge and is never cited as evidence.
- `wiki/wiki-graph.json` — harness-owned graph export derived from current
  pages and links. It is not wiki knowledge and is never edited by the model.
- `SCHEMA.md` — this file. Conventions and workflows. Revisions are logged.

## Page conventions

- Page IDs are kebab-case slugs, unique across the wiki: `bronze-age-collapse`.
- If a source uses the same noun for different roles, make the PageId
  describe the role. Prefer PageIds like `<source>-<topic>-rules`,
  `<source>-<topic>-spell`, `<source>-<topic>-monster`,
  `<source>-<topic>-item`, or `<source>-<topic>-lore` over bare
  singular/plural sibling pages.
- Every page has one page kind:
  - `source` — summary of one raw source; named after the source.
  - `entity` — a person, place, organization, system, or thing.
  - `concept` — an idea, theme, claim, or recurring pattern.
  - `synthesis` — cross-source analysis, comparisons, answers worth keeping.
- Link to other pages inline with `[[page-id]]`. Link liberally — links to
  pages that do not exist yet mark pages worth creating.
- Cite evidence by SourceLocator, e.g. `(raw/some-article.md)`. For paged
  sources (PDFs), include the page range: `(raw/book.pdf p.28-41)`.
- For high-audit claims, you may add an optional normalized line locator after
  the source path, e.g. `(raw/article.md normalized:L12-L18)`. Do not add
  normalized locators unless you have line-addressed source text.
- Book-scale sources get a hub `source` WikiPage with a PageId after the file (e.g.
  `javascriptallonge`) that summarizes the whole source and links
  per-chapter source pages named `<hub>-<chapter-slug>`.
- Text marked `[figure text (OCR, unverified)]` was machine-recognized from
  an image: usable as evidence with that caveat, never as a verbatim quote.
- When a new source contradicts an existing claim, do not overwrite silently:
  state both claims, mark the conflict with `**Contradiction:**`, and cite
  both sources.
- Contradiction audits are report-only: record conflicts for curator review
  without deciding which source wins and without rewriting content pages.
- Grounding audits are report-only: judge selected cited claims against
  resolved evidence excerpts and record curator actions without rewriting
  content pages.
- Semantic lint audits are report-only: record stale-claim, supersession, and
  data-gap leads for curator review without rewriting content pages.
- Frontmatter (`page_id`, `page_kind`, summary, sources, updated date) is composed by the
  harness from `write_page` arguments — do not write it in page content.
- `write_page` replaces the entire page. When updating an existing page,
  `read_page` it first and carry forward the content you are not changing.
- In ingest workflows, call `plan_pages` before any `write_page`. The ingest
  route plan is a page write allowlist for the current run: each page write
  must match a planned page ID and page kind. Use route gaps for source material
  that should not become a page in the current run. The ingest route plan is
  not source evidence and never supports wiki claims by itself.
- Some source-page writes are planned as `SourceSummaryPlan` writes. For those
  writes, ignore `page_body`: the harness renders the page from
  `source_record_text` and `claim_bullets`. Keep `source_record_text` to one or
  two short paraphrased sentences. Write three to five short bullets, use only
  selected `SourceClaim` IDs in `covered_source_claims`, include the required
  raw citation in every bullet, and do not copy eight or more consecutive words
  from the source. If `write_page` rejects a source-summary draft, rewrite the
  rejected `claim_bullets` themselves before retrying.
- On hub source pages, the `Key concepts:` / `Key entities:` lines are
  derived navigation maintained by the harness — like index.md entries,
  never write or edit key-entity/key-concept lists yourself; they are
  replaced from computed evidence after every ingest.
- On book-scale hub source pages, the harness may add a `Page-Map Navigation`
  section from the chunk manifest when model-authored prose under-links the
  pages written during chunking. Treat that section as deterministic
  navigation, like index.md entries and hub key lists.
- Candidate page backlog entries are not pages. Promote a candidate only by
  writing a real `entity`/`concept`/`synthesis` page through the normal
  workflow.
- Ingest profiles are optional prompt overlays selected by the curator for a
  source type. They add guidance, but do not replace this schema, change page
  kinds, or bypass any tool/workflow rule.

## Graph export

`wiki/wiki-graph.json` is a deterministic export generated by
`uv run llmwiki graph`. It includes content-page nodes, resolved/unresolved
edges, and metadata such as graph schema version and generator. Harness-owned
system report pages are excluded from the export so reports do not reshape the
content graph. Use `uv run llmwiki graph --check` when you need to verify that
the artifact matches the current wiki.

## index.md

One entry per page, grouped by page kind. Maintained deterministically by the
harness on every `write_page` — never edited by hand or by the model directly,
but readable via the `read_index` tool: it is the catalog to consult for
questions about the wiki itself or its overall coverage.
Entry format: `- [[page-id]] — one-line summary`.

## log.md

Append-only chronology, written by the harness when an operation completes.
Entry prefix: `## [YYYY-MM-DD] <op> | <subject>` so that
`grep "^## \[" wiki/log.md | tail -5` lists recent activity.

## Candidate page backlog

`wiki/wiki-candidates.json` records recurring missing page candidates detected
by the harness, currently from explicit `[[links]]` whose target page does not
exist. Candidate statuses are finite: `discovered`, `queued`, `promoted`,
`rejected`, and `merged`. The backlog supports curator review, but never counts
as source evidence or as existing wiki coverage.

## Workflows

### ingest

1. Read the source with `read_source`.
2. Search the wiki for related pages (`search_wiki`, `read_page`).
3. Call `plan_pages` with the page targets for this source and any route gaps.
4. Write or update a `source` page summarizing the key information.
5. Update every affected `entity`/`concept`/`synthesis` page: integrate new
   facts, add cross-references, flag contradictions. Create pages for
   important entities or concepts that lack one.
6. Call `finish_ingest` with a short report of what changed.

When an ingest profile is active, follow its additional source-type guidance
inside the same workflow. If profile guidance and this schema conflict, this
schema wins.

### query

1. For content questions, search the wiki (`search_wiki`), then read the
   relevant pages. For questions about the wiki itself or its coverage,
   `read_index` is the relevant wiki document.
2. Answer from wiki content with page and source citations.
3. If the answer is a new synthesis worth keeping (a comparison, an analysis,
   a connection not yet recorded), file it with `write_page` (`page_kind`
   `synthesis`) before responding. Do not write pages for simple coverage,
   status, or catalog answers.
4. Call `respond` with the answer.

### chat-file

1. Ordinary chat answers are conversational context, not source evidence.
2. When the curator explicitly files an answer with `/file <page-id>`, re-read
   the current wiki pages that support the durable claims.
3. Write only synthesis pages through `write_page`; cite current wiki pages and
   raw sources when available.
4. If the current wiki does not support the requested synthesis, do not write a
   page. Finish with the missing evidence or curator action needed.

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

### contradictions

1. The harness selects a bounded set of candidate page pairs before the model
   is invoked. Candidate reasons include shared sources, direct links, shared
   raw citations, and keyword overlap.
2. Read the relevant pages before deciding whether a pair contains a real
   contradiction.
3. Use `record_contradiction` only when two claims cannot both be true as
   written. Differences in emphasis, scope, terminology, or abstraction level
   are not contradictions.
4. Do not rewrite pages, resolve the conflict, or decide which source wins.
   The human curator resolves contradictions.
5. Call `finish_contradictions` with audited scope, findings recorded,
   uncertainty, and curator next steps. The harness files the structured report
   as the `wiki-contradictions` synthesis page (rewritten each audit pass;
   history is in log.md). `wiki-contradictions` is exempt from orphan checks.

### grounding

1. The harness selects a bounded set of citation-bearing claim candidates and
   resolves available evidence excerpts before the model is invoked.
2. Judge only whether the cited evidence supports the selected claim as
   written. Do not judge style, importance, or whether the page is complete.
3. Use `record_grounding_verdict` for each inspected claim with exactly one
   verdict: `supported`, `too_broad`, `not_supported`, or `unclear`.
4. Do not rewrite pages, add sources, or decide silently that a claim is fine
   when deterministic citation evidence failed. Fatal deterministic evidence
   findings skip model judgment.
5. Call `finish_grounding` with audited scope, uncertainty, and curator next
   steps. The harness files the structured report as the `wiki-grounding`
   synthesis page (rewritten each audit pass; history is in log.md).
   `wiki-grounding` is exempt from orphan checks.

### semantic-lint

1. The harness selects a bounded set of semantic maintenance leads before the
   model is invoked. Candidate reasons can include exact shared citations,
   direct links, updated-date differences, or candidate-page backlog entries.
2. Read the relevant pages before deciding whether a lead is actionable.
3. Use `record_semantic_finding` only for `stale_claim`,
   `possible_supersession`, or `data_gap` findings. These are curator leads,
   not final truth declarations.
4. Do not rewrite pages, invent missing sources, or perform web search.
   Compatible wording differences are not findings.
5. Call `finish_semantic_lint` with audited scope, findings recorded,
   uncertainty, and curator next steps. The harness files the structured report
   as the `wiki-semantic-lint` synthesis page (rewritten each pass; history is
   in log.md). `wiki-semantic-lint` is exempt from orphan checks.
