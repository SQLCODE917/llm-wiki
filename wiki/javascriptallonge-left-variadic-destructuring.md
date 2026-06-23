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
