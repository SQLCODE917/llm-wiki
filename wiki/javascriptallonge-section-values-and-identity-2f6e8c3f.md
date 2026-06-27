---
page_id: javascriptallonge-section-values-and-identity-2f6e8c3f
page_kind: source
summary: values and identity: 29 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-and-identity-2f6e8c3f@fb456e0bf1d84987d6e00b01587eeaec
---

# values and identity

From [[javascriptallonge]].

## Statements

- And then you’re shown another cup of coffee. _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- For example, the string "2" is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- One is a demitasse, the other a mug. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- This corresponds to comparing two things in JavaScript that have different _types_ . _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- First, sometimes, the cups are of different kinds. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- For example, the string "2" is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- One holds a single, one a double. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. _(javascriptallonge.pdf (source-range-83ecb080-00194))_
- This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-83ecb080-00194))_
- Third, some types of cups have no distinguishing marks on them. _(javascriptallonge.pdf (source-range-83ecb080-00194))_
- Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- We’ll use both terms interchangeably. _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- We haven’t encountered the fourth possibility yet. _(javascriptallonge.pdf (source-range-83ecb080-00198))_
- **Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia** _(javascriptallonge.pdf (source-range-83ecb080-00200))_
- Let’s meet a data structure that is very common in contemporary programming languages, the _Array_ (other languages sometimes call it a List or a Vector). _(javascriptallonge.pdf (source-range-83ecb080-00202))_
- This is an expression, and you can combine [] with other expressions. _(javascriptallonge.pdf (source-range-83ecb080-00205))_
- Notice that you are always generating arrays with the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. _(javascriptallonge.pdf (source-range-83ecb080-00209))_
- They look the same, but if you examine them with ===, you see that they are different. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book. _(javascriptallonge.pdf (source-range-83ecb080-00210))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00188))_

> Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00189))_

> **true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00195))_

> - 2 + 2 === 4 _//=> true_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00196))_

> - (2 + 2 === 4) === (2 !== 5) _//=> true_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00198))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00205))_

> An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00206))_

> [2-1, 2, 2+1] [1, 1+1, 1+1+1]

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00207))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00208))_

> [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3]
