---
page_id: javascriptallonge-a-history-lesson
page_kind: source
summary: a history lesson from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.90-91
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter.

## Key supported claims

- 53 Another history lesson. In 'Ye Olde Days,' JavaScript could not gather parameters. (raw/javascriptallonge.pdf p.90-91)
- A right-variadic function has one or more fixed arguments, and the rest are gathered into the rightmost argument. (raw/javascriptallonge.pdf p.90-91)
- In ECMAScript-5, a rightVariadic decorator was used to gather arguments into the last declared parameter. (raw/javascriptallonge.pdf p.90-91)

## Technical details

### `technical-atom-d14e7ecdd4fc5321` code

Citation: (raw/javascriptallonge.pdf p.90-91)

```javascript
var __slice = Array.prototype.slice; function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]) : []); return fn.apply( this , args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```

### `technical-atom-58b10bbb681d1f4a` code

Citation: (raw/javascriptallonge.pdf p.90-91)

```javascript
var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); We now simply write: const firstAndButFirst = (first, ...butFirst) [first, butFirst];
```

### `technical-atom-ad7485469ed4d3e0` code

Citation: (raw/javascriptallonge.pdf p.90-91)

```javascript
=>
```

### `technical-atom-9af87e0724794c97` formula

Citation: (raw/javascriptallonge.pdf p.90-91)

__slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ?
