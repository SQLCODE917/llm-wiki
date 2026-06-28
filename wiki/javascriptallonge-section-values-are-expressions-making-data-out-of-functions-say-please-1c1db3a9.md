---
page_id: javascriptallonge-section-values-are-expressions-making-data-out-of-functions-say-please-1c1db3a9
page_kind: source
summary: values are expressions / Making Data Out Of Functions / say “please”: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-making-data-out-of-functions-say-please-1c1db3a9@5f8044042cb8a198b8b458e4798e7cf2
---

# values are expressions / Making Data Out Of Functions / say “please”

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-8e373317]] - broader source section

## Statements

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-83ecb080-01385))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-01386))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-01386))_
- Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. _(javascriptallonge.pdf (source-range-83ecb080-01387))_
- Now we’ll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-83ecb080-01388))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-83ecb080-01394))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-01397))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01390))_

> How would all this work? Let’s start with the obvious. What is an empty list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01391))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() And what is a node of a list?

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01391))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() And what is a node of a list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01392))_

> **const** node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
