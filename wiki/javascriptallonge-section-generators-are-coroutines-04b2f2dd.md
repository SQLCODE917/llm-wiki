---
page_id: javascriptallonge-section-generators-are-coroutines-04b2f2dd
page_kind: source
summary: generators are coroutines: 25 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generators-are-coroutines-04b2f2dd@b8c636633eae117a83dc3025679a0a29
---

# generators are coroutines

From [[javascriptallonge]].

## Statements

- This is where generators behave very, very differently from ordinary functions. What happens semantically ? _(javascriptallonge.pdf (source-range-8eb13d6b-01678))_
- The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-8eb13d6b-01680))_
- When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-8eb13d6b-01681))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-8eb13d6b-01685))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-8eb13d6b-01686))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-8eb13d6b-01690))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-8eb13d6b-01691))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-8eb13d6b-01695))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-8eb13d6b-01696))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-8eb13d6b-01697))_
- This behaviour is not unique to JavaScript, generators are called coroutines 92 in other languages: _(javascriptallonge.pdf (source-range-8eb13d6b-01699))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-8eb13d6b-01700))_
- Instead of thinking of there being on execution context, we can imagine that there are two execution contexts. With an iterator, we can call them the producer and the consumer . The iterator is the producer, and the code that iterates over it is the consumer. When the consumer calls .next() , it 'suspends' and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next() . _(javascriptallonge.pdf (source-range-8eb13d6b-01701))_
- Of course, generators need not be implemented exactly as coroutines. For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-8eb13d6b-01703))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-8eb13d6b-01705))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-8eb13d6b-01700))_
- For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-8eb13d6b-01703))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-8eb13d6b-01705))_

## Technical atoms

### Technical frame 1: generators are coroutines

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01678))_

> This is where generators behave very, very differently from ordinary functions. What happens semantically ?

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01677))_

```
const oneTwoThree = function * () { yield 1; yield 2; yield 3; }; oneTwoThree().next() //=> {"done": false , value: 1} oneTwoThree().next() //=> {"done": false , value: 1} oneTwoThree().next() //=> {"done": false , value: 1} const iterator = oneTwoThree(); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### Technical frame 2: generators are coroutines

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01705))_

> But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01704))_

```
const oneTwoThree = function () { let state = 'newborn'; return { next () { switch (state) { case 'newborn': state = 1; return {value: 1}; case 1: state = 2; return {value: 2} case 2: state = 3; return {value: 3} case 3: return {done: true }; } } } };
```
