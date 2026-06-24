---
page_id: javascriptallonge-which-came-first-the-chicken-or-the-egg
page_kind: source
summary: which came first, the chicken or the egg? from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.47-48
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explores the ancestry of JavaScript functions and environments, specifically discussing pure functions, closures, and the global environment. It also touches on mutable state and how to avoid direct interaction with the global environment by creating isolated environments.

## Key supported claims

- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions (raw/javascriptallonge.pdf p.47-48).
- As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program (raw/javascriptallonge.pdf p.47-48).
- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software (raw/javascriptallonge.pdf p.47-48).

## Technical details

### `technical-atom-94a9db2d6061e08c` code

Citation: (raw/javascriptallonge.pdf p.47-48)

```javascript
// top of the file (() => { // ... lots of JavaScript ... })(); // bottom of the file
```

### `technical-atom-4c659777740464a5` code

Citation: (raw/javascriptallonge.pdf p.47-48)

```
So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .
```

### `technical-atom-c637696a35997aea` code

Citation: (raw/javascriptallonge.pdf p.47-48)

```
The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} .
```

### `technical-atom-93fe1495d6cb435a` requirement

Citation: (raw/javascriptallonge.pdf p.47-48)

JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions.

## Related technical details

### From [[javascriptallonge-shadowy-variables-from-a-shadowy-planet]]: `technical-atom-592864b8cc8594c9` procedure

Relation: nearby source page; matched terms `always`, `environment`, `functions`, `javascript`, `one`

Citation: (raw/javascriptallonge.pdf p.47)

JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one.

### From [[javascriptallonge-it-s-always-the-environment]]: `technical-atom-6582cc9837c81ff3` requirement

Relation: nearby source page; matched terms `always`, `environment`, `has`

Citation: (raw/javascriptallonge.pdf p.46-47)

So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### From [[javascriptallonge-it-s-always-the-environment]]: `technical-atom-562cfa7c3d8654ff` code

Relation: nearby source page; matched terms `always`, `can`, `code`, `environment`, `how`

Citation: (raw/javascriptallonge.pdf p.46-47)

```
And now you can guess how we evaluate ((y) => x)(2) in the environment {y: 2, '..': {x: 1, ...}} .
```

### From [[javascriptallonge-it-s-always-the-environment]]: `technical-atom-8990dcd4a42533b8` code

Relation: nearby source page; matched terms `always`, `code`, `environment`

Citation: (raw/javascriptallonge.pdf p.46-47)

```
b
```
