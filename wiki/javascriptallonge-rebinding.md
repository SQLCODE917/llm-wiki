---
page_id: javascriptallonge-rebinding
page_kind: source
summary: rebinding from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.60-61
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on rebinding in JavaScript Allongé, discussing how names bound with const cannot be rebound, but can be shadowed in new scopes.

## Key supported claims

- JavaScript permits rebinding new values to names bound with a parameter, as shown in the evenStevens example (raw/javascriptallonge.pdf p.60-61).
- The line n = n -2; rebinds a new value to the name n, demonstrating reassignment (raw/javascriptallonge.pdf p.60-61).
- JavaScript does not permit rebinding a name bound with const, although it can be shadowed in a new scope (raw/javascriptallonge.pdf p.60-61).
- Rebinding a const-bound name results in an error, as the name is read-only (raw/javascriptallonge.pdf p.60-61).

## Technical details

### `technical-atom-0d7fbb43c34ba804` code

Citation: (raw/javascriptallonge.pdf p.60-61)

```javascript
const evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { n = n - 2; return evenStevens(n); } } evenStevens(42) //=> true
```

### `technical-atom-b2d9b66c6b9cb49b` code

Citation: (raw/javascriptallonge.pdf p.60-61)

```javascript
evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { return evenStevens(n - 2); } } //=> ERROR, evenStevens is read-only
```

### `technical-atom-3a359314c7fff607` formula

Citation: (raw/javascriptallonge.pdf p.60-61)

The line n = n -2; rebinds a new value to the name n .

### `technical-atom-3ee28a0dd987831d` exception

Citation: (raw/javascriptallonge.pdf p.60-61)

JavaScript does not permit us to rebind a name that has been bound with const .

### `technical-atom-7c21d7d7a5e7d689` exception

Citation: (raw/javascriptallonge.pdf p.60-61)

We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

### `technical-atom-5be81a8c86a84134` worked-example

Citation: (raw/javascriptallonge.pdf p.60-61)

For example, we can write:

## Related technical details

### From [[javascriptallonge-naming-functions]]: `technical-atom-b521eb56bb5cda47` exception

Relation: nearby source page; matched terms `does`, `name`, `not`

Citation: (raw/javascriptallonge.pdf p.62)

This code does not name a function:

### From [[javascriptallonge-function-declaration-caveats-34]]: `technical-atom-f822e3366648ac82` worked-example

Relation: nearby source page; matched terms `although`, `example`, `javascript`, `permit`

Citation: (raw/javascriptallonge.pdf p.66-67)

Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:
