---
page_id: javascriptallonge-it-s-always-the-environment
page_kind: source
summary: it's always the environment from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.46-47
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses environments and closures in JavaScript, specifically how functions are associated with environments and how closures are evaluated.

## Key supported claims

- So whenever a function is applied to arguments, its environment always has a reference to its parent environment (raw/javascriptallonge.pdf p.46-47).
- As we've said before, all functions are associated with an environment (raw/javascriptallonge.pdf p.46-47).
- We also hand-waved something when describing our environment (raw/javascriptallonge.pdf p.46-47).
- To understand how closures are evaluated, we need to revisit environments (raw/javascriptallonge.pdf p.46-47).

## Technical details

### `technical-atom-8990dcd4a42533b8` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```
b
```

### `technical-atom-0f257aa93452b36e` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```javascript
(x) => (y) => (z) => x + y + z
```

### `technical-atom-ec89248e65cc15c2` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```javascript
(x, y, z) => x + y + z
```

### `technical-atom-99a5eb8960ea8a05` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```
a b
```

### `technical-atom-070b602fce748acf` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```
Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ?
```

### `technical-atom-1716060b0812887f` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```
The environment for ((y) => x)(2) is actually {y: 2, '..': {x: 1, ...}} .
```

### `technical-atom-562cfa7c3d8654ff` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```
And now you can guess how we evaluate ((y) => x)(2) in the environment {y: 2, '..': {x: 1, ...}} .
```

### `technical-atom-6582cc9837c81ff3` requirement

Citation: (raw/javascriptallonge.pdf p.46-47)

So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

## Related technical details

### From [[javascriptallonge-which-came-first-the-chicken-or-the-egg]]: `technical-atom-93fe1495d6cb435a` requirement

Relation: nearby source page; matched terms `always`, `environment`, `functions`, `has`, `javascript`

Citation: (raw/javascriptallonge.pdf p.47-48)

JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions.

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-e8199c3947c572cb` requirement

Relation: nearby source page; matched terms `always`, `arguments`, `closures`, `function`, `our`, `reference`

Citation: (raw/javascriptallonge.pdf p.42-43)

When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to:

### From [[javascriptallonge-shadowy-variables-from-a-shadowy-planet]]: `technical-atom-592864b8cc8594c9` procedure

Relation: nearby source page; matched terms `always`, `environment`, `functions`, `javascript`, `parent`

Citation: (raw/javascriptallonge.pdf p.47)

JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one.

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-247ce19e93a86869` requirement

Relation: nearby source page; matched terms `environment`, `function`, `javascript`, `when`

Citation: (raw/javascriptallonge.pdf p.42-43)

There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original.
