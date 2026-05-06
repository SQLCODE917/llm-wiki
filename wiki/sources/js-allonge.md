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

Extracted 276 claims from 30 chunks, organized into 13 viable topics.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript Allongé is a book about programming with functions and how they compose to build larger p | "JavaScript Allongé is a first and foremost, a book about programming with functions." | `normalized:L169-L169` |
| Functions in JavaScript have first-class status with lexical scope, making them ideal for functional | "JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope." | `normalized:L170-L172` |
| Programming with functions emphasizes composing small, independent entities to build larger programs | "The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas." | `normalized:L293-L294` |
| An iterator is a function that returns objects with done and value properties to traverse data struc | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5609-L5609` |
| Iterator functions can be used to abstract traversal logic from operations performed on data. | "The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true }." | `normalized:L5611-L5611` |
| Iterators can be implemented for different data structures like arrays and linked lists to enable ge | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612-L5612` |
| Functional programming techniques in JavaScript involve building programs by composing small, flexib | "Thus, the "six" edition introduces classes and mixins. It introduces the notion of implementing private properties with symbols. It introduces iterato" | `normalized:L271-L277` |
| Higher-order functions are functions that take functions as arguments, return functions, or both. | "Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a "higher-order" function." | `normalized:L2094-L2095` |
| A combinator is a higher-order function that uses only function application and previously defined c | "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments." | `normalized:L2113-L2114` |
| JavaScript has primitive types including strings, numbers, and booleans that are identical if they h | "Strings, numbers, and booleans are examples of what JavaScript calls "value" or "primitive" types." | `normalized:L599-L600` |
| Arrays and functions in JavaScript are reference types, meaning each array or function created is a  | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array " | `normalized:L631-L633` |
| JavaScript numbers are represented internally as double-precision floating-point values, which can l | "Internally, both 042 and 34 have the same representation, as double-precision floating point numbers. A computer's internal representation for numbers" | `normalized:L659-L663` |
| Prior to ES2015, JavaScript lacked block-structured variables, requiring workarounds like IIFEs to a | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and woul" | `normalized:L195-L210` |
| JavaScript operators follow an order of precedence that mimics human parsing of arithmetic expressio | "JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, " | `normalized:L723-L725` |
| Blocks can be used in control flow structures like if statements to contain variable declarations. | "if (x === 0) return true; else { const odd = (y) => !even(y); return odd(x - 1); }" | `normalized:L1599-L1603` |


## Major concepts

### Natural groupings

- **Functions** (108 claims)
- **Iterators** (35 claims)
- **Functional Programming** (27 claims)
- **Data Types** (18 claims)
- **Control Flow** (17 claims)
- **Objects** (16 claims)
- **ES6 Features** (15 claims)
- **Arrays** (11 claims)
- **Closures** (6 claims)
- **Recursion** (6 claims)
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
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 11 claims covering array, destructuring, elements | not created yet |
| Closures | `../concepts/closures.md` | Deep extraction | should create | 6 claims covering bound, closure, function | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 17 claims covering blocks, javascript, operators | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 18 claims covering arrays, functions, javascript | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 15 claims covering added, brought, ecmascript | not created yet |
| Functional Programming | [../concepts/functional-programming.md](../concepts/functional-programming.md) | Deep extraction | must create | 27 claims covering combinator, functional, higher | created |
| Functions | [../concepts/functions.md](../concepts/functions.md) | Deep extraction | must create | 108 claims covering book, functions, javascript | created |
| Generators | `../concepts/generators.md` | Deep extraction | should create | 5 claims covering function, functions, generator | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 35 claims covering function, functions, implemented | not created yet |
| Mutation | `../concepts/mutation.md` | Deep extraction | could create | 3 claims covering array, arrays, mutating | not created yet |
| Objects | [../concepts/objects.md](../concepts/objects.md) | Deep extraction | must create | 16 claims covering javascript, literal, object | created |
| Recursion | `../concepts/recursion.md` | Deep extraction | should create | 6 claims covering call, functions, recursive | not created yet |
| Variables | [../concepts/variables.md](../concepts/variables.md) | Deep extraction | could create | 3 claims covering behave, declarations, function | created |
