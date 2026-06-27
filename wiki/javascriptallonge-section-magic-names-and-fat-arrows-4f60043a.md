---
page_id: javascriptallonge-section-magic-names-and-fat-arrows-4f60043a
page_kind: source
summary: **magic names and fat arrows**: 21 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-magic-names-and-fat-arrows-4f60043a@ce6dc60838601ff30a31db405b2b61c8
---

# **magic names and fat arrows**

From [[javascriptallonge]].

## Statements

- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00881))_
- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00881))_
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. _(javascriptallonge.pdf (source-range-83ecb080-00885))_
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. _(javascriptallonge.pdf (source-range-83ecb080-00887))_
- It uses mapWith, which we discussed in Building Blocks.[44] We’ll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-83ecb080-00888))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. _(javascriptallonge.pdf (source-range-83ecb080-00888))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row. _(javascriptallonge.pdf (source-range-83ecb080-00890))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row. _(javascriptallonge.pdf (source-range-83ecb080-00890))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- > 44Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- Sometimes, a function is meant to be used as a Big-F function. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- It has a name, it is called by different pieces of code, it’s a first-class entity in the code. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- It has a name, it is called by different pieces of code, it’s a first-class entity in the code. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- It’s a simple representation of an expression to be computed. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- But sometimes, a function is a small-f function. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00898))_

## Technical atoms

> Context: But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. And thus arguments[0] will refer to "outer", not to "inner":
_(context: javascriptallonge.pdf (source-range-83ecb080-00885))_

> ( **function** () { **return** (() => arguments[0])('inner'); })('outer') _//=> "outer"_
_(source: javascriptallonge.pdf (source-range-83ecb080-00886))_
