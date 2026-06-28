---
page_id: javascriptallonge-block
page_kind: concept
summary: Block: 11 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-block@8ae909d7775d1b4a61a5cb5fb477ce4f
---

# Block

What [[javascriptallonge]] covers about block:

## Statements

- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-83ecb080-00314))_
- We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00612))_
- Another basic building block is _partial application_ . _(javascriptallonge.pdf (source-range-83ecb080-00839))_
- Block bodies evaluate to whatever is returned with the return keyword, or to undefined. _(javascriptallonge.pdf (source-range-83ecb080-00913))_
- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-83ecb080-00917))_
- In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. _(javascriptallonge.pdf (source-range-83ecb080-00931))_
- Let’s start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the “Kestrel”, the “Idiot Bird”, and the “Vireo:” _(javascriptallonge.pdf (source-range-83ecb080-02044))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00039))_

> For example, block-structured languages allow us to write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00040))_

> **for** ( **int** i = 0; i < array.length; ++i) {

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00354))_

> (() => { 2 + 2 })() _//=> undefined_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00355))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00356))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_


## Related pages

- [[javascriptallonge-evaluate]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-return]] - shared statements (2 shared statement(s))
- [[javascriptallonge-bind]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
