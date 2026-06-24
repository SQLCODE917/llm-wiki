---
page_id: javascriptallonge-implementing-methods-with-iteration
page_kind: source
summary: implementing methods with iteration from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.246-253
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on implementing methods with iteration in JavaScript Allongé.

## Key supported claims

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding (raw/javascriptallonge.pdf p.246-253).
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack (raw/javascriptallonge.pdf p.246-253).
- And if we want to create convenience methods, we can reuse common pieces (raw/javascriptallonge.pdf p.246-253).

## Technical details

### `technical-atom-97f38994d145c734` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined : fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```

### `technical-atom-e1ff59e78d47b263` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
}, filter(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { do { const { done, value } = iterator.next(); } while (!done && !fn(value)); return { done, value }; } } } }, LazyCollection) }, find(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { let { done, value } = iterator.next(); done = done || fn(value); return ({ done, value: done ? undefined : value }); } } }
```

### `technical-atom-5d2006f43ca209f1` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
}, LazyCollection) }, until(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { let { done, value } = iterator.next(); done = done || fn(value); return ({ done, value: done ? undefined : value }); } } } }, LazyCollection) }, first() { return this [Symbol.iterator]().next().value; }, rest() { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); iterator.next(); return iterator; } }, LazyCollection); }, take(numberToTake) { return Object.assign({
```

### `technical-atom-7d874efc589b7ad9` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
[Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); let remainingElements = numberToTake; return { next: () => { let { done, value } = iterator.next(); done = done || remainingElements-- <= 0; return ({ done, value: done ? undefined : value }); } } } }, LazyCollection); } }
```

### `technical-atom-c66bcf65c2866661` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } }, LazyCollection); // Pair, a/k/a linked lists const EMPTY = { isEmpty: () => true
```

### `technical-atom-fc389e60e8902924` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
}; const isEmpty = (node) => node === EMPTY; const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false , [Symbol.iterator]: function () { let currentPair = this ; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false , value} } } } } }, LazyCollection); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); // Stack const Stack = () => Object.assign({ array: [], index: -1, push: function (value) {
```

### `technical-atom-80a3ee280a8229ba` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
return this .array[ this .index += 1] = value; }, pop: function () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty: function () { return this .index < 0 }, [Symbol.iterator]: function () { let iterationIndex = this .index; return { next: () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }, LazyCollection); Stack.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; }
```

### `technical-atom-0432dbb698bbba10` code

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
// Pair and Stack in action Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() //=> 100 Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0)
```

## Related technical details

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-f3a0c8d86a0e5487` code

Relation: nearby source page; matched terms `collections`, `iterable`, `iteration`, `map`

Citation: (raw/javascriptallonge.pdf p.256-260)

```javascript
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false , [Symbol.iterator]: function () { let currentPair = this ; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false , value} } } } } }, EagerCollection(Pair)); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); Pair.from([1, 2, 3, 4, 5]).map(x => x * 2) //=>
```

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-d0ae077ae5d77a24` requirement

Relation: nearby source page; matched terms `collections`, `how`, `map`, `requirement`, `should`

Citation: (raw/javascriptallonge.pdf p.246)

This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail.

### From [[javascriptallonge-lazy-collection-operations]]: `technical-atom-0a45861b594c6c78` code

Relation: nearby source page; matched terms `filtering`, `map`, `stack`

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => { console.log(`squaring ${ x } `); return x * x }) .filter((x) => { console.log(`filtering ${ x } `); return x % 2 == 0 }) .first() //=> squaring 29 filtering 841 squaring 28 filtering 784 784
```

### From [[javascriptallonge-lazy-collection-operations]]: `technical-atom-744115e2e3a310d4` procedure

Relation: nearby source page; matched terms `iterable`, `javascript`, `stack`

Citation: (raw/javascriptallonge.pdf p.253-256)

Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer.
