---
page_id: javascriptallonge-array-literals
page_kind: source
summary: array literals from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.101-102
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript has a literal syntax for creating an array using square brackets. Arrays are reference types, and each array literal evaluates to a new, distinct array.

## Key supported claims

- JavaScript has a literal syntax for creating an array using [ and ] characters (raw/javascriptallonge.pdf p.101-102).
- Array literals are expressions that evaluate to new, distinct arrays, even with identical elements (raw/javascriptallonge.pdf p.101-102).
- JavaScript array literals support any expression, including nested arrays and function calls (raw/javascriptallonge.pdf p.101-102).
- Array literals can contain one or more elements, separated by commas (raw/javascriptallonge.pdf p.101-102).
- Empty arrays are created with empty brackets [] (raw/javascriptallonge.pdf p.101-102).

## Technical details

### `technical-atom-4f905dd3c0367011` code

Citation: (raw/javascriptallonge.pdf p.101-102)

```javascript
[] //=> []
```

### `technical-atom-ee53ff4052bf5910` code

Citation: (raw/javascriptallonge.pdf p.101-102)

```javascript
[1] //=> [1] [2, 3, 4] //=> [2,3,4]
```

### `technical-atom-6c5a48c00e70474f` code

Citation: (raw/javascriptallonge.pdf p.101-102)

```javascript
[ 2, 3, 2 + 2 ] //=> [2,3,4]
```

### `technical-atom-1eb3c4cf8f87fa79` code

Citation: (raw/javascriptallonge.pdf p.101-102)

```
[[[[[]]]]]
```

### `technical-atom-b4fe83baf08d80bb` code

Citation: (raw/javascriptallonge.pdf p.101-102)

```javascript
const wrap = (something) => [something]; wrap("lunch") //=> ["lunch"]
```

### `technical-atom-9f18ee82fdfbbf2b` code

Citation: (raw/javascriptallonge.pdf p.101-102)

```javascript
[] === [] //=> false [2 + 2] === [2 + 2] //=> false const array_of_one = () => [1]; array_of_one() === array_of_one() //=> false
```
