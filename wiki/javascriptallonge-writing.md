---
page_id: javascriptallonge-writing
page_kind: concept
summary: Writing: 6 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-writing@ee6e20fabf92f2be658f3bc846aff7e6
---

# Writing

What [[javascriptallonge]] covers about writing:

## Statements

### michael fogus

- The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I've found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude. _(javascriptallonge.pdf (source-range-8eb13d6b-00085))_

### void

- By writing undefined ourselves. _(javascriptallonge.pdf (source-range-8eb13d6b-00232))_

### a balanced statement about combinators

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-8eb13d6b-00573))_

### A Warm Cup: Basic Strings and Quasi-Literals

- String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-8eb13d6b-01502))_

### more generators

- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-8eb13d6b-01724))_

### Summary

- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-8eb13d6b-01758))_


## Technical atoms

### Technical frame 1: a balanced statement about combinators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00579))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00574))_

```
const something = (x) => x != null ;
```


## Related pages

- [[javascriptallonge-instead]] - shared statements and technical atoms: Instead shares source evidence from a balanced statement about combinators: So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:; Instead shares technical record from a balanced statement about combinators: const something = (x) => x != null ; (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from more generators: We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of s ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from more generators: We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of s ... [truncated] (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Summary: A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from more generators: We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of s ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
