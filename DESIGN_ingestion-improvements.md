# Design: Ingestion Pipeline Improvements

> Status: APPROVED  
> Date: 2026-05-08  
> Context: Tighten gaps between current implementation and LLM-Wiki reference pattern

## Summary

The current ingestion pipeline is coherent and implements the core pattern well. This design proposes eight improvements to make evidence, idempotency, visual grounding, and failure states explicit rather than implicit.

---

## Design Principles

1. **The markdown wiki is the primary compiled artifact.** JSON state exists to support reproducibility, validation, retry, and debugging—not to replace the wiki.
2. **Raw imported sources are immutable.** The `raw/imported/` directory is the audit root. The compiled wiki should always be traceable back to source artifacts.
3. **Generated indexes and graphs are rebuilt from wiki contents.** Only `wiki/log.md` is append-only; everything else can be deterministically regenerated.
4. **LLM-generated claims must remain traceable to source evidence.** Every synthesized page links back to normalized source locators.
5. **Human curation happens through override files, not by editing generated state directly.** This preserves regeneration while allowing curator control.
6. **Failure states are explicit and preserved.** Failed drafts often contain useful partial synthesis and should not be silently discarded.

---

## Non-goals

- **Replace the markdown wiki with a database.** The wiki remains simple, inspectable, and editable through ordinary tools.
- **Require visual evidence extraction for every source type.** Visual grounding is opt-in based on source characteristics.
- **Guarantee that every proposed candidate page is adopted.** Partial success with recorded failures is acceptable.
- **Make Phase 2 fully deterministic.** LLM synthesis is inherently non-deterministic; only validation, adoption, and finalization are deterministic.
- **Over-engineer `.wiki-extraction-state/`.** State files support the wiki, not replace it.

---

## Current State

The pipeline has four phases:

- **Phase 0**: Import + normalize (PDF → markdown)
- **Phase 1**: Deep extract claims + aggregate by topic
- **Phase 2**: Create source page + synthesize candidate pages
- **Phase 3**: Finalize (index, graph, lint, log)

Strengths:

- Clear phase separation
- Good provenance discipline (immutable originals, locators)
- Validation and repair are first-class
- Addresses retrieval/grounding failure modes

Gaps:

- No explicit manifest for resume/audit
- Claim extraction coupled with page candidacy
- No stable claim IDs
- No visual/spatial evidence support
- Idempotency rules are implicit
- Phase 3 has incremental mutation risk
- Failed drafts are silently lost
- No formal acceptance contract

---

## Proposed Changes

### 1. Add Explicit Artifact Manifest

**Location**: `.wiki-extraction-state/<slug>/manifest.json`

**Schema**:

```json
{
  "schema_version": 1,
  "slug": "javascriptallonge",
  "source_file": "raw/inbox/javascriptallonge.pdf",
  "source_kind": "pdf",
  "command": "pnpm wiki:ingest raw/inbox/javascriptallonge.pdf --slug javascriptallonge --structured",
  "git_commit": "abc123...",
  "original_sha256": "a1b2c3...",
  "normalized_sha256": "d4e5f6...",
  "extractor": "pymupdf4llm",
  "structured": true,
  "target_tokens": 3500,
  "render_pages": "auto",
  "model_backend": "bedrock",
  "candidate": "local-4090",
  "allow_partial_pages": false,
  "partial_success_reason": null,
  "created_at": "2026-05-08T10:30:00Z",
  "updated_at": "2026-05-08T11:45:00Z",
  "paths": {
    "imported_original": "raw/imported/javascriptallonge/original.pdf",
    "normalized_source": "raw/normalized/javascriptallonge/source.md",
    "state_dir": ".wiki-extraction-state/javascriptallonge",
    "source_page": "wiki/sources/javascriptallonge.md"
  },
  "phase_status": {
    "phase0_import": "complete",
    "phase0_normalize": "complete",
    "phase1a_extract": "complete",
    "phase1b_dedupe": "complete",
    "phase1c_candidates": "complete",
    "phase2a_source": "complete",
    "phase2b_synthesize": "partial",
    "phase2c_adopt": "partial",
    "phase3a_index": "pending",
    "phase3b_graph": "pending",
    "phase3c_lint": "pending",
    "phase3d_log": "pending"
  },
  "phase2b_progress": {
    "total_candidates": 13,
    "synthesized": 8,
    "adopted": 7,
    "failed": 1,
    "pending": 5
  },
  "last_error": null
}
```

