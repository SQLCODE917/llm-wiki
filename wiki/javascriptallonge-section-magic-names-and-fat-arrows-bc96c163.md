---
page_id: javascriptallonge-section-magic-names-and-fat-arrows-bc96c163
page_kind: source
summary: magic names and fat arrows: 24 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-magic-names-and-fat-arrows-bc96c163@28bea4a45570542f24b9398e558c1358
---

# magic names and fat arrows

From [[javascriptallonge]].

## Statements

- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-31a4cf47-00621))_
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" : _(javascriptallonge.pdf (source-range-31a4cf47-00623))_
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. _(javascriptallonge.pdf (source-range-31a4cf47-00625))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-31a4cf47-00626))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working: _(javascriptallonge.pdf (source-range-31a4cf47-00628))_
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-31a4cf47-00629))_
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code. _(javascriptallonge.pdf (source-range-31a4cf47-00632))_
- But sometimes, a function is a small-f function. It's a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-31a4cf47-00633))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith . _(javascriptallonge.pdf (source-range-31a4cf47-00634))_
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-31a4cf47-00621))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . _(javascriptallonge.pdf (source-range-31a4cf47-00628))_
- It has a name, it is called by different pieces of code, it's a first-class entity in the code. _(javascriptallonge.pdf (source-range-31a4cf47-00632))_

## Technical atoms

### Technical frame 1: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00623))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00622))_

```
( function () { return ( function () { return arguments[0]; })('inner'); })('outer') //=> "inner"
```

### Technical frame 2: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00625))_

> Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00624))_

```
( function () { return (() => arguments[0])('inner'); })('outer') //=> "outer"
```

### Technical frame 3: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00628))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00627))_

```
const row = function () { return mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### Technical frame 4: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00632))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00630))_

```
const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36,49,64,81,100,121,144]
```
