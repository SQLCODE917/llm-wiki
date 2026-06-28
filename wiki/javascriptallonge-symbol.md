---
page_id: javascriptallonge-symbol
page_kind: concept
summary: Symbol: 4 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-symbol@69227d939dc7902808dcbfcefed8fe4e
---

# Symbol

What [[javascriptallonge]] covers about symbol:

## Statements

### iterables

- To ensure that the method would not conflict with any existing code, JavaScript provides a symbol . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols. 88 _(javascriptallonge.pdf (source-range-31a4cf47-01556))_

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-31a4cf47-01557))_

### generators and iterables

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01715))_


## Technical atoms

### Technical frame 1: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01560))_

```
const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, [Symbol.iterator] () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }); const stack = Stack3();
```

### Technical frame 2: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01561))_

```
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### Technical frame 3: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01564))_

> As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01563))_

```
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, [Symbol.iterator] () { let currentPair = this ; return { next () { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.first; currentPair = currentPair.rest; return {done: false , value} } } } } }); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : Pair1(first, list(...rest)) } const someSquares = list(1, 4, 9, 16, 25); iterableSum(someSquares) //=> 55
```

### Technical frame 4: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01710))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 5: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01711))_

```
const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumbers] //=> [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### Technical frame 6: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01714))_

```
const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }
```


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Iterator shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Object shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Function shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Iterable shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Method shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Expression shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms: Generator shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (3 shared atom(s))
- [[javascriptallonge-instead]] - shared technical atoms: Instead shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared atom(s))
- [[javascriptallonge-directly]] - shared technical atoms: Directly shares technical record from iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-recall]] - shared technical atoms: Recall shares technical record from generators and iterables: const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumber ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))

## Source

- [[javascriptallonge]]
