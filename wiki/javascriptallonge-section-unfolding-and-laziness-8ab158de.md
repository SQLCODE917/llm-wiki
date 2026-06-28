---
page_id: javascriptallonge-section-unfolding-and-laziness-8ab158de
page_kind: source
summary: unfolding and laziness: 17 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-unfolding-and-laziness-8ab158de@e49e8e69b970cb675ee8fa4f5c2b7426
---

# unfolding and laziness

From [[javascriptallonge]].

## Statements

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-31a4cf47-01299))_
- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-31a4cf47-01303))_
- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-31a4cf47-01307))_
- How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-31a4cf47-01309))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-31a4cf47-01312))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-31a4cf47-01314))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-31a4cf47-01303))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-31a4cf47-01307))_

## Technical atoms

### Technical frame 1: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01300))_

```
const NumberIterator = (number = 0) => () => ({ done: false , value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne().value; //=> 3 fromOne().value; //=> 4 fromOne().value; //=> 5
```

### Technical frame 2: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01302))_

```
const FibonacciIterator = () => { let previous = 0, current = 1; return () => { const value = current; [previous, current] = [current, current + previous]; return {done: false , value}; }; }; const fib = FibonacciIterator() fib().value //=> 1 fib().value //=> 1 fib().value //=> 2 fib().value //=> 3 fib().value //=> 5
```

### Technical frame 3: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01307))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01305))_

```
const mapIteratorWith = (fn, iterator) => () => { const {done, value} = iterator(); return ({done, value: done ? undefined : fn(value)}); } const squares = mapIteratorWith((x) => x * x, NumberIterator(1)); squares().value //=> 1 squares().value
```

### Technical frame 4: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01307))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01306))_

```
//=> 4 squares().value //=> 9
```

### Technical frame 5: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01309))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01308))_

```
const take = (iterator, numberToTake) => { let count = 0; return () => { if (++count <= numberToTake) { return iterator(); } else { return {done: true }; } }; }; const toArray = (iterator) => { let eachIteration, array = []; while ((eachIteration = iterator(), !eachIteration.done)) { array.push(eachIteration.value); } return array; } toArray(take(FibonacciIterator(), 5)) //=> [1, 1, 2, 3, 5] toArray(take(squares, 5)) //=> [1, 4, 9, 16, 25]
```

### Technical frame 6: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01312))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01310))_

```
const odds = () => {
```

### Technical frame 7: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01312))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01311))_

```
let number = 1; return () => { const value = number; number += 2; return {done: false , value}; } } const squareOf = callLeft(mapIteratorWith, (x) => x * x) toArray(take(squareOf(odds()), 5)) //=> [1, 9, 25, 49, 81]
```

### Technical frame 8: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01314))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01313))_

```
const filterIteratorWith = (fn, iterator) => () => { do { const {done, value} = iterator(); } while (!done && !fn(value)); return {done, value}; } const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1); toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) //=> [1, 9, 25, 49, 81]
```
