---
page_id: javascriptallonge-section-array-literals-c27f7954
page_kind: source
summary: **array literals**: 13 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-array-literals-c27f7954@ece8b2fadb9ef1e56c216eeaaff1a651
---

# **array literals**

From [[javascriptallonge]].

## Statements

- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-01189))_
- We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. _(javascriptallonge.pdf (source-range-83ecb080-01192))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- Array literals are expressions, and arrays are _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-01204))_

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
