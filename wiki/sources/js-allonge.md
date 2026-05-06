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

Extracted 269 claims from 30 chunks, organized into 12 viable topics.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript Allongé is a book about programming with functions and how they compose to build larger p | "JavaScript Allongé is a first and foremost, a book about programming with functions." | `normalized:L169` |
| Functions in JavaScript have first-class status with lexical scope, making them ideal for functional | "JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope." | `normalized:L171` |
| The 'Six' edition of JavaScript Allongé introduces classes, mixins, iterators, and generators while  | "Thus, the 'six' edition introduces classes and mixins. It introduces the notion of implementing private properties with symbols. It introduces iterato" | `normalized:L271` |
| An iterator is a function that returns objects with done and value properties to traverse data struc | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5609` |
| Iterators allow separation of traversal logic from the operations performed on data elements. | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612` |
| An iterator can be limited to return only a specified number of elements using a take function. | "const take = (iterator, numberToTake) => { let count = 0; return () => { if (++count <= numberToTake) { return iterator(); } else { return {done: true" | `normalized:L5728` |
| Functional programming techniques involve composing small, independent entities to build larger prog | "The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas." | `normalized:L293` |
| Programming with functions emphasizes techniques like decorators, methods, delegation, and mixins. | "From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions." | `normalized:L292` |
| The compose combinator combines two functions by applying the second to an input and then applying t | "Most programmers call it Compose, although the logicians call it the B combinator or "Bluebird."" | `normalized:L2132` |
| JavaScript is chosen as the language for Allongé because it has a large audience and supports functi | "JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language fe" | `normalized:L264` |
| JavaScript has primitive types including numbers, strings, and booleans that are identical if they h | "Strings, numbers, and booleans are examples of what JavaScript calls "value" or "primitive" types." | `normalized:L599` |
| Arrays and functions in JavaScript are reference types and each array or function created is a uniqu | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array " | `normalized:L631` |
| ECMAScript 2015 introduced block-structured variables allowing local scoping in loops using the 'let | "for (let i = 0; i < array.length; ++i) {" | `normalized:L234` |
| ECMAScript 2015 added rest parameters that collect variable arguments into an array without needing  | "function foo (first, ...rest) {" | `normalized:L245` |
| ECMAScript 6 was developed after a conflict over ECMAScript 4 and was split into two upgrades: ES5 a | "After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon ECMAScript 4 and to replace it with two upgrades: " | `normalized:L375` |


## Major concepts

### Natural groupings

- **Functions** (102 claims)
- **Iterators** (37 claims)
- **Functional Programming** (22 claims)
- **Data Types** (20 claims)
- **ES6 Features** (17 claims)
- **Control Flow** (17 claims)
- **Objects** (12 claims)
- **Arrays** (11 claims)
- **Closures** (8 claims)
- **Recursion** (8 claims)
- **Generators** (5 claims)
- **Variables** (4 claims)

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
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 11 claims covering array, arrays, elements | not created yet |
| Closures | `../concepts/closures.md` | Deep extraction | must create | 8 claims covering bound, closures, evaluating | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 17 claims covering javascript, lack, operators | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 20 claims covering arrays, chosen, functions | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 17 claims covering added, developed, ecmascript | not created yet |
| Functional Programming | `../concepts/functional-programming.md` | Deep extraction | must create | 22 claims covering combinator, compose, functional | not created yet |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 102 claims covering book, edition, functions | not created yet |
| Generators | `../concepts/generators.md` | Deep extraction | should create | 5 claims covering function, functions, generator | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 37 claims covering allow, function, iterator | not created yet |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 12 claims covering javascript, objects | not created yet |
| Recursion | `../concepts/recursion.md` | Deep extraction | must create | 8 claims covering functions, linear, recursion | not created yet |
| Variables | `../concepts/variables.md` | Deep extraction | could create | 4 claims covering behave, declarations, function | not created yet |
