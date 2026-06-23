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

### `technical-atom-93fe1495d6cb435a` requirement

Citation: (raw/javascriptallonge.pdf p.47-48)

JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions.

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
