---
page_id: javascriptallonge-section-we-ll-keep-it-simple-generators-are-coroutines-a23babe6
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / generators are coroutines: 24 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-generators-are-coroutines-a23babe6@2f2831bb5750dcfea5dd8eada95a305d
---

# We'll keep it simple: / generators are coroutines

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:

## Statements

- This is where generators behave very, very differently from ordinary functions. What happens semantically ? _(javascriptallonge.pdf (source-range-7239e085-01679))_
- The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-7239e085-01681))_
- When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-7239e085-01682))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-7239e085-01686))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-7239e085-01687))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-7239e085-01698))_
- This behaviour is not unique to JavaScript, generators are called coroutines 92 in other languages: _(javascriptallonge.pdf (source-range-7239e085-01700))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-7239e085-01701))_
- Instead of thinking of there being on execution context, we can imagine that there are two execution contexts. With an iterator, we can call them the producer and the consumer . The iterator is the producer, and the code that iterates over it is the consumer. When the consumer calls .next() , it 'suspends' and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next() . _(javascriptallonge.pdf (source-range-7239e085-01702))_
- Of course, generators need not be implemented exactly as coroutines. For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-7239e085-01704))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-7239e085-01706))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-7239e085-01701))_
- For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-7239e085-01704))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-7239e085-01706))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / generators are coroutines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01706))_

> But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01705))_

<a id="atom-technical-atom-e0bca2d9e767995c"></a>

```
const oneTwoThree = function () {
let state = 'newborn';
return {
next () {
switch (state) {
case 'newborn':
state = 1;
return {value: 1};
case 1:
state = 2;
return {value: 2}
case 2:
state = 3;
return {value: 3}
case 3:
return {done: true};
}
}
}
};
```
