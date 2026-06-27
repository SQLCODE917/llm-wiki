---
page_id: javascriptallonge-section-defaults-and-destructuring-a42a676b
page_kind: source
summary: **defaults and destructuring**: 6 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-defaults-and-destructuring-a42a676b@90b7587ad5afacc513e393c727045362
---

# **defaults and destructuring**

From [[javascriptallonge]].

## Statements

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-83ecb080-01493))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-83ecb080-01500))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01493))_

> We saw earlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01496))_

> **const** [first, second = "two"] = ["one"];

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01497))_

> ` ` **${** first **}** . **${** second **}** _//=> "one . two"_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01498))_

> **const** [first, second = "two"] = ["primus", "secundus"];

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01499))_

> ` ` **${** first **}** . **${** second **}** _//=> "primus . secundus"_
