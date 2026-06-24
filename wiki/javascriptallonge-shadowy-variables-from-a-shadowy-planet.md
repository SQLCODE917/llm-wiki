---
page_id: javascriptallonge-shadowy-variables-from-a-shadowy-planet
page_kind: source
summary: shadowy variables from a shadowy planet from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.47-47
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. JavaScript searches for a binding starting with the function's own environment and then each parent in turn until it finds one. An interesting thing happens when a variable has the same name as an ancestor environment's variable.

## Key supported claims

- A variable shadows an ancestor when names match, (raw/javascriptallonge.pdf p.47-47).
- JavaScript searches environments from child to parent, (raw/javascriptallonge.pdf p.47-47).
- A function is pure if its x is defined within its own environment, (raw/javascriptallonge.pdf p.47-47).

## Technical details

### `technical-atom-09c4361291d7bd60` code

Citation: (raw/javascriptallonge.pdf p.47)

```javascript
(x) => (x, y) => x + y
```

### `technical-atom-2238642332b0495e` code

Citation: (raw/javascriptallonge.pdf p.47)

```javascript
(x) => (x, y) => (w, z) => (w) => x + y + z
```

### `technical-atom-592864b8cc8594c9` procedure

Citation: (raw/javascriptallonge.pdf p.47)

JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one.

## Related technical details

### From [[javascriptallonge-it-s-always-the-environment]]: `technical-atom-6582cc9837c81ff3` requirement

Relation: nearby source page; matched terms `environment`, `function`, `has`, `its`, `parent`

Citation: (raw/javascriptallonge.pdf p.46-47)

So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### From [[javascriptallonge-which-came-first-the-chicken-or-the-egg]]: `technical-atom-93fe1495d6cb435a` requirement

Relation: nearby source page; matched terms `environment`, `has`, `javascript`, `one`

Citation: (raw/javascriptallonge.pdf p.47-48)

JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions.

### From [[javascriptallonge-which-came-first-the-chicken-or-the-egg]]: `technical-atom-4c659777740464a5` code

Relation: nearby source page; matched terms `environment`, `its`, `when`

Citation: (raw/javascriptallonge.pdf p.47-48)

```
So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .
```

### From [[javascriptallonge-inside-out]]: `technical-atom-7c02e176bb54dfd2` procedure

Relation: nearby source page; matched terms `function`, `its`, `name`, `then`

Citation: (raw/javascriptallonge.pdf p.50-51)

There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression.
