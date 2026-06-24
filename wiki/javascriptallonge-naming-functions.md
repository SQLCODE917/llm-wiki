---
page_id: javascriptallonge-naming-functions
page_kind: source
summary: Naming Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.62-62
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on naming functions in JavaScript Allongé, covering arrow functions, function keyword, named function expressions, and hoisting.

## Key supported claims

- Binding an anonymous function to a name in an environment does not name the function itself (raw/javascriptallonge.pdf p.62-62).
- Arrow functions bind anonymous functions; the function stays unnamed (raw/javascriptallonge.pdf p.62-62).
- Named function expressions provide an internal name for recursion but do not affect the environment binding (raw/javascriptallonge.pdf p.62-62).

## Technical details

### `technical-atom-0ea8d8d83b9803e9` code

Citation: (raw/javascriptallonge.pdf p.62)

```javascript
const repeat = (str) => str + str
```

### `technical-atom-948ee531147ee69c` formula

Citation: (raw/javascriptallonge.pdf p.62)

It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 .

### `technical-atom-b521eb56bb5cda47` exception

Citation: (raw/javascriptallonge.pdf p.62)

This code does not name a function:

## Related technical details

### From [[javascriptallonge-rebinding]]: `technical-atom-3ee28a0dd987831d` exception

Relation: nearby source page; matched terms `does`, `javascript`, `name`, `not`

Citation: (raw/javascriptallonge.pdf p.60-61)

JavaScript does not permit us to rebind a name that has been bound with const .

### From [[javascriptallonge-the-function-keyword]]: `technical-atom-e3ae7448df2db828` code

Relation: nearby source page; matched terms `function`, `keyword`, `repeat`

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
const repeat = function repeat (str) { return str + str; }; const fib = function fib (n) { return (1.618**n - -1.618**-n) / 2.236; };
```

### From [[javascriptallonge-the-function-keyword]]: `technical-atom-8aacb0eaceffe66c` code

Relation: nearby source page; matched terms `function`, `keyword`, `repeat`

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
const double = function repeat (str) { return str + str; }
```

### From [[javascriptallonge-function-declaration-caveats-34]]: `technical-atom-68210eea018a360c` code

Relation: nearby source page; matched terms `but`, `function`, `not`

Citation: (raw/javascriptallonge.pdf p.66-67)

```javascript
function trueDat () { return true } But this is not: ( function trueDat () { return true })
```
