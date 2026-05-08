---
title: "Source: js-allonge"
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-08
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# Source: js-allonge

## Summary

**JavaScript Allongé, the "Six" Edition** Programming from Functions to Classes in ECMAScript 2015 This book is for sale at http://leanpub.com/javascriptallongesix This version was published on 2017-11-03

Extracted 275 claims from 19 chunks, organized into 10 viable topics.

### Extraction Metadata

- Claim count: 275
- Topic count: 10
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 (ES6) introduced features that make programming with functions e | "ECMAScript 2015 (formerly called ECMAScript 6 or "ES6"), is ushering in a very large number of impro" | `normalized:L119-L120` |
| Before ES6, JavaScript did not support collecting a variable number of arguments | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into " | `normalized:L147-L150` |
| ES6 introduced let for block-scoped variables and ...rest for collecting variabl | "We can also write: function foo (first, ...rest) { // ... } And presto, rest collects the rest of th" | `normalized:L159-L168` |
| ECMAScript 2015 introduced three major groups of features: better syntax for exi | "ECMAScript 6 has three major groups of features: - Better syntax for features that already exist (e." | `normalized:L253-L266` |
| Length can be computed using a fold operation with a terminal value of 0 and a f | "const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);" | `normalized:L2767-L2767` |
| Prior to ES6, JavaScript lacked block-structured variables, requiring workaround | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a tr" | `normalized:L131-L141` |
| ECMAScript 2015 was ratified as a standard on June 17, 2015, after years of deve | "ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17" | `normalized:L247-L251` |
| JavaScript Allongé is a book about programming with functions, emphasizing how f | "JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from " | `normalized:L201-L202` |
| JavaScript Allongé is organized to introduce new aspects of programming with fun | "_JavaScript Allongé_ introduces new aspects of programming with functions in each chapter, explainin" | `normalized:L231-L232` |
| The 'Six' edition emphasizes that all these new features can still be approached | "But the common thread that runs through all these things is that since they are all simple objects a" | `normalized:L187-L190` |

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 96 | 41 | synthesized |  |
| Data Types | 45 | 19 | synthesized |  |
| Iterators | 40 | 16 | synthesized |  |
| Arrays | 19 | 10 | synthesized |  |
| ES6 Features | 18 | 13 | synthesized |  |
| Recursion | 15 | 9 | synthesized |  |
| Control Flow | 11 | 7 | synthesized |  |
| Closures | 10 | 6 | synthesized |  |
| Objects | 10 | 5 | synthesized |  |
| Functional Programming | 8 | 6 | synthesized |  |
| Strings | 2 | 1 | deferred | Too few claims (2 < 3) |
| Generators | 1 | 1 | deferred | Too few claims (1 < 3) |

## Major concepts

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Arrays | `../concepts/arrays.md` | not_started | - | 19 | - |
| Closures | `../concepts/closures.md` | not_started | - | 10 | - |
| Control Flow | `../concepts/control-flow.md` | not_started | - | 11 | - |
| Data Types | `../concepts/data-types.md` | not_started | - | 45 | - |
| ES6 Features | `../concepts/es6-features.md` | not_started | - | 18 | - |
| Functional Programming | `../concepts/functional-programming.md` | not_started | - | 8 | - |
| Functions | `../concepts/functions.md` | not_started | - | 96 | - |
| Iterators | `../concepts/iterators.md` | not_started | - | 40 | - |
| Objects | `../concepts/objects.md` | not_started | - | 10 | - |
| Recursion | `../concepts/recursion.md` | not_started | - | 15 | - |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Arrays | arrays | must create | 19 | 10 | 1 | discovered |
| Closures | closures | must create | 10 | 6 | 1 | discovered |
| Control Flow | control-flow | must create | 11 | 7 | 1 | discovered |
| Data Types | data-types | must create | 45 | 19 | 1 | discovered |
| ES6 Features | es6-features | must create | 18 | 13 | 1 | discovered |
| Functional Programming | functional-programming | must create | 8 | 6 | 1 | discovered |
| Functions | functions | must create | 96 | 41 | 1 | discovered |
| Iterators | iterators | must create | 40 | 16 | 1 | discovered |
| Objects | objects | must create | 10 | 5 | 1 | discovered |
| Recursion | recursion | must create | 15 | 9 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 3-24 | - | Reg "raganwald" Braithwaite |
| 25-56 | - | **Contents** |
| 57-90 | - | CONTENTS |
| 91-106 | Control Flow, ES6 Features | **A Pull of the Lever: Prefaces** |
| 107-116 | - | **About JavaScript Allongé** |
| 117-172 | Functions | **why the "six" edition?** |
| 173-194 | Functions | **that's nice. is that the only reason?** |
| 195-228 | Functions | **What JavaScript Allongé is. And isn't.** |
| 229-244 | Functions | **how this book is organized** |
| 245-280 | ES6 Features | **Foreword to the "Six" edition** |
| 281-282 | - | **Forewords to the First Edition** |
| 283-296 | - | **michael fogus** |
| 297-320 | - | **matthew knox** |
| 321-336 | - | **About The Sample PDF** |
| 337-352 | - | **Prelude: Values and Expressions over Coffee** |
| 353-358 | Data Types | **values are expressions** |
| 359-364 | - | 42 |
| 365-394 | Data Types | 42 |
| 395-416 | Data Types | **values and identity** |
| 417-432 | Data Types | **value types** |

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
| Arrays | [../concepts/arrays.md](../concepts/arrays.md) | Deep extraction | must create | 19 claims covering array, destructuring, elements | created |
| Closures | `../concepts/closures.md` | Deep extraction | must create | 10 claims covering access, closure, closures | not created yet |
| Control Flow | [../concepts/control-flow.md](../concepts/control-flow.md) | Deep extraction | must create | 11 claims covering blocks, contain, every | created |
| Data Types | [../concepts/data-types.md](../concepts/data-types.md) | Deep extraction | must create | 45 claims covering expressions, javascript, that | created |
| ES6 Features | [../concepts/es6-features.md](../concepts/es6-features.md) | Deep extraction | must create | 18 claims covering const, ecmascript, introduced | created |
| Functional Programming | [../concepts/functional-programming.md](../concepts/functional-programming.md) | Deep extraction | must create | 8 claims covering composed, folding, functions | created |
| Functions | [../concepts/functions.md](../concepts/functions.md) | Deep extraction | must create | 96 claims covering book, focuses, javascript | created |
| Iterators | [../concepts/iterators.md](../concepts/iterators.md) | Deep extraction | must create | 40 claims covering filtering, function, iterator | created |
| Objects | [../concepts/objects.md](../concepts/objects.md) | Deep extraction | must create | 10 claims covering created, javascript, object | created |
| Recursion | `../concepts/recursion.md` | Deep extraction | must create | 15 claims covering algorithms, functions, linear | not created yet |
