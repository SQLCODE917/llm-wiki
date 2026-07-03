---
page_id: javascriptallonge-recipe-flipping-methods
page_kind: recipe
page_family: recipe-pattern
summary: flipping methods: reusable source-backed pattern with 1 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: flipping-methods
projection_coverage: recipe-javascriptallonge-recipe-flipping-methods@408687dd1098fdf5512caaab2e1101da
---

# flipping methods

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-79368074]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. _(javascriptallonge.pdf (source-range-7239e085-01470))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01471)_

```
const flipAndCurry = (fn) =>
(first) =>
function (second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn.call(this, second, first);
}
else {
return function (second) {
return fn.call(this, second, first);
};
};
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-79368074]]
