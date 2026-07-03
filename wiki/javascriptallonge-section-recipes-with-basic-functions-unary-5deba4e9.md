---
page_id: javascriptallonge-section-recipes-with-basic-functions-unary-5deba4e9
page_kind: source
page_family: section-reference
summary: Recipes with Basic Functions / Unary: 15 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-unary-5deba4e9@9e1dbf6347336a95d81745f958e15900
---

# Recipes with Basic Functions / Unary

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-c9137465]] - broader source section: Recipes with Basic Functions

## Statements

- The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: _(javascriptallonge.pdf (source-range-7239e085-00669))_
- If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: _(javascriptallonge.pdf (source-range-7239e085-00674))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-7239e085-00676))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_
