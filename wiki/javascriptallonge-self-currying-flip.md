---
page_id: javascriptallonge-self-currying-flip
page_kind: source
summary: self-currying flip from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.196-196
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on self-currying flip function in JavaScriptAllongé, covering flip function and argument order reversal.

## Key supported claims

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). (raw/javascriptallonge.pdf p.196-196)
- Now if we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice. (raw/javascriptallonge.pdf p.196-196)

## Technical details

### `technical-atom-8a3beed3e846ae78` code

Citation: (raw/javascriptallonge.pdf p.196)

```javascript
const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn(second, first); } else { return function (second) { return fn(second, first); }; }; };
```

### `technical-atom-f30515c7413d55b0` formula

Citation: (raw/javascriptallonge.pdf p.196)

Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

## Related technical details

### From [[javascriptallonge-flip]]: `technical-atom-ab4c64285651bea2` code

Relation: nearby source page; matched terms `but`, `flip`, `map`, `mapwith`, `now`, `sometimes`

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const flipAndCurry = (fn) => (first) => (second) => fn(second, first); Sometimes you want to flip, but not curry: const flip = (fn) => (first, second) => fn(second, first); This is gold. Consider how we define mapWith now: var mapWith = flipAndCurry(map); Much nicer!
```

### From [[javascriptallonge-flip]]: `technical-atom-c98c3c8ea3954036` code

Relation: nearby source page; matched terms `flip`, `list`, `map`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapWith = (fn) => (list) => list.map(fn);
```

### From [[javascriptallonge-flip]]: `technical-atom-1f3c2d6843c073f6` code

Relation: nearby source page; matched terms `flip`, `list`, `map`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapWith = (fn) => (list) => map(list, fn);
```

### From [[javascriptallonge-flip]]: `technical-atom-e88a9b96397776fe` code

Relation: nearby source page; matched terms `flip`, `list`, `map`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.195-196)

```javascript
const mapWith = (fn, list) => map(list, fn);
```
