---
page_id: javascriptallonge-section-values-are-expressions-combinators-and-function-decorators-function-decorators-b959afa1
page_kind: source
summary: values are expressions / Combinators and Function Decorators / function decorators: 5 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-combinators-and-function-decorators-function-decorators-b959afa1@43876b40e11c4300d429dfb84d2c9595
---

# values are expressions / Combinators and Function Decorators / function decorators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-combinators-and-function-decorators-bc938683]] - broader source section
- [[javascriptallonge-function-decorator]] - topic hub

## Statements

- Here’s a ridiculously simple decorator:[38] > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. _(javascriptallonge.pdf (source-range-83ecb080-00586))_
- A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. _(javascriptallonge.pdf (source-range-83ecb080-00586))_
- > 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) The first sip: Basic Functions _(javascriptallonge.pdf (source-range-83ecb080-00587))_
- 47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
