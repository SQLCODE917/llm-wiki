---
page_id: javascriptallonge-section-lazy-collection-operations-e526a20c
page_kind: source
summary: **lazy collection operations**: 22 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-collection-operations-e526a20c@4092ad3f0c3f9c7f9e927872125b4377
---

# **lazy collection operations**

From [[javascriptallonge]].

## Statements

- Let’s be precise: _Laziness_ is the characteristic of not doing any work until you know you need the result of the work. _(javascriptallonge.pdf (source-range-83ecb080-02778))_
- “Laziness” is a very pejorative word when applied to people. _(javascriptallonge.pdf (source-range-83ecb080-02778))_
- But it can be an excellent strategy for efficiency in algorithms. _(javascriptallonge.pdf (source-range-83ecb080-02778))_
- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) _(javascriptallonge.pdf (source-range-83ecb080-02780))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-02781))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-02781))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-83ecb080-02782))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-83ecb080-02782))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-83ecb080-02783))_
- Whereas the .map and .filter methods on Pair work with iterators. _(javascriptallonge.pdf (source-range-83ecb080-02783))_
- This expression begins with a stack containing 30 elements. _(javascriptallonge.pdf (source-range-83ecb080-02788))_
- Same with .filter, we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-83ecb080-02788))_
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. _(javascriptallonge.pdf (source-range-83ecb080-02788))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-83ecb080-02789))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-83ecb080-02789))_
- Let’s make iterable numbers. _(javascriptallonge.pdf (source-range-83ecb080-02797))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-02801))_
- This is why “pure” functional languages like Haskell combine lazy semantics with immutable collections, and why even “impure” languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-83ecb080-02801))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-02801))_

## Technical atoms

> Context: Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.
_(context: javascriptallonge.pdf (source-range-83ecb080-02781))_

> When working with very large collections and many operations, this can be important.
_(source: javascriptallonge.pdf (source-range-83ecb080-02783))_

> Context: Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.
_(context: javascriptallonge.pdf (source-range-83ecb080-02781))_

> The effect is even more pronounced when we use methods like first, until, or take:
_(source: javascriptallonge.pdf (source-range-83ecb080-02784))_

> Context: We can confirm this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02790))_

> If we write the almost identical thing with an array, we get a different behaviour:
_(source: javascriptallonge.pdf (source-range-83ecb080-02792))_
