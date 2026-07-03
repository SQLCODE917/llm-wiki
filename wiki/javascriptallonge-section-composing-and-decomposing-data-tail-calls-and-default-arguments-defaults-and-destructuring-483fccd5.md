---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-defaults-and-destructuring-483fccd5
page_kind: source
page_family: section-reference
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-defaults-and-destructuring-483fccd5@f3bf7e98bacc37d709b9403a0f5d2211
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1]] - broader source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

## Statements

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-7239e085-01011))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-7239e085-01013))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01013))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01012))_

<a id="atom-technical-atom-84d6051e5ecacc53"></a>

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```
