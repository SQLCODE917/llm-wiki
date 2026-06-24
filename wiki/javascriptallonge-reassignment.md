---
page_id: javascriptallonge-reassignment
page_kind: source
summary: Reassignment from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.148-150
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript allows re-assignment of values to parameters, but not to names bound with const. The let keyword provides a way to declare variables that can be reassigned.

## Key supported claims

- JavaScript does not permit us to rebind a name that has been bound with const. (raw/javascriptallonge.pdf p.148-150)
- JavaScript permits reassigning values to parameters. (raw/javascriptallonge.pdf p.148-150)
- The let keyword allows reassignment of variables. (raw/javascriptallonge.pdf p.148-150)

## Technical details

### `technical-atom-bb801bddb89971bc` code

Citation: (raw/javascriptallonge.pdf p.148-150)

```javascript
const evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { n = n - 2; return evenStevens(n); } } evenStevens(42) //=> true
```

### `technical-atom-e30a7169fb9c0891` code

Citation: (raw/javascriptallonge.pdf p.148-150)

```javascript
evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { return evenStevens(n - 2); } } //=> ERROR, evenStevens is read-only
```

### `technical-atom-4edee216c43a9f21` code

Citation: (raw/javascriptallonge.pdf p.148-150)

```javascript
let age = 52; age = 53; age //=> 53
```

### `technical-atom-77d790de2cbd266a` code

Citation: (raw/javascriptallonge.pdf p.148-150)

```javascript
(() => { let age = 49; if ( true ) { let age = 50; } return age; })() //=> 49
```

### `technical-atom-bd1be086eed15b29` code

Citation: (raw/javascriptallonge.pdf p.148-150)

```
{age: 49, '..': global-environment} To: {age: 50, '..': {age: 49, '..': global-environment}} Then back to:
```

### `technical-atom-b8cb6ee3932dde7a` code

Citation: (raw/javascriptallonge.pdf p.148-150)

```
{age: 49, '..': global-environment}
```

### `technical-atom-d49f5c4655f7a60d` code

Citation: (raw/javascriptallonge.pdf p.148-150)

```javascript
(() => { let age = 49; if ( true ) { age = 50; } return age; })() //=> 50
```

### `technical-atom-975d2292539f6339` worked-example

Citation: (raw/javascriptallonge.pdf p.148-150)

For example, we can write:

## Related technical details

### From [[javascriptallonge-var]]: `technical-atom-9598b23ff904732b` code

Relation: nearby source page; matched terms `but`, `const`, `javascript`, `let`, `not`

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { let innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } return innerFactorial(n, 1); } JavaScript hoists the let and the assignment. But not so with var : const factorial = (n) => { return innerFactorial(n, 1); var innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### From [[javascriptallonge-var]]: `technical-atom-80d6a8f6590009b0` code

Relation: nearby source page; matched terms `const`, `let`, `names`

Citation: (raw/javascriptallonge.pdf p.151-154)

```
const and let bind names.
```

### From [[javascriptallonge-why-const-and-let-were-invented]]: `technical-atom-41f22a8358713fe0` code

Relation: nearby source page; matched terms `const`, `javascript`, `let`

Citation: (raw/javascriptallonge.pdf p.154)

```
const and let are recent additions to JavaScript.
```

### From [[javascriptallonge-why-const-and-let-were-invented]]: `technical-atom-626cd93fa12868d4` formula

Relation: nearby source page; matched terms `but`, `can`, `const`, `let`, `way`

Citation: (raw/javascriptallonge.pdf p.154)

Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?
