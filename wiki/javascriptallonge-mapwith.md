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
