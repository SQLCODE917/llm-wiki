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

Extracted 275 claims from 30 chunks, organized into 12 viable topics.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript Allongé is a book about programming with functions and how they compose to build larger p | "JavaScript Allongé is a first and foremost, a book about programming with functions." | `normalized:L169` |
| Functions in JavaScript have first-class status with lexical scope, making them ideal for functional | "JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope." | `normalized:L170` |
| In JavaScript, functions are values that represent computations to be performed. | "In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Fun" | `normalized:L757` |
| ECMAScript 2015 introduced iterators and generators which provide new ways to work with collections. | "It introduces iterators and generators. But the common thread that runs through all these things is that since they are all simple objects and simple " | `normalized:L271` |
| An iterator is a function that returns objects with done and value properties to traverse data struc | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5609` |
| Iterators allow separation of traversal logic from the operations performed on data elements. | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612` |
| Functional programming techniques in JavaScript involve composing small, independent entities to mak | "Working with small, independent entities that compose together to make bigger programs." | `normalized:L262` |
| Programming with functions enables techniques like decorators, methods, delegation, and mixins. | "From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions." | `normalized:L291` |
| Higher-order functions are functions that take functions as arguments, return functions, or both. | "Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a "higher-order" function." | `normalized:L2094` |
| JavaScript supports various data types including numbers, strings, and objects, forming the foundati | "JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes" | `normalized:L173` |
| JavaScript has primitive types including numbers, strings, and booleans that are identical if they h | "Strings, numbers, and booleans are examples of what JavaScript calls "value" or "primitive" types." | `normalized:L599` |
| Arrays and functions in JavaScript are reference types, meaning each instance is unique even if they | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array " | `normalized:L631` |
| JavaScript's 'for' loop with 'let' creates block-scoped variables that are local to the loop body. | "for (let i = 0; i < array.length; ++i) {" | `normalized:L234` |
| Blocks can be used in if statements to contain const declarations and other statements. | "else { const odd = (y) => !even(y); return odd(x - 1); }" | `normalized:L1601` |
| The ternary operator (?:) is a control-flow operator that evaluates only one of two expressions base | "The ternary operator (?:), \|\|, and && are control flow operators, they do not always return true or false, and they have short-cut semantics." | `normalized:L3017` |


## Major concepts

### Natural groupings

- **Functions** (108 claims)
- **Iterators** (39 claims)
- **Functional Programming** (23 claims)
- **Data Types** (21 claims)
- **Control Flow** (15 claims)
- **ES6 Features** (14 claims)
- **Objects** (14 claims)
- **Arrays** (12 claims)
- **Generators** (7 claims)
- **Closures** (6 claims)
- **Recursion** (6 claims)
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
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 12 claims covering array, arrays, javascript | not created yet |
| Closures | `../concepts/closures.md` | Deep extraction | should create | 6 claims covering bindings, closures, created | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 15 claims covering blocks, javascript, loop | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 21 claims covering arrays, functions, javascript | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 14 claims covering allows, created, ecmascript | not created yet |
| Functional Programming | `../concepts/functional-programming.md` | Deep extraction | must create | 23 claims covering functional, higher, order | not created yet |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 108 claims covering book, functions, javascript | not created yet |
| Generators | `../concepts/generators.md` | Deep extraction | should create | 7 claims covering functions, generator, generators | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 39 claims covering allow, ecmascript, function | not created yet |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 14 claims covering javascript, literal, object | not created yet |
| Recursion | `../concepts/recursion.md` | Deep extraction | should create | 6 claims covering functions, linear, recursion | not created yet |
| Variables | `../concepts/variables.md` | Deep extraction | could create | 3 claims covering declarations, function, hoists | not created yet |
