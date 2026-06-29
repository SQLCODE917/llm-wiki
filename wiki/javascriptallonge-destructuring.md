---
page_id: javascriptallonge-destructuring
page_kind: concept
summary: Destructuring: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-destructuring@ab40757e7e456733d1cfd01d112097e1
---

# Destructuring

What [[javascriptallonge]] covers about destructuring:

## Statements

### defaults and destructuring

- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-8eb13d6b-01013))_


## Technical atoms

### Technical frame 1: destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00872))_

```
const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameAndOccupation; return [` ${ first } is a ${ occupation } `, "ok"]; } } const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); reg //=> "Reginald is a programmer" status //=> "ok"
```

### Technical frame 2: defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01013))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01012))_

```
const [first, second = "two"] = ["one"]; ` ${ first } . ${ second } ` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } . ${ second } ` //=> "primus . secundus"
```


## Related pages

- [[javascriptallonge-default]] - shared statements and technical atoms: Default shares source evidence from defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Default shares technical record from defaults and destructuring: const [first, second = "two"] = ["one"]; ` ${ first } . ${ second } ` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } . ${ seco ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms: Learn shares technical record from defaults and destructuring: const [first, second = "two"] = ["one"]; ` ${ first } . ${ second } ` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } . ${ seco ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
