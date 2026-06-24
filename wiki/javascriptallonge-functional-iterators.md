---
page_id: javascriptallonge-functional-iterators
page_kind: source
summary: a look back at functional iterators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.206-209
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explores the concept of functional iterators and how to separate the mechanism of traversing data structures from the operations performed on them.

## Key supported claims

- The way we've written .iterator as a method, each object knows how to return an iterator for itself. (raw/javascriptallonge.pdf p.206-209)
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: (raw/javascriptallonge.pdf p.206-209)
- Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . (raw/javascriptallonge.pdf p.206-209)

## Technical details

### `technical-atom-5731dcf57cf98fde` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55
```

### `technical-atom-8d57bb8e6f72d728` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
const callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) //=> 55
```

### `technical-atom-139f64877680ce9c` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const foldArray = (array) => callRight(foldArrayWith, array); const sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldArray([1, 4, 9, 16, 25])) //=> 55
```

### `technical-atom-efc2fe8f63040ceb` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldTreeWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : Array.isArray(first) ? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); const foldTree = (tree) => callRight(foldTreeWith, tree); const sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldTree([1, [4, [9, 16]], 25])) //=> 55
```

### `technical-atom-35102b9ffb976d9e` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } }); const stack = Stack1(); stack.push("Greetings"); stack.push("to"); stack.push("you!")
```

### `technical-atom-9d0e44598ab0af32` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
const iter = stack.iterator(); iter().value //=> "you!" iter().value //=> "to"
```

### `technical-atom-66284ad4815503e0` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```

### `technical-atom-df7b31243eb10f16` code

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum }
```

## Related technical details

### From [[javascriptallonge-unfolding-and-laziness]]: `technical-atom-a58aa219307d4812` code

Relation: nearby source page; matched terms `iterator`, `return`, `value`

Citation: (raw/javascriptallonge.pdf p.172-175)

```javascript
const take = (iterator, numberToTake) => { let count = 0; return () => { if (++count <= numberToTake) { return iterator(); } else { return {done: true }; } }; }; const toArray = (iterator) => { let eachIteration, array = []; while ((eachIteration = iterator(), !eachIteration.done)) { array.push(eachIteration.value); } return array; } toArray(take(FibonacciIterator(), 5)) //=> [1, 1, 2, 3, 5] toArray(take(squares, 5)) //=> [1, 4, 9, 16, 25]
```

### From [[javascriptallonge-iterating]]: `technical-atom-16b403e6c3a4e278` code

Relation: nearby source page; matched terms `function`, `iterator`, `return`, `separate`, `value`

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
const arraySum = (array) => { let iter, sum = 0, index = 0; while ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : undefined }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } return sum; } arraySum([1, 4, 9, 16, 25]) //=> 55 With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value . Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ? undefined : array[i++] } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) {
```

### From [[javascriptallonge-iterating]]: `technical-atom-820beff3f61f6705` code

Relation: nearby source page; matched terms `function`, `return`, `separate`, `value`

Citation: (raw/javascriptallonge.pdf p.169-172)

```
Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ?
```

### From [[javascriptallonge-iterating]]: `technical-atom-fb1410295f080372` code

Relation: nearby source page; matched terms `iterator`, `return`, `value`

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
return { done, value: first } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0;; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum } const aListIterator = listIterator(list(1, 4, 9, 16, 25)); iteratorSum(aListIterator) //=> 55
```
