---
page_id: javascriptallonge-evaluate
page_kind: concept
summary: Evaluate: 6 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-evaluate@53aaa0b79f2f79081457cab4b6c583e4
---

# Evaluate

What [[javascriptallonge]] covers about evaluate:

## Statements

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- No matter how you evaluate undefined, you get an identical value back. _(javascriptallonge.pdf (source-range-83ecb080-00269))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00407))_
- Block bodies evaluate to whatever is returned with the return keyword, or to undefined. _(javascriptallonge.pdf (source-range-83ecb080-00655))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-00779))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00269))_

> No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00267))_

> **undefined** === **undefined**

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00396))_

> To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00397))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.


## Related pages

- [[javascriptallonge-evaluate-expression]] - narrower topic
- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-closure]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements (2 shared statement(s))
- [[javascriptallonge-block]] - shared statements (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
