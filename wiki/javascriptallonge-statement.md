---
page_id: javascriptallonge-statement
page_kind: concept
summary: Statement: 6 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-statement@4168375be7046e6705ed7cbb179bec43
---

# Statement

What [[javascriptallonge]] covers about statement:

## Statements

- One of the important possible statements is a return statement. _(javascriptallonge.pdf (source-range-83ecb080-00320))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. _(javascriptallonge.pdf (source-range-83ecb080-00469))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00487))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00502))_
- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-83ecb080-00658))_
- The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. _(javascriptallonge.pdf (source-range-83ecb080-00851))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00851))_

> The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00853))_

> 81 **const** surname = (name) => { **const** [first, last] = name; **return** last; } surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_


## Related pages

- [[javascriptallonge-array]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-block]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
