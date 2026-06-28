---
page_id: javascriptallonge-version
page_kind: concept
summary: Version: 5 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-version@1a2273778451ccb0ffb5d0f489a30d34
---

# Version

What [[javascriptallonge]] covers about version:

## Statements

- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-83ecb080-01650))_
- That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. _(javascriptallonge.pdf (source-range-83ecb080-00077))_
- > 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) The first sip: Basic Functions _(javascriptallonge.pdf (source-range-83ecb080-00587))_
- This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-83ecb080-00976))_
- So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. _(javascriptallonge.pdf (source-range-83ecb080-01677))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00976))_

> This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00978))_

> 98 **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === **undefined**


## Related pages

- [[javascriptallonge-length]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-foreword-six-edition]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function-decorator]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