**Error tracking**: When a phase fails, record a compact error pointer:

```json
{
  "last_error": {
    "phase": "phase2b_synthesize",
    "message": "3 candidate pages failed validation",
    "artifact": ".wiki-extraction-state/javascriptallonge/failures/closures.json",
    "occurred_at": "2026-05-08T11:30:00Z"
  }
}
```

This avoids forcing users to inspect every failure file just to see what happened.

**Phase status enum**:

- `initialized` — Phase created but not started
- `pending` — Waiting for prerequisites
- `running` — Currently executing
- `complete` — Finished successfully
- `partial` — Partially complete (e.g., some chunks processed)
- `failed` — Failed with error
- `skipped` — Explicitly skipped (e.g., `--skip-phase0`)

**Benefits**:

- Deterministic resume after interruption
- Audit trail for debugging
- Clear phase status for UI/tooling
- Config reproducibility (extractor, tokens, model)

**Source kinds** (extensible):

- `pdf` — PDF documents
- `markdown` — Markdown files
- `html` — Web articles
- `repo` — Code repositories
- `dataset` — Structured data files
- `image` — Image collections

**Implementation**:

- **Create manifest before any Phase 0 work** (not after):
  1. Create manifest with `status = initialized`
  2. Copy original and record `original_sha256`
  3. Normalize and record `normalized_sha256`
  4. Mark phase0 complete
- Add `pnpm wiki:manifest <slug>` to view status
- Add `--resume` flag that reads manifest to skip completed phases

---

### 2. Separate Claim Extraction from Page Candidacy

**Current**: Phase 1 extracts claims AND aggregates by topic in one pass.

**Proposed**:

```
Phase 1a: Extract atomic claims (conservative, source-faithful)
Phase 1b: Normalize/deduplicate claims (mechanical)
Phase 1c: Propose page candidates (editorial, regenerable)
```

**Rationale**:

- Claim extraction is expensive (LLM calls per chunk)
- Page candidacy is cheap (aggregation + heuristics)
- If candidacy logic changes, don't redo extraction

**State files**:

```
.wiki-extraction-state/<slug>/
├── manifest.json
├── claims-raw.jsonl           # Phase 1a output (append-only JSONL, one claim per line)
├── claims-normalized.json     # Phase 1b output (deduped, normalized topics, stable IDs)
├── candidates.generated.json  # Phase 1c output (machine-generated proposals)
├── candidates.override.json   # Human curator overrides (add/remove/modify candidates)
├── candidates.json            # Merged candidates = generated + override
└── state.json                 # Legacy compat (derives from above)
```

**Why JSONL for raw claims**: Append-only JSON is awkward. JSONL allows safe resumable writes—each line contains one extracted claim or chunk result.

**Candidate override schema**:

`candidates.override.json` supports three operations:

- `add`: manually add candidate pages
- `modify`: override fields on generated candidates
- `remove`: suppress generated candidates

```json
{
  "add": [
    {
      "title": "Closures",
      "path": "../concepts/closures.md",
      "page_type": "concept",
      "priority": "should create",
      "reason": "Recurring concept across extracted claims"
    }
  ],
  "modify": [
    {
      "path": "../concepts/functions.md",
      "priority": "must create"
    }
  ],
  "remove": [
    {
      "path": "../concepts/weak-candidate.md",
      "reason": "Too broad"
    }
  ]
}
```

**Merge semantics**: `candidates.json = candidates.generated.json + candidates.override.json`

- Override `add` entries are appended
- Override `modify` entries update matching paths
- Override `remove` entries filter out matching paths

**Merge validation**: After applying overrides, `candidates.json` must contain unique `path` values. Duplicate paths are a validation error.

**Merge tracking**: To verify candidates are fresh, `candidates.json` includes merge metadata:

```json
{
  "_meta": {
    "generated_hash": "abc123...",
    "override_hash": "def456...",
    "merged_hash": "789ghi...",
    "merged_at": "2026-05-08T11:00:00Z"
  },
  "candidates": [...]
}
```

This supports the acceptance check: "candidates.json was regenerated after latest generated/override change."

**Commands**:

