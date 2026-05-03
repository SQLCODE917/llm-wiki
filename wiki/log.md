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
