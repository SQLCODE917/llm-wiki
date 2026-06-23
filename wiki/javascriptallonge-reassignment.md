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
