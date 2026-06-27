---
page_id: javascriptallonge-section-reference-types-b672735f
page_kind: source
summary: **reference types**: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reference-types-b672735f@1bec368e339af9c2a127e6447d68aace
---

# **reference types**

From [[javascriptallonge]].

## Statements

- Let’s meet a data structure that is very common in contemporary programming languages, the _Array_ (other languages sometimes call it a List or a Vector). _(javascriptallonge.pdf (source-range-83ecb080-00202))_
- This is an expression, and you can combine [] with other expressions. _(javascriptallonge.pdf (source-range-83ecb080-00205))_
- Notice that you are always generating arrays with the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. _(javascriptallonge.pdf (source-range-83ecb080-00209))_
- They look the same, but if you examine them with ===, you see that they are different. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book. _(javascriptallonge.pdf (source-range-83ecb080-00210))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00205))_

> An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00206))_

> [2-1, 2, 2+1] [1, 1+1, 1+1+1]

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00207))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00208))_

> [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3]
