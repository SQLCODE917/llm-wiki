---
page_id: javascriptallonge-destructuring-and-return-values
page_kind: source
summary: destructuring and return values from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.106-107
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses how some languages support multiple return values, and how this can be emulated in JavaScript using destructuring.

## Key supported claims

- Some languages support multiple return values: A function can return several things at once, like a value and an error code. (raw/javascriptallonge.pdf p.106-107)
- This can easily be emulated in JavaScript with destructuring. (raw/javascriptallonge.pdf p.106-107)
- In JavaScript, a function can return multiple values using destructuring. (raw/javascriptallonge.pdf p.106-107)

## Technical details

### `technical-atom-41384d0ebd0a8674` code

Citation: (raw/javascriptallonge.pdf p.106-107)

```javascript
const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameAndOccupation; return [` ${ first } is a ${ occupation } `, "ok"]; } } const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); reg //=> "Reginald is a programmer" status //=> "ok"
```

## Related technical details

### From [[javascriptallonge-destructuring-arrays]]: `technical-atom-1e5a58d3eb938f40` code

Relation: nearby source page; matched terms `code`, `const`, `description`, `destructuring`, `nameandoccupation`, `occupation`

Citation: (raw/javascriptallonge.pdf p.103-104)

```javascript
const description = (nameAndOccupation) => { const [[first, last], occupation] = nameAndOccupation; return ` ${ first } is a ${ occupation } `; } description([["Reginald", "Braithwaite"], "programmer"]) //=> "Reginald is a programmer"
```

### From [[javascriptallonge-gathering]]: `technical-atom-fdf4ebc731b1361f` code

Relation: nearby source page; matched terms `code`, `const`, `destructuring`, `error`

Citation: (raw/javascriptallonge.pdf p.104-105)

```javascript
const [...butLast, last] = [1, 2, 3, 4, 5]; //=> ERROR const [first, ..., last] = [1, 2, 3, 4, 5]; //=> ERROR Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. So if const wrapped = [something]; Then: const [unwrapped] = something; What is the reverse of gathering? We know that: const [car, ...cdr] = [1, 2, 3, 4, 5]; What is the reverse? It would be: const cons = [car, ...cdr]; oneTwoThree = ["one", "two", "three"];
```

### From [[javascriptallonge-destructuring-is-not-pattern-matching]]: `technical-atom-89cdabc3cb9e7f9f` code

Relation: nearby source page; matched terms `code`, `const`, `destructuring`

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [what] = [];
```

### From [[javascriptallonge-destructuring-is-not-pattern-matching]]: `technical-atom-1b1f471330642106` code

Relation: nearby source page; matched terms `code`, `const`, `destructuring`

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [what] = []; what //=> undefined const [which, what, who //=> undefined
```
