---
page_id: javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-commas-49c0b74b
page_kind: source
summary: values are expressions / As Little As Possible About Functions, But No Less / commas: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-commas-49c0b74b@1b76a55e0a336d359132892fd291b7d6
---

# values are expressions / As Little As Possible About Functions, But No Less / commas

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-e91633ac]] - broader source section

## Statements

- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-83ecb080-00251))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00255))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00251))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00253))_

> (1 + 1, 2 + 2) _//=> 4_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00251))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00254))_

> We can use commas with functions to create functions that evaluate multiple expressions: (() => (1 + 1, 2 + 2))() _//=> 4_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00254))_

> We can use commas with functions to create functions that evaluate multiple expressions: (() => (1 + 1, 2 + 2))() _//=> 4_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00255))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later.
