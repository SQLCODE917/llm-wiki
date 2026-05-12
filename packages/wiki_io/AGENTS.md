# wiki_io — Package Rules

> I/O layer for state management, evidence handling, and file operations.

---

## Purpose

This package handles all file I/O for the wiki ingestion pipeline:
- Reading and writing extraction state (manifests, claims, candidates)
- Evidence resolution and validation
- Path utilities for the `.wiki-extraction-state/` directory

---

## Design constraints

1. **Depends on wiki_core only.** May import `wiki_core` types; must not import `wiki_llm`.
2. **No LLM calls.** Evidence validation uses deterministic text matching, not LLM judgment.
3. **Idempotent where possible.** Re-running a function with same inputs should be safe.
4. **Paths are relative to repo root.** Functions assume CWD is the repository root.

---

## Module structure

```
wiki_io/
├── state/           # Extraction state management
│   ├── paths.py     # get_state_dir(), get_*_path() utilities
│   ├── manifest.py  # Manifest, PhaseStatus, ErrorInfo
│   ├── claims.py    # RawClaim, NormalizedClaim storage
│   └── candidates.py  # Candidate, overrides, merge logic
└── evidence/        # Evidence handling
    ├── resolver.py  # EvidenceResolver, stable_evidence_id()
    ├── validator.py # validate_evidence_location(), canonicalize_for_evidence_match()
    └── ranges.py    # SourceRange, parse_locator_range(), locator_within_ranges()
```

---

## Import conventions

```python
# Preferred: import from submodules
from wiki_io.state import Manifest, PhaseStatus, load_normalized_claims
from wiki_io.evidence import EvidenceResolver, validate_evidence_location

# Types from wiki_core should be imported from wiki_core, not re-exported
from wiki_core import Claim, Locator  # correct
```

---

## State directory layout

All extraction state lives under `.wiki-extraction-state/<slug>/`:

```
.wiki-extraction-state/
└── js-allonge/
    ├── manifest.json           # Pipeline status and config
    ├── claims-raw.jsonl        # Append-only extracted claims
    ├── claims-normalized.json  # Deduplicated claims with stable IDs
    ├── candidates.generated.json  # Machine-generated page proposals
    ├── candidates.override.json   # Human curator overrides
    └── candidates.json         # Merged candidates (generated + override)
```

---

## Evidence ID format

Stable evidence IDs follow the pattern: `<slug>:<claim_id>`

Example: `js-allonge:claim_jsallonge_c001_abc12345`

The `EvidenceResolver` class resolves these IDs to full claim metadata including
the exact source excerpt and locator.

---

## Testing

Tests live in:
- `packages/wiki_io/tests/test_evidence_*.py` (unit tests)
- `tools/test_wiki_io_state.py` (integration tests)

Run with:

```bash
python -m pytest packages/wiki_io/tests/ -v
cd tools && python -m pytest test_wiki_io_state.py -v
```

Before merging changes:
1. All tests must pass.
2. Changes to state file formats require updating `SCHEMA_VERSION`.
3. Backward compatibility with existing `.wiki-extraction-state/` data is required.

---

## When to add code here

Add code to `wiki_io` when:
- It reads or writes files in `.wiki-extraction-state/`
- It validates evidence against source files
- It manages pipeline state (manifests, progress tracking)

Do **not** add code here if it:
- Is a pure data type with no I/O → use `wiki_core`
- Calls an LLM API → use `wiki_llm`
- Is a CLI entry point → keep in `tools/`
