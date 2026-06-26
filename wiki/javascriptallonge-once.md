---
page_id: javascriptallonge-once
page_kind: source
summary: Once from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.88-88
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

The Once combinator ensures a function is called only once.

## Key supported claims

- The Once combinator ensures a function is called only once (raw/javascriptallonge.pdf p.88-88).
- The Once combinator is a function that returns another function (raw/javascriptallonge.pdf p.88-88).
- Once has some subtleties when used with methods (raw/javascriptallonge.pdf p.88-88).
- The function returned by Once will return undefined on subsequent calls (raw/javascriptallonge.pdf p.88-88).
- The Once combinator is an extremely helpful combinator (raw/javascriptallonge.pdf p.88-88).

## Technical details

### `technical-atom-c8a91a61773905e3` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const once = (fn) => { let done = false; return function () { return done ? void 0: ((done = true), fn.apply( this, arguments)) } }
```

### `technical-atom-b120a4f7a43e70cd` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:
```

### `technical-atom-c3bcd8bbcb0c5717` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const askedOnBlindDate = once( () => "sure, why not?"); askedOnBlindDate() //=> 'sure, why not?'
```

### `technical-atom-8842e5c905e0249b` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const once = (fn) => { let done = false; return function () { return done ?
```

### `technical-atom-a8a5e302dccccc11` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
That function will call your function once, and thereafter will return undefined whenever it is called.
```

### `technical-atom-d895d8e104807911` formula

Citation: (raw/javascriptallonge.pdf p.88)

**void** 0 : ((done = **true** ), fn.apply( **this** , arguments)) } }

### `technical-atom-511fc92e6cfb7a4e` exception

Citation: (raw/javascriptallonge.pdf p.88)

It ensures that a function can only be called, well, _once_ .

### `technical-atom-a6e0ec385c062260` exception

Citation: (raw/javascriptallonge.pdf p.88)

It seems some people will only try blind dating once.

## Related technical details

### From [[javascriptallonge-tap]]: `technical-atom-e82edd8fc9d318e3` code

Relation: nearby source page; matched terms `function`, `return`, `undefined`

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const tap = (value, fn) => { const curried = (fn) => ( typeof (fn) === 'function' && fn(value), value); return fn === undefined ? curried: curried(fn); }
```

### From [[javascriptallonge-left-variadic-functions]]: `technical-atom-a1826ad5eefcc067` code

Relation: nearby source page; matched terms `call`, `function`, `return`, `there`, `why`

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1): []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]): []); return fn.apply( this, args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```

### From [[javascriptallonge-picking-the-bean-choice-and-truthiness]]: `technical-atom-69f71aab863b5fa0` code

Relation: nearby source page; matched terms `function`, `return`, `there`, `undefined`

Citation: (raw/javascriptallonge.pdf p.94-99)

```javascript
is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user.
```

### From [[javascriptallonge-unary]]: `technical-atom-ec926fbbeb68e94d` code

Relation: nearby source page; matched terms `call`, `function`, `return`

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
? fn: function (something) { return fn.call( this, something) }
```
