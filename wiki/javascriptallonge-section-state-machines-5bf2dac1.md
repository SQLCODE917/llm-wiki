---
page_id: javascriptallonge-section-state-machines-5bf2dac1
page_kind: source
summary: state machines: 10 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-state-machines-5bf2dac1@e0b759e58dac482e20e53177d1dd687e
---

# state machines

From [[javascriptallonge]].

## Statements

- Some iterables can be modelled as state machines. Let's revisit the Fibonacci sequence. Again. One way to define it is: _(javascriptallonge.pdf (source-range-8eb13d6b-01645))_
- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-8eb13d6b-01646))_
- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-8eb13d6b-01647))_
- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-8eb13d6b-01648))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-8eb13d6b-01652))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-8eb13d6b-01652))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-8eb13d6b-01652))_

## Technical atoms

### Technical frame 1: state machines

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01652))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01650))_

```
// Generation const fibonacci = () => { let a, b; console.log(a = 0); console.log(b = 1); while ( true ) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 1 1 2 3 5 8 13 21 34
```

### Technical frame 2: state machines

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01652))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01651))_

```
55 89 144 ...
```
