---
page_id: javascriptallonge-section-like-this-66cb3108
page_kind: source
summary: Like this:: 118 source-backed entries and 33 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-66cb3108@b686f5e0d4115ff56bf89badcb243e95
---

# Like this:

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-like-this-iterables-ed92ad54]] - narrower source section: Like this: / iterables
- [[javascriptallonge-section-like-this-iterables-out-to-infinity-7f1f5ba0]] - narrower source section: Like this: / iterables out to infinity
- [[javascriptallonge-section-like-this-ordered-collections-a2e8339c]] - narrower source section: Like this: / ordered collections
- [[javascriptallonge-section-like-this-operations-on-ordered-collections-286a5f1c]] - narrower source section: Like this: / operations on ordered collections
- [[javascriptallonge-section-like-this-from-28c3e8e3]] - narrower source section: Like this: / from
- [[javascriptallonge-section-like-this-summary-bc99b304]] - narrower source section: Like this: / summary
- [[javascriptallonge-section-like-this-generating-iterables-283d51ed]] - narrower source section: Like this: / Generating Iterables

## Statements

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-7239e085-01552))_

## Statements by subsection

### Like this: / iterables

- People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-7239e085-01554))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-7239e085-01555))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a symbol . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols. 88 _(javascriptallonge.pdf (source-range-7239e085-01556))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-7239e085-01557))_
- 88 You can read more about JavaScript symbols in Axel Rauschmayer's Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-7239e085-01558))_
- Our stack does, so instead of binding the existing iterator method to the name iterator , we bind it to the Symbol.iterator . We'll do that using the [ ] syntax for using an expression as an object literal key: _(javascriptallonge.pdf (source-range-7239e085-01559))_
- The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable: _(javascriptallonge.pdf (source-range-7239e085-01562))_
- As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-7239e085-01564))_
- Nowis the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal: _(javascriptallonge.pdf (source-range-7239e085-01565))_
- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-7239e085-01570))_
- And if we have an infinite collection, spreading is going to fail outright as we're about to see. _(javascriptallonge.pdf (source-range-7239e085-01571))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-7239e085-01570))_

### Like this: / iterables out to infinity

- There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them: _(javascriptallonge.pdf (source-range-7239e085-01575))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-7239e085-01577))_

### Like this: / ordered collections

- The iterables we're discussing represent ordered collections . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example: _(javascriptallonge.pdf (source-range-7239e085-01579))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-7239e085-01581))_
- Iterables needn't represent ordered collections. We could make an infinite iterable representing random numbers: _(javascriptallonge.pdf (source-range-7239e085-01582))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-7239e085-01584))_
- Right now, we're just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-7239e085-01585))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-7239e085-01584))_

### Like this: / operations on ordered collections

- Let's define some operations on ordered collections. Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 _(javascriptallonge.pdf (source-range-7239e085-01587))_
- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01588))_
- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-7239e085-01590))_
- Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith : _(javascriptallonge.pdf (source-range-7239e085-01591))_
- Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this: _(javascriptallonge.pdf (source-range-7239e085-01593))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation . _(javascriptallonge.pdf (source-range-7239e085-01596))_
- Like mapWith , they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-7239e085-01603))_
- Andhere's a computation performed using operations on ordered collections: We'll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-7239e085-01604))_
- As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning. _(javascriptallonge.pdf (source-range-7239e085-01606))_
- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-7239e085-01607))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-7239e085-01609))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-7239e085-01596))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-7239e085-01596))_

### Like this: / from

- Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-7239e085-01611))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one: _(javascriptallonge.pdf (source-range-7239e085-01612))_
- We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-7239e085-01614))_
- Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-7239e085-01617))_

### Like this: / summary

- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. Iterable ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-7239e085-01620))_
- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-7239e085-01621))_

### Like this: / Generating Iterables

- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. What is there they don't do well? _(javascriptallonge.pdf (source-range-7239e085-01625))_
- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-7239e085-01626))_
- Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-7239e085-01627))_
- Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-7239e085-01630))_
- Of course, when we have some code that makes a bunch of something, we don't usually write it like that. We usually just write something like: _(javascriptallonge.pdf (source-range-7239e085-01631))_
- And magically, the numbers would pour forth. We would generate numbers. Let's put that beside the code for the iterator, minus the iterable scaffolding: _(javascriptallonge.pdf (source-range-7239e085-01633))_
- They're of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let's look at one: _(javascriptallonge.pdf (source-range-7239e085-01635))_
- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. _(javascriptallonge.pdf (source-range-7239e085-01625))_

