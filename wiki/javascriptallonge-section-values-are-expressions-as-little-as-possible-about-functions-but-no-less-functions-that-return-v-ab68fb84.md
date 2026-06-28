---
page_id: javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-functions-that-return-v-ab68fb84
page_kind: source
summary: values are expressions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: 13 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-functions-that-return-v-ab68fb84@f0f325ac74ce9d8fdc0144ce8a8c84d3
---

# values are expressions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-e91633ac]] - broader source section

## Statements

- Likewise, the following all ought to be obvious: (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_ _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00240))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-83ecb080-00241))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00241))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00245))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00242))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00243))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00244))_

> Let’s try it: (() => (() => 0)())() _//=> 0_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00245))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00246))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00246))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00248))_

> The first sip: Basic Functions (() => (() => 0 )() )() _//=> 0_
