---
page_id: javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-void-a81e28f2
page_kind: source
summary: values are expressions / As Little As Possible About Functions, But No Less / void: 5 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-void-a81e28f2@0a52078326379d2aff30974967b601b5
---

# values are expressions / As Little As Possible About Functions, But No Less / void

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-e91633ac]] - broader source section

## Statements

- We’ve seen that JavaScript represents an undefined value by typing undefined, and we’ve generated undefined values in two ways: _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. _(javascriptallonge.pdf (source-range-83ecb080-00278))_
- Behold: **void** 0 _//=> undefined_ **void** 1 _//=> undefined_ **void** (2 + 2) _//=> undefined_ void is an operator that takes any value and evaluates to undefined, always. _(javascriptallonge.pdf (source-range-83ecb080-00278))_
- The first form works but it’s cumbersome. _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we’ll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-83ecb080-00279))_
