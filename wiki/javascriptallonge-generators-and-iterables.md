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

## Related technical details

### From [[javascriptallonge-generators-are-coroutines]]: `technical-atom-e1013b40c3bcd26c` procedure

Relation: nearby source page; matched terms `call`, `generator`, `generators`, `our`

Citation: (raw/javascriptallonge.pdf p.231-234)

- When we call interator.next() , the body of our generator begins to be evaluated.

### From [[javascriptallonge-generators-are-coroutines]]: `technical-atom-d1a307d6e07de4e9` procedure

Relation: nearby source page; matched terms `generator`, `generators`, `our`

Citation: (raw/javascriptallonge.pdf p.231-234)

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2; .

### From [[javascriptallonge-generators-are-coroutines]]: `technical-atom-66ba4e7ea1a0df88` procedure

Relation: nearby source page; matched terms `generator`, `generators`, `our`

Citation: (raw/javascriptallonge.pdf p.231-234)

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3; .

### From [[javascriptallonge-implementing-methods-with-iteration]]: `technical-atom-97f38994d145c734` code

Relation: nearby source page; matched terms `function`, `iterator`, `key`, `methods`, `object`, `value`

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined : fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```
