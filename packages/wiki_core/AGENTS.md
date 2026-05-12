# wiki_core — Package Rules

> Pure types and parsing utilities. No I/O, no network, no LLM calls.

---

## Purpose

This package provides the foundational types and pure functions used throughout
the wiki ingestion pipeline. It has **zero side effects** — no file reads, no
network calls, no state mutation.

---

## Design constraints

1. **No I/O.** Functions must not read files, write files, or make network requests.
2. **No LLM dependencies.** This package cannot import `wiki_llm` or any LLM SDK.
3. **No wiki_io dependency.** This package cannot import `wiki_io`.
4. **Deterministic.** Given the same inputs, functions must return the same outputs.
5. **Minimal dependencies.** Standard library only; no third-party packages.

---

## Module structure

```
wiki_core/
├── types/           # Dataclasses and type definitions
│   ├── claim.py     # Claim, RawClaim, NormalizedClaim, SynthesisClaim, SourceClaim
│   ├── locator.py   # Locator class with parse/normalize/overlap logic
│   └── frontmatter.py  # Frontmatter, PageType, PageStatus
└── parsing/         # Pure text processing
    ├── markdown.py  # strip_markdown(), normalize_for_search()
    ├── tables.py    # split_table_row(), table_rows(), is_separator_row()
    └── evidence.py  # clean_evidence_excerpt()
```

---

## Import conventions

```python
# Preferred: import types from package root
from wiki_core import Claim, Locator, Frontmatter

# Also valid: import from submodules
from wiki_core.types import NormalizedClaim, RawClaim
from wiki_core.parsing import strip_markdown, table_rows
```

---

## Testing

Tests live in `tools/test_wiki_core_*.py`. Run with:

```bash
cd tools && python -m pytest test_wiki_core_types.py test_wiki_core_parsing.py -v
```

Before merging changes to this package:
1. All existing tests must pass.
2. New public functions must have tests.
3. Type hints are required on all public functions.

---

## When to add code here

Add code to `wiki_core` when:
- It defines a data structure used across multiple tools
- It performs text transformation without reading/writing files
- It needs to be imported by both `wiki_io` and `wiki_llm`

Do **not** add code here if it:
- Reads or writes files → use `wiki_io`
- Calls an LLM API → use `wiki_llm`
- Is specific to one CLI tool → keep in `tools/`
