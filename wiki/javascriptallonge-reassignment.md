---
page_id: javascriptallonge-reassignment
page_kind: source
summary: Reassignment from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.148-157
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter from JavaScript Allongé discusses rebinding and reassignment in JavaScript, focusing on how different declaration keywords (`const`, `let`, `var`) handle variable bindings and scoping.

## Key supported claims

- JavaScript allows rebinding values to parameters, but not to names bound with const (raw/javascriptallonge.pdf p.148-157).
- const prevents rebinding of names, while let allows rebinding, both supporting block scoping (raw/javascriptallonge.pdf p.148-157).
- var is function-scoped, not block-scoped, and hoisted to the top of the function, unlike let and const (raw/javascriptallonge.pdf p.148-157).

## Technical details

### `technical-atom-0d930a8b7c62fbeb` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```javascript
const evenStevens = (n) => { if (n === 0) { return true; } else if (n == 1) { return false; } else { n = n - 2; return evenStevens(n); } } evenStevens(42) //=> true
```

### `technical-atom-a57123c4b3176540` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```javascript
evenStevens = (n) => { if (n === 0) { return true; } else if (n == 1) { return false; } else { return evenStevens(n - 2); } } //=> ERROR, evenStevens is read-only
```

### `technical-atom-69532e105fd4d8c7` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```javascript
let age = 52;
```

### `technical-atom-2d53626201b41db5` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```javascript
age = 53; age //=> 53
```

### `technical-atom-f00b8d7258128714` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```javascript
(() => { let age = 49; if ( true) { let age = 50; } return age; })() //=> 49
```

### `technical-atom-39f6f333444623f5` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```
{age: 49, '..': global-environment}
```

### `technical-atom-ef10a9701ccccacf` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```
{age: 50, '..': {age: 49, '..': global-environment}}
```

### `technical-atom-78d79112d6914d2a` code

Citation: (raw/javascriptallonge.pdf p.148-157)

```javascript
(() => { let age = 49; if ( true) { age = 50; } return age; })() //=> 50
```

## Related technical details

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-d6ba7e5f33c9f02b` code

Relation: nearby source page; matched terms `allong`, `const`, `javascript`

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### From [[javascriptallonge-garbage-garbage-everywhere]]: `technical-atom-4551df707589c382` exception

Relation: nearby source page; matched terms `does`, `not`

Citation: (raw/javascriptallonge.pdf p.126-131)

Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-0c6f56ffdca20542` code

Relation: nearby source page; matched terms `const`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
const K = (x) => (y) => x; const I = (x) => (x); const V = (x) => (y) => (z) => z(x)(y);
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-e872e51be415c3cc` code

Relation: nearby source page; matched terms `const`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
const K = (x) => (y) => x; const fortyTwo = K(42);
```
