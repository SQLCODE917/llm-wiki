---
page_id: javascriptallonge-section-more-generators-d217e00d
page_kind: source
summary: more generators: 9 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-more-generators-d217e00d@698e579b6f0f4c2718658928cbab7002
---

# more generators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-generator]] - topic hub: opens the topic page for Generator

## Statements

- Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state: _(javascriptallonge.pdf (source-range-8eb13d6b-01719))_
- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-8eb13d6b-01724))_

## Technical atoms

### Technical frame 1: more generators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01719))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01717))_

```
const Numbers = { *[Symbol.iterator] () { let i = 0; while ( true ) { yield i++; } } }; for ( const i of Numbers) { console.log(i); } //=> 0 1 2 3 4 5 6 7
```

### Technical frame 2: more generators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01719))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01718))_

```
8 9 10 ...
```

### Technical frame 3: more generators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01724))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01720))_

```
const Fibonacci = { [Symbol.iterator]: () => { let a = 0, b = 1, state = 0; return { next: () => { switch (state) { case 0: state = 1; return {value: a}; case 1: state = 2; return {value: b}; case 2: [a, b] = [b, a + b]; return {value: b}; } } } } }; for ( let n of Fibonacci) { console.log(n) } //=> 0 1 1 2 3 5 8 13
```

### Technical frame 4: more generators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01724))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01721))_

```
21 34 55 89 144 ...
```

### Technical frame 5: more generators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01724))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01723))_

```
const Fibonacci = { *[Symbol.iterator] () { let a, b; yield a = 0; yield b = 1; while ( true ) { [a, b] = [b, a + b] yield b; } } } for ( const i of Fibonacci) { console.log(i); } //=> 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
```

### Technical frame 6: more generators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01724))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01726))_

```
function * fibonacci () { let a, b; yield a = 0; yield b = 1; while ( true ) { [a, b] = [b, a + b] yield b; } } for ( const i of fibonacci()) { console.log(i); } //=> 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
```
