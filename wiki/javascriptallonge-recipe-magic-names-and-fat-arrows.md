---
page_id: javascriptallonge-recipe-magic-names-and-fat-arrows
page_kind: recipe
page_family: recipe-pattern
summary: magic names and fat arrows: reusable source-backed pattern with 15 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: magic-names-and-fat-arrows
projection_coverage: recipe-javascriptallonge-recipe-magic-names-and-fat-arrows@04e7990da66a7dcfdc0622cd037dc353
---

# magic names and fat arrows

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-magic-names-magic-names-and-fat-arrows-a644f644]].
- Evidence roles: decision, definition, explanation, procedure, constraint, example.

## Applicability And Rationale

- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-7239e085-00620))_
- 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-7239e085-00625))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. _(javascriptallonge.pdf (source-range-7239e085-00625))_
- It uses mapWith , which we discussed in Building Blocks. _(javascriptallonge.pdf (source-range-7239e085-00625))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . _(javascriptallonge.pdf (source-range-7239e085-00627))_
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-7239e085-00628))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00621)_

```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00623)_

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00626)_

```
const row = function () {
return mapWith(
(column) => column * arguments[0],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00629)_

```
const row = function () {
return mapWith(
function (column) { return column * arguments[0] },
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-magic-names-magic-names-and-fat-arrows-a644f644]]
