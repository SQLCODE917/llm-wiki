---
page_id: javascriptallonge-var
page_kind: source
summary: var from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.151-154
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This page summarizes the 'var' keyword in JavaScript as described in 'JavaScript Allongé', focusing on its function-scoped nature and differences from 'let' and 'const'.

## Key supported claims

- JavaScript has one more way to bind a name to a value, var . (raw/javascriptallonge.pdf p.151-154)
- var looks a lot like let (raw/javascriptallonge.pdf p.151-154)
- var is not block scoped, it's function scoped, just like function declarations (raw/javascriptallonge.pdf p.151-154)

## Technical details

### `technical-atom-73f73a426d5e0d66` code

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { let x = n; if (x === 1) { return 1; } else { --x; return n * factorial(x); } } factorial(5) //=> 120 const factorial2 = (n) => { var x = n; if (x === 1) { return 1; } else { --x;
```

### `technical-atom-6a3206c3563396f5` code

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
return n * factorial2(x); } } factorial2(5) //=> 120
```

### `technical-atom-a08ce7e68f68e54e` code

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
(() => { var age = 49; if ( true ) { var age = 50; } return age; })() //=> 50
```

### `technical-atom-e58ba5c4019242ca` code

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> 24
```

### `technical-atom-9598b23ff904732b` code

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { let innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } return innerFactorial(n, 1); } JavaScript hoists the let and the assignment. But not so with var : const factorial = (n) => { return innerFactorial(n, 1); var innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### `technical-atom-0dfea89b52f9475e` code

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { let innerFactorial = undefined ; return innerFactorial(n, 1); innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### `technical-atom-80d6a8f6590009b0` code

Citation: (raw/javascriptallonge.pdf p.151-154)

```
const and let bind names.
```

### `technical-atom-7406906fd94872f7` procedure

Citation: (raw/javascriptallonge.pdf p.151-154)

First, var is not block scoped, it's function scoped, just like function declarations:
