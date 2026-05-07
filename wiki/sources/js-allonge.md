---
title: "Source: js-allonge"
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

# Source: js-allonge

## Summary

*Extracted from javascriptallonge.pdf (297 pages)* --- JavaScript Allongé, the “Six” Edition

Extracted 273 claims from 30 chunks, organized into 12 viable topics.

### Extraction Metadata

- Claim count: 273
- Topic count: 12
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 allows collecting a variable number of arguments into a paramete | "We can also write: function foo (first, ...rest) { // ... }" | `normalized:L237-L247` |
| ECMAScript 6 introduced three major groups of features: improved syntax for exis | "ECMAScript 6 has three major groups of features: • Better syntax for features that already exist (e." | `normalized:L382-L389` |
| The simplest possible function in JavaScript is represented as () => 0. | "The second simplest possible function.16 In JavaScript, it looks like this: () => 0" | `normalized:L760-L761` |
| The length function can be implemented using folding with a terminal value of 0  | "const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);" | `normalized:L3613-L3613` |
| ECMAScript 2015 introduced block-structured variables that allow local scoping i | "With ECMAScript 2015, we can write: for (let i = 0; i < array.length; ++i) { // ... }" | `normalized:L233-L237` |
| ECMAScript 6 (ES6) was ratified as a standard on June 17, 2015, and was develope | "ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17" | `normalized:L370-L371` |
| ECMAScript 4 was abandoned due to internal conflicts and replaced with two upgra | "After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon " | `normalized:L375-L376` |
| A function can be defined using arrow syntax with no arguments as () => 0 which  | "(() => 0) //=> [Function]" | `normalized:L761-L765` |
| In JavaScript, every value is either truthy or falsy, with specific values consi | "In JavaScript, there is a notion of "truthiness." Every value is either "truthy" or "falsy." Obvious" | `normalized:L2931-L2938` |
| JavaScript Allongé is a book about programming with functions and how they compo | "JavaScript Allongé is a first and foremost, a book about programming with functions. It's written in" | `normalized:L169-L172` |

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 125 | 5 | synthesized |  |
| Iterators | 41 | 1 | synthesized | Single section |
| Data Types | 15 | 5 | synthesized |  |
| Functional Programming | 15 | 3 | synthesized |  |
| Objects | 15 | 2 | synthesized |  |
| ES6 Features | 13 | 4 | synthesized |  |
| Control Flow | 12 | 4 | synthesized |  |
| Arrays | 11 | 1 | synthesized | Single section |
| Recursion | 7 | 2 | synthesized |  |
| Closures | 6 | 2 | synthesized |  |
| Generators | 5 | 1 | synthesized | Single section |
| Variables | 3 | 2 | synthesized |  |
| Mutation | 2 | 2 | deferred | Too few claims (2 < 3) |
| Strings | 2 | 1 | deferred | Too few claims (2 < 3) |
| Reassignment | 1 | 1 | deferred | Too few claims (1 < 3) |

## Major concepts

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Arrays | `../concepts/arrays.md` | not_started | - | 11 | - |
| Closures | `../concepts/closures.md` | not_started | - | 6 | - |
| Control Flow | `../concepts/control-flow.md` | not_started | - | 12 | - |
| Data Types | `../concepts/data-types.md` | not_started | - | 15 | - |
| ES6 Features | `../concepts/es6-features.md` | not_started | - | 13 | - |
| Functional Programming | `../concepts/functional-programming.md` | not_started | - | 15 | - |
| Functions | `../concepts/functions.md` | not_started | - | 125 | - |
| Generators | `../concepts/generators.md` | not_started | - | 5 | - |
| Iterators | `../concepts/iterators.md` | not_started | - | 41 | - |
| Objects | `../concepts/objects.md` | not_started | - | 15 | - |
| Recursion | `../concepts/recursion.md` | not_started | - | 7 | - |
| Variables | `../concepts/variables.md` | not_started | - | 3 | - |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Arrays | arrays | must create | 11 | 1 | 1 | discovered |
| Closures | closures | should create | 6 | 2 | 1 | discovered |
| Control Flow | control-flow | must create | 12 | 4 | 1 | discovered |
| Data Types | data-types | must create | 15 | 5 | 1 | discovered |
| ES6 Features | es6-features | must create | 13 | 4 | 1 | discovered |
| Functional Programming | functional-programming | must create | 15 | 3 | 1 | discovered |
| Functions | functions | must create | 125 | 5 | 1 | discovered |
| Generators | generators | should create | 5 | 1 | 1 | discovered |
| Iterators | iterators | must create | 41 | 1 | 1 | discovered |
| Objects | objects | must create | 15 | 2 | 1 | discovered |
| Recursion | recursion | should create | 7 | 2 | 1 | discovered |
| Variables | variables | could create | 3 | 2 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 1-214 | Data Types, Functions | javascriptallonge |
| 215-1257 | Control Flow, Data Types | ... |
| 1258-4572 | Arrays, Closures | => 1 |
| 5027-10070 | Closures, Control Flow | => 5050 |

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
| Closures | [../concepts/closures.md](../concepts/closures.md) | Deep extraction | should create | 6 claims covering access, closure, closures | created |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 12 claims covering blocks, book, explains | not created yet |
| Data Types | [../concepts/data-types.md](../concepts/data-types.md) | Deep extraction | must create | 15 claims covering arrays, functions, javascript | created |
| ES6 Features | [../concepts/es6-features.md](../concepts/es6-features.md) | Deep extraction | must create | 13 claims covering allows, ecmascript, introduced | created |
| Functional Programming | [../concepts/functional-programming.md](../concepts/functional-programming.md) | Deep extraction | must create | 15 claims covering combinator, functional, higher | created |
| Functions | [../concepts/functions.md](../concepts/functions.md) | Deep extraction | must create | 125 claims covering book, javascript, programming | created |
| Generators | [../concepts/generators.md](../concepts/generators.md) | Deep extraction | should create | 5 claims covering functions, generator, generators | created |
| Iterators | [../concepts/iterators.md](../concepts/iterators.md) | Deep extraction | must create | 41 claims covering allow, function, generate | created |
| Objects | [../concepts/objects.md](../concepts/objects.md) | Deep extraction | must create | 15 claims covering javascript, objects | created |
| Recursion | [../concepts/recursion.md](../concepts/recursion.md) | Deep extraction | should create | 7 claims covering call, defined, linear | created |
| Variables | [../concepts/variables.md](../concepts/variables.md) | Deep extraction | could create | 3 claims covering behave, declarations, function | created |
