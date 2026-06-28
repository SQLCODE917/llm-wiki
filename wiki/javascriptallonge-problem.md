---
page_id: javascriptallonge-problem
page_kind: concept
summary: Problem: 7 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-problem@2709a10e7c3681902fe9800dd9ea7d32
---

# Problem

What [[javascriptallonge]] covers about problem:

## Statements

- A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). _(javascriptallonge.pdf (source-range-83ecb080-00714))_
- When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-83ecb080-00914))_
- Another common problem is applying a function to every element of an array. _(javascriptallonge.pdf (source-range-83ecb080-00925))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01062))_
- One strategy for avoiding problems is to be _pessimistic_ . _(javascriptallonge.pdf (source-range-83ecb080-01233))_
- The problem is this: The game board is hidden from us. _(javascriptallonge.pdf (source-range-83ecb080-01833))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-83ecb080-01863))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00916))_

> This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00917))_

> Array.isArray("foo") - _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00916))_

> This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00918))_

> Array.isArray(["foo"]) - _//=> true_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01833))_

> The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01834))_

> You may use babeljs.io[95] , or ES6Fiddle[96] to check your work.


## Related pages

- [[javascriptallonge-element]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-recursion]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-algorithm]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements (1 shared statement(s))
- [[javascriptallonge-section-values-are-expressions-interlude-the-carpenter-interviews-for-a-job-the-problem-0505b65a]] - source section (8 shared statement(s), 2 shared atom(s))

## Source

- [[javascriptallonge]]
