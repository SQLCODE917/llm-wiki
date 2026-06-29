---
page_id: javascriptallonge-destructuring
page_kind: concept
summary: Destructuring: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-destructuring@56098512aaeb447c8eed83a939179c55
---

# Destructuring

What [[javascriptallonge]] covers about destructuring:

## Statements

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-7239e085-01013))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00872))_

```
const description = (nameAndOccupation) => {
if (nameAndOccupation.length < 2) {
return ["", "occupation missing"]
}
else {
const [[first, last], occupation] = nameAndOccupation;
return [`${first} is a ${occupation}`, "ok"];
}
}
const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]);
reg
//=> "Reginald is a programmer"
status
//=> "ok"
```

### Technical frame 2: Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

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

- [[javascriptallonge-default]] - shared statements and technical atoms: Default shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Default shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms: Learn shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
