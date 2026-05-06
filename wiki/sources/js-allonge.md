---
title: js-allonge
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-06
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# js-allonge

## Summary

*Extracted from javascriptallonge.pdf (297 pages)* --- JavaScript Allongé, the “Six” Edition

Extracted 274 claims from 30 chunks, organized into 12 viable topics.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript Allongé is a book about programming with functions and how they compose to build larger p | "JavaScript Allongé is a first and foremost, a book about programming with functions." | `normalized:L169` |
| Functions in JavaScript have first-class status with lexical scope, making them ideal for functional | "JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope." | `normalized:L171` |
| Functions in JavaScript are values that represent computations to be performed. | "In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Fun" | `normalized:L757` |
| ECMAScript 2015 introduced iterators and generators as new features that enhance JavaScript's expres | "It introduces iterators and generators. But the common thread that runs through all these things is that since they are all simple objects and simple " | `normalized:L271` |
| An iterator is a function that returns objects with done and value properties to traverse data struc | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5609` |
| Iterator functions can be used to traverse different data structures like arrays and linked lists un | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612` |
| Programming with functions emphasizes composing small, independent entities to make bigger programs. | "The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas." | `normalized:L293` |
| The book teaches programming techniques that make code easier to read, modify, debug, and refactor. | "JavaScript Allongé teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down." | `normalized:L180` |
| A combinator is a higher-order function that uses only function application and previously defined c | "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments." | `normalized:L2113` |
| JavaScript's approach to handling data includes working with values, expressions, and identity. | "JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes" | `normalized:L173` |
| JavaScript has primitive types including numbers, strings, and booleans that are identical if they h | "Strings, numbers, and booleans are examples of what JavaScript calls "value" or "primitive" types." | `normalized:L599` |
| Arrays and functions in JavaScript are reference types and are not identical even if they appear to  | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array " | `normalized:L631` |
| ECMAScript 2015 introduced block-structured variables that allow local scoping in loops using the 'l | "for (let i = 0; i < array.length; ++i) {" | `normalized:L234` |
| ECMAScript 2015 allows functions to collect a variable number of arguments into a single array param | "function foo (first, ...rest) {" | `normalized:L245` |
| ECMAScript 6 was developed as a successor to ECMAScript 3 after abandoning the more radical ECMAScri | "After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. That version was planned to have numerous n" | `normalized:L372` |


## Major concepts

### Natural groupings

- **Functions** (105 claims)
- **Iterators** (41 claims)
- **Functional Programming** (26 claims)
- **Data Types** (21 claims)
- **ES6 Features** (18 claims)
- **Objects** (15 claims)
- **Control Flow** (14 claims)
- **Arrays** (12 claims)
- **Closures** (6 claims)
- **Recursion** (6 claims)
- **Generators** (4 claims)
- **Variables** (3 claims)

## Entities

None identified.

## Procedures

None identified.

## References

None identified.

## Open questions

- Additional topics may emerge from deeper analysis

## Related pages

| Candidate page | Intended path | Group | Priority | Evidence basis | Status |
|---|---|---|---|---|---|
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 12 claims covering array, arrays, destructuring | not created yet |
| Closures | `../concepts/closures.md` | Deep extraction | should create | 6 claims covering access, bindings, closure | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 14 claims covering blocks, javascript, operators | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 21 claims covering approach, arrays, functions | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 18 claims covering allows, developed, ecmascript | not created yet |
| Functional Programming | `../concepts/functional-programming.md` | Deep extraction | must create | 26 claims covering book, combinator, higher | not created yet |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 105 claims covering book, functions, javascript | not created yet |
| Generators | `../concepts/generators.md` | Deep extraction | could create | 4 claims covering functions, generator, generators | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 41 claims covering ecmascript, function, functions | not created yet |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 15 claims covering covers, javascript, objects | not created yet |
| Recursion | `../concepts/recursion.md` | Deep extraction | should create | 6 claims covering call, functions, recursive | not created yet |
| Variables | `../concepts/variables.md` | Deep extraction | could create | 3 claims covering declaration, declarations, function | not created yet |
