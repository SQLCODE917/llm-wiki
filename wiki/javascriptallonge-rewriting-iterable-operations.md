---
page_id: javascriptallonge-rewriting-iterable-operations
page_kind: source
summary: rewriting iterable operations from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.243-245
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on rewriting iterable operations using generators in JavaScript Allongé.

## Key supported claims

- Generators simplify rewriting iterable operations like mapWith, filterWith, and untilWith. (raw/javascriptallonge.pdf p.243-245)
- The first function works directly with iterators, but rest can be rewritten using generators. (raw/javascriptallonge.pdf p.243-245)
- This approach simplifies implementation of iterable operations by leveraging generators. (raw/javascriptallonge.pdf p.243-245)

## Technical details

### `technical-atom-653bde3e9e9c4aff` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
const mapWith = (fn, iterable) => ({ [Symbol.iterator]: () => { const iterator = iterable[Symbol.iterator](); return { next: () => { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```

### `technical-atom-c172f364acc1fc24` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
function * mapWith (fn, iterable) { for ( const element of iterable) { yield fn(element); } }
```

### `technical-atom-03d1fc7cec3dda78` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } }
```

### `technical-atom-077d7b8cac2a0edc` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break ; yield fn(element); } }
```

### `technical-atom-0945972be4c692ed` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
const first = (iterable) => iterable[Symbol.iterator]().next().value; function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next(); yield * iterator; }
```

### `technical-atom-b7122d7c07937413` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```
No need to fool around with {done} or {value} , just yield values until we're done.
```

### `technical-atom-e5fe0bb1382fd951` procedure

Citation: (raw/javascriptallonge.pdf p.243-245)

No need to return an object with a .next() method.

## Related technical details

### From [[javascriptallonge-generators-and-iterables]]: `technical-atom-1384299a1f559507` procedure

Relation: nearby source page; matched terms `can`, `function`, `generators`, `iterables`, `javascript`, `next`

Citation: (raw/javascriptallonge.pdf p.234-236)

We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

### From [[javascriptallonge-implementing-methods-with-iteration]]: `technical-atom-97f38994d145c734` code

Relation: nearby source page; matched terms `function`, `key`, `next`, `object`, `return`

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined : fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```

### From [[javascriptallonge-implementing-methods-with-iteration]]: `technical-atom-5d2006f43ca209f1` code

Relation: nearby source page; matched terms `first`, `next`, `object`, `rest`, `return`

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
}, LazyCollection) }, until(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { let { done, value } = iterator.next(); done = done || fn(value); return ({ done, value: done ? undefined : value }); } } } }, LazyCollection) }, first() { return this [Symbol.iterator]().next().value; }, rest() { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); iterator.next(); return iterator; } }, LazyCollection); }, take(numberToTake) { return Object.assign({
```

### From [[javascriptallonge-implementing-methods-with-iteration]]: `technical-atom-e1ff59e78d47b263` code

Relation: nearby source page; matched terms `next`, `object`, `return`

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
}, filter(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { do { const { done, value } = iterator.next(); } while (!done && !fn(value)); return { done, value }; } } } }, LazyCollection) }, find(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { let { done, value } = iterator.next(); done = done || fn(value); return ({ done, value: done ? undefined : value }); } } }
```
