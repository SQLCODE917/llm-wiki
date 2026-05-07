---
title: Arrays
type: concept
tags: [data-types, es6-features, functional-programming, iterators, objects]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3137-L3140
  - js-allonge:normalized:L3147-L3151
  - js-allonge:normalized:L3169-L3170
  - js-allonge:normalized:L3194-L3195
  - js-allonge:normalized:L3194-L3196
  - js-allonge:normalized:L3212-L3216
  - js-allonge:normalized:L3222-L3226
  - js-allonge:normalized:L3254-L3258
  - js-allonge:normalized:L3277-L3282
  - js-allonge:normalized:L4067-L4069
  - js-allonge:normalized:L4565-L4567
  - js-allonge:normalized:L9311-L9315
---

# Arrays

## Summary

Arrays in JavaScript are ordered collections of values that can hold elements of any type. They are reference types, meaning each array literal creates a new object, and elements are stored by reference. Arrays support various operations including indexing, destructuring, and manipulation through methods like map and spread syntax.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Array literals in JavaScript produce new, distinct objects each time they are evaluated, regardless of their contents. | "Array literals are expressions, and arrays are reference types. We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:" | `normalized:L3137-L3140` | [Source](../sources/js-allonge.md) |
| Array elements can be accessed using bracket notation with numeric indices, and the values stored are references to the original objects rather than copies. | "Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0]" | `normalized:L3147-L3151` | [Source](../sources/js-allonge.md) |
| Array elements can be accessed using bracket notation with numeric indices, and the values stored are references to the original objects rather than copies. | "a[0] === x //=> true, arrays store references to the things you put in them." | `normalized:L3169-L3170` | [Source](../sources/js-allonge.md) |
| JavaScript supports array destructuring which allows extracting values from arrays into variables, including nested structures and rest patterns. | "const [something] = wrapped; destructures the array represented by wrapped, binding the value of its single element to the name something." | `normalized:L3194-L3195` | [Source](../sources/js-allonge.md) |
| JavaScript supports array destructuring which allows extracting values from arrays into variables, including nested structures and rest patterns. | "The statement const [something] = wrapped; destructures the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one..." | `normalized:L3194-L3196` | [Source](../sources/js-allonge.md) |
| JavaScript supports array destructuring which allows extracting values from arrays into variables, including nested structures and rest patterns. | "Destructuring can nest: const description = (nameAndOccupation) => { const [[first, last], occupation] = nameAndOccupation; return `${first} is a ${occupation}`; }" | `normalized:L3212-L3216` | [Source](../sources/js-allonge.md) |
| JavaScript supports array destructuring which allows extracting values from arrays into variables, including nested structures and rest patterns. | "const [car, ...cdr] = [1, 2, 3, 4, 5]; car //=> 1 cdr //=> [2, 3, 4, 5]" | `normalized:L3222-L3226` | [Source](../sources/js-allonge.md) |
| Arrays can be manipulated using the spread operator to combine elements, and destructuring can be combined with rest parameters to capture remaining elements. | "const cons = [car, ...cdr]; Let's try it: const oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] //=> ["zero","one","two","three"]" | `normalized:L3254-L3258` | [Source](../sources/js-allonge.md) |
| Arrays can be manipulated using the spread operator to combine elements, and destructuring can be combined with rest parameters to capture remaining elements. | "const [car, ...cdr] = [1, 2, 3, 4, 5]; car //=> 1 cdr //=> [2, 3, 4, 5]" | `normalized:L3222-L3226` | [Source](../sources/js-allonge.md) |
| Array elements can be assigned to specific indices, allowing modification of existing arrays, and accessing out-of-bounds indices returns undefined. | "oneTwoThree[3] = 'four'; oneTwoThree //=> [ 1, 2, 3, 'four' ]" | `normalized:L4565-L4567` | [Source](../sources/js-allonge.md) |
| Array elements can be assigned to specific indices, allowing modification of existing arrays, and accessing out-of-bounds indices returns undefined. | "const [what] = []; what //=> undefined const [which, what, who] = ["duck feet", "tiger tail"]; who //=> undefined" | `normalized:L3277-L3282` | [Source](../sources/js-allonge.md) |
| Arrays can be constructed dynamically using array literals and the spread operator, enabling functional programming techniques such as building new arrays from existing ones. | "const cons = [car, ...cdr]; Let's try it: const oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] //=> ["zero","one","two","three"]" | `normalized:L3254-L3258` | [Source](../sources/js-allonge.md) |
| Arrays can be constructed dynamically using array literals and the spread operator, enabling functional programming techniques such as building new arrays from existing ones. | "Every time we call mapWith, we're calling [...prepend, fn(first)]. To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next..." | `normalized:L4067-L4069` | [Source](../sources/js-allonge.md) |
| Array destructuring handles cases where there are fewer elements than expected by assigning undefined to missing variables. | "const [what] = []; what //=> undefined const [which, what, who] = ["duck feet", "tiger tail"]; who //=> undefined" | `normalized:L3277-L3282` | [Source](../sources/js-allonge.md) |
| Arrays can be represented as sequences of characters, such as in string-like arrays for grid representations. | "[ 'o', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]" | `normalized:L9311-L9315` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
