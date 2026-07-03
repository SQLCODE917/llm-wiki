---
page_id: javascriptallonge-recipe-function-decorators
page_kind: recipe
page_family: recipe-pattern
summary: function decorators: reusable source-backed pattern with 1 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-decorators
projection_coverage: recipe-javascriptallonge-recipe-function-decorators@525404c09cc6ca2707e1d3e1a6855133
---

# function decorators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-913f90c6]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-7239e085-00578))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00571)_

```
const not = (fn) => (x) => !fn(x)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00573)_

```
const something = (x) => x != null;
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00575)_

```
const nothing = (x) => !something(x);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00577)_

```
const nothing = not(something);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-913f90c6]]
