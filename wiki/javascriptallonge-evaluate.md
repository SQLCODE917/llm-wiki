---
page_id: javascriptallonge-evaluate
page_kind: concept
summary: Evaluate: 8 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-evaluate@0e5a66ba1c611eb25684534ee358f80b
---

# Evaluate

What [[javascriptallonge]] covers about evaluate:

## Statements

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- No matter how you evaluate undefined, you get an identical value back. _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- Block bodies evaluate to whatever is returned with the return keyword, or to undefined. _(javascriptallonge.pdf (source-range-83ecb080-00913))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-01121))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00325))_

> No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00323))_

> **undefined** === **undefined**

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00354))_

> (() => { 2 + 2 })() _//=> undefined_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00355))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00356))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00503))_

> To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00504))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01119))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01120))_

> **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';


## Related pages

- [[javascriptallonge-expression]] - shared statements and technical atoms (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements (2 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
