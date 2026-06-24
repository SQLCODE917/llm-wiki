---
page_id: javascriptallonge-unfolding-and-laziness
page_kind: source
summary: unfolding and laziness from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.172-175
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on unfolding and laziness in JavaScript allonge.

## Key supported claims

- An unfold function starts with a seed and expands it into a data structure, being the opposite of a fold (raw/javascriptallonge.pdf p.172-175).
- A generic unfold mechanism can be written, but the focus is on what we can do with unfolded iterators (raw/javascriptallonge.pdf p.172-175).
- Iterators can be mapped and filtered, allowing composition of parts rather than complex code (raw/javascriptallonge.pdf p.172-175).

## Technical details

### `technical-atom-f6697799183d7874` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
const NumberIterator = (number = 0) => () => ({ done: false , value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne().value; //=> 3 fromOne().value; //=> 4 fromOne().value; //=> 5
```

### `technical-atom-75ae0924429e445f` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
const FibonacciIterator = () => { let previous = 0, current = 1; return () => { const value = current; [previous, current] = [current, current + previous]; return {done: false , value}; }; }; const fib = FibonacciIterator() fib().value //=> 1 fib().value //=> 1 fib().value //=> 2 fib().value //=> 3 fib().value //=> 5
```

### `technical-atom-94d21b6320210845` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
const mapIteratorWith = (fn, iterator) => () => { const {done, value} = iterator(); return ({done, value: done ? undefined : fn(value)}); } const squares = mapIteratorWith((x) => x * x, NumberIterator(1)); squares().value //=> 1 squares().value
```

### `technical-atom-47b1f6ecd26a5109` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
//=> 4 squares().value //=> 9
```

### `technical-atom-a58aa219307d4812` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
const take = (iterator, numberToTake) => { let count = 0; return () => { if (++count <= numberToTake) { return iterator(); } else { return {done: true }; } }; }; const toArray = (iterator) => { let eachIteration, array = []; while ((eachIteration = iterator(), !eachIteration.done)) { array.push(eachIteration.value); } return array; } toArray(take(FibonacciIterator(), 5)) //=> [1, 1, 2, 3, 5] toArray(take(squares, 5)) //=> [1, 4, 9, 16, 25]
```

### `technical-atom-7186051d1e3eccc6` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
const odds = () => {
```

### `technical-atom-7788fc12c59985b6` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
let number = 1; return () => { const value = number; number += 2; return {done: false , value}; } } const squareOf = callLeft(mapIteratorWith, (x) => x * x) toArray(take(squareOf(odds()), 5)) //=> [1, 9, 25, 49, 81]
```

### `technical-atom-73d00f77c3d7adb3` code

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
const filterIteratorWith = (fn, iterator) => () => { do { const {done, value} = iterator(); } while (!done && !fn(value)); return {done, value}; } const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1); toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) //=> [1, 9, 25, 49, 81]
```

## Related technical details

### From [[javascriptallonge-functional-iterators]]: `technical-atom-66284ad4815503e0` code

Relation: nearby source page; matched terms `but`, `code`, `function`, `iterators`, `javascript`, `returns`

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```

### From [[javascriptallonge-iterating]]: `technical-atom-16b403e6c3a4e278` code

Relation: nearby source page; matched terms `can`, `code`, `function`

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
const arraySum = (array) => { let iter, sum = 0, index = 0; while ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : undefined }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } return sum; } arraySum([1, 4, 9, 16, 25]) //=> 55 With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value . Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ? undefined : array[i++] } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) {
```

### From [[javascriptallonge-iterating]]: `technical-atom-820beff3f61f6705` code

Relation: nearby source page; matched terms `can`, `code`, `function`

Citation: (raw/javascriptallonge.pdf p.169-172)

```
Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ?
```

### From [[javascriptallonge-iterating]]: `technical-atom-e082dcf0169ed9ae` code

Relation: nearby source page; matched terms `code`, `function`, `returns`

Citation: (raw/javascriptallonge.pdf p.169-172)

```
The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .
```
