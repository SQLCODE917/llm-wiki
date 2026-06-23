---
page_id: javascriptallonge-generators-and-iterables
page_kind: source
summary: generators and iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.234-236
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on generators and iterables from JavaScript Allongé.

## Key supported claims

- A generator function yields values instead of returning a single value (raw/javascriptallonge.pdf p.234-236).
- Calling a generator function multiple times produces new iterators (raw/javascriptallonge.pdf p.234-236).
- Objects can be made iterable using generator methods (raw/javascriptallonge.pdf p.234-236).
- JavaScript provides concise syntax for generator methods (raw/javascriptallonge.pdf p.234-236).
- The for...of loop and spread syntax work with iterables (raw/javascriptallonge.pdf p.234-236).

## Technical details

### `technical-atom-7b3c1fbdae533bb1` code

Citation: (raw/javascriptallonge.pdf p.234-236)

```javascript
const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumbers] //=> [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### `technical-atom-4576c5afd85b40d4` code

Citation: (raw/javascriptallonge.pdf p.234-236)

```javascript
const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }
```

### `technical-atom-1384299a1f559507` procedure

Citation: (raw/javascriptallonge.pdf p.234-236)

We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.
