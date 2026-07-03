---
page_id: javascriptallonge-recipe-unfolding-and-laziness
page_kind: recipe
page_family: recipe-pattern
summary: unfolding and laziness: reusable source-backed pattern with 7 statement(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: unfolding-and-laziness
projection_coverage: recipe-javascriptallonge-recipe-unfolding-and-laziness@67d56cd9a685245d6539f8471b0c0c3c
---

# unfolding and laziness

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-unfolding-and-laziness-bcf7ec6a]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- When they iterate over an array or linked list, they are traversing something that is already there. _(javascriptallonge.pdf (source-range-7239e085-01299))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-7239e085-01303))_
- This business of going on forever has some drawbacks. _(javascriptallonge.pdf (source-range-7239e085-01307))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_
- We'll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-7239e085-01309))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-7239e085-01312))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01300)_

```
const NumberIterator = (number = 0) =>
() => ({ done: false, value: number++ })
fromOne = NumberIterator(1);
fromOne().value;
//=> 1
fromOne().value;
//=> 2
fromOne().value;
//=> 3
fromOne().value;
//=> 4
fromOne().value;
//=> 5
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01302)_

```
const FibonacciIterator
= () => {
let previous = 0,
current = 1;
return () => {
const value = current;
[previous, current] = [current, current + previous];
return {done: false, value};
};
};
const fib = FibonacciIterator()
fib().value
//=> 1
fib().value
//=> 1
fib().value
//=> 2
fib().value
//=> 3
fib().value
//=> 5
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01305)_

```
const mapIteratorWith = (fn, iterator) =>
() => {
const {done, value} = iterator();
return ({done, value: done ? undefined : fn(value)});
}
const squares = mapIteratorWith((x) => x * x, NumberIterator(1));
squares().value
//=> 1
squares().value
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01306)_

```
//=> 4
squares().value
//=> 9
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01308)_

```
const take = (iterator, numberToTake) => {
let count = 0;
return () => {
if (++count <= numberToTake) {
return iterator();
} else {
return {done: true};
}
};
};
const toArray = (iterator) => {
let eachIteration,
array = [];
while ((eachIteration = iterator(), !eachIteration.done)) {
array.push(eachIteration.value);
}
return array;
}
toArray(take(FibonacciIterator(), 5))
//=> [1, 1, 2, 3, 5]
toArray(take(squares, 5))
//=> [1, 4, 9, 16, 25]
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01310)_

```
const odds = () => {
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-unfolding-and-laziness-bcf7ec6a]]
