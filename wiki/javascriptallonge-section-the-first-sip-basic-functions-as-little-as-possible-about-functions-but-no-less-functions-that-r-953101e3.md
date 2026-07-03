---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-953101e3
page_kind: source
page_family: section-reference
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: 13 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-953101e3@bf51e0c8a6d033b036d0014b1d9a96cf
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-0ed59777]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-7239e085-00188))_
- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-7239e085-00190))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-7239e085-00191))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-7239e085-00193))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-7239e085-00196))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-7239e085-00193))_
