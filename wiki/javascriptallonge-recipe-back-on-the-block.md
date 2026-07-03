---
page_id: javascriptallonge-recipe-back-on-the-block
page_kind: recipe
page_family: recipe-pattern
summary: back on the block: reusable source-backed pattern with 9 statement(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: back-on-the-block
projection_coverage: recipe-javascriptallonge-recipe-back-on-the-block@158fe5b8614059a97dbad8f6507134e7
---

# back on the block

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-back-on-the-block-b9587c98]].
- Evidence roles: decision, constraint, procedure, example, structured-state.

## Applicability And Rationale

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. _(javascriptallonge.pdf (source-range-7239e085-00236))_
- There are many kinds of JavaScript statements, but the first kind is one we've already met. _(javascriptallonge.pdf (source-range-7239e085-00239))_
- Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-7239e085-00239))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-7239e085-00239))_
- This feature was originally created as a kind of helpful error-correction. _(javascriptallonge.pdf (source-range-7239e085-00246))_
- 21 You can also separate statements with line breaks. _(javascriptallonge.pdf (source-range-7239e085-00246))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00235)_

```
(() => {})()
//=> undefined
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00240)_

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00242)_

```
() => {
1 + 1;
2 + 2
}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00244)_

```
(() => { 2 + 2 })()
//=> undefined
(() => { 1 + 1; 2 + 2 })()
//=> undefined
(() => {
1 + 1;
2 + 2
})()
//=> undefined
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00247)_

```
(() => 2 + 2)()
//=> 4
(() => { 2 + 2 })()
//=> undefined
(() => (1 + 1, 2 + 2))()
//=> 4
(() => { 1 + 1; 2 + 2 })()
//=> undefined
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00249)_

```
(() => { return 0 })()
//=> 0
(() => { return 1 })()
//=> 1
(() => { return 'Hello ' + 'World' })()
// 'Hello World'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-or-even-back-on-the-block-b9587c98]]
