---
page_id: javascriptallonge-section-values-are-expressions-maybe-73d80097
page_kind: source
summary: values are expressions / Maybe: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-maybe-73d80097@a293240ef39e6973eb4943ada795d945
---

# values are expressions / Maybe

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section

## Statements

- A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). _(javascriptallonge.pdf (source-range-83ecb080-00714))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-83ecb080-00714))_
- Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } > 50https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad > 51https://github.com/raganwald/andand Recipes with Basic Functions 64 **return** fn.apply( **this** , args) } } maybe reduces the logic of checking for nothing to a function call: maybe((a, b, c) => a + b + c)(1, 2, 3) _//=> 6_ maybe((a, b, c) => a + b + c)(1, **null** , 3) _//=> undefined_ As a bonus, maybe plays very nicely with instance methods, we’ll discuss those later: **function** Model () {}; _(javascriptallonge.pdf (source-range-83ecb080-00716))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-83ecb080-00718))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00717))_

> Model.prototype.setSomething = maybe( **function** (value) { **this** .something = value; });
