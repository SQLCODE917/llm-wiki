---
page_id: javascriptallonge-section-state-machines-80efd398
page_kind: source
summary: **state machines**: 17 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-state-machines-80efd398@f8131a18760e02f0c57c07d316294375
---

# **state machines**

From [[javascriptallonge]].

## Statements

- Some iterables can be modelled as state machines. _(javascriptallonge.pdf (source-range-83ecb080-02560))_
- - The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-83ecb080-02561))_
- - The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-83ecb080-02562))_
- - Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-83ecb080-02563))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning the natural linear state. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. _(javascriptallonge.pdf (source-range-83ecb080-02588))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02564))_

> Let’s write a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02566))_

> **const** fibonacci = () => { **let** a, b;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02564))_

> Let’s write a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02567))_

> console.log(a = 0);

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02568))_

> console.log(b = 1);

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02569))_

> **while** ( **true** ) { [a, b] = [b, a + b]; console.log(b); }

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02588))_

> Whereas the iteration version must make that state explicit.
