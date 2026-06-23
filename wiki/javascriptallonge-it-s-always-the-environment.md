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

### `technical-atom-6582cc9837c81ff3` requirement

Citation: (raw/javascriptallonge.pdf p.46-47)

So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### `technical-atom-562cfa7c3d8654ff` code

Citation: (raw/javascriptallonge.pdf p.46-47)

```
And now you can guess how we evaluate ((y) => x)(2) in the environment {y: 2, '..': {x: 1, ...}} .
```
