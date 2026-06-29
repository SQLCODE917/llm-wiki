---
page_id: javascriptallonge-default
page_kind: concept
summary: Default: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-default@692893982ce8c4f945971a1687ed640b
---

# Default

What [[javascriptallonge]] covers about default:

## Statements

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-7239e085-01011))_

- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-7239e085-01013))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01013))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01012))_

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```


## Related pages

- [[javascriptallonge-destructuring]] - shared statements and technical atoms: Destructuring shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Destructuring shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-learn]] - shared statements and technical atoms: Learn shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we creat ... [truncated]; Learn shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
