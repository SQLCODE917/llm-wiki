---
page_id: javascriptallonge-section-implementing-methods-with-iteration-3763e522
page_kind: source
summary: implementing methods with iteration: 14 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-implementing-methods-with-iteration-3763e522@a08be542f63a49a96383da74fcf4b0e5
---

# implementing methods with iteration

From [[javascriptallonge]].

## Statements

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-31a4cf47-01770))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-31a4cf47-01771))_
- To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs: _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

## Technical atoms

### Technical frame 1: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01773))_

```
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined : fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```

### Technical frame 2: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01774))_

```
}, filter(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { do { const { done, value } = iterator.next(); } while (!done && !fn(value)); return { done, value }; } } } }, LazyCollection) }, find(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { let { done, value } = iterator.next(); done = done || fn(value); return ({ done, value: done ? undefined : value }); } } }
```

### Technical frame 3: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01775))_

```
}, LazyCollection) }, until(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { let { done, value } = iterator.next(); done = done || fn(value); return ({ done, value: done ? undefined : value }); } } } }, LazyCollection) }, first() { return this [Symbol.iterator]().next().value; }, rest() { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); iterator.next(); return iterator; } }, LazyCollection); }, take(numberToTake) { return Object.assign({
```

### Technical frame 4: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01776))_

```
[Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); let remainingElements = numberToTake; return { next: () => { let { done, value } = iterator.next(); done = done || remainingElements-- <= 0; return ({ done, value: done ? undefined : value }); } } } }, LazyCollection); } }
```

### Technical frame 5: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01778))_

```
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } }, LazyCollection); // Pair, a/k/a linked lists const EMPTY = { isEmpty: () => true
```

### Technical frame 6: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01779))_

```
}; const isEmpty = (node) => node === EMPTY; const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false , [Symbol.iterator]: function () { let currentPair = this ; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false , value} } } } } }, LazyCollection); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); // Stack const Stack = () => Object.assign({ array: [], index: -1, push: function (value) {
```

### Technical frame 7: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01780))_

```
return this .array[ this .index += 1] = value; }, pop: function () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty: function () { return this .index < 0 }, [Symbol.iterator]: function () { let iterationIndex = this .index; return { next: () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }, LazyCollection); Stack.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; }
```

### Technical frame 8: implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01777))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01781))_

```
// Pair and Stack in action Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() //=> 100 Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0)
```
