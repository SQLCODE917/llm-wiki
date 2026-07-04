---
page_id: javascriptallonge-section-maybe-f587fcc2
page_kind: source
page_family: section-reference
summary: Maybe: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-maybe-f587fcc2@5d5bf0fdcb67af8ea373297de8b5a868
---

# Maybe

From [[javascriptallonge]].

## Statements

- Recipes with Basic Functions 

63 

## **Maybe** 

A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. 

This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: 

**const** isSomething = (value) => value !== **null** && value !== **void** 0; 

**const** checksForSomething = (value) => { **if** (isSomething(value)) { 

_// function's true logic_ } 

} 

Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: 

**var** something = isSomething(value) ? doesntCheckForSomething(value) : value; 

Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: 

**const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } 

> 50https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad 

> 51https://github.com/raganwald/andand _(javascriptallonge.pdf (source-range-af806fb1-00104))_
- Recipes with Basic Functions 

64 

**return** fn.apply( **this** , args) } } 

maybe reduces the logic of checking for nothing to a function call: 

maybe((a, b, c) => a + b + c)(1, 2, 3) _//=> 6_ maybe((a, b, c) => a + b + c)(1, **null** , 3) _//=> undefined_ 

As a bonus, maybe plays very nicely with instance methods, we’ll discuss those later: 

**function** Model () {}; 

Model.prototype.setSomething = maybe( **function** (value) { **this** .something = value; }); 

If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-af806fb1-00105))_
