---
page_id: javascriptallonge-iterator
page_kind: concept
summary: Iterator: 27 statement(s) and 19 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterator@57bd5b28d4720bfe0b61caf0fba938bc
---

# Iterator

What [[javascriptallonge]] covers about iterator:

## Statements

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-02025))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-83ecb080-02013))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _(javascriptallonge.pdf (source-range-83ecb080-02522))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02523))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- Iterators maintain state, that’s what they do. _(javascriptallonge.pdf (source-range-83ecb080-02547))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- The iterator is in a nascent or “newborn” state. _(javascriptallonge.pdf (source-range-83ecb080-02619))_
- The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02627))_
- The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02632))_
- The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02637))_
- With an iterator, we can call them the _producer_ and the _consumer_ . _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- The iterator is the producer, and the code that iterates over it is the consumer. _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- We’ve writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-83ecb080-02681))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-83ecb080-02726))_
- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. _(javascriptallonge.pdf (source-range-83ecb080-02731))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01988))_

> **const** NumberIterator = (number = 0) => () => ({ done: **false** , value: number++ })

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01989))_

> fromOne = NumberIterator(1);

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01990))_

> fromOne().value; _//=> 1_ fromOne().value; _//=> 2_ fromOne().value; _//=> 3_ fromOne().value; _//=> 4_ fromOne().value; _//=> 5_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02011))_

> **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02012))_

> toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02378))_

> And here’s a sum function implemented as a fold over a functional iterator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02379))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02378))_

> And here’s a sum function implemented as a fold over a functional iterator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02380))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02389))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02390))_

> **let** eachIteration, sum = 0;

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02391))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02475))_

> Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02476))_

> **const** Evens = mapWith((x) => 2 * x, Numbers);

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02531))_

> Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02532))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02604))_

> Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02605))_

> only("you").next() _//=>_ {"done": **false** , value: "you"} only("the lonely").next() _//=>_ {"done": **false** , value: "the lonely"}

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02606))_

> We can invoke the same iterator twice:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02607))_

> **const** sixteen = only("sixteen"); sixteen.next() _//=>_ {"done": **false** , value: "sixteen"} sixteen.next() _//=>_ {"done": **true** }

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02651))_

> Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02652))_

> If we call our generator function more than once, we get new iterators.

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02658))_

> Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02656))_

> **const** iterator = ThreeNumbers[Symbol.iterator]();

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02663))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02726))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02727))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value;

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02726))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02728))_

> **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator]();


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (6 shared statement(s), 14 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms (5 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
