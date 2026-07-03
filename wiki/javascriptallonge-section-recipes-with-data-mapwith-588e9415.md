---
page_id: javascriptallonge-section-recipes-with-data-mapwith-588e9415
page_kind: source
page_family: section-reference
summary: Recipes with Data / mapWith: 14 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-mapwith-588e9415@23fb6786c0c640cd2c37ce295faa6ea3
---

# Recipes with Data / mapWith

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-data-178f0a89]] - broader source section: Recipes with Data

### Topics

- [[javascriptallonge-mapwith]] - topic hub: opens the topic page for Mapwith

## Statements

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map : _(javascriptallonge.pdf (source-range-7239e085-01437))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01440))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-7239e085-01442))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-7239e085-01444))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-7239e085-01437))_

## Technical atoms

### Technical frame 1: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01435))_

<a id="atom-technical-atom-92d9e96e2e180c9e"></a>

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 2: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01440))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01438))_

<a id="atom-technical-atom-119fde11eb201f8c"></a>

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 3: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01442))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01441))_

<a id="atom-technical-atom-b020d8626cf2b008"></a>

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 4: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01444))_

> Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01443))_

<a id="atom-technical-atom-f371fc3e501b7ae0"></a>

```
const squaresOf = callRight(map, (n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```
