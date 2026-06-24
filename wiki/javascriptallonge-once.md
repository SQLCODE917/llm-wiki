---
page_id: javascriptallonge-once
page_kind: source
summary: Once from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.88-88
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

The "Once" chapter from JavaScript Allongé introduces the once combinator, a function that ensures another function can only be called once.

## Key supported claims

- once is an extremely helpful combinator. (raw/javascriptallonge.pdf p.88-88)
- It ensures that a function can only be called, well, once. (raw/javascriptallonge.pdf p.88-88)
- That function will call your function once, and thereafter will return undefined whenever it is called. (raw/javascriptallonge.pdf p.88-88)
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. (raw/javascriptallonge.pdf p.88-88)

## Technical details

### `technical-atom-86c133660af7308d` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const once = (fn) => { let done = false ; return function () { return done ? void 0 : ((done = true ), fn.apply( this , arguments)) } }
```

### `technical-atom-94efa685814f6560` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() //=> 'sure, why not?' askedOnBlindDate() //=> undefined askedOnBlindDate() //=> undefined
```

### `technical-atom-f74baf81c6759358` exception

Citation: (raw/javascriptallonge.pdf p.88)

It ensures that a function can only be called, well, once .

### `technical-atom-7b7d103b3baeda3d` exception

Citation: (raw/javascriptallonge.pdf p.88)

It seems some people will only try blind dating once.

## Related technical details

### From [[javascriptallonge-tap]]: `technical-atom-c8fa273077e85aaf` code

Relation: nearby source page; matched terms `can`, `function`, `return`, `undefined`

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const tap = (value, fn) => { const curried = (fn) => ( typeof (fn) === 'function' && fn(value), value ); return fn === undefined ? curried : curried(fn); } Now we can write: tap('espresso')((it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso' Or: tap('espresso', (it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso'
```

### From [[javascriptallonge-a-history-lesson]]: `technical-atom-d14e7ecdd4fc5321` code

Relation: nearby source page; matched terms `call`, `function`, `return`, `there`

Citation: (raw/javascriptallonge.pdf p.90-91)

```javascript
var __slice = Array.prototype.slice; function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]) : []); return fn.apply( this , args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```

### From [[javascriptallonge-left-variadic-functions]]: `technical-atom-9bf75248160dbe49` worked-example

Relation: nearby source page; matched terms `function`, `record`, `some`

Citation: (raw/javascriptallonge.pdf p.89-90)

For example, we might want to have a function that builds some kind of team record.

### From [[javascriptallonge-unary]]: `technical-atom-6630b376b8107ac2` code

Relation: nearby source page; matched terms `call`, `function`, `return`

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
const unary = (fn) => fn.length === 1 ? fn : function (something) { return fn.call( this , something) }
```
