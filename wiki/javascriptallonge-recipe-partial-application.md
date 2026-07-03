---
page_id: javascriptallonge-recipe-partial-application
page_kind: recipe
page_family: recipe-pattern
summary: partial application: reusable source-backed pattern with 9 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: partial-application
projection_coverage: recipe-javascriptallonge-recipe-partial-application@bbd0adfc06291f3ac15fbb4509e303f8
---

# partial application

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-building-blocks-partial-application-a5e51d71]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Another basic building block is partial application . _(javascriptallonge.pdf (source-range-7239e085-00591))_
- In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-7239e085-00591))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-7239e085-00592))_
- The Underscore 39 library provides a higher-order function called map . _(javascriptallonge.pdf (source-range-7239e085-00592))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. _(javascriptallonge.pdf (source-range-7239e085-00597))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-7239e085-00597))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00593)_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00596)_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00598)_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00601)_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00602)_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-building-blocks-partial-application-a5e51d71]]
