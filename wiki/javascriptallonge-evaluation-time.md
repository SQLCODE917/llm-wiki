---
page_id: javascriptallonge-evaluation-time
page_kind: source
summary: evaluation time from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.204-204
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the evaluation time section from JavaScript Allongé, focusing on quasi-literals and their evaluation timing.

## Key supported claims

- Like any other expression, quasi-literals are evaluated late, when that line or lines of code is evaluated. (raw/javascriptallonge.pdf p.204-204)
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. (raw/javascriptallonge.pdf p.204-204)
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. (raw/javascriptallonge.pdf p.204-204)

## Technical details

### `technical-atom-b953a8b77eeafa45` code

Citation: (raw/javascriptallonge.pdf p.204)

```javascript
const name = "Harry"; const greeting = (name) => `Hello my name is ${ name } `; greeting('Arthur Dent') //=> 'Hello my name is Arthur Dent'
```

### `technical-atom-2b2624939ec3068f` code

Citation: (raw/javascriptallonge.pdf p.204)

```javascript
const greeting = (name) => 'Hello my name is ' + name; greeting('Arthur Dent') //=> 'Hello my name is Arthur Dent'
```

## Related technical details

### From [[javascriptallonge-quasi-literals]]: `technical-atom-46fa8cdbb930a009` code

Relation: nearby source page; matched terms `code`, `expression`, `quasi-literal`

Citation: (raw/javascriptallonge.pdf p.203-204)

```
Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} .
```

### From [[javascriptallonge-like-this]]: `technical-atom-c4518a45f6d0ca3a` code

Relation: nearby source page; matched terms `code`, `like`, `value`

Citation: (raw/javascriptallonge.pdf p.210-211)

```javascript
const Stack2 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } });
```

### From [[javascriptallonge-like-this]]: `technical-atom-6a2bb4b3b3abb688` code

Relation: nearby source page; matched terms `code`, `like`, `value`

Citation: (raw/javascriptallonge.pdf p.210-211)

```javascript
const stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-3f7ceba972853444` code

Relation: nearby source page; matched terms `code`, `like`, `value`

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```
