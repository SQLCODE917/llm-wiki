---
page_id: javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b
page_kind: source
summary: Yes. Consider this variation: / Functional Iterators: 57 source-backed entries and 20 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b@c1e05d22a200764bb0b3402f69a57f31
---

# Yes. Consider this variation: / Functional Iterators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-yes-consider-this-variation-b8b28d41]] - broader source section: Yes. Consider this variation:
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-iterating-c8ddd51e]] - narrower source section: Yes. Consider this variation: / Functional Iterators / iterating
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-unfolding-and-laziness-bcf7ec6a]] - narrower source section: Yes. Consider this variation: / Functional Iterators / unfolding and laziness
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-bonus-6b4a06d7]] - narrower source section: Yes. Consider this variation: / Functional Iterators / bonus
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-caveat-c90295dd]] - narrower source section: Yes. Consider this variation: / Functional Iterators / caveat
- [[javascriptallonge-functional-iterator]] - topic hub: opens the topic page for Functional Iterator
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-4c177971]] - same source heading: another source section with the same heading, Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

## Statements

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-7239e085-01276))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-7239e085-01278))_
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-7239e085-01280))_
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-7239e085-01283))_
- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-7239e085-01276))_

## Statements by subsection

### Yes. Consider this variation: / Functional Iterators / iterating

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-7239e085-01285))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-7239e085-01286))_
- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-7239e085-01288))_
- Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient: _(javascriptallonge.pdf (source-range-7239e085-01291))_
- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-7239e085-01294))_
- We can write a different iterator for a different data structure. Here's one for linked lists: _(javascriptallonge.pdf (source-range-7239e085-01295))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-7239e085-01291))_

### Yes. Consider this variation: / Functional Iterators / unfolding and laziness

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-7239e085-01299))_
- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-7239e085-01303))_
- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_
- How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-7239e085-01309))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-7239e085-01312))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-7239e085-01314))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-7239e085-01303))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_

### Yes. Consider this variation: / Functional Iterators / bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-7239e085-01316))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-7239e085-01319))_
- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-7239e085-01321))_
- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-7239e085-01316))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-7239e085-01319))_

### Yes. Consider this variation: / Functional Iterators / caveat

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-7239e085-01323))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-7239e085-01324))_

## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01273))_

```
const arraySum = ([first, ...rest], accumulator = 0) =>
first === undefined
? accumulator
: arraySum(rest, first + accumulator)
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 2: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01275))_

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0);
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 3: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01280))_

> What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01279))_

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const foldArray = (array) => callRight(foldArrayWith, array);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldArray([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 4: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01283))_

> We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really).

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01282))_

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldTreeWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: Array.isArray(first)
? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\
e, rest))
: fn(first, foldTreeWith(fn, terminalValue, rest));
const foldTree = (tree) => callRight(foldTreeWith, tree);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldTree([1, [4, [9, 16]], 25]))
//=> 55
```

### Technical frame 5: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01288))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01287))_

```
const arraySum = (array) => {
let sum = 0;
for (let i = 0; i < array.length; ++i) {
sum += array[i];
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 6: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01291))_

> Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01290))_

```
const arraySum = (array) => {
let done,
sum = 0,
i = 0;
while ((done = i == array.length, !done)) {
const value = array[i++];
sum += value;
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 7: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01294))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01292))_

```
const arraySum = (array) => {
let iter,
sum = 0,
index = 0;
while (
(eachIteration = {
done: index === array.length,
value: index < array.length ? array[index] : undefined
},
++index,
!eachIteration.done)
) {
sum += eachIteration.value;
}
return sum;
}
arraySum([1, 4, 9, 16, 25])
//=> 55
With this code, we make a POJO that has done and value keys. All the summing code needs to know
is to add eachIteration.value. Now we can extract the ickiness into a separate function:
const arrayIterator = (array) => {
let i = 0;
return () => {
const done = i === array.length;
return {
done,
value: done ? undefined : array[i++]
}
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
```

### Technical frame 8: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01294))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01293))_

```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 9: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01295))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01296))_

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const print = (aPair) =>
isEmpty(aPair)
? ""
: `${aPair.first} ${print(aPair.rest)}`
const listIterator = (aPair) =>
() => {
const done = isEmpty(aPair);
if (done) {
return {done};
}
else {
const {first, rest} = aPair;
aPair = aPair.rest;
```

### Technical frame 10: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01295))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01297))_

```
return { done, value: first }
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
const aListIterator = listIterator(list(1, 4, 9, 16, 25));
iteratorSum(aListIterator)
//=> 55
```

### Technical frame 11: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01300))_

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

### Technical frame 12: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01302))_

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

### Technical frame 13: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01307))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01305))_

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

### Technical frame 14: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01307))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01306))_

```
//=> 4
squares().value
//=> 9
```

### Technical frame 15: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01309))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01308))_

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

### Technical frame 16: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01312))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01310))_

```
const odds = () => {
```

### Technical frame 17: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01312))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01311))_

```
let number = 1;
return () => {
const value = number;
number += 2;
return {done: false, value};
}
}
const squareOf = callLeft(mapIteratorWith, (x) => x * x)
toArray(take(squareOf(odds()), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 18: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01314))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01313))_

```
const filterIteratorWith = (fn, iterator) =>
() => {
do {
const {done, value} = iterator();
} while (!done && !fn(value));
return {done, value};
}
const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
toArray(take(squareOf(oddsOf(NumberIterator(1))), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 19: Yes. Consider this variation: / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01319))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01318))_

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 20: Yes. Consider this variation: / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01321))_

> JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01320))_

```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```
