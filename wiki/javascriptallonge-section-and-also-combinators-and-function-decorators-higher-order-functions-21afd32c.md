---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-21afd32c
page_kind: source
summary: And also: / Combinators and Function Decorators / higher-order functions: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-21afd32c@eb8e8cc478b12f3d4a1e22be49b525c0
---

# And also: / Combinators and Function Decorators / higher-order functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-c48f42db]] - broader source section: And also: / Combinators and Function Decorators

## Statements

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-7239e085-00557))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00557))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00559))_

```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```
