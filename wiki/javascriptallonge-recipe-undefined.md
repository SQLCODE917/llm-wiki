---
page_id: javascriptallonge-recipe-undefined
page_kind: recipe
page_family: recipe-pattern
summary: undefined: reusable source-backed pattern with 9 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: undefined
projection_coverage: recipe-javascriptallonge-recipe-undefined@99fde11c0fef1fa98022e8a219d5b765
---

# undefined

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-the-simplest-possible-block-undefined-19cd59e5]].
- Evidence roles: decision, definition, explanation, constraint, example.

## Applicability And Rationale

- It will crop up again. _(javascriptallonge.pdf (source-range-7239e085-00217))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-7239e085-00217))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-7239e085-00220))_
- No matter how you evaluate undefined , you get an identical value back. _(javascriptallonge.pdf (source-range-7239e085-00222))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-7239e085-00223))_
- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. _(javascriptallonge.pdf (source-range-7239e085-00223))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00218)_

```
undefined
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00219)_

```
//=> undefined
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00221)_

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-or-even-the-simplest-possible-block-undefined-19cd59e5]]
