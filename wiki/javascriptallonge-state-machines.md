---
page_id: javascriptallonge-state-machines
page_kind: source
summary: Summary of the state machines chapter from JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.228-229
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter introduces the concept of state machines and applies it to the Fibonacci sequence.

## Key supported claims

- Some iterables can be modelled as state machines (raw/javascriptallonge.pdf p.228-229).
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that (raw/javascriptallonge.pdf p.228-229).
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 (raw/javascriptallonge.pdf p.228-229).
