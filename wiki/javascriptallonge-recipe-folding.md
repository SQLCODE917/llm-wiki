---
page_id: javascriptallonge-recipe-folding
page_kind: recipe
page_family: recipe-pattern
summary: folding: reusable source-backed pattern with 3 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: folding
projection_coverage: recipe-javascriptallonge-recipe-folding@2fa1a8e2bcf5bd345e950ddb293ca985
---

# folding

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-6afcd1fe]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-7239e085-00936))_
- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-7239e085-00945))_
- We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-7239e085-00945))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00937)_

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00942)_

```
const foldWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldWith(fn, terminalValue, rest));
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00944)_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00946)_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00948)_

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\
], array),
squareAll = (array) => mapWith((x) => x * x, array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00950)_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-6afcd1fe]]
