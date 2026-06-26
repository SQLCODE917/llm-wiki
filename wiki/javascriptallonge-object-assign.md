---
page_id: javascriptallonge-object-assign
page_kind: source
summary: Object.assign from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.198-200
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on Object.assign in JavaScript Allongé, covering its usage for extending objects and copying properties.

## Key supported claims

- Object.assign extends objects by assigning properties to them (raw/javascriptallonge.pdf p.198-200).
- Object.assign can copy properties from one object to another, functioning as a shallow copy (raw/javascriptallonge.pdf p.198-200).

## Technical details

### `technical-atom-fcf876e08a0eaadc` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
const inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24;
```

### `technical-atom-25985e8d0ddf7593` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
for ( let fruit in shipment) { inventory[fruit] = shipment[fruit] }
```

### `technical-atom-6a4fb7240578c177` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
Object.assign({}, { apples: 12, oranges: 12 }) //=> { apples: 12, oranges: 12 }
```

### `technical-atom-f0f478cebf6525ce` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
const inventory = { apples: 12, oranges: 12 }; const shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)
```

### `technical-atom-e9465560de9bc8b1` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
//=> { apples: 12, // oranges: 12, // bananas: 54, // pears: 24 }
```

### `technical-atom-87b8267933bf4b18` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
const Queue = function () { this .array = []; this .head = 0; this .tail = -1 }; Queue.prototype.pushTail = function (value) { // ... }; Queue.prototype.pullHead = function () { // ... }; Queue.prototype.isEmpty = function () { // ... } Into this: const Queue = function () { Object.assign( this, { array: [], head: 0, tail: -1 }) }; Object.assign(Queue.prototype, { pushTail (value) { // ... }, pullHead () { // ... }, isEmpty () { // ...
```

### `technical-atom-1294486230367b21` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```
## });
```

### `technical-atom-c7664a77b0b16687` procedure

Citation: (raw/javascriptallonge.pdf p.198-200)

And when we discuss prototypes, we will use Object.assign to turn this:

## Related technical details

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-d3b675be6d62eed9` code

Relation: nearby source page; matched terms `function`, `its`, `javascript`, `one`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.
```
