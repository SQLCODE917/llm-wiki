---
page_id: javascriptallonge-flip
page_kind: source
summary: Flip from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.195-196
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on function flipping and currying in JavaScript Allongé

## Key supported claims

- We wrote mapWith like this: const mapWith = (fn) => (list) => list.map(fn); (raw/javascriptallonge.pdf p.195-196)
- Looking at this, we see we're conflating two separate transformations. First, we're reversing the order of arguments. (raw/javascriptallonge.pdf p.195-196)
- We're going to extract these two operations by refactoring our function to parameterize map. (raw/javascriptallonge.pdf p.195-196)

## Technical details

### `technical-atom-c98c3c8ea3954036` code

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapWith = (fn) => (list) => list.map(fn);
```

### `technical-atom-1f3c2d6843c073f6` code

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapWith = (fn) => (list) => map(list, fn);
```

### `technical-atom-e88a9b96397776fe` code

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapWith = (fn, list) => map(list, fn);
```

### `technical-atom-0b2ff039cec68b5d` code

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapper = (list) => (fn) => map(list, fn);
```

### `technical-atom-141f9d143722e61e` code

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapWith = (first) => (second) => map(second, first);
```

### `technical-atom-8bcbad8891f70a60` code

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const wrapper = (fn) => (first) => (second) => fn(second, first);
```

### `technical-atom-ab4c64285651bea2` code

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const flipAndCurry = (fn) => (first) => (second) => fn(second, first); Sometimes you want to flip, but not curry: const flip = (fn) => (first, second) => fn(second, first); This is gold. Consider how we define mapWith now: var mapWith = flipAndCurry(map); Much nicer!
```

### `technical-atom-8d4b3dc1488c31b6` worked-example

Citation: (raw/javascriptallonge.pdf p.195-196)

Let's consider the case whether we have a map function of our own, perhaps from the allong.es 84 library, perhaps from Underscore 85 .

## Related technical details

### From [[javascriptallonge-mapwith]]: `technical-atom-509aaa6a164b3595` code

Relation: nearby source page; matched terms `const`, `list`, `map`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const map = (list, fn) => list.map(fn);
```

### From [[javascriptallonge-mapwith]]: `technical-atom-5cf0b0ae67489479` code

Relation: nearby source page; matched terms `const`, `list`, `map`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### From [[javascriptallonge-self-currying-flip]]: `technical-atom-f30515c7413d55b0` formula

Relation: nearby source page; matched terms `currying`, `flip`, `list`, `map`, `mapwith`, `our`

Citation: (raw/javascriptallonge.pdf p.196)

Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### From [[javascriptallonge-say-please]]: `technical-atom-0174c35337cda35a` code

Relation: nearby source page; matched terms `const`, `list`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.186-188)

```javascript
const reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); //=> 3 2 1 const mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed)) ); print(mapWith(x => x * x, reverse(l123))) //=> 941
```
