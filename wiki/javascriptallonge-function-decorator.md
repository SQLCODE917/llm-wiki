---
page_id: javascriptallonge-function-decorator
page_kind: concept
summary: Function Decorator: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-decorator@6f0ccc41e161657e73b1c481c5747d30
---

# Function Decorator

What [[javascriptallonge]] covers about function decorator:

## Statements

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- Here’s a ridiculously simple decorator:[38] > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. _(javascriptallonge.pdf (source-range-83ecb080-00586))_
- A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. _(javascriptallonge.pdf (source-range-83ecb080-00586))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- > 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) The first sip: Basic Functions _(javascriptallonge.pdf (source-range-83ecb080-00587))_

## Related pages

- [[javascriptallonge-function]] - broader topic (3 shared statement(s))
- [[javascriptallonge-combinator]] - shared statements (2 shared statement(s))
- [[javascriptallonge-argument]] - shared statements (1 shared statement(s))
- [[javascriptallonge-implementation]] - shared statements (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements (1 shared statement(s))
- [[javascriptallonge-version]] - shared statements (1 shared statement(s))
- [[javascriptallonge-section-values-are-expressions-combinators-and-function-decorators-function-decorators-b959afa1]] - source section (5 shared statement(s))

## Source

- [[javascriptallonge]]
