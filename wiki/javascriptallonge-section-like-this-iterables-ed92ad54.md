---
page_id: javascriptallonge-section-like-this-iterables-ed92ad54
page_kind: source
summary: Like this: / iterables: 22 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-iterables-ed92ad54@16225f799185ac2b72500e981e6bd9b2
---

# Like this: / iterables

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-like-this-66cb3108]] - broader source section: Like this:
- [[javascriptallonge-iterable]] - topic hub: opens the topic page for Iterable

## Statements

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

## Technical atoms

### Technical frame 1: Like this: / iterables

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

### Technical frame 2: Like this: / iterables

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

### Technical frame 3: Like this: / iterables

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

### Technical frame 4: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01570))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01566))_

```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

### Technical frame 5: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01570))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01568))_

```
const firstAndSecondElement = (first, second) =>
({first, second})
firstAndSecondElement(...stack)
//=> {"first":5,"second":10}
```
