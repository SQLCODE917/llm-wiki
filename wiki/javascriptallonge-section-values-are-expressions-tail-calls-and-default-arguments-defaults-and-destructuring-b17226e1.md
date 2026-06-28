---
page_id: javascriptallonge-section-values-are-expressions-tail-calls-and-default-arguments-defaults-and-destructuring-b17226e1
page_kind: source
summary: values are expressions / Tail Calls (and Default Arguments) / defaults and destructuring: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-tail-calls-and-default-arguments-defaults-and-destructuring-b17226e1@3635862e25ba527e76da5ccff0945a47
---

# values are expressions / Tail Calls (and Default Arguments) / defaults and destructuring

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-tail-calls-and-default-arguments-a342c756]] - broader source section

## Statements

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-83ecb080-01005))_
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

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01009))_

> ` ` **${** first **}** . **${** second **}** _//=> "primus . secundus"_
