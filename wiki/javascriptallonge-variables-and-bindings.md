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

### `technical-atom-4104013a1bcd0825` code

Citation: (raw/javascriptallonge.pdf p.41-42)

```
When we talk about environments, we'll use an unsurprising syntax 25 for showing their bindings: {x: 2, ...} .
```

### `technical-atom-2df7b8701e2981a7` procedure

Citation: (raw/javascriptallonge.pdf p.41-42)

- It then starts evaluating the expression, including evaluating sub-expressions

### `technical-atom-2a1d586167017e1b` requirement

Citation: (raw/javascriptallonge.pdf p.41-42)

In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries').

## Related technical details

### From [[javascriptallonge-functions-that-evaluate-to-functions]]: `technical-atom-e3624af5aae576df` procedure

Relation: nearby source page; matched terms `argument`, `functions`, `make`

Citation: (raw/javascriptallonge.pdf p.38)

So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-247ce19e93a86869` requirement

Relation: nearby source page; matched terms `argument`, `call`, `environment`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.42-43)

There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original.

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-9aa4fc764ee229f5` exception

Relation: nearby source page; matched terms `call`, `environment`, `javascript`, `not`, `values`

Citation: (raw/javascriptallonge.pdf p.42-43)

JavaScript does not place copies of reference values in any environment.

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-e8199c3947c572cb` requirement

Relation: nearby source page; matched terms `argument`, `arguments`, `call`, `function`

Citation: (raw/javascriptallonge.pdf p.42-43)

When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to:
