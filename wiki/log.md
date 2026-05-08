# Log

## [2026-05-02] scaffold | repository created
- initialized raw/, wiki/, packages/concepts/, and tools/
- verified TypeScript typecheck and Vitest test
- verified Marker PDF tool and CUDA Torch on RTX 4090

## [2026-05-02] ingest | compound-interest
- created wiki/sources/compound-interest.md
- updated wiki/concepts/compound-interest.md
- updated wiki/index.md

---

## [2026-05-02] schema-change | deterministic local-model rails

- Updated AGENTS.md with phased ingest contracts for source pages, synthesized pages, navigation/graph/log, and executable concepts.
- Added deterministic wiki scripts: `pnpm wiki:check-source`, `pnpm wiki:graph`, `pnpm wiki:graph:check`, and `pnpm wiki:lint`.
- Clarified that phase-1 source pages should list not-yet-created related pages as candidate code paths, not broken Markdown links.
- Current lint report intentionally exposes existing cleanup work for AoE2 and compound-interest pages.

---

## [2026-05-02] schema-change | mechanical phase-1 benchmark

- Added a mechanical Phase 1 prompt template for source-page repair under `tools/prompts/`.
- Added `pnpm wiki:phase1-benchmark` to run local Codex candidates in disposable worktrees and score them with deterministic validation.
- Tightened source-page validation with stricter claim length, related-page count, weak-claim language checks, and an optional lexical source-grounding check for benchmark runs.
- Benchmarked `qwen3-coder:30b` and `gpt-oss:20b` through the local Ollama profile on `aoe2-basics`; both passed the structural harness with one repair loop available, while the optional grounding check and manual inspection favored `qwen3-coder:30b`.

---

## [2026-05-02] cleanup | clean lint baseline and helper rails

- Updated compound-interest source and concept pages to current frontmatter and source-page formats.
- Added deterministic wiki index and log helper scripts.

---

## [2026-05-02] schema-change | semantic grounding check

- Added pnpm wiki:grounding and wiki/_grounding-report.md for source-claim and synthesized-page grounding checks.
- Moved token grounding helpers into shared wiki_common utilities.

---

## [2026-05-02] schema-change | phase-2 synthesis harness

- Added a Phase 2 synthesis prompt template for creating source-backed concept/entity/procedure/reference pages.
- Added pnpm wiki:check-synthesis to validate synthesized page backlinks, frontmatter sources, and source-page related links.

---

## [2026-05-02] ingest | adopted AoE2 basics synthesis

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] schema-change | atomic local ingest gates strengthened

- Source-page Key claims now use exact Evidence and Locator tables verified against normalized sources.
- Phase 2 adoption now requires local claim-judge success or an explicit curator override reason.
- Added wiki:phase2-single for one-candidate local synthesis worktrees.
- Reference page lookup tables now require Evidence and Locator columns.

---

## [2026-05-03] schema-change | phase2 single-page judge gate tightened

- wiki:phase2-single now runs local claim judging after deterministic validation unless --skip-judge is used.
- Single-page runs can issue a judge-specific repair prompt scoped to the selected page.
- The claim judge now applies deterministic overreach checks and includes reference-data rows.
- Phase 2 validation cleans obvious backup artifacts in disposable worktrees and prompts forbid backup files.

---

## [2026-05-03] schema-change | strengthened local ingest and query tooling

- Added reference-specific Phase 2 prompt and repair path for wiki/references pages.
- Added deterministic claim repair hints and stricter reference-data validation.
- Added bounded query helper with plan-only context selection and optional analysis filing.
- AoE2 economy-upgrades trial showed qwen3-coder still struggles with weak repeated reference facts; do not adopt that page yet without a stronger model or deterministic table repair.

---

## [2026-05-03] ingest | adopted AoE2 economy upgrades reference

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] schema-change | added deterministic reference repair and local model comparison

- Added wiki:repair-reference and wired it into Phase 2 validation for selected reference pages.
- Added repeated-phrase validation for synthesized claim and reference fact cells.
- Carried Related pages evidence-basis text into Phase 2 evidence-bank retrieval to reduce generic upgrade drift.
- Adopted wiki/references/aoe2-economy-upgrades.md after deterministic validation and local batch judge passed.
- Compared qwen3-coder:30b and gpt-oss:20b on aoe2-military-upgrades; qwen was faster and more topical, while gpt-oss needed repetition cleanup and drifted into economy-upgrade content.

