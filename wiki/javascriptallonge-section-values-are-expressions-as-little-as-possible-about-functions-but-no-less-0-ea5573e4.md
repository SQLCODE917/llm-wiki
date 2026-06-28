---
page_id: javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-0-ea5573e4
page_kind: source
summary: values are expressions / As Little As Possible About Functions, But No Less / () => 0: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-0-ea5573e4@f74501bc28c49947b0085c11b3950a11
---

# values are expressions / As Little As Possible About Functions, But No Less / () => 0

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-e91633ac]] - broader source section

## Statements

- This is a function that is applied to no values and returns 0. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. _(javascriptallonge.pdf (source-range-83ecb080-00225))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00220))_

> This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00221))_

> If you try the same thing in a browser, you may see something else.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00221))_

> (() => 0) _//=> [Function]_ What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00222))_

> > 16 The simplest possible function is () => {}, we’ll see that later.
