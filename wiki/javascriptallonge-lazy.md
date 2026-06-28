---
page_id: javascriptallonge-lazy
page_kind: concept
summary: Lazy: 2 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-lazy@cbe4297279bdbfd68064ac262b3b95e9
---

# Lazy

What [[javascriptallonge]] covers about lazy:

## Statements

### Lazy and Eager Collections

- 227

Served by the Pot: Collections

[Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **let** remainingElements = numberToTake; **return** { next: () => { **let** { done, value } = iterator.next(); done = done || remainingElements-- <= 0; **return** ({ done, value: done ? **undefined** : value }); } } } }, LazyCollection); } }

To use LazyCollection, we mix it into an any iterable object. For simplicity, we’ll show how to mix it into Numbers and Pair. But it can also be mixed into prototypes (a/k/a “classes”), traits, or other OO constructs: **const** Numbers = Object.assign({ [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }, LazyCollection);

_// Pair, a/k/a linked lists_ **const** EMPTY = { isEmpty: () => **true** _(javascriptallonge.pdf (source-range-83ecb080-00291))_

- 233

Served by the Pot: Collections **const** Numbers = Object.assign({ [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }, LazyCollection); **const** firstCubeOver1234 = Numbers .map((x) => x * x * x) .filter((x) => x > 1234) .first() _//=> 1331_

Balanced against their flexibility, our “lazy collections” use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why “pure” functional languages like Haskell combine lazy semantics with immutable collections, and why even “impure” languages like Clojure emphasize the use of immutable collections.

## **eager collections**

An _eager_ collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is _gatherable_ , meaning it has a .from method: **const** extend = **function** (consumer, ...providers) { **for** ( **let** i = 0; i < providers.length; ++i) { **const** provider = providers[i]; **for** ( **let** key **in** provider) { **if** (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } **return** consumer }; _(javascriptallonge.pdf (source-range-83ecb080-00297))_


## Source

- [[javascriptallonge]]