```bash
pnpm wiki:extract-claims <slug>        # Phase 1a only
pnpm wiki:normalize-claims <slug>      # Phase 1b only
pnpm wiki:propose-candidates <slug>    # Phase 1c only
pnpm wiki:deep-extract <slug>          # All of 1a+1b+1c (current behavior)
```

---

### 3. Add Claim Schema with Stable IDs

**Current**: Claims have no stable IDs; identified by (topic, claim_text) tuple.

**Proposed claim schema**:

```json
{
  "id": "claim_javascriptallonge_c007_b7f3a2",
  "claim": "Arrow functions do not have their own `this` binding.",
  "topic": "Functions",
  "claim_type": "fact",
  "tags": ["javascript", "function-semantics", "this-binding"],
  "specificity": 0.35,
  "confidence": 0.9,
  "chunk_index": 7,
  "evidence": [
    {
      "excerpt": "Arrow functions don't have their own this binding",
      "locator": "normalized:L1847-L1847",
      "excerpt_hash": "b7f3a2..."
    }
  ],
  "suggested_pages": ["../concepts/functions.md", "../concepts/closures.md"],
  "created_at": "2026-05-08T10:35:00Z",
  "source_chunk_hash": "c8d9e0..."
}
```

**Claim types**:
| Type | Description | Example |
|------|-------------|---------|
| `definition` | Defines a term or concept | "A closure is a function that..." |
| `fact` | Factual statement | "JavaScript has 7 primitive types" |
| `procedure` | How to do something | "To create a generator, use function\*" |
| `comparison` | Contrasts two things | "Unlike var, let is block-scoped" |
| `warning` | Common mistake or gotcha | "Don't use == for equality checks" |
| `example` | Illustrative code or scenario | "For instance: `const add = (a,b) => a+b`" |

**ID format**: `claim_<slug>_c<chunk-index>_<8-char-hash>`

Example: `claim_javascriptallonge_c007_b7f3a2ef`

- **Deterministic**: same input → same ID (reproducible)
- **Stable**: does not shift if earlier claims change (unlike sequence numbers)
- Hash derived from: `hash(normalized_claim_text + primary_evidence_locator)`

**Claim text normalization** (before hashing): Trim whitespace, collapse repeated spaces, and normalize Unicode. Do not lowercase by default because code, symbols, and proper nouns may be case-sensitive.

**Claim types** (extensible via `tags`):

- Start with the defined enum values
- Use `tags` for domain-specific categorization
- Unknown future claim types can be added without schema changes

**Benefits**:

- Judge verdicts reference claim IDs
- Repair logs reference claim IDs
- Debugging: "claim_foo_c003_a1b2c3 failed validation"
- Cross-reference: multiple pages can cite same claim

---

### 4. Track Visual/Page-Region Evidence

**Problem**: Line locators work for text, but PDFs have visual content (diagrams, tables, figures) where spatial position matters. AEC-Bench shows agents fail at visual-spatial grounding even when text is available.

**Proposed evidence schema extension**:

```json
{
  "excerpt": "See Figure 2.1",
  "locator": "normalized:L234",
  "visual": {
    "page": 12,
    "bbox": [72, 144, 300, 220],
    "render_path": "raw/normalized/<slug>/pages/page-012.png",
    "region_path": "raw/normalized/<slug>/regions/claim_000123.png"
  }
}
```

**Locator syntax extension**:

```
normalized:L100-L108           # Text lines (existing)
pdf:p12                        # Full page reference
pdf:p12:bbox(72,144,300,220)   # Bounding box on page
image:pages/page-012.png       # Page render
image:regions/claim_000123.png # Cropped region
```

**Phase 0 changes**:

- Add `--render-pages` flag with modes:
  - `never`: no page renders (default for markdown sources)
  - `auto`: render if figures/tables/images/drawings detected (default for PDFs)
  - `always`: render every page
- Store in `raw/normalized/<slug>/pages/`

**Phase 1 changes**:

- If claim references figure/table, extract bbox from PDF
- Optionally crop region to `raw/normalized/<slug>/regions/`

**Phase 2 changes**:

- Synthesized pages can embed images: `![Figure 2.1](../../raw/normalized/<slug>/regions/claim_000123.png)`
- Judge can verify visual evidence exists

**Priority by source type**:

| Source type                 | Visual evidence priority |
| --------------------------- | -----------------------: |
| Plain markdown/article      |                      Low |
| Book-like PDF               |                   Medium |
| Paper with figures/tables   |                   Medium |
| Slides                      |                     High |
| Engineering/design drawings |                     High |
| Image-heavy corpus          |                     High |

