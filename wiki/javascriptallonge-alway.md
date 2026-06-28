---
page_id: javascriptallonge-alway
page_kind: concept
summary: Alway: 6 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-alway@25eecd69927706dd0f52da2599ace082
---

# Alway

What [[javascriptallonge]] covers about alway:

## Statements

- They always mean the same thing wherever you use them. _(javascriptallonge.pdf (source-range-83ecb080-00383))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00421))_
- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-83ecb080-00652))_
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-01027))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00383, source-range-83ecb080-00387))_

> Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00386))_

> - (x) => (y) => x

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00391))_

> Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00390))_

> If pure functions can contain closures, can a closure contain a pure function?

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00421))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00422))_

> If you don’t want your code to operate directly within the global environment, what can you do?


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-pure]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-closure]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-argument]] - shared statements (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
