---
page_id: javascriptallonge-applying-functions
page_kind: source
summary: Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.78-78
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the 'Functions' section from JavaScript Allongé.

## Key supported claims

- Functions are values that can be part of expressions, returned from other functions, and so forth (raw/javascriptallonge.pdf p.78-78).
- Functions are reference values (raw/javascriptallonge.pdf p.78-78).
- Functions are applied to arguments (raw/javascriptallonge.pdf p.78-78).
- Fat arrow functions have expressions or blocks as their bodies (raw/javascriptallonge.pdf p.78-78).
- Function keyword functions always have blocks as their bodies (raw/javascriptallonge.pdf p.78-78).

## Technical details

### `technical-atom-0a0a236a703ac3df` code

Citation: (raw/javascriptallonge.pdf p.78)

```
fn_expr ( args )
```

### `technical-atom-9b869fb5642755dc` code

Citation: (raw/javascriptallonge.pdf p.78)

```javascript
(() => 0)() //=> 0
```

### `technical-atom-a16c68b137f59cbe` requirement

Citation: (raw/javascriptallonge.pdf p.31)

- function keyword functions always have blocks as their bodies.

### `technical-atom-b0a12df78d1155e0` exception

Citation: (raw/javascriptallonge.pdf p.31)

Right now, we only know about one such expression: () => 0 , so let's use it.

## Related technical details

### From [[javascriptallonge-functions-that-return-values-and-evaluate-expressions]]: `technical-atom-053e216a0ba143de` code

Relation: nearby source page; matched terms `expressions`, `functions`, `javascript`, `values`

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => 1)() //=> 1 (() => "Hello, JavaScript")() //=> "Hello, JavaScript" (() => Infinity )() //=> Infinity
```

### From [[javascriptallonge-functions-that-return-values-and-evaluate-expressions]]: `technical-atom-b5a28ac67439659d` code

Relation: nearby source page; matched terms `expressions`, `functions`, `javascript`, `values`

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity
```

### From [[javascriptallonge-functions-that-return-values-and-evaluate-expressions]]: `technical-atom-1172baccc0a24ff7` code

Relation: nearby source page; matched terms `expressions`, `functions`, `values`

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => (() => 0)())() //=> 0
```

### From [[javascriptallonge-functions-that-return-values-and-evaluate-expressions]]: `technical-atom-be7839225be60f3a` code

Relation: nearby source page; matched terms `expressions`, `functions`, `values`

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => (() => 0 )() )() //=> 0
```
