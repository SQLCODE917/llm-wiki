---
page_id: javascriptallonge-section-maybe-72c82460
page_kind: source
summary: **Maybe**: 10 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-maybe-72c82460@a12a4cf3d1ae51e035c6aa9cebf7ad94
---

# **Maybe**

From [[javascriptallonge]].

## Statements

- A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). _(javascriptallonge.pdf (source-range-83ecb080-01001))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-83ecb080-01001))_
- This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: _(javascriptallonge.pdf (source-range-83ecb080-01002))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-83ecb080-01007))_
- Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: _(javascriptallonge.pdf (source-range-83ecb080-01009))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-83ecb080-01021))_

## Technical atoms

> Context: This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01002))_

> **const** isSomething = (value) => value !== **null** && value !== **void** 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-01003))_

> Context: This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01002))_

> **const** checksForSomething = (value) => { **if** (isSomething(value)) {
_(source: javascriptallonge.pdf (source-range-83ecb080-01004))_

> Context: Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01007))_

> **var** something = isSomething(value) ? doesntCheckForSomething(value) : value;
_(source: javascriptallonge.pdf (source-range-83ecb080-01008))_

> Context: As a bonus, maybe plays very nicely with instance methods, we’ll discuss those later:
_(context: javascriptallonge.pdf (source-range-83ecb080-01018))_

> Model.prototype.setSomething = maybe( **function** (value) { **this** .something = value; });
_(source: javascriptallonge.pdf (source-range-83ecb080-01020))_
