---
page_id: javascriptallonge-object
page_kind: concept
summary: Object: 17 statement(s) and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-object@669c553ec142266056e59991b3825bc7
---

# Object

What [[javascriptallonge]] covers about object:

## Statements

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- When working with objects, we do things the object way. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- The for...of loop works directly with any object that is _iterable_ , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. _(javascriptallonge.pdf (source-range-83ecb080-02431))_
- in the older style of object-oriented programming, we built “fat” objects. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-83ecb080-01585))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-83ecb080-01711))_
- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-02396))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. _(javascriptallonge.pdf (source-range-83ecb080-02731))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-83ecb080-02783))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01592))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01593))_

> - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01594))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01595))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01598))_

> - x = unique(),

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01599))_

> - y = unique(),

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01636))_

> Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01637))_

> **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `;

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01688))_

> In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01689))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01694))_

> You can do the same thing with both syntaxes for accessing objects:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01695))_

> **const** name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name _//=> { firstName: 'Leonard',_ # lastName: 'Braithwaite', # middleName: 'Austin' }

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

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02531))_

> Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02532))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02651))_

> Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02652))_

> If we call our generator function more than once, we get new iterators.

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02663))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms (5 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-collection]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
