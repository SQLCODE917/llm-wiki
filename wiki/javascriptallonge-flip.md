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
