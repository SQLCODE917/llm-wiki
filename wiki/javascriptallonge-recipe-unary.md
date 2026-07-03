---
page_id: javascriptallonge-recipe-unary
page_kind: recipe
page_family: recipe-pattern
summary: Unary: reusable source-backed pattern with 6 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: unary
projection_coverage: recipe-javascriptallonge-recipe-unary@3e5fc3bba538842c5d0fb33f8bc77116
---

# Unary

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-unary-5deba4e9]].
- Evidence roles: decision, explanation, definition, example, structured-state.

## Applicability And Rationale

- The most common use case is to fix a problem. _(javascriptallonge.pdf (source-range-7239e085-00669))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-7239e085-00669))_
- But some functions have optional second or even third arguments. _(javascriptallonge.pdf (source-range-7239e085-00674))_
- And when you call parseInt with map , the index is interpreted as a radix. _(javascriptallonge.pdf (source-range-7239e085-00676))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-7239e085-00676))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00670)_

```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00673)_

```
[1, 2, 3].map(function (element, index, arr) {
console.log({element: element, index: index, arr: arr})
})
//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] }
//
{ element: 2, index: 1, arr: [ 1, 2, 3 ] }
//
{ element: 3, index: 2, arr: [ 1, 2, 3 ] }
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00675)_

```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00678)_

```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00680)_

```
['1', '2', '3'].map(unary(parseInt))
//=> [1, 2, 3]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-unary-5deba4e9]]
