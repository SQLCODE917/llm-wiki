---
page_id: javascriptallonge-maybe
page_kind: source
summary: Maybe from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.86-87
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the 'Maybe' pattern, a common approach in JavaScript for handling null or undefined values, and how it can be implemented using function decorators.

## Key supported claims

- The 'Maybe' pattern is a common solution for handling null or undefined values in JavaScript, as discussed in (raw/javascriptallonge.pdf p.86-87).
- A function using the 'Maybe' pattern checks for 'nothing' (null or undefined) and does nothing if the parameter is nothing, as described in (raw/javascriptallonge.pdf p.86-87).
- The 'Maybe' pattern can be implemented using a function decorator, borrowing concepts from Haskell's Maybe monad and Ruby's andand, as explained in (raw/javascriptallonge.pdf p.86-87).

## Technical details

### `technical-atom-157e959658e23810` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } }
```

### `technical-atom-34425860a3c743dc` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```
var something = isSomething(value) ? doesntCheckForSomething(value) : value;
```

### `technical-atom-65823b222c58213a` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for ( let arg of args) { if (arg == null ) return ; }
```

### `technical-atom-0a9ab21a902bd123` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```
return fn.apply( this , args) } }
```

### `technical-atom-c6d5d41b2b1c2236` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
maybe((a, b, c) => a + b + c)(1, 2, 3) //=> 6 maybe((a, b, c) => a + b + c)(1, null , 3) //=> undefined
```

### `technical-atom-e70b7b490931fb2a` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
function Model () {}; Model.prototype.setSomething = maybe( function (value) { this .something = value; });
```
