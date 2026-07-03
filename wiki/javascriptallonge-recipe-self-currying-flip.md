---
page_id: javascriptallonge-recipe-self-currying-flip
page_kind: recipe
page_family: recipe-pattern
summary: self-currying flip: reusable source-backed pattern with 1 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: self-currying-flip
projection_coverage: recipe-javascriptallonge-recipe-self-currying-flip@16c61181a2f4203dfa10374d6c397b55
---

# self-currying flip

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-3aa1de4b]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-7239e085-01466))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01467)_

```
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn(second, first);
}
else {
return function (second) {
return fn(second, first);
};
};
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-3aa1de4b]]
