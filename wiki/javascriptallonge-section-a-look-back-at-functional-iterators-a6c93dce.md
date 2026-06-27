---
page_id: javascriptallonge-section-a-look-back-at-functional-iterators-a6c93dce
page_kind: source
summary: **a look back at functional iterators**: 17 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-look-back-at-functional-iterators-a6c93dce@005fada0fcfbc19c89e67a81db2e11a6
---

# **a look back at functional iterators**

From [[javascriptallonge]].

## Statements

- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-83ecb080-02367))_
- Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02375))_
- } function, and that’s where this is bound to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-83ecb080-02388))_
- If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_
- Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02373))_

> **const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02378))_

> And here’s a sum function implemented as a fold over a functional iterator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02379))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02378))_

> And here’s a sum function implemented as a fold over a functional iterator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02380))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02381))_

> We can use it with our stack:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02384))_

> **const** stack = Stack1();

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02389))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02390))_

> **let** eachIteration, sum = 0;

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02391))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02392))_

> collectionSum(stack) _//=> 6_
