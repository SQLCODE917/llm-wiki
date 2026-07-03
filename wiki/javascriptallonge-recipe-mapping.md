---
page_id: javascriptallonge-recipe-mapping
page_kind: recipe
page_family: recipe-pattern
summary: mapping: reusable source-backed pattern with 3 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: mapping
projection_coverage: recipe-javascriptallonge-recipe-mapping@b6e98dd71b9e064e4f8682631d78d8d4
---

# mapping

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-mapping-d1acef31]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- Another common problem is applying a function to every element of an array. _(javascriptallonge.pdf (source-range-7239e085-00925))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-7239e085-00930))_
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-7239e085-00933))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00927)_

```
const squareAll = ([first, ...rest]) => first === undefined
? []
: [first * first, ...squareAll(rest)\
];
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00929)_

```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00932)_

```
const mapWith = (fn, array) => // ...
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00934)_

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
mapWith((x) => !!x, [null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-mapping-d1acef31]]
