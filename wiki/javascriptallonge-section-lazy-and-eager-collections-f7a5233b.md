---
page_id: javascriptallonge-section-lazy-and-eager-collections-f7a5233b
page_kind: source
page_family: section-reference
summary: Lazy and Eager Collections: 39 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-f7a5233b@9b306e327881ebf7eb9fa81201fdf1e7
---

# Lazy and Eager Collections

From [[javascriptallonge]].

## Statements

- Served by the Pot: Collections 

223 

## **Lazy and Eager Collections** 

The operations on iterables are tremendously valuable, but let’s reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms. 

Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack 

in the older style of object-oriented programming, we built “fat” objects. Each collection knew how to map itself (.map), how to fold itself (.reduce), how to filter itself (.filter) and how to find one element within itself (.find). If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. 

Over time, this informal “interface” for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself. 

But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. Each one has its own variation, but the overall form is identical. That’s a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. 

This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. 

## **implementing methods with iteration** 

Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith. 

Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces. 

Here is LazyCollection, a mixin we can use with any ordered collection that is also an iterable: _(javascriptallonge.pdf (source-range-af806fb1-00271))_
- 227 

Served by the Pot: Collections 

[Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **let** remainingElements = numberToTake; **return** { next: () => { **let** { done, value } = iterator.next(); done = done || remainingElements-- <= 0; **return** ({ done, value: done ? **undefined** : value }); } } } }, LazyCollection); } } 

To use LazyCollection, we mix it into an any iterable object. For simplicity, we’ll show how to mix it into Numbers and Pair. But it can also be mixed into prototypes (a/k/a “classes”), traits, or other OO constructs: 

**const** Numbers = Object.assign({ [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }, LazyCollection); 

_// Pair, a/k/a linked lists_ 

**const** EMPTY = { isEmpty: () => **true** _(javascriptallonge.pdf (source-range-af806fb1-00275))_
- 230 

Served by the Pot: Collections 

_// Pair and Stack in action_ Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() _//=> 100_ Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) 

_//=> 220_ 

## **lazy collection operations** 

“Laziness” is a very pejorative word when applied to people. But it can be an excellent strategy for efficiency in algorithms. Let’s be precise: _Laziness_ is the characteristic of not doing any work until you know you need the result of the work. 

Here’s an example. Compare these two: 

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) 

Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. 

But it’s still illustrative to dissect something important: Array’s .map and .filter methods gather their results into new arrays. Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. 

Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working with very large collections and many operations, this can be important. 

The effect is even more pronounced when we use methods like first, until, or take: _(javascriptallonge.pdf (source-range-af806fb1-00278))_
- Served by the Pot: Collections 

231 

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() 

This expression begins with a stack containing 30 elements. The top two are 29 and 28. It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter, we get an iterable that can iterate over the even squares, but not an actual stack or array. 

Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. 

We can confirm this: 

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => { console.log(`squaring **${** x **}** `); **return** x * x }) .filter((x) => { console.log(`filtering **${** x **}** `); **return** x % 2 == 0 }) .first() _//=>_ squaring 29 filtering 841 squaring 28 filtering 784 784 

If we write the almost identical thing with an array, we get a different behaviour: _(javascriptallonge.pdf (source-range-af806fb1-00279))_
- 232 

Served by the Pot: Collections 

[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29] .reverse() .map((x) => { console.log(`squaring **${** x **}** `); **return** x * x }) .filter((x) => { console.log(`filtering **${** x **}** `); **return** x % 2 == 0 })[0] _//=>_ squaring 0 squaring 1 squaring 2 squaring 3 ... squaring 28 squaring 29 filtering 0 filtering 1 filtering 4 ... filtering 784 filtering 841 784 

Arrays copy-on-read, so every time we perform a map or filter, we get a new array and perform all the computations. This might be expensive. 

You recall we briefly touched on the idea of infinite collections? Let’s make iterable numbers. They _have_ to be lazy, otherwise we couldn’t write things like: _(javascriptallonge.pdf (source-range-af806fb1-00280))_
- 233 

Served by the Pot: Collections 

**const** Numbers = Object.assign({ [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }, LazyCollection); **const** firstCubeOver1234 = Numbers .map((x) => x * x * x) .filter((x) => x > 1234) .first() _//=> 1331_ 

Balanced against their flexibility, our “lazy collections” use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why “pure” functional languages like Haskell combine lazy semantics with immutable collections, and why even “impure” languages like Clojure emphasize the use of immutable collections. 

## **eager collections** 

An _eager_ collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is _gatherable_ , meaning it has a .from method: 

**const** extend = **function** (consumer, ...providers) { **for** ( **let** i = 0; i < providers.length; ++i) { **const** provider = providers[i]; **for** ( **let** key **in** provider) { **if** (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } **return** consumer }; _(javascriptallonge.pdf (source-range-af806fb1-00281))_
- Served by the Pot: Collections 

236 

Here is our Pair implementation. Pair is gatherable, because it implements .from(). We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: 

**const** EMPTY = { isEmpty: () => **true** }; **const** isEmpty = (node) => node === EMPTY; **const** Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => **false** , [Symbol.iterator]: **function** () { **let** currentPair = **this** ; **return** { next: () => { **if** (currentPair.isEmpty()) { **return** {done: **true** } } **else** { **const** value = currentPair.car; currentPair = currentPair.cdr; **return** {done: **false** , value} } } } } }, EagerCollection(Pair)); Pair.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next(); **return** done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); Pair.from([1, 2, 3, 4, 5]).map(x => x * 2) _//=>_ _(javascriptallonge.pdf (source-range-af806fb1-00284))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-af806fb1-00271))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-af806fb1-00278))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-af806fb1-00278))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-af806fb1-00279))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-af806fb1-00281))_
- Pair is gatherable, because it implements .from(). _(javascriptallonge.pdf (source-range-af806fb1-00284))_
