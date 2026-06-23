---
page_id: javascriptallonge-object-assign
page_kind: source
summary: Object.assign from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.198-200
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Object.assign copies properties from source objects into a target object, enabling cloning, extension, and prototype manipulation.

## Key supported claims

- Assigning properties from one object to another (also called “cloning” or “shallow copying”) is a basic building block that we will later use to implement more advanced paradigms like mixins. (raw/javascriptallonge.pdf p.198-200)

## Technical details

### `technical-atom-8f65f7067e458779` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
const inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24;
```

### `technical-atom-cf7340181bf68ed1` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
for ( let fruit in shipment) { inventory[fruit] = shipment[fruit] }
```

### `technical-atom-9164174e39f5e174` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
Object.assign({}, { apples: 12, oranges: 12 }) //=> { apples: 12, oranges: 12 }
```

### `technical-atom-3c484ea391ceec50` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
const inventory = { apples: 12, oranges: 12 }; const shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)
```

### `technical-atom-00af60de98e85023` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
//=> { apples: 12, // // // pears: 24 }
```

### `technical-atom-e033b9a5ae2f3787` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```javascript
const Queue = function () { this .array = []; this .head = 0; this .tail = -1 }; Queue.prototype.pushTail = function (value) { // ... }; Queue.prototype.pullHead = function () { // ... }; Queue.prototype.isEmpty = function () { // ... } Into this: const Queue = function () { Object.assign( this , { array: [], head: 0, tail: -1 }) }; Object.assign(Queue.prototype, { pushTail (value) { // ... }, pullHead () { // ... }, isEmpty () { // ...
```

### `technical-atom-8051cb5125231399` code

Citation: (raw/javascriptallonge.pdf p.198-200)

```
Recipes with Data } });
```

### `technical-atom-0564229cb33662d3` procedure

Citation: (raw/javascriptallonge.pdf p.198-200)

oranges: 12, bananas: 54, And when we discuss prototypes, we will use Object.assign to turn this:
