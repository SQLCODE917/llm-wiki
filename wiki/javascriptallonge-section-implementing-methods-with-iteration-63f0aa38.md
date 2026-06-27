---
page_id: javascriptallonge-section-implementing-methods-with-iteration-63f0aa38
page_kind: source
summary: **implementing methods with iteration**: 11 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-implementing-methods-with-iteration-63f0aa38@e8c96acc38f5eba5ec53252d5bb55373
---

# **implementing methods with iteration**

From [[javascriptallonge]].

## Statements

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- To use LazyCollection, we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-83ecb080-02759))_
- For simplicity, we’ll show how to mix it into Numbers and Pair. _(javascriptallonge.pdf (source-range-83ecb080-02759))_
- **return this** .array[ **this** .index += 1] = value; }, pop: **function** () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty: **function** () { **return this** .index < 0 }, [Symbol.iterator]: **function** () { **let** iterationIndex = **this** .index; **return** { next: () => { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }, LazyCollection); Stack.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } _(javascriptallonge.pdf (source-range-83ecb080-02772))_
- _// Pair and Stack in action_ Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() _//=> 100_ Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) _(javascriptallonge.pdf (source-range-83ecb080-02775))_

## Technical atoms

> Context: _// Pair, a/k/a linked lists_
_(context: javascriptallonge.pdf (source-range-83ecb080-02761))_

> **const** EMPTY = { isEmpty: () => **true**
_(source: javascriptallonge.pdf (source-range-83ecb080-02762))_

> **const** isEmpty = (node) => node === EMPTY;
_(source: javascriptallonge.pdf (source-range-83ecb080-02766))_

> _// Stack_ **const** Stack = () => Object.assign({ array: [], index: -1, push: **function** (value) {
_(source: javascriptallonge.pdf (source-range-83ecb080-02769))_
