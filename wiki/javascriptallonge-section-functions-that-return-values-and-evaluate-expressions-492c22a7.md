---
page_id: javascriptallonge-section-functions-that-return-values-and-evaluate-expressions-492c22a7
page_kind: source
summary: **functions that return values and evaluate expressions**: 10 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functions-that-return-values-and-evaluate-expressions-492c22a7@98c85c63575b6a62c38ef3e0015ea335
---

# **functions that return values and evaluate expressions**

From [[javascriptallonge]].

## Statements

- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00283))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00285))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00286))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-83ecb080-00286))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00291))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00285))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00287))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00291))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00292))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.
