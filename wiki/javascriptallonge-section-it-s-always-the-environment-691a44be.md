---
page_id: javascriptallonge-section-it-s-always-the-environment-691a44be
page_kind: source
summary: **it’s always the environment**: 15 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-it-s-always-the-environment-691a44be@98dca293396e83d10803e1d0d5f2034f
---

# **it’s always the environment**

From [[javascriptallonge]].

## Statements

- We also hand-waved something when describing our environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument. _(javascriptallonge.pdf (source-range-83ecb080-00505))_
- Some people get so excited by this that they write entire books about them, some are great _[a]_ , some–how shall I put this–are interesting _[b]_ if you use Ruby. _(javascriptallonge.pdf (source-range-83ecb080-00506))_
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3). _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3). _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- The first function is the result of currying _[a]_ the second function. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00516))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00503))_

> To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00504))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00509))_

> Functions can have grandparents too:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00510))_

> (x) => (y) => (z) => x + y + z

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00511))_

> This function does much the same thing as:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00512))_

> (x, y, z) => x + y + z
