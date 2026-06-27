---
page_id: javascriptallonge-section-mapwith-269eb4c6
page_kind: source
summary: **mapWith**: 18 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mapwith-269eb4c6@2004b668b48ee238467316adcdf26f4a
---

# **mapWith**

From [[javascriptallonge]].

## Statements

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-83ecb080-02219))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-83ecb080-02219))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- > 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-83ecb080-02228))_
- mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-83ecb080-02231))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02212))_

> In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02212))_

> In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02213))_

> [1, 2, 3, 4, 5].map(x => x * x) _//=> [1, 4, 9, 16, 25]_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02214))_

> We could write a function that behaves like the .map method if we wanted:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02215))_

> **const** map = (list, fn) => list.map(fn);

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02215, source-range-83ecb080-02219))_

> **const** map = (list, fn) => list.map(fn); That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02217))_

> **const** mapWith = (fn) => (list) => list.map(fn);

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02219))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02220))_

> **const** squaresOf = (list) => list.map(x => x * x);

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02220))_

> **const** squaresOf = (list) => list.map(x => x * x);

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02221))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02223, source-range-83ecb080-02228))_

> > 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02226))_

> **const** squaresOf = mapWith(n => n * n);

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02228))_

> If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02227))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02228))_

> If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02229))_

> **const** squaresOf = callRight(map, (n => n * n);

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02228))_

> If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02230))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_
