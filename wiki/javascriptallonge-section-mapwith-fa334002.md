---
page_id: javascriptallonge-section-mapwith-fa334002
page_kind: source
summary: mapWith: 14 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mapwith-fa334002@15ed2aca387b4a11e3a3416a2a7051ef
---

# mapWith

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-mapwith]] - topic hub: opens the topic page for Mapwith

## Statements

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map : _(javascriptallonge.pdf (source-range-31a4cf47-01437))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-31a4cf47-01440))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-31a4cf47-01442))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-31a4cf47-01444))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-31a4cf47-01437))_

## Technical atoms

### Technical frame 1: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01430))_

> In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

### Technical frame 2: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01431))_

```
[1, 2, 3, 4, 5].map(x => x * x) //=> [1, 4, 9, 16, 25]
```

### Technical frame 3: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01433))_

```
const map = (list, fn) => list.map(fn);
```

### Technical frame 4: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01435))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 5: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01440))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01438))_

```
const squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### Technical frame 6: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01442))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01441))_

```
const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### Technical frame 7: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01444))_

> Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01443))_

```
const squaresOf = callRight(map, (n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```
