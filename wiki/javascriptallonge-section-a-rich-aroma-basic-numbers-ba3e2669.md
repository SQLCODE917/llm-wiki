---
page_id: javascriptallonge-section-a-rich-aroma-basic-numbers-ba3e2669
page_kind: source
summary: A Rich Aroma: Basic Numbers: 38 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-rich-aroma-basic-numbers-ba3e2669@bf72a068f3a77a26300f4ac7f970258c
---

# A Rich Aroma: Basic Numbers

From [[javascriptallonge]].

## Statements

- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- In computer science, a literal is a notation for representing a fixed value in source code. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- We saw that an expression consisting solely of numbers, like 42, is a literal. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- It represents the number forty-two, which is 42 base 10. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- all numbers are base ten. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- If we start a literal with a zero, it is an octal literal. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- A computer’s internal representation for numbers is important to understand. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- Internally, both 042 and 34 have the same representation, as double-precision floating point[13] numbers. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
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
- As we’ve seen, JavaScript has many common arithmetic operators. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- These can be combined to make more complex expressions, like 2 * 5 + 1. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. _(javascriptallonge.pdf (source-range-83ecb080-00240))_
- JavaScript has many more operators. _(javascriptallonge.pdf (source-range-83ecb080-00242))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00221))_

> The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.”

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00226))_

> One of the most oft-repeated examples is this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00228))_

> - 1.0 + 1.0 _//=> 2_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00226))_

> One of the most oft-repeated examples is this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00229))_

> - 1.0 + 1.0 + 1.0 _//=> 3_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00232))_

> > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00235))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00236))_

> This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00236))_

> This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00237))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240, source-range-83ecb080-00242))_

> In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the nam

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00241))_

> 2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_
