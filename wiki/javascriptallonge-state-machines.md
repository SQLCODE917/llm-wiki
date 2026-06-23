---
page_id: javascriptallonge-state-machines
page_kind: source
summary: state machines from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.228-229
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter introduces the concept of state machines and applies it to the Fibonacci sequence.

## Key supported claims

- Some iterables can be modelled as state machines (raw/javascriptallonge.pdf p.228-229).
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that (raw/javascriptallonge.pdf p.228-229).
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 (raw/javascriptallonge.pdf p.228-229).

## Technical details

### `technical-atom-da3cd0ef29babd23` code

Citation: (raw/javascriptallonge.pdf p.228-229)

```javascript
// Generation const fibonacci = () => { let a, b; console.log(a = 0); console.log(b = 1); while ( true ) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 1 1 2 3 5 8 13 21 34
```

### `technical-atom-6b989320465ca673` code

Citation: (raw/javascriptallonge.pdf p.228-229)

```
55 89 144 ...
```
