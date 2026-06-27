---
page_id: javascriptallonge-array-and-destructuring-argument
page_kind: concept
summary: Arrays and Destructuring Arguments: 31 statement(s) and 31 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-array-and-destructuring-argument@ae593963658382e13330af3389ed3354
---

# Arrays and Destructuring Arguments

What [[javascriptallonge]] covers about arrays and destructuring arguments:

## Statements

- Array literals are expressions, and arrays are _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-01209))_
- Arrays are JavaScript’s “native” representation of lists. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-83ecb080-01213))_
- car and cdr[57] are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. _(javascriptallonge.pdf (source-range-83ecb080-01245))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- While we have mentioned arrays briefly, we haven’t had a close look at them. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-01189))_
- We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. _(javascriptallonge.pdf (source-range-83ecb080-01192))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- As we can see, JavaScript Arrays are zero-based[56] . _(javascriptallonge.pdf (source-range-83ecb080-01212))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_

## Technical atoms

> Context: Any expression will work:
_(context: javascriptallonge.pdf (source-range-83ecb080-01194))_

> [ 2, 3, 2 + 2 ] _//=> [2,3,4]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01195))_

> Context: Any expression will do, including names:
_(context: javascriptallonge.pdf (source-range-83ecb080-01199))_

> **const** wrap = (something) => [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01202))_

> wrap("lunch") _//=> ["lunch"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01203))_

> Context: Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:
_(context: javascriptallonge.pdf (source-range-83ecb080-01204))_

> [] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01205))_

> Context: Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:
_(context: javascriptallonge.pdf (source-range-83ecb080-01204))_

> **const** array_of_one = () => [1];
_(source: javascriptallonge.pdf (source-range-83ecb080-01206))_

> Context: Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:
_(context: javascriptallonge.pdf (source-range-83ecb080-01204))_

> array_of_one() === array_of_one() _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01207))_


## Source

- [[javascriptallonge]]
