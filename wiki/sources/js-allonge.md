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

Extracted 282 claims from 30 chunks, organized into 13 viable topics.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript Allongé is a book about programming with functions and how they compose to build larger p | "JavaScript Allongé is a first and foremost, a book about programming with functions." | `normalized:L169` |
| Functions in JavaScript have lexical scope and are first-class citizens. | "JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope." | `normalized:L171` |
| In JavaScript, functions are values that represent computations to be performed. | "In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Fun" | `normalized:L757` |
| An iterator is a function that returns objects with done and value properties to traverse data struc | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5609` |
| Iterator functions can be used to abstract traversal logic from operations performed on data element | "The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true }." | `normalized:L5611` |
| Iterators can be implemented for different data structures like arrays and linked lists to enable ge | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612` |
| Programming with functions emphasizes composing small, independent entities to make bigger programs. | "The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas." | `normalized:L293` |
| The book teaches programming techniques that make code easier to read, modify, debug, and refactor. | "JavaScript Allongé teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down." | `normalized:L180` |
| A combinator is a higher-order function that uses only function application and previously defined c | "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments." | `normalized:L2113` |
| Prior to ES6, JavaScript lacked block-structured variables, requiring workarounds like IIFEs. | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language..." | `normalized:L196` |
| Before ES6, JavaScript required workarounds to collect variable arguments into a parameter. | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter..." | `normalized:L217` |
| JavaScript operators follow an order of precedence similar to how humans parse arithmetic expression | "JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, " | `normalized:L723` |
| JavaScript's approach to programming with functions is suitable for building complex software. | "JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes" | `normalized:L173` |
| JavaScript has primitive types including strings, numbers, and booleans that are identical if they h | "Strings, numbers, and booleans are examples of what JavaScript calls "value" or "primitive" types." | `normalized:L599` |
| Arrays and functions in JavaScript are reference types and are not identical even if they appear to  | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array " | `normalized:L631` |


## Major concepts

### Natural groupings

- **Functions** (100 claims)
- **Iterators** (38 claims)
- **Functional Programming** (27 claims)
- **Control Flow** (23 claims)
- **Data Types** (21 claims)
- **ES6 Features** (18 claims)
- **Objects** (16 claims)
- **Arrays** (10 claims)
- **Recursion** (8 claims)
- **Closures** (7 claims)
- **Generators** (5 claims)
- **Mutation** (3 claims)
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
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 10 claims covering array, arrays, javascript | not created yet |
| Closures | `../concepts/closures.md` | Deep extraction | should create | 7 claims covering bound, closures, functions | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 23 claims covering before, javascript, operators | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 21 claims covering approach, arrays, functions | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 18 claims covering allows, developed, ecmascript | not created yet |
| Functional Programming | `../concepts/functional-programming.md` | Deep extraction | must create | 27 claims covering book, combinator, higher | not created yet |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 100 claims covering book, functions, javascript | not created yet |
| Generators | `../concepts/generators.md` | Deep extraction | should create | 5 claims covering functions, generator | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 38 claims covering function, functions, implemented | not created yet |
| Mutation | `../concepts/mutation.md` | Deep extraction | could create | 3 claims covering javascript, mutating, objects | not created yet |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 16 claims covering edition, javascript, objects | not created yet |
| Recursion | `../concepts/recursion.md` | Deep extraction | must create | 8 claims covering functions, linear, recursion | not created yet |
| Variables | `../concepts/variables.md` | Deep extraction | could create | 3 claims covering declaration, declarations, function | not created yet |
