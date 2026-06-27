---
page_id: javascriptallonge-section-defaults-and-destructuring-a42a676b
page_kind: source
summary: **defaults and destructuring**: 6 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-defaults-and-destructuring-a42a676b@b30c13e5a62f3fb5197a850ce257dd1d
---

# **defaults and destructuring**

From [[javascriptallonge]].

## Statements

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-83ecb080-01493))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-83ecb080-01500))_

## Technical atoms

> Context: We saw earlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment?
_(context: javascriptallonge.pdf (source-range-83ecb080-01493))_

> **const** [first, second = "two"] = ["one"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01496))_

> ` ` **${** first **}** . **${** second **}** _//=> "one . two"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01497))_

> **const** [first, second = "two"] = ["primus", "secundus"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01498))_

> ` ` **${** first **}** . **${** second **}** _//=> "primus . secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01499))_
