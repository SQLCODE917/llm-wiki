---
page_id: javascriptallonge-variables-and-bindings
page_kind: source
summary: variables and bindings from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.41-42
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on variables and bindings from 'JavaScript Allongé', discussing functions, environments, and variable bindings.

## Key supported claims

- Functions that make functions, environments, and variables are important (raw/javascriptallonge.pdf p.41-42).
- An environment is a dictionary mapping variables to values (raw/javascriptallonge.pdf p.41-42).
- The second x in => x is an expression referring to a variable (raw/javascriptallonge.pdf p.41-42).
- Arguments and variables work the same way in nested functions (raw/javascriptallonge.pdf p.41-42).
- Variables are evaluated by looking up values in the environment (raw/javascriptallonge.pdf p.41-42).

## Technical details

### `technical-atom-2be534c1fdc45eb4` code

Citation: (raw/javascriptallonge.pdf p.41-42)

```javascript
(x) => (y) => x
```

### `technical-atom-1d04afad197de418` code

Citation: (raw/javascriptallonge.pdf p.41-42)

```javascript
((x) => x)(2) //=> 2
```

### `technical-atom-2a1d586167017e1b` requirement

Citation: (raw/javascriptallonge.pdf p.41-42)

In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries').

### `technical-atom-2df7b8701e2981a7` procedure

Citation: (raw/javascriptallonge.pdf p.41-42)

- It then starts evaluating the expression, including evaluating sub-expressions

### `technical-atom-4104013a1bcd0825` code

Citation: (raw/javascriptallonge.pdf p.41-42)

```
When we talk about environments, we'll use an unsurprising syntax 25 for showing their bindings: {x: 2, ...} .
```
