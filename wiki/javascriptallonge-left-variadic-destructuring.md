---
page_id: javascriptallonge-left-variadic-destructuring
page_kind: source
summary: left-variadic destructuring from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.92-93
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses left-variadic destructuring, a method for gathering array elements from the left side of an array, similar to how left-variadic functions gather parameters from the left.

## Key supported claims

- Left-variadic destructuring gathers array elements from the left side of an array, similar to how left-variadic functions gather parameters from the left (raw/javascriptallonge.pdf p.92-93).
- The leftGather utility function allows gathering excess arguments from the left side of an array (raw/javascriptallonge.pdf p.92-93).
- Unlike regular destructuring, left-variadic destructuring requires specifying the length of the result array (raw/javascriptallonge.pdf p.92-93).

## Technical details

### `technical-atom-96b05e6472863213` code

Citation: (raw/javascriptallonge.pdf p.92-93)

```javascript
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first //=> 'why' butFirst //=> ["hello","there","little","droid"]
```

### `technical-atom-de4e8e00d7867920` code

Citation: (raw/javascriptallonge.pdf p.92-93)

```javascript
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid']; //=> Unexpected token
```

### `technical-atom-84ee61afa60e92f3` code

Citation: (raw/javascriptallonge.pdf p.92-93)

```javascript
const [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']); butLast //=> ['why', 'hello', 'there', 'little'] last //=> 'droid'
```

### `technical-atom-4a5a829e19a8067b` code

Citation: (raw/javascriptallonge.pdf p.92-93)

```javascript
const leftGather = (outputArrayLength) => { return function (inputArray) { return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\ at( inputArray.slice(inputArray.length - outputArrayLength + 1) ) } }; const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\ ']); butLast //=> ['why', 'hello', 'there', 'little'] last //=> 'droid'
```

### `technical-atom-0d10744b5e6190a9` exception

Citation: (raw/javascriptallonge.pdf p.92-93)

But we can write our own left-gathering function utility using the same principles without all the tedium:

## Related technical details

### From [[javascriptallonge-overcoming-limitations]]: `technical-atom-da5e8aae05dc73cc` procedure

Relation: nearby source page; matched terms `arguments`, `function`, `functions`, `left-variadic`, `write`

Citation: (raw/javascriptallonge.pdf p.91-92)

But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function?

### From [[javascriptallonge-overcoming-limitations]]: `technical-atom-0cc478268532bafb` procedure

Relation: nearby source page; matched terms `function`, `gathers`, `left`, `our`, `parameters`

Citation: (raw/javascriptallonge.pdf p.91-92)

Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right.

### From [[javascriptallonge-a-history-lesson]]: `technical-atom-d14e7ecdd4fc5321` code

Relation: nearby source page; matched terms `arguments`, `array`, `function`, `length`

Citation: (raw/javascriptallonge.pdf p.90-91)

```javascript
var __slice = Array.prototype.slice; function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]) : []); return fn.apply( this , args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```

### From [[javascriptallonge-left-variadic-functions]]: `technical-atom-788752f4a1e82bb0` exception

Relation: nearby source page; matched terms `functions`, `gathering`, `left`, `parameters`, `variadic`

Citation: (raw/javascriptallonge.pdf p.89-90)

ECMAScript 2015 only permits gathering parameters from the end of the parameter list.
