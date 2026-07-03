---
page_id: javascriptallonge-destructuring
page_kind: concept
page_family: topic-concept
summary: Destructuring: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-destructuring@bee3e3bbde858d0e0fc28eece02077db
---

# Destructuring

What [[javascriptallonge]] covers about destructuring:

## Statements

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

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

### Technical atom 2

<a id="atom-technical-atom-e059157473f56d35"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00871))_

> Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring:

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


## Related pages

### Shared technical atoms

- [[javascriptallonge-default]] - shared statements and technical atoms: Default shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Default shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms: Learn shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