### Like this: / Generating Iterables / recursive iterators

- Iterators maintain state, that's what they do. Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something. _(javascriptallonge.pdf (source-range-7239e085-01637))_
- For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-7239e085-01638))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . _(javascriptallonge.pdf (source-range-7239e085-01643))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-7239e085-01644))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-7239e085-01644))_

### Like this: / Generating Iterables / state machines

- Some iterables can be modelled as state machines. Let's revisit the Fibonacci sequence. Again. One way to define it is: _(javascriptallonge.pdf (source-range-7239e085-01646))_
- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-7239e085-01647))_
- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-7239e085-01648))_
- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-7239e085-01649))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-7239e085-01653))_

## Technical atoms

### Technical frame 1: Like this:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01552))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01550))_

```
const Stack2 = () =>
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
iterator () {
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
```

### Technical frame 2: Like this:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01552))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01551))_

```
const stack = Stack2();
stack.push(2000);
stack.push(10);
stack.push(5)
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator.next(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 2015
```

### Technical frame 3: Like this: / iterables

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

### Technical frame 4: Like this: / iterables

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

### Technical frame 5: Like this: / iterables

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

### Technical frame 6: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01570))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01566))_

```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

### Technical frame 7: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01570))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01568))_

```
const firstAndSecondElement = (first, second) =>
({first, second})
firstAndSecondElement(...stack)
//=> {"first":5,"second":10}
```

### Technical frame 8: Like this: / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01575))_

> There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01574))_

```
const Numbers = {
[Symbol.iterator] () {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}
```

### Technical frame 9: Like this: / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01577))_

> Attempting to spread an infinite iterable into an array is always going to fail.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01576))_

```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```

### Technical frame 10: Like this: / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01581))_

> This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01580))_

```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
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

### Technical frame 15: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01598))_

```
const ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
5
1
9
...
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
3
```

### Technical frame 16: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01599))_

```
6
1
...
```

### Technical frame 17: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01600))_

> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines , but if RandomNumbers doesn't behave like an ordered collection, that's not mapWith 's fault.

### Technical frame 18: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01602))_

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
do {
const {done, value} = iterator.next();
} while (!done && !fn(value));
return {done, value};
}
}
}
});
const untilWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
let {done, value} = iterator.next();
done = done || fn(value);
return ({done, value: done ? undefined : value});
}
}
}
});
```

### Technical frame 19: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01606))_

> As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01605))_

```
const Squares = mapWith((x) => x * x, Numbers);
const EndWithOne = filterWith((x) => x % 10 === 1, Squares);
const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
```

### Technical frame 20: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01609))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01608))_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```

### Technical frame 21: Like this: / from

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01614))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01613))_

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 22: Like this: / from

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01617))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01616))_

```
Stack3.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
Pair1.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair1(value, iterationToList(iteration));
})(iterable[Symbol.iterator]())
```

### Technical frame 23: Like this: / from

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01617))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01618))_

```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```

### Technical frame 24: Like this: / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01625))_

> Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. What is there they don't do well?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01623))_

> [Figure] (p.224)

### Technical frame 25: Like this: / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01630))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01627))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical frame 26: Like this: / Generating Iterables

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

### Technical frame 27: Like this: / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01633))_

> And magically, the numbers would pour forth. We would generate numbers. Let's put that beside the code for the iterator, minus the iterable scaffolding:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01632))_

```
let n = 0;
while (true) {
console.log(n++)
}
```

### Technical frame 28: Like this: / Generating Iterables

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

### Technical frame 29: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01638))_

> For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01637))_

> One of those cases is when we have to recursively enumerate something.

### Technical frame 30: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01643))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01639))_

```
// Generation
const isIterable = (something) =>
!!something[Symbol.iterator];
const generate = (iterable) => {
for (let element of iterable) {
if (isIterable(element)) {
generate(element)
}
else {
console.log(element)
}
}
}
generate([1, [2, [3, 4], 5]])
//=>
1
2
3
4
5
```

### Technical frame 31: Like this: / Generating Iterables / recursive iterators

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

### Technical frame 32: Like this: / Generating Iterables / state machines

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

### Technical frame 33: Like this: / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01653))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01652))_

```
55
89
144
...
```
