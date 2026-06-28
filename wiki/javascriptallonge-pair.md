---
page_id: javascriptallonge-pair
page_kind: concept
summary: Pair: 4 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pair@11ffe41cf4d99f3f49a954c81085667c
---

# Pair

What [[javascriptallonge]] covers about pair:

## Statements

### why const and let were invented

- 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . . . . + 99 + 100 = ? But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . . . . + (50 + 51) = ? If you notice every pair of numbers adds up to 101. There are 50 pairs of numbers, so the answer is 50*101 = 5050. Of course Gauss came up with the answer about 20 times faster than the other kids. _(javascriptallonge.pdf (source-range-31a4cf47-01206))_

### a return to backward thinking

- The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it: _(javascriptallonge.pdf (source-range-31a4cf47-01411))_

### eager collections

- Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-31a4cf47-01807))_


## Technical atoms

### Technical frame 1: why const and let were invented

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01205))_

> Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01204))_

```
var sum = 0; for ( var i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050
```

### Technical frame 2: a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01413))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01412))_

```
const first = K, second = K(I), pair = (first) => (second) => { const pojo = {first, second}; return (selector) => selector(pojo.first)(pojo.second); }; const latin = pair("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```

### Technical frame 3: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01805))_

```
const EagerCollection = (gatherable) => ({ map(fn) { const original = this ; return gatherable.from( ( function * () { for ( let element of original) { yield fn(element); } })() ); }, reduce(fn, seed) { let accumulator = seed; for ( let element of this ) { accumulator = fn(accumulator, element); } return accumulator; }, filter(fn) { const original = this ; return gatherable.from( ( function * () { for ( let element of original) { if (fn(element)) yield element; } })() ); }, find(fn) { for ( let element of this ) { if (fn(element)) return element; } }, until(fn) {
```

### Technical frame 4: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01806))_

```
const original = this ; return gatherable.from( ( function * () { for ( let element of original) { if (fn(element)) break ; yield element; } })() ); }, first() { return this [Symbol.iterator]().next().value; }, rest() { const iteration = this [Symbol.iterator](); iteration.next(); return gatherable.from( ( function * () { yield * iteration; })() ); return gatherable.from(iterable); }, take(numberToTake) { const original = this ; let numberRemaining = numberToTake; return gatherable.from( ( function * () { for ( let element of original) { if (numberRemaining-- <= 0) break ; yield element; } })() ); } });
```

### Technical frame 5: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01808))_

```
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false , [Symbol.iterator]: function () { let currentPair = this ; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false , value} } } } } }, EagerCollection(Pair)); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); Pair.from([1, 2, 3, 4, 5]).map(x => x * 2) //=>
```

### Technical frame 6: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01809))_

```
{"car": 2, "cdr": {"car": 4, "cdr": {"car": 6, "cdr": {"car": 8, "cdr": {"car": 10, "cdr": {} } } } } }
```


## Source

- [[javascriptallonge]]
