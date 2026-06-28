---
page_id: javascriptallonge-section-defaults-and-destructuring-bb2261b7
page_kind: source
summary: defaults and destructuring: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-defaults-and-destructuring-bb2261b7@7d0c5e6dd9aa8d89d61678a4a03c0ad1
---

# defaults and destructuring

From [[javascriptallonge]].

## Statements

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-31a4cf47-01011))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-31a4cf47-01013))_

## Technical atoms

### Technical frame 1: defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01013))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01012))_

```
const [first, second = "two"] = ["one"]; ` ${ first } . ${ second } ` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } . ${ second } ` //=> "primus . secundus"
```
