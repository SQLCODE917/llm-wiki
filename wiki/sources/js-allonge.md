---
title: js-allonge
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-07
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# js-allonge

## Summary

*Extracted from javascriptallonge.pdf (297 pages)* --- JavaScript Allongé, the “Six” Edition

Extracted 273 claims from 30 chunks, organized into 12 viable topics.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript Allongé is a book about programming with functions and how they compose to build larger p | "JavaScript Allongé is a first and foremost, a book about programming with functions. It's written in JavaScript, because JavaScript hits the perfect s" | `normalized:L169-L172` |
| The book teaches how to handle complex code and simplify it without dumbing it down. | "JavaScript Allongé teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down." | `normalized:L180-L181` |
| Programming with functions emphasizes composing small, independent entities to make bigger programs. | "The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. The intention is to impro" | `normalized:L293-L295` |
| An iterator is a function that returns values one at a time, allowing traversal of data structures w | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5591-L5591` |
| Iterators allow separation of data traversal logic from the operations performed on the data element | "Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the arra" | `normalized:L5609-L5611` |
| Iterators can be implemented for different data structures such as arrays and linked lists to provid | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612-L5612` |
| Functional programming techniques in JavaScript involve composing small, flexible, and decoupled ent | "Thus, the focus on things like writing decorators. As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of ha" | `normalized:L262-L266` |
| A combinator is a higher-order function that uses only function application and previously defined c | "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments." | `normalized:L2113-L2114` |
| In this book, a combinator is defined as a higher-order pure function that takes only functions as a | "In this book, we will be using a looser definition of "combinator:" Higher-order pure functions that take only functions as arguments and return a fun" | `normalized:L2129-L2131` |
| JavaScript objects are maps from string keys to values. | "In JavaScript, an object is a map from string keys to values." | `normalized:L4258-L4258` |
| JavaScript objects are maps from string keys to values and can be created using literal syntax | "JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day: { year: 2012, month: 6, day: 14 }" | `normalized:L4267-L4270` |
| Objects use bracket notation to access values by string keys | "Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day']" | `normalized:L4274-L4276` |
| ECMAScript 2015 introduced block-structured variables that allow local scoping in loops. | "With ECMAScript 2015, we can write: for (let i = 0; i < array.length; ++i) { // ... }" | `normalized:L233-L237` |
| ECMAScript 2015 allows collecting a variable number of arguments into a parameter using rest syntax. | "We can also write: function foo (first, ...rest) { // ... }" | `normalized:L237-L247` |
| ECMAScript 2015 adds features that make programming techniques easier to explain and use. | "ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. It makes a number of inte" | `normalized:L267-L270` |


## Major concepts

### Natural groupings

- **Functions** (122 claims)
- **Iterators** (34 claims)
- **Functional Programming** (18 claims)
- **Objects** (18 claims)
- **ES6 Features** (15 claims)
- **Data Types** (14 claims)
- **Arrays** (14 claims)
- **Control Flow** (12 claims)
- **Closures** (7 claims)
- **Recursion** (5 claims)
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
| Arrays | [../concepts/arrays.md](../concepts/arrays.md) | Deep extraction | must create | 14 claims covering array, arrays, elements | created |
| Closures | `../concepts/closures.md` | Deep extraction | should create | 7 claims covering access, closure, closures | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 12 claims covering blocks, book, introduces | not created yet |
| Data Types | [../concepts/data-types.md](../concepts/data-types.md) | Deep extraction | must create | 14 claims covering arrays, functions, javascript | created |
| ES6 Features | [../concepts/es6-features.md](../concepts/es6-features.md) | Deep extraction | must create | 15 claims covering adds, allows, ecmascript | created |
| Functional Programming | [../concepts/functional-programming.md](../concepts/functional-programming.md) | Deep extraction | must create | 18 claims covering book, combinator, functional | created |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 122 claims covering book, javascript, programming | not created yet |
| Generators | `../concepts/generators.md` | Deep extraction | should create | 5 claims covering functions, generator, generators | not created yet |
| Iterators | [../concepts/iterators.md](../concepts/iterators.md) | Deep extraction | must create | 34 claims covering allow, function, implemented | created |
| Objects | [../concepts/objects.md](../concepts/objects.md) | Deep extraction | must create | 18 claims covering bracket, javascript, objects | created |
| Recursion | [../concepts/recursion.md](../concepts/recursion.md) | Deep extraction | should create | 5 claims covering call, defined, list | created |
| Variables | [../concepts/variables.md](../concepts/variables.md) | Deep extraction | could create | 4 claims covering declarations, function, hoisted | created |
