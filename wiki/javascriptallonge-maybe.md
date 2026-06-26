---
page_id: javascriptallonge-maybe
page_kind: source
summary: Maybe from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.86-87
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the Maybe pattern and a function decorator for handling null or undefined values in JavaScript, borrowing ideas from Haskell's Maybe monad, Ruby's andand, and CoffeeScript's existential method invocation.

## Key supported claims

- The Maybe pattern checks for null or undefined values in JavaScript, as per raw/javascriptallonge.pdf p.86-87.
- The Maybe pattern is inspired by Haskell's Maybe monad, Ruby's andand, and CoffeeScript's existential method invocation, per raw/javascriptallonge.pdf p.86-87.
- The maybe decorator reduces the logic of checking for nothing to a function call, as noted in raw/javascriptallonge.pdf p.86-87.

## Technical details

### `technical-atom-1bd590dcf147fd4a` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
const isSomething = (value) => value !== null && value !== void 0;
```

### `technical-atom-bd52e6052086d753` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
const checksForSomething = (value) => { if (isSomething(value)) {
```

### `technical-atom-ff114878203bea62` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```
var something = isSomething(value) ? doesntCheckForSomething(value): value;
```

### `technical-atom-0354ebfb80359cec` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for ( let arg of args) { if (arg == null) return; }
```

### `technical-atom-e937c2bf2a6905cf` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```
return fn.apply( this, args) } }
```

### `technical-atom-a86e1001edea1d1d` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
function Model () {};
```

### `technical-atom-937bc370ec3a1ac2` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
Model.prototype.setSomething = maybe( function (value) { this .something = value; });
```

### `technical-atom-030be2e52dfd42a0` code

Citation: (raw/javascriptallonge.pdf p.86-87)

```
var something = isSomething(value) ?
```

## Related technical details

### From [[javascriptallonge-picking-the-bean-choice-and-truthiness]]: `technical-atom-69f71aab863b5fa0` code

Relation: nearby source page; matched terms `function`, `null`, `there`, `undefined`

Citation: (raw/javascriptallonge.pdf p.94-99)

```javascript
is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user.
```

### From [[javascriptallonge-unary]]: `technical-atom-2fb846e09e5cacfd` procedure

Relation: nearby source page; matched terms `decorator`, `function`

Citation: (raw/javascriptallonge.pdf p.82-83)

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

### From [[javascriptallonge-once]]: `technical-atom-b120a4f7a43e70cd` code

Relation: nearby source page; matched terms `call`, `function`, `undefined`, `very`

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:
```

### From [[javascriptallonge-once]]: `technical-atom-a8a5e302dccccc11` code

Relation: nearby source page; matched terms `call`, `function`, `undefined`

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
That function will call your function once, and thereafter will return undefined whenever it is called.
```
