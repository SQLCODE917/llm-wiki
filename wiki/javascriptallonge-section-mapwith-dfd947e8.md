---
page_id: javascriptallonge-section-mapwith-dfd947e8
page_kind: source
summary: mapWith: 7 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mapwith-dfd947e8@163963d3c58792deb8742d9550b707a0
---

# mapWith

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-mapwith]] - topic hub: opens the topic page for Mapwith

## Statements

- Recipes with Data

170

## **mapWith**

In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

[1, 2, 3, 4, 5].map(x => x * x) _//=> [1, 4, 9, 16, 25]_ We could write a function that behaves like the .map method if we wanted: **const** map = (list, fn) => list.map(fn);

This recipe isn’t for map: It’s for mapWith, a function that wraps around map and turns any other function into a mapper. mapWith is very simple:[82] **const** mapWith = (fn) => (list) => list.map(fn); mapWith differs from map in two ways. It reverses the arguments, taking the function first and the list second. It also “curries” the function: Instead of taking two arguments, it takes one argument and returns a function that takes another argument.

That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map: **const** squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ We can call mapWith in one step:

> 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- Recipes with Data

171 **const** squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result: **const** squaresOf = callRight(map, (n => n * n); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _mapWith was suggested by ludicast_[83] > 83http://github.com/ludicast _(javascriptallonge.pdf (source-range-83ecb080-00229))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
