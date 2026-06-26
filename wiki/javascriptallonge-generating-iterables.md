---
page_id: javascriptallonge-generating-iterables
page_kind: source
summary: Generating Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.224-245
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on generating iterables from JavaScript Allongé, covering iterators, generators, and their use in handling recursive data structures and state machines.

## Key supported claims

- Generators in JavaScript allow for simpler code when dealing with recursive iterations or state patterns, as they implicitly manage state (raw/javascriptallonge.pdf p.224-245).
- JavaScript generators are functions defined with function* syntax that use yield or yield* to generate values, making them useful for creating iterables (raw/javascriptallonge.pdf p.224-245).
- Generators can be used to implement state machines like the Fibonacci sequence more naturally than traditional iterators (raw/javascriptallonge.pdf p.224-245).

## Technical details

### `technical-atom-bca2e4bfd0841b6d` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
const Numbers = { [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false, value: n++}) } } };
```

### `technical-atom-40b9a355f1137cd2` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
let n = 0;
```

### `technical-atom-cc969d4501dec30a` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```
while ( true) { console.log(n++) }
```

### `technical-atom-0c8e59c8703e13ee` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
// Iteration let n = 0; () => ({done: false, value: n++}) // Generation let n = 0; while ( true) { console.log(n++) }
```

### `technical-atom-d2da521818613ea1` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
// Generation const isIterable = (something) => !!something[Symbol.iterator];
```

### `technical-atom-7ed179c7b89bbe8f` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
const generate = (iterable) => { for ( let element of iterable) { if (isIterable(element)) { generate(element) } else { console.log(element) } } } generate([1, [2, [3, 4], 5]]) //=> 1 2 3 4 5
```

### `technical-atom-8939346e4f8483e2` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
// Iteration const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]()]; return () => { while (!!iterators[0]) { const iterationResult = iterators[0].next(); if (iterationResult.done) { iterators.shift(); } else if (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } else { return iterationResult.value; } } return; } } const i = treeIterator([1, [2, [3, 4], 5]]); let n; while (n = i()) { console.log(n) } //=> 1 2 3 4 5
```

### `technical-atom-51de95e2ff208fe6` code

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
const fibonacci = () => { let a, b;
```

## Related technical details

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-be126e6eb38ca51a` code

Relation: nearby source page; matched terms `code`, `defined`, `function`, `iterables`, `iterator`, `javascript`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-4cea242ebaa5e4ee` code

Relation: nearby source page; matched terms `code`, `function`, `iterables`, `iterator`, `iterators`

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
function * zip (...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]());
```

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-d3b675be6d62eed9` code

Relation: nearby source page; matched terms `code`, `function`, `iterables`, `iterator`, `its`, `javascript`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.
```

### From [[javascriptallonge-interactive-generators]]: `technical-atom-f2826d58755cc716` code

Relation: nearby source page; matched terms `code`, `function`, `generators`, `like`, `state`, `when`

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
Our statelessNaughtsAndCrosses function pushes the work of tracking the game’s state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our “API” will work like this: When we want a new game, we’ll call a function that will return a game function, We’ll call the game function repeatedly, passing our moves, and get the opponent’s moves from it.
```
