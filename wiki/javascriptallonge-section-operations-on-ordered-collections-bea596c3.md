---
page_id: javascriptallonge-section-operations-on-ordered-collections-bea596c3
page_kind: source
summary: **operations on ordered collections**: 26 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-on-ordered-collections-bea596c3@2830024399a6ad3fff99c5d9a234fcca
---

# **operations on ordered collections**

From [[javascriptallonge]].

## Statements

- Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] _(javascriptallonge.pdf (source-range-83ecb080-02469))_
- Let’s define some operations on ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02469))_
- > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- Many operations on ordered collections return another ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02475))_
- They do so by taking care to iterate over a result freshly every time we get an iterator for them. _(javascriptallonge.pdf (source-range-83ecb080-02475))_
- Numbers is an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02480))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Like mapWith, they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-83ecb080-02496))_
- And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-83ecb080-02497))_
- As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02500))_
- For completeness, here are two more handy iterable functions. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-83ecb080-02503))_

## Technical atoms

> Context: Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-02475))_

> **const** Evens = mapWith((x) => 2 * x, Numbers);
_(source: javascriptallonge.pdf (source-range-83ecb080-02476))_

> Context: Mind you, we can also map non-collection iterables, like RandomNumbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-02484))_

> **const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
_(source: javascriptallonge.pdf (source-range-83ecb080-02485))_

> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines, but if RandomNumbers doesn’t behave like an ordered collection, that’s not mapWith’s fault.
_(source: javascriptallonge.pdf (source-range-83ecb080-02491))_

> Context: And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000:
_(context: javascriptallonge.pdf (source-range-83ecb080-02497))_

> [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961]
_(source: javascriptallonge.pdf (source-range-83ecb080-02499))_

> Context: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]:
_(context: javascriptallonge.pdf (source-range-83ecb080-02501))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } });
_(source: javascriptallonge.pdf (source-range-83ecb080-02502))_
