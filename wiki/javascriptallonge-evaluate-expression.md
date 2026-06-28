---
page_id: javascriptallonge-evaluate-expression
page_kind: concept
summary: Evaluate Expression: 4 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-evaluate-expression@aec8c7241a2a2867e26e7a99a2b82ae5
---

# Evaluate Expression

What [[javascriptallonge]] covers about evaluate expression:

## Statements

- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-83ecb080-00241))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00241))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00243))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00243))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00244))_

> Let’s try it: (() => (() => 0)())() _//=> 0_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00246))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00248))_

> The first sip: Basic Functions (() => (() => 0 )() )() _//=> 0_


## Related pages

- [[javascriptallonge-expression]] - broader topic (2 shared atom(s))
- [[javascriptallonge-evaluate]] - broader topic
- [[javascriptallonge-function-return-value]] - shared statements (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
