---
page_id: javascriptallonge-mapwith
page_kind: source
summary: mapWith from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.193-194
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on mapWith function in JavaScript Allongé

## Key supported claims

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. (raw/javascriptallonge.pdf p.193-194)
- mapWith is a very convenient abstraction for a very common pattern. (raw/javascriptallonge.pdf p.193-194)
- This recipe isn't for map : It's for mapWith , a function that wraps around map and turns any other function into a mapper. (raw/javascriptallonge.pdf p.193-194)
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. (raw/javascriptallonge.pdf p.193-194)
- mapWith differs from map in two ways. (raw/javascriptallonge.pdf p.193-194)

## Technical details

### `technical-atom-ac9b758af2169f1f` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
[1, 2, 3, 4, 5].map(x => x * x) //=> [1, 4, 9, 16, 25]
```

### `technical-atom-509aaa6a164b3595` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const map = (list, fn) => list.map(fn);
```

### `technical-atom-d0d33ed680f250ad` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const mapWith = (fn) => (list) => list.map(fn);
```

### `technical-atom-5cf0b0ae67489479` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### `technical-atom-b83ee0152874acf5` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### `technical-atom-27c0d5080d1e87d0` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const squaresOf = callRight(map, (n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### `technical-atom-6966da198e4497f2` procedure

Citation: (raw/javascriptallonge.pdf p.193-194)

Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array.

### `technical-atom-9e71aa454dfd51aa` procedure

Citation: (raw/javascriptallonge.pdf p.193-194)

This recipe isn't for map : It's for mapWith , a function that wraps around map and turns any other function into a mapper.

## Related technical details

### From [[javascriptallonge-flip]]: `technical-atom-8d4b3dc1488c31b6` worked-example

Relation: nearby source page; matched terms `allong`, `function`, `map`

Citation: (raw/javascriptallonge.pdf p.195-196)

Let's consider the case whether we have a map function of our own, perhaps from the allong.es 84 library, perhaps from Underscore 85 .

### From [[javascriptallonge-flip]]: `technical-atom-ab4c64285651bea2` code

Relation: nearby source page; matched terms `map`, `mapwith`, `you`

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const flipAndCurry = (fn) => (first) => (second) => fn(second, first); Sometimes you want to flip, but not curry: const flip = (fn) => (first, second) => fn(second, first); This is gold. Consider how we define mapWith now: var mapWith = flipAndCurry(map); Much nicer!
```

### From [[javascriptallonge-self-currying-flip]]: `technical-atom-f30515c7413d55b0` formula

Relation: nearby source page; matched terms `can`, `map`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.196)

Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-1facdd66430f4b84` code

Relation: nearby source page; matched terms `can`, `mapwith`, `yes`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(rest(aPair), pair(first(aPair), delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); const doubled = mapWith((x) => x * 2, l123); first(doubled) //=> 2 first(rest(doubled)) //=> 4 first(rest(rest(doubled))) //=> 6 Can we do the same with the linked lists we build out of functions? Yes: const first = K, l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```
