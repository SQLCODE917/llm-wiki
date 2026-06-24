---
page_id: javascriptallonge-destructuring-is-not-pattern-matching
page_kind: source
summary: destructuring is not pattern matching from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.105-106
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the section 'destructuring is not pattern matching' from javascriptallonge.pdf

## Key supported claims

- But this is not how JavaScript works, as it tries its best to assign things and binds undefined when there isn't a match. (raw/javascriptallonge.pdf p.105-106)
- That match would fail in pattern matching languages, but JavaScript binds undefined instead. (raw/javascriptallonge.pdf p.105-106)
- JavaScript coerces values and passes undefined to keep executing, often requiring custom code to detect failure conditions. (raw/javascriptallonge.pdf p.105-106)

## Technical details

### `technical-atom-89cdabc3cb9e7f9f` code

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [what] = [];
```

### `technical-atom-1b1f471330642106` code

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [what] = []; what //=> undefined const [which, what, who //=> undefined
```

### `technical-atom-b77da3ce96a4fb74` code

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [...they] = []; they //=> [] const [which, what, they //=> []
```

### `technical-atom-880219b3a5b552f7` exception

Citation: (raw/javascriptallonge.pdf p.105-106)

As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing.

### `technical-atom-820341aea79f7af4` exception

Citation: (raw/javascriptallonge.pdf p.105-106)

This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

## Related technical details

### From [[javascriptallonge-gathering]]: `technical-atom-fdf4ebc731b1361f` code

Relation: nearby source page; matched terms `array`, `code`, `destructuring`, `when`, `would`

Citation: (raw/javascriptallonge.pdf p.104-105)

```javascript
const [...butLast, last] = [1, 2, 3, 4, 5]; //=> ERROR const [first, ..., last] = [1, 2, 3, 4, 5]; //=> ERROR Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. So if const wrapped = [something]; Then: const [unwrapped] = something; What is the reverse of gathering? We know that: const [car, ...cdr] = [1, 2, 3, 4, 5]; What is the reverse? It would be: const cons = [car, ...cdr]; oneTwoThree = ["one", "two", "three"];
```

### From [[javascriptallonge-self-similarity]]: `technical-atom-5d9fe5bf28074a51` exception

Relation: nearby source page; matched terms `but`, `not`, `undefined`

Citation: (raw/javascriptallonge.pdf p.109-111)

61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples.

### From [[javascriptallonge-self-similarity]]: `technical-atom-9f1556f765136bb2` code

Relation: nearby source page; matched terms `array`, `but`, `code`, `keep`, `would`

Citation: (raw/javascriptallonge.pdf p.109-111)

```
A more robust implementation would be (array) => array.length === 0 , but we are doing backflips to keep this within a very small and contrived playground.
```

### From [[javascriptallonge-destructuring-and-return-values]]: `technical-atom-41384d0ebd0a8674` code

Relation: nearby source page; matched terms `code`, `destructuring`, `values`

Citation: (raw/javascriptallonge.pdf p.106-107)

```javascript
const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameAndOccupation; return [` ${ first } is a ${ occupation } `, "ok"]; } } const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); reg //=> "Reginald is a programmer" status //=> "ok"
```
