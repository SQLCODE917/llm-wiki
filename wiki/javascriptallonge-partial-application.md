---
page_id: javascriptallonge-partial-application
page_kind: concept
summary: **partial application**: 15 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-partial-application@d991adb346ffe5cabcba41e79874cd04
---

# **partial application**

What [[javascriptallonge]] covers about **partial application**:

## Statements

- Partial application also has a combinator, which we’ll see in the partial recipe. _(javascriptallonge.pdf (source-range-83ecb080-00613))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00607))_
- Another basic building block is _partial application_ . _(javascriptallonge.pdf (source-range-83ecb080-00604))_
- In that case, we can’t get the final value, but we can get a function that represents _part_ of our application. _(javascriptallonge.pdf (source-range-83ecb080-00604))_
- The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-83ecb080-00608))_
- In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. _(javascriptallonge.pdf (source-range-83ecb080-00672))_
- This is such a common tool that many libraries provide some form of partial application. _(javascriptallonge.pdf (source-range-83ecb080-00672))_
- We’d need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-83ecb080-00674))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: **const** callLeft = (fn, ...args) => _(javascriptallonge.pdf (source-range-83ecb080-00681))_
- The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. _(javascriptallonge.pdf (source-range-83ecb080-00607))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-83ecb080-00607))_
- > 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache. _(javascriptallonge.pdf (source-range-83ecb080-00610))_
- > 48 callFirst and callLast were inspired by Michael Fogus’ Lemonad. _(javascriptallonge.pdf (source-range-83ecb080-00678))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00681))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: **const** callLeft = (fn, ...args) =>

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00682))_

> (...remainingArgs) => fn(...args, ...remainingArgs); **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);


## Related pages

- [[javascriptallonge-block]] - shared statements (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements (2 shared statement(s))
- [[javascriptallonge-argument]] - shared statements (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))
- [[javascriptallonge-implementation]] - shared statements (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements (1 shared statement(s))
- [[javascriptallonge-section-values-are-expressions-building-blocks-partial-application-75c3f473]] - source section (10 shared statement(s))
- [[javascriptallonge-section-values-are-expressions-partial-application-667a6672]] - source section (5 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
