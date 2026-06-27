---
page_id: javascriptallonge-section-arrays-and-destructuring-arguments-38eaf28a
page_kind: source
summary: Arrays and Destructuring Arguments: 71 source-backed entries and 31 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-arrays-and-destructuring-arguments-38eaf28a@053426f9b5c2ff9630c1e0ff34ec5b30
---

# Arrays and Destructuring Arguments

From [[javascriptallonge]].

## Statements

- Arrays are JavaScript’s “native” representation of lists. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- While we have mentioned arrays briefly, we haven’t had a close look at them. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-01189))_
- We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. _(javascriptallonge.pdf (source-range-83ecb080-01192))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- Array literals are expressions, and arrays are _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-01209))_
- As we can see, JavaScript Arrays are zero-based[56] . _(javascriptallonge.pdf (source-range-83ecb080-01212))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-83ecb080-01213))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- The line const wrapped = [something]; is interesting. _(javascriptallonge.pdf (source-range-83ecb080-01227))_
- In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-83ecb080-01228))_
- The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. _(javascriptallonge.pdf (source-range-83ecb080-01232))_
- We could do the same thing with (name) => name[1], but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-83ecb080-01237))_
- Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- car and cdr[57] are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. _(javascriptallonge.pdf (source-range-83ecb080-01245))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-83ecb080-01246))_
- Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. _(javascriptallonge.pdf (source-range-83ecb080-01252))_
- to place the elements of an array inside another array. _(javascriptallonge.pdf (source-range-83ecb080-01262))_
- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-83ecb080-01264))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-01287))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-01287))_
- 59Gathering in parameters has a long history, and the usual terms are to call gathering “pattern matching” and to call a name that is bound to gathered values a “rest parameter.” The term “rest” is perfectly compatible with gather: “Rest” is the noun, and “gather” is the verb. _(javascriptallonge.pdf (source-range-83ecb080-01292))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01194))_

> Any expression will work:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01195))_

> [ 2, 3, 2 + 2 ] _//=> [2,3,4]_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01199))_

> Any expression will do, including names:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01202))_

> **const** wrap = (something) => [something];

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01203))_

> wrap("lunch") _//=> ["lunch"]_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01205))_

> [] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01206))_

> **const** array_of_one = () => [1];

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01207))_

> array_of_one() === array_of_one() _//=> false_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01209))_

> Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01210))_

> **const** oneTwoThree = ["one", "two", "three"];

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01209))_

> Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01211))_

> oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01217))_

> **const** x = [], a = [x];

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01218))_

> a[0] === x

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01221))_

> There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01222))_

> **const** wrap = (something) => [something];

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01223))_

> Let’s expand it to use a block and an extra name:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01224))_

> **const** wrap = (something) => { **const** wrapped = [something];

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01223))_

> Let’s expand it to use a block and an extra name:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01226))_

> wrap("package") _//=> ["package"]_

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01228))_

> In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01229))_

> **const** unwrap = (wrapped) => { **const** [something] = wrapped;

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01228))_

> In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01231))_

> unwrap(["present"]) _//=> "present"_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01232))_

> The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01235))_

> **const** surname = (name) => { **const** [first, last] = name; **return** last; }

### Technical atom 17

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01236))_

> surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01238))_

> Destructuring can nest:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01239))_

> **const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation;

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01242))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01243))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01242))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01244))_

> car _//=> 1_ cdr _//=> [2, 3, 4, 5]_

### Technical atom 21

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01251))_

> **const** [...butLast, last] = [1, 2, 3, 4, 5]; _//=> ERROR_ **const** [first, ..., last] = [1, 2, 3, 4, 5]; _//=> ERROR_

### Technical atom 22

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01253))_

> **const** wrapped = [something];

### Technical atom 23

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01255))_

> **const** [unwrapped] = something;

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01256))_

> What is the reverse of gathering? We know that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01257))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];

### Technical atom 25

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01258))_

> What is the reverse? It would be:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01259))_

> **const** cons = [car, ...cdr];

### Technical atom 26

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01261))_

> **const** oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] _//=> ["zero","one","two","three"]_

### Technical atom 27

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01269))_

> That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01271))_

> what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_

### Technical atom 28

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01272, source-range-83ecb080-01274))_

> And if there aren’t any items to assign with ..., JavaScript assigns an empty array: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01273))_

> **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_

### Technical atom 29

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01280))_

> **const** [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]);

### Technical atom 30

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01281))_

> reg _//=> "Reginald is a programmer"_ status _//=> "ok"_

### Technical atom 31

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01285))_

> It is very much like an array literal. And consider how we bind values to parameter names:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01286))_

> **const** foo = () => ... **const** bar = (name) => ... **const** baz = (a, b, c) => ...
