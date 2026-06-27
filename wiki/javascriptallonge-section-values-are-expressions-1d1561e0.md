---
page_id: javascriptallonge-section-values-are-expressions-1d1561e0
page_kind: source
summary: values are expressions: 19 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-1d1561e0@a99a1d376db85efb56cf0adecc283c4a
---

# values are expressions

From [[javascriptallonge]].

## Statements

- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- Yup, you hand over a cup with some coffee infused through partially caramelized sugar. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00168))_
- Instead of handing over the finished coffee, we can hand over the ingredients. _(javascriptallonge.pdf (source-range-83ecb080-00168))_
- Astute readers will realize we’re omitting something. _(javascriptallonge.pdf (source-range-83ecb080-00169))_
- Ground coffee is a value. _(javascriptallonge.pdf (source-range-83ecb080-00170))_
- So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. _(javascriptallonge.pdf (source-range-83ecb080-00170))_
- Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00170))_
- You and I both understand that this means “42,” and so does the computer. _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- You and I both understand that this means “42,” and so does the computer. _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- > 11In some languages, expressions are a kind of value unto themselves and can be manipulated. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- The grandfather of such languages is Lisp. _(javascriptallonge.pdf (source-range-83ecb080-00175))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00162))_

> Let’s try this with something the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00165))_

> The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00168))_

> All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00170))_

> And if we hand over the espresso, we get the espresso right back.

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00178))_

> Now we see that “strings” are values, and you can make an expression out of strings and an operator +. Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our “coffee grounds plus hot water” example. The coffee grounds were a value, the boiling hot water was a value, and the “plus” operator between them made the whole thing an expression that was not a value.
