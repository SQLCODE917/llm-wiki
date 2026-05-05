---
title: Arrays
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Arrays

Arrays in JavaScript are zero-based indexed collections that store references to their elements rather than copies, enabling efficient memory usage but requiring careful consideration when modifying nested structures.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Arrays in JavaScript are zero-based indexed collections | "As we can see, JavaScript Arrays are zero-based." | `normalized:L3156` | [Source](../sources/js-allonge.md) |
| Arrays store references to their elements rather than copies | "arrays store references to the things you put in them." | `normalized:L3169` | [Source](../sources/js-allonge.md) |
| Arrays store references to the things you put in them | "//=> true, arrays store references to the things you put in them." | `normalized:L3170` | [Source](../sources/js-allonge.md) |
| Destructuring allows extracting elements from arrays by pattern matching | "The statement const [something] = wrapped; destructures the array represented by wrapped, binding the value of its single element to the name something." | `normalized:L3194` | [Source](../sources/js-allonge.md) |
| Destructuring can handle nested arrays by using nested patterns | "Destructuring can nest: const description = (nameAndOccupation) => { const [[first, last], occupation] = nameAndOccupation;" | `normalized:L3212` | [Source](../sources/js-allonge.md) |
| The spread operator can be used to gather remaining elements from an array into a new array | "const [car, ...cdr] = [1, 2, 3, 4, 5];" | `normalized:L3222` | [Source](../sources/js-allonge.md) |
| The spread operator can be used to insert elements of one array into another array literal | "const cons = [car, ...cdr];" | `normalized:L3254` | [Source](../sources/js-allonge.md) |
| JavaScript's destructuring does not perform strict pattern matching and will bind undefined when elements are missing | "JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name." | `normalized:L3275` | [Source](../sources/js-allonge.md) |
| Mapping is a common operation that applies a function to every element of an array | "Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let's write our own using linear recursion" | `normalized:L3527` | [Source](../sources/js-allonge.md) |
| Using array destructuring with rest syntax in recursive functions leads to inefficient memory usage due to creating new arrays | "Every time we call mapWith, we're calling [...prepend, fn(first)]. To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith." | `normalized:L4067` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding arrays in JavaScript is crucial for effective programming because they form the foundation of many data manipulation techniques. The zero-based indexing system affects how developers access elements, while the fact that arrays store references rather than copies impacts how modifications propagate through nested structures. Destructuring provides powerful syntactic shortcuts for extracting values, especially when combined with the spread operator for gathering remaining elements or inserting array contents. These features enable concise and expressive code, but also introduce potential pitfalls such as unexpected mutations and performance issues when used in recursive operations with array destructuring and rest syntax.

## Source pages

- [Source](../sources/js-allonge.md)