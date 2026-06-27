---
page_id: javascriptallonge-section-a-look-back-at-functional-iterators-a6c93dce
page_kind: source
summary: **a look back at functional iterators**: 17 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-look-back-at-functional-iterators-a6c93dce@d2034084039c2dd0f89c34ce8f08fac1
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

> **const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02373))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02379))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02380))_

> Context: We can use it with our stack:
_(context: javascriptallonge.pdf (source-range-83ecb080-02381))_

> **const** stack = Stack1();
_(source: javascriptallonge.pdf (source-range-83ecb080-02384))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();
_(source: javascriptallonge.pdf (source-range-83ecb080-02389))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02390))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02391))_

> collectionSum(stack) _//=> 6_
_(source: javascriptallonge.pdf (source-range-83ecb080-02392))_