---

## [2026-05-03] ingest | adopted AoE2 military upgrades reference

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] schema-change | strengthened local ingest verification

- Added reference row scope validation to catch topical drift inside generated reference pages.
- Added analysis-page validation and wired saved query analyses through it before index, graph, and log updates.
- Added Phase 2 run reports and batch-judge-to-row-wise fallback for local judge JSON failures.
- Adopted AoE2 military upgrades after deterministic synthesis validation and row-wise local claim judging passed.

---
## [2026-05-03] lint | 0 FAIL | 1 WARN

- FAIL: 0
- WARN: 1
- Report: wiki/_linter-report.md

---

## [2026-05-03] ingest | adopted AoE2 scouting techniques procedure

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] schema-change | tracked candidate backlog and query filing smoke test

- Changed linter output so uncreated Related-pages candidate paths are TODO backlog instead of WARN health issues.
- Added wiki:query:smoke to test saved-analysis filing, analysis validation, index refresh, and graph refresh in a temp repo copy.
- Adopted AoE2 scouting techniques after deterministic repair and row-wise local claim judging passed.

---
## [2026-05-03] lint | 0 FAIL | 0 WARN | 1 TODO

- FAIL: 0
- WARN: 0
- TODO: 1
- Report: wiki/_linter-report.md

---

## [2026-05-03] schema-change | tightened Phase 2 procedure repair prompts

- Phase 2 synthesis prompts now require likely-sounding claims and procedure steps to be directly supported by evidence rows.
- Judge repair prompts now explicitly repair rows listed under Deterministic Flags as well as failed semantic verdict rows.

---
## [2026-05-03] lint | 0 FAIL | 0 WARN | 1 TODO

- FAIL: 0
- WARN: 0
- TODO: 1
- Report: wiki/_linter-report.md

---

## [2026-05-03] ingest | adopted AoE2 resource management concept

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] schema-change | added deterministic Phase 0 importer

- Added wiki:phase0 for safe PDF and Markdown import from raw/inbox into raw/imported and raw/normalized.
- PDF import wraps TORCH_DEVICE=cuda marker_single with markdown output and --disable_tqdm.
- Imported originals are not overwritten; --reuse-imported requires matching bytes before rerunning normalization.
- Added wiki:phase0:smoke to test markdown import, duplicate refusal, reuse, and PDF dry-run behavior in a temp repo.
- Synthesis validation now rejects synthesized pages with placeholder Page title text, uncreated-candidate mentions, or executable sections without packages links.

---
## [2026-05-03] lint | 0 FAIL | 0 WARN | 1 TODO

- FAIL: 0
- WARN: 0
- TODO: 1
- Report: wiki/_linter-report.md

---

## [2026-05-03] ingest | adopted AoE2 game plans procedure

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] ingest | adopted AoE2 decision making concept

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] schema-change | added semantic maintenance and analysis judging

- Added wiki:semantic-lint for deterministic duplicate/overlap triage across synthesized pages.
- Added wiki:judge-analysis and wired the query smoke test through deterministic analysis judging.
- Added wiki:contradictions to scan source claim tables for possible cross-source contradictions once multiple substantial sources exist.
- Model comparison on AoE2 decision-making favored local-4090 qwen: qwen passed deterministic validation quickly; gpt-oss:20b timed out then failed validation.

---

## [2026-05-03] lint | 0 semantic overlap warning(s)

- Semantic report: wiki/_semantic-linter-report.md
- WARN: 0

---
## [2026-05-03] lint | 0 FAIL | 0 WARN | 1 TODO

- FAIL: 0
- WARN: 0
- TODO: 1
- Report: wiki/_linter-report.md

---

## [2026-05-03] lint | 0 candidate contradiction(s)

- Contradiction report: wiki/_contradiction-report.md

---

## [2026-05-03] ingest | added AoE2 water and mixed map concepts

- Finalized source `aoe2-basics` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-03] query | filed 2026-05-03-aoe2-water-and-mixed-map-strategy

