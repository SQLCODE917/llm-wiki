---
page_id: javascriptallonge-pattern
page_kind: concept
summary: Pattern: 7 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pattern@7abececce805e03c491e672e309599b5
---

# Pattern

What [[javascriptallonge]] covers about pattern:

## Statements

- Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-83ecb080-00593))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” The first sip: Basic Functions _(javascriptallonge.pdf (source-range-83ecb080-00444))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00597))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-83ecb080-01139))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01249))_
- This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . _(javascriptallonge.pdf (source-range-83ecb080-01593))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing _(javascriptallonge.pdf (source-range-83ecb080-01725))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00597))_

> If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00599))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements.


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-follow]] - shared statements (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements (1 shared statement(s))
- [[javascriptallonge-data-structure]] - shared statements (1 shared statement(s))
- [[javascriptallonge-mutation]] - shared statements (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
