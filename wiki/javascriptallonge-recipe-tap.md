---
page_id: javascriptallonge-recipe-tap
page_kind: recipe
page_family: recipe-pattern
summary: Tap: reusable source-backed pattern with 3 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: tap
projection_coverage: recipe-javascriptallonge-recipe-tap@d4019c0d8c187b31e1a247dbe35643fd
---

# Tap

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-tap-904019d9]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-7239e085-00685))_
- It has some surprising applications. _(javascriptallonge.pdf (source-range-7239e085-00685))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-7239e085-00693))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00684)_

```
const K = (x) => (y) => x;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00686)_

```
const tap = (value) =>
(fn) => (
typeof(fn) === 'function' && fn(value),
value
)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00691)_

```
const tap = (value, fn) => {
const curried = (fn) => (
typeof(fn) === 'function' && fn(value),
value
);
return fn === undefined
? curried
: curried(fn);
}
Now we can write:
tap('espresso')((it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
Or:
tap('espresso', (it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-tap-904019d9]]
