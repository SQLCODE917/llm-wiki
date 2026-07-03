---
page_id: javascriptallonge-recipe-defaults-and-destructuring
page_kind: recipe
page_family: recipe-pattern
summary: defaults and destructuring: reusable source-backed pattern with 2 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: defaults-and-destructuring
projection_coverage: recipe-javascriptallonge-recipe-defaults-and-destructuring@abab1c040915e7e0fa00518ba58bd4e5
---

# defaults and destructuring

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-defaults-and-destructuring-483fccd5]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-7239e085-01011))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-7239e085-01013))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01012)_

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-defaults-and-destructuring-483fccd5]]
