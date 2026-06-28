---
page_id: javascriptallonge-section-values-are-expressions-building-blocks-partial-application-75c3f473
page_kind: source
summary: values are expressions / Building Blocks / partial application: 10 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-building-blocks-partial-application-75c3f473@d58f340a3f57cec9d1630392beaa4bcc
---

# values are expressions / Building Blocks / partial application

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-building-blocks-60f0a526]] - broader source section
- [[javascriptallonge-partial-application]] - topic hub
- [[javascriptallonge-section-values-are-expressions-partial-application-667a6672]] - same source heading

## Statements

- Another basic building block is _partial application_ . _(javascriptallonge.pdf (source-range-83ecb080-00604))_
- In that case, we can’t get the final value, but we can get a function that represents _part_ of our application. _(javascriptallonge.pdf (source-range-83ecb080-00604))_
- The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. _(javascriptallonge.pdf (source-range-83ecb080-00607))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00607))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-83ecb080-00607))_
- The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-83ecb080-00608))_
- > 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache. _(javascriptallonge.pdf (source-range-83ecb080-00610))_
- Partial application also has a combinator, which we’ll see in the partial recipe. _(javascriptallonge.pdf (source-range-83ecb080-00613))_
