---
page_id: javascriptallonge-section-values-are-expressions-left-variadic-functions-overcoming-limitations-f1a43b74
page_kind: source
summary: values are expressions / Left-Variadic Functions / overcoming limitations: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-left-variadic-functions-overcoming-limitations-f1a43b74@75a0e75c41fb5c09f7dd8e609d88654f
---

# values are expressions / Left-Variadic Functions / overcoming limitations

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-left-variadic-functions-547e4e7a]] - broader source section

## Statements

- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-83ecb080-00744))_
- Mind you, we can take advantage of modern JavaScript to simplify the code: **const** leftVariadic = (fn) => { **if** (fn.length < 1) { **return** fn; } **else** { **return function** (...args) { **const** gathered = args.slice(0, args.length - fn.length + 1), spread = args.slice(args.length - fn.length + 1); **return** fn.apply( **this** , [gathered].concat(spread) 69 Recipes with Basic Functions ); } } }; **const** butLastAndLast = leftVariadic((butLast, last) => [butLast, last]); butLastAndLast('why', 'hello', 'there', 'little', 'droid') _//=> [["why","hello","there","little"],"droid"]_ Our leftVariadic function is a decorator that turns any function into a function that gathers parameters _from the left_ , instead of from the right. _(javascriptallonge.pdf (source-range-83ecb080-00745))_
- We sure can, by using the techniques from rightVariadic. _(javascriptallonge.pdf (source-range-83ecb080-00745))_
