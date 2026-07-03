---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-96b730f4
page_kind: source
page_family: section-reference
summary: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-96b730f4@012e6b5238ee315555b8dfae1962ae72
---

# Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-d00f2bc0]] - broader source section: Recipes with Basic Functions / Left-Variadic Functions

## Statements

- That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function? _(javascriptallonge.pdf (source-range-7239e085-00735))_
- We sure can, by using the techniques from rightVariadic . Mind you, we can take advantage of modern JavaScript to simplify the code: _(javascriptallonge.pdf (source-range-7239e085-00736))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. _(javascriptallonge.pdf (source-range-7239e085-00739))_
