---
page_id: javascriptallonge-section-higher-order-functions-058e77d1
page_kind: source
summary: higher-order functions: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-higher-order-functions-058e77d1@845865ef3e9cf2d006e4e403ae4f12cb
---

# higher-order functions

From [[javascriptallonge]].

## Statements

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-31a4cf47-00560))_
- In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-31a4cf47-00565))_
- This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-31a4cf47-00568))_
- We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-31a4cf47-00565))_
- While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-31a4cf47-00568))_

## Technical atoms

### Technical frame 1: higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00565))_

> In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00562))_

```
const repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : undefined repeat(3, function (n) { console.log(`Hello ${ n } `) }) //=> 'Hello 1' 'Hello 2' 'Hello 3' undefined
```

### Technical frame 2: higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00568))_

> This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00567))_

```
const compose = (a, b) => (c) => a(b(c)) Let's say we have: const addOne = (number) => number + 1; const doubleOf = (number) => number * 2; With compose , anywhere you would write const doubleOfAddOne = (number) => doubleOf(addOne(number)); You could also write: const doubleOfAddOne = compose(doubleOf, addOne);
```

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00564))_

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

<details>
<summary>Raw table text</summary>

```
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

</details>
