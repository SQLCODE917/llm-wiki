---
page_id: javascriptallonge-lists-with-functions-as-data
page_kind: source
summary: lists with functions as data from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.183-186
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explores using functions as data structures, particularly focusing on linked lists.

## Key supported claims

- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. (raw/javascriptallonge.pdf p.183-186)
- Presto, we can use pure functions to represent a linked list. (raw/javascriptallonge.pdf p.183-186)
- We used functions to replace arrays and POJOs, but we still use JavaScript's built-in operators to test for equality (===) and to branch ?: . (raw/javascriptallonge.pdf p.183-186)
- Here's another look at linked lists using POJOs. (raw/javascriptallonge.pdf p.183-186)

## Technical details

### `technical-atom-7fbeb05554d21b25` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const first = ({first, rest}) => first, rest = ({first, rest}) => rest, pair = (first, rest) => ({first, rest}), EMPTY = ({}); const l123 = pair(1, pair(2, pair(3, EMPTY))); first(l123) //=> 1 first(rest(l123)) //=> 2 first(rest(rest(l123))) //=3
```

### `technical-atom-1facdd66430f4b84` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(rest(aPair), pair(first(aPair), delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); const doubled = mapWith((x) => x * 2, l123); first(doubled) //=> 2 first(rest(doubled)) //=> 4 first(rest(rest(doubled))) //=> 6 Can we do the same with the linked lists we build out of functions? Yes: const first = K, l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### `technical-atom-b43850c16ef07986` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
rest = K(I), pair = V, EMPTY = (() => {}); const l123(first) //=> 1 l123(rest)(first)
```

### `technical-atom-21a61344f2e84d80` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
//=> 2 return l123(rest)(rest)(first) //=> 3 We write them in a backwards way, but they seem to work. How about
```

### `technical-atom-bafff516faf1e5ae` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest)); length(l123) //=> 3 And mapWith ? const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(aPair(rest), pair(aPair(first))(delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed)); const doubled = mapWith((x) => x * 2, l123) doubled(first) //=> 2 doubled(rest)(first) //=> 4 doubled(rest)(rest)(first) //=> 6
```

### `technical-atom-524bbdeeff2aabb1` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```
0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ?
```

### `technical-atom-513f5a512f78d09a` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```
delayed : reverse(rest(aPair), pair(first(aPair), delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ?
```

### `technical-atom-2e988d29b725b136` code

Citation: (raw/javascriptallonge.pdf p.183-186)

```
const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ?
```

## Related technical details

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-ac4a59dfcff9d986` worked-example

Relation: nearby source page; matched terms `arrays`, `data`, `functions`, `linked`, `list`, `lists`

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list.

### From [[javascriptallonge-a-return-to-backward-thinking]]: `technical-atom-e2b2c0d8e3d358fe` requirement

Relation: nearby source page; matched terms `but`, `can`, `data`, `functions`, `structures`, `use`

Citation: (raw/javascriptallonge.pdf p.189-190)

It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both.

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-5b37e3daf21d3949` worked-example

Relation: nearby source page; matched terms `data`, `function`, `functions`, `list`, `pojos`

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-9c77a5de5c2d57ec` procedure

Relation: nearby source page; matched terms `data`, `functions`, `like`

Citation: (raw/javascriptallonge.pdf p.177-179)

A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations.