- Question: How should an AoE2 player adapt strategy across water and mixed maps?
- Analysis page: wiki/analyses/2026-05-03-aoe2-water-and-mixed-map-strategy.md
- Pages used: wiki/sources/aoe2-basics.md, wiki/concepts/aoe2-mixed-maps.md, wiki/concepts/aoe2-map-awareness.md, wiki/concepts/aoe2-resource-management.md, wiki/concepts/aoe2-water-maps.md, wiki/concepts/aoe2-army-composition.md, wiki/concepts/aoe2-build-orders.md, wiki/concepts/aoe2-decision-making.md

---

## [2026-05-03] todo | need second substantial source for contradiction scanning

- Contradiction scanner is implemented, but only aoe2-basics is substantial enough for meaningful cross-source comparison.

---

## [2026-05-03] lint | maintenance 1 failure(s)

- Report: wiki/_maintenance-report.md
- Checks run: 9
- Failed: 1

---

## [2026-05-03] lint | maintenance 0 failure(s)

- Report: wiki/_maintenance-report.md
- Checks run: 9
- Failed: 0

---

## [2026-05-03] lint | maintenance 0 failure(s)

- Report: wiki/_maintenance-report.md
- Checks run: 9
- Failed: 0

---

## [2026-05-03] lint | maintenance 0 failure(s)

- Report: wiki/_maintenance-report.md
- Checks run: 11
- Failed: 0

---

## [2026-05-03] lint | maintenance 0 failure(s)

- Report: wiki/_maintenance-report.md
- Checks run: 11
- Failed: 0

---

## [2026-05-05] proposal | smart ingestion for large documents

- Created DESIGN_smart-ingestion.md with 8 testable hypotheses: H1 chunked PDF normalization, H2 source outline extraction, H3 SQLite FTS evidence index, H4 vector embeddings, H5 hybrid search, H6 context budget tracking, H7 incremental source reading, H8 parallel processing. Priority order: reliability (H1, H6, H2), search quality (H3, H5), scalability (H7, H4, H8).

---

## [2026-05-05] ingest | Cloud ingest of js-allonge

- Source: js-allonge
- Backend: bedrock
- Synthesized pages: 0

---

## [2026-05-05] ingest | Cloud ingest of js-allonge-test

- Source: js-allonge-test
- Backend: bedrock
- Synthesized pages: 2

---

## [2026-05-05] ingest | Cloud ingest of clean-test

- Source: clean-test
- Backend: bedrock
- Synthesized pages: 2

---

## [2026-05-05] ingest | Cloud ingest of js-allonge

- Source: js-allonge
- Backend: bedrock
- Synthesized pages: 3

---

## [2026-05-05] ingest | Deep extraction of js-allonge

- Chunks: 30, Claims: 274, Topics: 14, Pages: 11. Created: functions, es6-features, control-flow, data-types, arrays, +6 more

---

## [2026-05-05] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-05] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-05] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-05] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-05] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-05] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-06] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | Deep extraction of js-allonge

- Chunks: 18, Claims: 170, Topics: 8, Pages: 8. Created: functions, es6-features, data-types, control-flow, arrays, +3 more

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---

## [2026-05-07] ingest | Deep extraction of js-allonge

- Chunks: 15, Claims: 143, Topics: 8, Pages: 8. Created: functions, es6-features, control-flow, data-types, arrays, +3 more

---

## [2026-05-07] ingest | Deep extraction of js-allonge

- Chunks: 13, Claims: 130, Topics: 9, Pages: 7. Created: functions, es6-features, data-types, control-flow, arrays, +2 more

---

## [2026-05-07] ingest | Deep extraction of js-allonge

- Chunks: 13, Claims: 128, Topics: 8, Pages: 8. Created: functions, es6-features, data-types, control-flow, objects, +3 more

---

## [2026-05-08] ingest | Deep extraction of js-allonge

- Chunks: 15, Claims: 182, Topics: 12, Pages: 11. Created: functions, es6-features, data-types, control-flow, variables, +6 more

---

## [2026-05-08] ingest | Deep extraction of js-allonge

- Chunks: 25, Claims: 378, Topics: 15, Pages: 14. Created: functions, es6-features, functional-programming, data-types, arrays, +9 more

---

## [2026-05-08] ingest | finalized ingest for js-allonge

- Finalized source `js-allonge` after phased ingest.
- Updated wiki/index.md and wiki/_graph.json.
- Generated wiki/_linter-report.md.

---
