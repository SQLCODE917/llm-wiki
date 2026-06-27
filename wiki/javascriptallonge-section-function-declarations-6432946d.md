---
page_id: javascriptallonge-section-function-declarations-6432946d
page_kind: source
summary: **function declarations**: 14 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-declarations-6432946d@1df99e3919b1c69d9564b2948ce4622a
---

# **function declarations**

From [[javascriptallonge]].

## Statements

- There is another syntax for naming and/or defining a function. _(javascriptallonge.pdf (source-range-83ecb080-00742))_
- However, there are two important differences. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- First, function declarations are _hoisted_ to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- In that it binds a name in the environment to a named function. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. _(javascriptallonge.pdf (source-range-83ecb080-00762))_
- The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). _(javascriptallonge.pdf (source-range-83ecb080-00762))_
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code. _(javascriptallonge.pdf (source-range-83ecb080-00762))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00746))_

> This behaves a _little_ like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00747))_

> **const** someName = **function** someName () {

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00751))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00751))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00754))_

> **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> undefined is not a function (evaluating 'fizzbuzz()')_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00759))_

> **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00760))_

> Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00761))_

> ( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })()
