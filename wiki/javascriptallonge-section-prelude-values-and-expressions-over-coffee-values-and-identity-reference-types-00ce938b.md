---
page_id: javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-reference-types-00ce938b
page_kind: source
summary: Prelude: Values and Expressions over Coffee / values and identity / reference types: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-reference-types-00ce938b@fb26159a6195a51c062dc44cbf56dfda
---

# Prelude: Values and Expressions over Coffee / values and identity / reference types

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-7389665c]] - broader source section: Prelude: Values and Expressions over Coffee / values and identity

## Statements

- An array looks like this: [1, 2, 3] . This is an expression, and you can combine [] with other expressions. Go wild with things like: _(javascriptallonge.pdf (source-range-7239e085-00132))_
- Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself: _(javascriptallonge.pdf (source-range-7239e085-00134))_
- How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom. _(javascriptallonge.pdf (source-range-7239e085-00136))_
- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-7239e085-00137))_

## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values and identity / reference types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00134))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00133))_

```
[2-1, 2, 2+1]
[1, 1+1, 1+1+1]
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values and identity / reference types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00136))_

> How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00135))_

```
[2-1, 2, 2+1] === [1,2,3]
[1,2,3] === [1, 2, 3]
[1, 2, 3] === [1, 2, 3]
```
