---
page_id: javascriptallonge-default
page_kind: concept
summary: Default: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-default@97423f76cd0627a5d297ca161b16fedb
---

# Default

What [[javascriptallonge]] covers about default:

## Statements

### defaults and destructuring

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


## Related pages

- [[javascriptallonge-destructuring]] - shared statements and technical atoms: Destructuring shares source evidence from defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Destructuring shares technical record from defaults and destructuring: const [first, second = "two"] = ["one"]; ` ${ first } . ${ second } ` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } . ${ seco ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-learn]] - shared statements and technical atoms: Learn shares source evidence from defaults and destructuring: Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we creat ... [truncated]; Learn shares technical record from defaults and destructuring: const [first, second = "two"] = ["one"]; ` ${ first } . ${ second } ` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } . ${ seco ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
