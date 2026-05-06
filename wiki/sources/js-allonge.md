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

Extracted 268 claims from 30 chunks, organized into 11 viable topics.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript Allongé is a book about programming with functions and how they compose to build larger p | "JavaScript Allongé is a first and foremost, a book about programming with functions." | `normalized:L169` |
| Functions in JavaScript have first-class status with lexical scope, making them ideal for functional | "JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope." | `normalized:L171` |
| Functions in JavaScript are values that represent computations to be performed | "In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Fun" | `normalized:L757` |
| An iterator is a function that returns objects with done and value properties to traverse data struc | "The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true }." | `normalized:L5611` |
| Iterators can be created for different data structures like arrays and linked lists to enable generi | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612` |
| Iterators can generate data on-demand rather than working with pre-existing data structures. | "But they could just as easily manufacture the data as they go. Let's consider the simplest example:" | `normalized:L5657` |
| The book emphasizes that programming with functions focuses on composing small, independent entities | "Thus, the focus on things like writing decorators.  As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of h" | `normalized:L262` |
| Programming with functions allows for building programs by composing small, flexible, and decoupled  | "Thus, the "six" edition introduces classes and mixins. It introduces the notion of implementing private properties with symbols. It introduces iterato" | `normalized:L271` |
| The book distinguishes itself by focusing on underlying programming ideas rather than prescribing sp | "JavaScript Allongé attempts to be provocative, it is not prescriptive. There is absolutely no suggestion that any of the techniques shown here are the" | `normalized:L296` |
| JavaScript's design makes it suitable for teaching fundamental programming concepts including values | "JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes" | `normalized:L173` |
| JavaScript has primitive types including strings, numbers, and booleans that are identical if they h | "Strings, numbers, and booleans are examples of what JavaScript calls "value" or "primitive" types." | `normalized:L599` |
| Arrays and functions in JavaScript are reference types that are not identical even when they appear  | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array " | `normalized:L631` |
| Prior to ES2015, JavaScript lacked block-structured variables, requiring workarounds like IIFEs to a | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and woul" | `normalized:L195` |
| Before ES2015, JavaScript required awkward workarounds to collect variable arguments into a paramete | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage o" | `normalized:L217` |
| Blocks can contain const declarations and nested blocks, allowing for complex control flow structure | "We've used a block as the else clause, and since it's a block, we've placed a const statement inside it." | `normalized:L1628` |


## Major concepts

### Natural groupings

- **Functions** (106 claims)
- **Iterators** (39 claims)
- **Functional Programming** (22 claims)
- **Data Types** (21 claims)
- **Control Flow** (16 claims)
- **Objects** (14 claims)
- **ES6 Features** (12 claims)
- **Arrays** (11 claims)
- **Closures** (10 claims)
- **Recursion** (6 claims)
- **Generators** (4 claims)

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
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 11 claims covering array, arrays, destructuring | not created yet |
| Closures | [../concepts/closures.md](../concepts/closures.md) | Deep extraction | must create | 10 claims covering access, bound, closure | created |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 16 claims covering before, blocks, contain | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 21 claims covering arrays, design, functions | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 12 claims covering added, developed, ecmascript | not created yet |
| Functional Programming | `../concepts/functional-programming.md` | Deep extraction | must create | 22 claims covering book, distinguishes, emphasizes | not created yet |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 106 claims covering book, functions, javascript | not created yet |
| Generators | `../concepts/generators.md` | Deep extraction | could create | 4 claims covering functions, generator | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 39 claims covering created, function, generate | not created yet |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 14 claims covering javascript, objects | not created yet |
| Recursion | [../concepts/recursion.md](../concepts/recursion.md) | Deep extraction | should create | 6 claims covering call, functions, recursive | created |
