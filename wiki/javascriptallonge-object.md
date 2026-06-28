---
page_id: javascriptallonge-object
page_kind: concept
summary: Object: 17 statement(s) and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-object@4bdd38e680b489eb728549fd6e6c397a
---

# Object

What [[javascriptallonge]] covers about object:

## Statements

### Plain Old JavaScript Objects

- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-31a4cf47-01069))_

### Mutation

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-31a4cf47-01121))_

- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-31a4cf47-01138))_

### Iteration and Iterables

- Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-31a4cf47-01528))_

### iterator objects

- Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-31a4cf47-01546))_

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-31a4cf47-01547))_

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-31a4cf47-01548))_

### Like this:

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-31a4cf47-01552))_

### iterables

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-31a4cf47-01557))_

- The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable: _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

### Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-31a4cf47-01626))_

### generators and iterables

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

### Summary

- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-31a4cf47-01760))_

### Lazy and Eager Collections

- in the older style of object-oriented programming, we built 'fat' objects. Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-31a4cf47-01765))_

- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-31a4cf47-01768))_

### implementing methods with iteration

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-31a4cf47-01770))_

### lazy collection operations

- Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working with very large collections and many operations, this can be important. _(javascriptallonge.pdf (source-range-31a4cf47-01789))_


## Technical atoms

### Technical frame 1: Mutation

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01122))_

```
const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ]
```

### Technical frame 2: Mutation

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01126))_

```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name //=> { firstName: 'Leonard', # lastName: 'Braithwaite', # middleName: 'Austin' }
```

### Technical frame 3: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01560))_

```
const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, [Symbol.iterator] () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }); const stack = Stack3();
```

### Technical frame 4: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01561))_

```
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### Technical frame 5: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01564))_

> As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01563))_

```
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, [Symbol.iterator] () { let currentPair = this ; return { next () { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.first; currentPair = currentPair.rest; return {done: false , value} } } } } }); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : Pair1(first, list(...rest)) } const someSquares = list(1, 4, 9, 16, 25); iterableSum(someSquares) //=> 55
```

### Technical frame 6: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01630))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01627))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical frame 7: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01710))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 8: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01714))_

```
const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }
```

### Technical frame 9: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01778))_

```
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } }, LazyCollection); // Pair, a/k/a linked lists const EMPTY = { isEmpty: () => true
```

### Technical frame 10: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01779))_

```
}; const isEmpty = (node) => node === EMPTY; const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false , [Symbol.iterator]: function () { let currentPair = this ; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false , value} } } } } }, LazyCollection); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); // Stack const Stack = () => Object.assign({ array: [], index: -1, push: function (value) {
```

### Technical frame 11: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01780))_

```
return this .array[ this .index += 1] = value; }, pop: function () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty: function () { return this .index < 0 }, [Symbol.iterator]: function () { let iterationIndex = this .index; return { next: () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }, LazyCollection); Stack.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; }
```

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00614))_

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

<details>
<summary>Raw table text</summary>

```
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

</details>


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated]; Iterator shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (5 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-symbol]] - shared statements and technical atoms: Symbol shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Symbol shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from iterator objects: Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional i ... [truncated]; Function shares technical record from Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Method shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Plain Old JavaScript Objects: In JavaScript, an object is a map from string keys to values.; Javascript shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Mutation: In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall t ... [truncated]; Array shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Expression shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-instead]] - shared statements and technical atoms: Instead shares source evidence from Summary: A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object th ... [truncated]; Instead shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Iterable shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-directly]] - shared statements and technical atoms: Directly shares source evidence from iterables: The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterato ... [truncated]; Directly shares technical record from iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Functional shares technical record from Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms: Generator shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared technical atoms: the function keyword shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-recall]] - shared technical atoms: Recall shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms: Type shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared atom(s))
- [[javascriptallonge-collection]] - shared statements: Collection shares source evidence from iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (2 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated] (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements: Program shares source evidence from iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (1 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from Summary: A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object th ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
