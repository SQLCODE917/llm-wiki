---
page_id: javascriptallonge-recipe-nested-blocks
page_kind: recipe
page_family: recipe-pattern
summary: nested blocks: reusable source-backed pattern with 4 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: nested-blocks
projection_coverage: recipe-javascriptallonge-recipe-nested-blocks@eebb43729135efce9e959fa9372815d8
---

# nested blocks

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-that-constant-coffee-craving-nested-blocks-e1d3b152]].
- Evidence roles: decision, explanation, procedure, structured-state, example.

## Applicability And Rationale

- But there are other kinds of blocks. _(javascriptallonge.pdf (source-range-7239e085-00438))_
- Up to now, we've only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-7239e085-00438))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. _(javascriptallonge.pdf (source-range-7239e085-00442))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-7239e085-00446))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00439)_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00441)_

```
((n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
})(13)
//=> false
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00443)_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00444)_

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00445)_

```
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-that-constant-coffee-craving-nested-blocks-e1d3b152]]
