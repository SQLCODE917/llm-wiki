---
page_id: javascriptallonge-section-we-ll-keep-it-simple-de0e7faa
page_kind: source
summary: We'll keep it simple:: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-de0e7faa@2eb48a60e45dede9bbe8eb6301ca81b3
---

# We'll keep it simple:

From [[javascriptallonge]].

## Statements

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-8eb13d6b-01657))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-8eb13d6b-01658))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-8eb13d6b-01657))_

## Technical atoms

### Technical frame 1: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01657))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01654))_

```
// Iteration let a, b, state = 0; const fibonacci = () => { switch (state) { case 0: state = 1; return a = 0; case 1: state = 2; return b = 1; case 2: [a, b] = [b, a + b]; return b } }; while ( true ) { console.log(fibonacci()); } //=> 0 1 1 2 3 5 8 13
```

### Technical frame 2: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01657))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01656))_

```
21 34 55 89 144 ...
```

### Technical frame 3: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01657))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01658))_

> Whereas the iteration version must make that state explicit.
