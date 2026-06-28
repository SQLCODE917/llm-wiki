---
page_id: javascriptallonge-array
page_kind: concept
summary: Array: 16 statement(s) and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-array@77ec94a4eba078dd347cb42db86b7a61
---

# Array

What [[javascriptallonge]] covers about array:

## Statements

- Array literals are expressions, and arrays are _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- Arrays are JavaScript’s “native” representation of lists. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-01209))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-83ecb080-01213))_
- While we have mentioned arrays briefly, we haven’t had a close look at them. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-01189))_
- We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. _(javascriptallonge.pdf (source-range-83ecb080-01192))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- As we can see, JavaScript Arrays are zero-based[56] . _(javascriptallonge.pdf (source-range-83ecb080-01212))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. _(javascriptallonge.pdf (source-range-83ecb080-01232))_
- Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. _(javascriptallonge.pdf (source-range-83ecb080-01252))_
- That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-01269))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01205))_

> [] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01206))_

> **const** array_of_one = () => [1];

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01207))_

> array_of_one() === array_of_one() _//=> false_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01209))_

> Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01210))_

> **const** oneTwoThree = ["one", "two", "three"];

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01209))_

> Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01211))_

> oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01221))_

> There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01222))_

> **const** wrap = (something) => [something];

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01232))_

> The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01235))_

> **const** surname = (name) => { **const** [first, last] = name; **return** last; }

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01242))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01243))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01242))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01244))_

> car _//=> 1_ cdr _//=> [2, 3, 4, 5]_

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01269))_

> That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01271))_

> what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01272, source-range-83ecb080-01274))_

> And if there aren’t any items to assign with ..., JavaScript assigns an empty array: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01273))_

> **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01285))_

> It is very much like an array literal. And consider how we bind values to parameter names:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01286))_

> **const** foo = () => ... **const** bar = (name) => ... **const** baz = (a, b, c) => ...


## Related pages

- [[javascriptallonge-literal]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (1 shared atom(s))

## Source

- [[javascriptallonge]]