**Implementation priority**: LOW by default, HIGH for visual-heavy PDFs/slides/drawings.

---

### 5. Add Idempotency Rules

| Phase               | Rerun Behavior  | Rule                                                         |
| ------------------- | --------------- | ------------------------------------------------------------ |
| Phase 0 import      | **Fail**        | Never overwrite `raw/imported/<slug>/`                       |
| Phase 0 normalize   | **Conditional** | Overwrite only if original hash matches (`--reuse-imported`) |
| Phase 1a extract    | **Resume**      | Skip completed chunks; `--force` redoes all                  |
| Phase 1b dedupe     | **Overwrite**   | Always regenerate from claims-raw.jsonl                      |
| Phase 1c candidates | **Overwrite**   | Always regenerate from claims-normalized.json                |
| Phase 2a source     | **Overwrite**   | Regenerate from current state                                |
| Phase 2b synthesize | **Worktree**    | Always write to disposable worktree first                    |
| Phase 2c adopt      | **Conditional** | Copy only if validation passes                               |
| Phase 3a index      | **Rebuild**     | Deterministic rebuild from wiki/ contents                    |
| Phase 3b graph      | **Rebuild**     | Deterministic rebuild from wiki/ contents                    |
| Phase 3c lint       | **Rebuild**     | Deterministic rebuild from wiki/ contents                    |
| Phase 3d log        | **Append**      | Append-only, never overwrite                                 |

**Implementation**:

- Add `--force` flag to extraction commands
- Add `--dry-run` to all phases (already exists for most)
- Manifest tracks which phases are "complete" vs "partial"

---

### 6. Make Phase 3 Deterministic

**Current**: `wiki_index.py`, `wiki_graph.py` may have incremental mutation risks.

**Proposed**: All Phase 3 steps rebuild from source of truth.

**Source of truth**:

- `wiki/index.md` ← rebuilt from `wiki/**/*.md` frontmatter
- `wiki/_graph.json` ← rebuilt from `wiki/**/*.md` links
- `wiki/_linter-report.md` ← rebuilt from `wiki/**/*.md` validation
- `wiki/log.md` ← append-only (never rebuilt)

**Commands** (rename for clarity):

```bash
pnpm wiki:rebuild-index   # was wiki:index
pnpm wiki:rebuild-graph   # was wiki:graph
pnpm wiki:lint            # unchanged
pnpm wiki:append-log      # explicit append
```

**Verification commands**:

```bash
pnpm wiki:index:check     # existing
pnpm wiki:graph:check     # existing
```

**Implementation**:

- `wiki_index.py` already rebuilds; ensure it's fully deterministic
- `wiki_graph.py` already rebuilds; ensure no stale state
- Add `wiki_append_log.py` for structured log appends

---

### 7. Add Failure Artifacts

**Problem**: When Phase 2 fails validation or judging, useful drafts are silently lost.

**Proposed**: Write failure artifacts for debugging and retry.

**Location**: `.wiki-extraction-state/<slug>/failures/<page-slug>.json`

**Schema**:

```json
{
  "candidate_page": "../concepts/closures.md",
  "attempted_at": "2026-05-08T11:30:00Z",
  "draft_path": ".wiki-worktrees/javascriptallonge-concepts-closures/wiki/concepts/closures.md",
  "validation_result": {
    "passed": false,
    "errors": [
      { "type": "missing_section", "section": "Source-backed details" },
      { "type": "bad_locator", "locator": "normalized:L9999", "claim_row": 3 }
    ]
  },
  "judge_result": {
    "passed": false,
    "verdicts": [
      {
        "claim_id": "claim_foo_c003_a1b2c3",
        "verdict": "not_supported",
        "reason": "..."
      }
    ]
  },
  "repair_attempted": true,
  "repair_result": "partial",
  "repair_errors_remaining": 1,
  "worktree_preserved": true,
  "next_action": "retry"
}
```

**Allowed `next_action` values**:

- `retry` — Attempt synthesis again with same or different model
- `inspect_manually` — Requires human review of draft
- `suppress_candidate` — Do not attempt this candidate again
- `needs_more_evidence` — Candidate lacks sufficient source claims

**Benefits**:

- Debug why specific pages fail
- Retry failed pages with `--retry-failed`
- Preserve drafts for human review
- Track which claims are hard to ground

