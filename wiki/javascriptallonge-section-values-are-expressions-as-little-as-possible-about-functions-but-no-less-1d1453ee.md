---
page_id: javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-1d1453ee
page_kind: source
summary: values are expressions / As Little As Possible About Functions, But No Less / (() => {})(): 8 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-1d1453ee@0848e063ef2d66eca3814a9c54fce04e
---

# values are expressions / As Little As Possible About Functions, But No Less / (() => {})()

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-e91633ac]] - broader source section

## Statements

- There are many kinds of JavaScript statements, but the first kind is one we’ve already met. _(javascriptallonge.pdf (source-range-83ecb080-00289))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-83ecb080-00289))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- > 21You can also separate statements with line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- This feature was originally created as a kind of helpful error-correction. _(javascriptallonge.pdf (source-range-83ecb080-00290))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00293))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example: (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_ And also: (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00294))_

> The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
