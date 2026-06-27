---
page_id: javascriptallonge-section-floating-991c07a5
page_kind: source
summary: **floating**: 20 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-floating-991c07a5@a5d6f142f383382067de5f001eb334c4
---

# **floating**

From [[javascriptallonge]].

## Statements

- We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- Most programmers never encounter the limit on the magnitude of an integer. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Nooooooooooooooooooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- > 14Implementations of JavaScript are free to handle larger numbers. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. _(javascriptallonge.pdf (source-range-83ecb080-00237))_
- In this book, we need not think about such details, but outside of this book, we must. _(javascriptallonge.pdf (source-range-83ecb080-00237))_
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic[15] . _(javascriptallonge.pdf (source-range-83ecb080-00237))_
- For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. _(javascriptallonge.pdf (source-range-83ecb080-00237))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00226))_

> One of the most oft-repeated examples is this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00228))_

> - 1.0 + 1.0 _//=> 2_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00226))_

> One of the most oft-repeated examples is this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00229))_

> - 1.0 + 1.0 + 1.0 _//=> 3_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00232))_

> > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00235))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00236))_

> This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00236))_

> This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00237))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.