**Commands**:

```bash
pnpm wiki:phase2-failures <slug>                    # List failed pages
pnpm wiki:phase2-retry <slug> <page-slug>           # Retry one failed page
pnpm wiki:phase2-retry-all <slug>                   # Retry all failed pages
pnpm wiki:phase2-clean-failures <slug> --older-than 30d  # Explicit cleanup only
```

**Cleanup policy**: No automatic cleanup. Failure artifacts are audit/debug state. Add explicit cleanup tooling only.

**Worktree path convention**:

```
.wiki-worktrees/<slug>-<candidate-page-type>-<candidate-page-slug>/
```

Example: `.wiki-worktrees/javascriptallonge-concepts-closures/wiki/concepts/closures.md`

This keeps worktrees organized by source slug, page type, and candidate name, preventing collisions when two candidates share the same slug under different directories (e.g., `../concepts/state.md` vs `../references/state.md`).

---

### 8. Add Minimal Acceptance Contract

**Definition of done for `pnpm wiki:ingest`**:

```
ACCEPTANCE CONTRACT

A successful ingest MUST satisfy:

□ Phase 0 - Import
  □ Original file exists at raw/imported/<slug>/original.{pdf,md}
  □ Original file hash recorded in manifest

□ Phase 0 - Normalize
  □ Normalized source exists at raw/normalized/<slug>/source.md
  □ Normalized source is non-empty
  □ Normalized hash recorded in manifest

□ Phase 1 - Extract
  □ Extraction state exists at .wiki-extraction-state/<slug>/
  □ All chunks processed (processed_chunks == total_chunks)
  □ At least 1 claim extracted (claims.length > 0)
  □ At least 1 topic identified (topics.length > 0)
  □ candidates.override.json, if present, validates against override schema
  □ candidates.json was regenerated after latest generated/override change

□ Phase 2a - Source Page
  □ Source page exists at wiki/sources/<slug>.md
  □ Source page passes wiki:check-source validation
  □ Source page has at least 1 key claim with evidence

□ Phase 2b - Synthesized Pages
  □ At least 1 synthesized page adopted (or explicit zero-page reason logged)
  □ Every adopted page passes wiki:check-synthesis validation
  □ Every adopted page has source-backed evidence
  □ Failed candidates recorded in failures/

□ Phase 3 - Finalize
  □ wiki/index.md includes new source page
  □ wiki/_graph.json includes nodes for new pages
  □ wiki/_linter-report.md regenerated
  □ wiki/log.md has ingest entry appended

□ Manifest
  □ manifest.json shows all phases complete
  □ No phases in "partial" or "failed" state (unless --allow-partial-pages)
```

**Partial-success semantics**:

Use `--allow-partial-pages` to permit ingest success when:

- Source page was created and validates
- Extraction completed
- At least one candidate page was adopted
- Some candidates failed (recorded in `failures/`)
- Adopted pages pass validation

When partial success is allowed, the manifest records the reason:

```json
{
  "allow_partial_pages": true,
  "partial_success_reason": "3 candidate pages failed validation but failures were recorded"
}
```

This prevents silent normalization of degraded ingests—every partial success has an explicit audit trail.

**Implementation**:

- Add `pnpm wiki:verify-ingest <slug>` that checks all contract items
- `wiki:ingest` runs `wiki:verify-ingest` at the end
- Non-zero exit if any contract item fails

---

## Revised Pipeline Flow

