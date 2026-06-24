---
page_id: javascriptallonge-why-const-and-let-were-invented
page_kind: source
summary: why const and let were invented from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.154-154
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the section 'why const and let were invented' from javascriptallonge.pdf

## Key supported claims

- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). (raw/javascriptallonge.pdf p.154-154)
- The other kids were adding the numbers like this: 1 + 2 + 3 + . (raw/javascriptallonge.pdf p.154-154)
- JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. (raw/javascriptallonge.pdf p.154-154)

## Technical details

### `technical-atom-cddb51c14221fbc7` code

Citation: (raw/javascriptallonge.pdf p.154)

```javascript
var sum = 0; for ( var i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050
```

### `technical-atom-41f22a8358713fe0` code

Citation: (raw/javascriptallonge.pdf p.154)

```
const and let are recent additions to JavaScript.
```

### `technical-atom-626cd93fa12868d4` formula

Citation: (raw/javascriptallonge.pdf p.154)

Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

### `technical-atom-8140ab99593fa9e9` formula

Citation: (raw/javascriptallonge.pdf p.154)

72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer.

## Related technical details

### From [[javascriptallonge-var]]: `technical-atom-7406906fd94872f7` procedure

Relation: nearby source page; matched terms `declarations`, `function`, `like`, `not`, `var`

Citation: (raw/javascriptallonge.pdf p.151-154)

First, var is not block scoped, it's function scoped, just like function declarations:

### From [[javascriptallonge-var]]: `technical-atom-80d6a8f6590009b0` code

Relation: nearby source page; matched terms `const`, `let`, `var`

Citation: (raw/javascriptallonge.pdf p.151-154)

```
const and let bind names.
```

### From [[javascriptallonge-var]]: `technical-atom-9598b23ff904732b` code

Relation: nearby source page; matched terms `const`, `function`, `javascript`, `let`, `not`, `var`

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { let innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } return innerFactorial(n, 1); } JavaScript hoists the let and the assignment. But not so with var : const factorial = (n) => { return innerFactorial(n, 1); var innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### From [[javascriptallonge-var]]: `technical-atom-0dfea89b52f9475e` code

Relation: nearby source page; matched terms `const`, `function`, `let`, `not`, `var`

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { let innerFactorial = undefined ; return innerFactorial(n, 1); innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```
