---
page_id: javascriptallonge-recipe-functions-that-return-values-and-evaluate-expressions
page_kind: recipe
page_family: recipe-pattern
summary: functions that return values and evaluate expressions: reusable source-backed pattern with 7 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: functions-that-return-values-and-evaluate-expressions
projection_coverage: recipe-javascriptallonge-recipe-functions-that-return-values-and-evaluate-expressions@d91a774b6011aeda3a15535d92448021
---

# functions that return values and evaluate expressions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-953101e3]].
- Evidence roles: decision, constraint, explanation, example, structured-state.

## Applicability And Rationale

- We know that (() => 0)() returns 0 , and this is unsurprising. _(javascriptallonge.pdf (source-range-7239e085-00188))_
- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-7239e085-00190))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-7239e085-00191))_
- Values like 0 are expressions, as are things like 40 + 2 . _(javascriptallonge.pdf (source-range-7239e085-00191))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-7239e085-00193))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-7239e085-00193))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00189)_

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00192)_

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00195)_

```
(() => (() => 0)())()
//=> 0
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00198)_

```
(() =>
(() => 0
)()
)()
//=> 0
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-953101e3]]