```
pnpm wiki:ingest raw/inbox/<file.pdf> --slug <slug> --structured
  |
  +-- PHASE 0: Import + Normalize
  |     |
  |     +-- 0a: Create manifest.json with status = initialized
  |     +-- 0b: Copy to raw/imported/<slug>/original.pdf, record original_sha256
  |     +-- 0c: Extract to raw/normalized/<slug>/source.md, record normalized_sha256
  |     +-- 0d: Mark phase0 complete in manifest
  |
  +-- PHASE 1: Extract + Candidate
  |     |
  |     +-- 1a: Extract atomic claims (chunk by chunk, resumable)
  |     |       Output: claims-raw.jsonl
  |     |
  |     +-- 1b: Normalize/deduplicate claims
  |     |       Output: claims-normalized.json (with stable IDs)
  |     |
  |     +-- 1c: Propose page candidates
  |             Output: candidates.generated.json
  |             Merge:  candidates.json = generated + override
  |
  +-- PHASE 2: Synthesize + Adopt
  |     |
  |     +-- 2a: Create source page
  |     |       Output: wiki/sources/<slug>.md
  |     |       Validate: pnpm wiki:check-source
  |     |
  |     +-- 2b: For each candidate page:
  |     |       +-- Synthesize to worktree
  |     |       +-- Validate (wiki:check-synthesis)
  |     |       +-- Judge (wiki:judge-claims)
  |     |       +-- Repair if needed
  |     |       +-- Record failure or adopt
  |     |
  |     +-- 2c: Update source page Related pages links
  |
  +-- PHASE 3: Finalize (deterministic)
  |     |
  |     +-- 3a: Rebuild wiki/index.md
  |     +-- 3b: Rebuild wiki/_graph.json
  |     +-- 3c: Generate wiki/_linter-report.md
  |     +-- 3d: Append to wiki/log.md
  |
  +-- VERIFY: Check acceptance contract
        |
        +-- pnpm wiki:verify-ingest <slug>
```

---

## Implementation Priority

| Change                        | Priority | Effort | Value                         |
| ----------------------------- | -------- | ------ | ----------------------------- |
| 1. Artifact manifest          | HIGH     | Medium | Resume, audit, debug          |
| 2. Separate extract/candidate | MEDIUM   | Medium | Regenerate candidates cheaply |
| 3. Stable claim IDs           | HIGH     | Low    | Debug judge failures          |
| 4. Visual evidence            | LOW      | High   | Only for visual-heavy PDFs    |
| 5. Idempotency rules          | HIGH     | Low    | Document existing behavior    |
| 6. Deterministic Phase 3      | MEDIUM   | Low    | Already mostly there          |
| 7. Failure artifacts          | HIGH     | Medium | Debug, retry, preserve work   |
| 8. Acceptance contract        | HIGH     | Low    | Clear definition of done      |

**Recommended order**:

1. Document idempotency rules (5) - just documentation
2. Add acceptance contract (8) - test definition of done
3. Add artifact manifest (1) - enables resume
4. Add stable claim IDs (3) - improves debugging
5. Add failure artifacts (7) - preserve failed work
6. Separate extract/candidate (2) - reduce rework
7. Formalize Phase 3 as deterministic (6) - minor renames
8. Visual evidence (4) - when needed

---

## Migration Path

1. **Backwards compatible**: Existing `state.json` continues to work
2. **Gradual adoption**: New fields added to manifest as phases run
3. **No breaking changes**: Commands keep current signatures, add new ones
4. **Deprecation path**:
   - `state.json` → `claims-normalized.json` + `candidates.json`
   - `claims-raw.json` → `claims-raw.jsonl`
   - `candidates.json` → `candidates.generated.json` + `candidates.override.json` + `candidates.json`

---

## Resolved Design Decisions

These questions were raised during design and have been resolved:

### 1. Claim IDs: UUIDs or deterministic hashes?

**Decision**: Use deterministic hash-based IDs.

**Format**: `claim_<slug>_c<chunk-index>_<8-char-hash>`

**Rationale**:

- Reproducible: same input → same ID
- Stable: does not shift if earlier claims change (unlike sequence numbers)
- Debuggable: chunk index visible in ID

**Hash input**: `hash(normalized_claim_text + primary_evidence_locator)`

### 2. Failure artifact cleanup?

**Decision**: No automatic cleanup by default.

**Rationale**: Failure artifacts are audit/debug state. Silent deletion loses valuable debugging information.

**Tooling**: Add explicit cleanup command only:

```bash
pnpm wiki:phase2-clean-failures <slug> --older-than 30d
```

### 3. Visual evidence: opt-in or auto-detected?

**Decision**: Both, via `--render-pages` flag.

**Options**:

- `--render-pages=never`: no page renders (default for markdown sources)
- `--render-pages=auto`: render if figures/tables/images detected (default for PDFs)
- `--render-pages=always`: render every page

### 4. Should `candidates.json` be human-editable?

**Decision**: Yes, through an override file.

**Files**:

```
candidates.generated.json  # Machine-generated (regenerable)
candidates.override.json   # Human curator additions/removals
candidates.json            # Merged result = generated + override
```

**Rationale**: Preserves regeneration while allowing curator control. Human curation happens through override files, not by editing generated state directly.
