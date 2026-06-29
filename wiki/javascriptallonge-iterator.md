---
page_id: javascriptallonge-iterator
page_kind: concept
summary: Iterator: 26 statement(s) and 27 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterator@43f6b2edf4fab1d60a9e34c02bb9c859
---

# Iterator

What [[javascriptallonge]] covers about iterator:

## Statements

### Yes. Consider this variation: / Functional Iterators / unfolding and laziness

- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-7239e085-01314))_

### Yes. Consider this variation: / Functional Iterators / caveat

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-7239e085-01324))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-7239e085-01548))_

### Like this:

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-7239e085-01552))_

### Like this: / iterables

- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-7239e085-01555))_

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-7239e085-01557))_

### Like this: / ordered collections

- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-7239e085-01584))_

- Right now, we're just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-7239e085-01585))_

### Like this: / operations on ordered collections

- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-7239e085-01590))_

### Like this: / summary

- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. Iterable ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-7239e085-01620))_

- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-7239e085-01621))_

### Like this: / Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-7239e085-01626))_

### Like this: / Generating Iterables / recursive iterators

- Iterators maintain state, that's what they do. Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something. _(javascriptallonge.pdf (source-range-7239e085-01637))_

### Like this: / Generating Iterables / state machines

- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_

### We'll keep it simple: / javascript's generators

- We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator . To write a generator, we write a function, but we make two changes: _(javascriptallonge.pdf (source-range-7239e085-01662))_

- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_

### We'll keep it simple: / generators are coroutines

- The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-7239e085-01681))_

- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-7239e085-01687))_

- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-7239e085-01692))_

- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-7239e085-01697))_

- Instead of thinking of there being on execution context, we can imagine that there are two execution contexts. With an iterator, we can call them the producer and the consumer . The iterator is the producer, and the code that iterates over it is the consumer. When the consumer calls .next() , it 'suspends' and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next() . _(javascriptallonge.pdf (source-range-7239e085-01702))_

### We'll keep it simple: / generators and iterables

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-7239e085-01714))_

### We'll keep it simple: / more generators

- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-7239e085-01725))_

### We'll keep it simple: / rewriting iterable operations

- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-7239e085-01756))_

### We'll keep it simple: / Summary

- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-7239e085-01759))_


## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

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

### Technical frame 2: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

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

### Technical frame 3: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01307))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01306))_

```
//=> 4
squares().value
//=> 9
```

### Technical frame 4: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

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

### Technical frame 5: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01312))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01310))_

```
const odds = () => {
```

### Technical frame 6: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

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

### Technical frame 7: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

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

### Technical frame 8: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01560))_

```
const Stack3 = () =>
({
array: [],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
[Symbol.iterator] () {
let iterationIndex = this.index;
return {
next () {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
}
});
const stack = Stack3();
```

### Technical frame 9: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01561))_

```
stack.push(2000);
stack.push(10);
stack.push(5)
const collectionSum = (collection) => {
const iterator = collection[Symbol.iterator]();
let eachIteration,
sum = 0;
while ((eachIteration = iterator.next(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 2015
Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing.
Do we get anything in return?
Indeed we do. Behold the for...of loop:
const iterableSum = (iterable) => {
let sum = 0;
for (const num of iterable) {
sum += num;
}
return sum
}
iterableSum(stack)
//=> 2015
```

### Technical frame 10: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01564))_

> As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01563))_

```
const EMPTY = {
isEmpty: () => true
};
const isEmpty = (node) => node === EMPTY;
const Pair1 = (first, rest = EMPTY) =>
({
first,
rest,
isEmpty () { return false },
[Symbol.iterator] () {
let currentPair = this;
return {
next () {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.first;
currentPair = currentPair.rest;
return {done: false, value}
}
}
}
}
});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: Pair1(first, list(...rest))
}
const someSquares = list(1, 4, 9, 16, 25);
iterableSum(someSquares)
//=> 55
```

### Technical frame 11: Like this: / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01584))_

> Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01583))_

```
const RandomNumbers = {
[Symbol.iterator]: () =>
({
next () {
return {value: Math.random()};
}
})
}
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.494052127469331
0.835459444206208
0.1408337657339871
...
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.7845381607767195
0.4956772483419627
0.20259276474826038
...
```

### Technical frame 12: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01590))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01589))_

```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 13: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01593))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01592))_

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

### Technical frame 14: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01596))_

> So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01594))_

```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```

### Technical frame 15: Like this: / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01630))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01627))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical frame 16: Like this: / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01630))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01628))_

```
const Numbers = {
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
};
```

### Technical frame 17: Like this: / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01635))_

> They're of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let's look at one:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01634))_

```
// Iteration
let n = 0;
() =>
({done: false, value: n++})
// Generation
let n = 0;
while (true) {
console.log(n++)
}
```

### Technical frame 18: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01643))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01642))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const treeIterator = (iterable) => {
const iterators = [ iterable[Symbol.iterator]() ];
return () => {
while (!!iterators[0]) {
const iterationResult = iterators[0].next();
if (iterationResult.done) {
iterators.shift();
}
else if (isIterable(iterationResult.value)) {
iterators.unshift(iterationResult.value[Symbol.iterator]());
}
else {
return iterationResult.value;
}
}
return;
}
}
const i = treeIterator([1, [2, [3, 4], 5]]);
let n;
while (n = i()) {
console.log(n)
}
//=>
1
2
3
4
5
```

### Technical frame 19: Like this: / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01653))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01651))_

```
// Generation
const fibonacci = () => {
let a, b;
console.log(a = 0);
console.log(b = 1);
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
```

### Technical frame 20: Like this: / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01653))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01652))_

```
55
89
144
...
```

### Technical frame 21: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01667))_

> When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01666))_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Technical frame 22: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01672))_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Technical frame 23: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01674))_

```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```

### Technical frame 24: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01709))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 25: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01710))_

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Technical frame 26: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01714))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01713))_

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```

### Technical frame 27: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01756))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01757))_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```


## Related pages

- [[javascriptallonge-functional-iterator]] - narrower topic: Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.; Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (5 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Functional Iterators / caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change.; Function shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (5 shared statement(s), 10 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated]; Object shares technical record from Like this: / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (5 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-symbol]] - shared statements and technical atoms: Symbol shares source evidence from Like this: / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Symbol shares technical record from Like this: / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from Like this:: Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterato ... [truncated]; Method shares technical record from Like this: / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from Like this: / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated]; Functional shares technical record from Like this: / Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from We'll keep it simple: / javascript's generators: Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:; Return shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from We'll keep it simple: / generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Iterable shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from Like this: / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Expression shares technical record from Like this: / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-instead]] - shared statements and technical atoms: Instead shares source evidence from We'll keep it simple: / Summary: A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object th ... [truncated]; Instead shares technical record from Like this: / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-purpose]] - shared statements and technical atoms: Purpose shares source evidence from Yes. Consider this variation: / Functional Iterators / caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change.; Purpose shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from Like this: / iterables: So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict wi ... [truncated]; Write shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms: Generator shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (3 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (3 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from Like this: / Generating Iterables / state machines: // Generation const fibonacci = () => { let a, b; console.log(a = 0); console.log(b = 1); while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms: Idea shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-needn]] - shared technical atoms: Needn shares technical record from Like this: / ordered collections: const RandomNumbers = { [Symbol.iterator]: () => ({ next () { return {value: Math.random()}; } }) } for (const i of RandomNumbers) { console.log(i) } //=> 0.49405212 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from We'll keep it simple: / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-version]] - shared technical atoms: Version shares technical record from Like this: / Generating Iterables / recursive iterators: const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]() ]; return () => ... [truncated] (1 shared atom(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from We'll keep it simple: / more generators: We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of s ... [truncated] (2 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Like this: / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Like this: / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from Like this: / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
