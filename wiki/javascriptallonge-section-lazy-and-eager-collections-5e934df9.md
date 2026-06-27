---
page_id: javascriptallonge-section-lazy-and-eager-collections-5e934df9
page_kind: source
summary: Lazy and Eager Collections: 51 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-5e934df9@07992343903a3ecd84dc620e9de4d2b7
---

# Lazy and Eager Collections

From [[javascriptallonge]].

## Statements

- The operations on iterables are tremendously valuable, but let’s reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms. _(javascriptallonge.pdf (source-range-83ecb080-02737))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-83ecb080-02738))_
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- in the older style of object-oriented programming, we built “fat” objects. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- Each collection knew how to map itself (.map), how to fold itself (.reduce), how to filter itself (.filter) and how to find one element within itself (.find). _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Each one has its own variation, but the overall form is identical. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- That’s a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- To use LazyCollection, we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-83ecb080-02759))_
- For simplicity, we’ll show how to mix it into Numbers and Pair. _(javascriptallonge.pdf (source-range-83ecb080-02759))_
- **return this** .array[ **this** .index += 1] = value; }, pop: **function** () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty: **function** () { **return this** .index < 0 }, [Symbol.iterator]: **function** () { **let** iterationIndex = **this** .index; **return** { next: () => { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }, LazyCollection); Stack.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } _(javascriptallonge.pdf (source-range-83ecb080-02772))_
- _// Pair and Stack in action_ Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() _//=> 100_ Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) _(javascriptallonge.pdf (source-range-83ecb080-02775))_
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
- We can make an eager collection out of any collection that is _gatherable_ , meaning it has a .from method: _(javascriptallonge.pdf (source-range-83ecb080-02803))_
- Here is our Pair implementation. _(javascriptallonge.pdf (source-range-83ecb080-02813))_
- Pair is gatherable, because it implements .from(). _(javascriptallonge.pdf (source-range-83ecb080-02813))_
- We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-83ecb080-02813))_
- Pair is gatherable, because it implements .from(). _(javascriptallonge.pdf (source-range-83ecb080-02813))_

## Technical atoms

> Context: _// Pair, a/k/a linked lists_
_(context: javascriptallonge.pdf (source-range-83ecb080-02761))_

> **const** EMPTY = { isEmpty: () => **true**
_(source: javascriptallonge.pdf (source-range-83ecb080-02762))_

> **const** isEmpty = (node) => node === EMPTY;
_(source: javascriptallonge.pdf (source-range-83ecb080-02766))_

> _// Stack_ **const** Stack = () => Object.assign({ array: [], index: -1, push: **function** (value) {
_(source: javascriptallonge.pdf (source-range-83ecb080-02769))_

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
