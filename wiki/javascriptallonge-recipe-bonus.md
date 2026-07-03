---
page_id: javascriptallonge-recipe-bonus
page_kind: recipe
page_family: recipe-pattern
summary: bonus: reusable source-backed pattern with 6 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: bonus
projection_coverage: recipe-javascriptallonge-recipe-bonus@f0c121a1fbee97627425b79986c63b6b
---

# bonus

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-bonus-6b4a06d7]].
- Evidence roles: decision, constraint, explanation, procedure, example.

## Applicability And Rationale

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-7239e085-01316))_
- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-7239e085-01316))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-7239e085-01319))_
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. _(javascriptallonge.pdf (source-range-7239e085-01321))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-7239e085-01321))_
- And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-7239e085-01321))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01318)_

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01320)_

```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-bonus-6b4a06d7]]
