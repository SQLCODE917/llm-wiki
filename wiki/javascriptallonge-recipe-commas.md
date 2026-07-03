---
page_id: javascriptallonge-recipe-commas
page_kind: recipe
page_family: recipe-pattern
summary: commas: reusable source-backed pattern with 2 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: commas
projection_coverage: recipe-javascriptallonge-recipe-commas@d81aa3de659a73da58a4c2444bbccd1e
---

# commas

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-613f6e9a]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-7239e085-00201))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-7239e085-00205))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00202)_

```
//=> 2
(1 + 1, 2 + 2)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00204)_

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00206)_

```
() =>
(1 + 1, 2 + 2)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-613f6e9a]]
