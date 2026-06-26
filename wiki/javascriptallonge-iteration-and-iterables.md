---
page_id: javascriptallonge-iteration-and-iterables
page_kind: source
summary: Iteration and Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.206-223
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses iteration and iterables in JavaScript, covering functional iterators, iterator objects, and the Symbol.iterator method. It explains how to create iterable collections and use constructs like for...of loops and the spread operator with iterables.

## Key supported claims

- JavaScript allows iterating over collection contents one by one, termed _iterating over the contents_ (raw/javascriptallonge.pdf p.206-223).
- Functional iterators can be implemented for objects, such as stacks, with methods like .iterator() (raw/javascriptallonge.pdf p.206-223).
- Iterables represent ordered collections, where each iteration returns elements in a consistent order (raw/javascriptallonge.pdf p.206-223).
- JavaScript introduced a standard way to write iterators using the Symbol.iterator method to avoid conflicts with existing code (raw/javascriptallonge.pdf p.206-223).
- The for...of loop works with any iterable object, enabling easy iteration over collections (raw/javascriptallonge.pdf p.206-223).

## Technical details

### `technical-atom-0306491be0fe1015` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false, value: this .array[iterationIndex--]} } } } }); const stack = Stack1(); stack.push("Greetings"); stack.push("to"); stack.push("you!")
```

### `technical-atom-5c9d5f0787955223` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
const iter = stack.iterator(); iter().value //=> "you!" iter().value //=> "to"
```

### `technical-atom-be126e6eb38ca51a` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?
```

### `technical-atom-d3b675be6d62eed9` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.
```

### `technical-atom-cbbd2a5302d282e1` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
const iteratorSum = (iterator) => { let eachIteration, sum = 0;
```

### `technical-atom-2394ac3255b88742` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```
while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum }
```

### `technical-atom-dd890e80a0706c73` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
const stack = Stack1();
```

### `technical-atom-5571923c135d26db` code

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
const collectionSum = (collection) => { const iterator = collection.iterator();
```

## Related technical details

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-8d6f83afe6ff7090` code

Relation: nearby source page; matched terms `code`, `collections`, `function`, `iterable`, `iteration`, `iterator`

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false, [Symbol.iterator]: function () { let currentPair = this; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false, value} } } } } }, LazyCollection); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next();
```

### From [[javascriptallonge-generating-iterables]]: `technical-atom-8939346e4f8483e2` code

Relation: nearby source page; matched terms `code`, `iterable`, `iterables`, `iteration`, `iterator`, `iterators`

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
// Iteration const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]()]; return () => { while (!!iterators[0]) { const iterationResult = iterators[0].next(); if (iterationResult.done) { iterators.shift(); } else if (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } else { return iterationResult.value; } } return; } } const i = treeIterator([1, [2, [3, 4], 5]]); let n; while (n = i()) { console.log(n) } //=> 1 2 3 4 5
```

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-a52c46f037bbeeb7` code

Relation: nearby source page; matched terms `code`, `collections`, `function`, `iterator`, `key`, `object`

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined: fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-32ba891739150b9e` code

Relation: nearby source page; matched terms `code`, `collections`, `iterable`, `iteration`, `iterator`, `symbol`

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
return done ? EMPTY: Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]());
```
