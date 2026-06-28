---
page_id: javascriptallonge-destructuring
page_kind: concept
summary: Destructuring: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-destructuring@4a02ab6c801d9f2f90b05db76e2b5fa6
---

# Destructuring

What [[javascriptallonge]] covers about destructuring:

## Statements

- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-83ecb080-01010))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01005))_

> We saw earlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01007))_

> 102 **const** [first, second = "two"] = ["one"];

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01005))_

> We saw earlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01008))_

> ` ` **${** first **}** . **${** second **}** _//=> "one . two"_ **const** [first, second = "two"] = ["primus", "secundus"];


## Related pages

- [[javascriptallonge-destructuring-argument]] - narrower topic
- [[javascriptallonge-default]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms (2 shared atom(s))

## Source

- [[javascriptallonge]]
