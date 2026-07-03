---
page_id: javascriptallonge-recipe-once
page_kind: recipe
page_family: recipe-pattern
summary: Once: reusable source-backed pattern with 2 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: once
projection_coverage: recipe-javascriptallonge-recipe-once@7b2233b155d040da3f517d7de8f5225e
---

# Once

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-once-99d6b11d]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-7239e085-00710))_
- once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-7239e085-00710))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00711)_

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00713)_

```
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-once-99d6b11d]]
