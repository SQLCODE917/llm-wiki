---
page_id: javascriptallonge-section-basic-operations-on-iterables-a156cdc3
page_kind: source
page_family: section-reference
summary: Basic Operations on Iterables: 2 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-basic-operations-on-iterables-a156cdc3@f5947f2f417d0b5c84c600c8eca2ed12
---

# Basic Operations on Iterables

From [[javascriptallonge]].

## Statements

- Served by the Pot: Collections 

261 

## **Basic Operations on Iterables** 

Here are the operations we’ve defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given: 

## **operations that transform one iterable into another** 

**function** * mapWith(fn, iterable) { **for** ( **const** element **of** iterable) { **yield** fn(element); } } **function** * mapAllWith (fn, iterable) { **for** ( **const** element **of** iterable) { **yield** * fn(element); } } **function** * filterWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (!!fn(element)) **yield** element; } } **function** * compact (iterable) { **for** ( **const** element **of** iterable) { **if** (element != **null** ) **yield** element; } } **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield** fn(element); } } **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator](); iterator.next(); _(javascriptallonge.pdf (source-range-af806fb1-00312))_
- 262 

Served by the Pot: Collections 

**yield** * iterator; 

} 

**function** * take (numberToTake, iterable) { **const** iterator = iterable[Symbol.iterator](); 

**for** ( **let** i = 0; i < numberToTake; ++i) { **const** { done, value } = iterator.next(); **if** (!done) **yield** value; } } 

## **operations that compose two or more iterables into an iterable** 

**function** * zip (...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]()); 

**while** ( **true** ) { **const** pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); **if** (dones.indexOf( **true** ) >= 0) **break** ; **yield** values; } }; **function** * zipWith (zipper, ...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]()); **while** ( **true** ) { **const** pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); **if** (dones.indexOf( **true** ) >= 0) **break** ; **yield** zipper(...values); } }; 

Note: zip is also the following special case of zipWith: _(javascriptallonge.pdf (source-range-af806fb1-00313))_
