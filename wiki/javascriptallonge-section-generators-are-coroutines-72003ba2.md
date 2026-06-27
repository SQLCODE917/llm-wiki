---
page_id: javascriptallonge-section-generators-are-coroutines-72003ba2
page_kind: source
summary: **generators are coroutines**: 26 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generators-are-coroutines-72003ba2@cc59de431ffc608389ad00157599dc7d
---

# **generators are coroutines**

From [[javascriptallonge]].

## Statements

- This is where generators behave very, very differently from ordinary functions. _(javascriptallonge.pdf (source-range-83ecb080-02617))_
- The iterator is in a nascent or “newborn” state. _(javascriptallonge.pdf (source-range-83ecb080-02619))_
- When we call interator.next(), the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02620))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02626))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02627))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02631))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02632))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02636))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02637))_
- There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-83ecb080-02638))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-83ecb080-02638))_
- This behaviour is not unique to JavaScript, generators are called coroutines[92] in other languages: _(javascriptallonge.pdf (source-range-83ecb080-02640))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- With an iterator, we can call them the _producer_ and the _consumer_ . _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- The iterator is the producer, and the code that iterates over it is the consumer. _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- Of course, generators need not be implemented exactly as coroutines. _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-02649))_

## Technical atoms

> Context: Here’s a generator that yields three numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-02610))_

> **const** oneTwoThree = **function** * () { **yield** 1; **yield** 2; **yield** 3; };
_(source: javascriptallonge.pdf (source-range-83ecb080-02613))_

> oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1}
_(source: javascriptallonge.pdf (source-range-83ecb080-02614))_

> **const** iterator = oneTwoThree();
_(source: javascriptallonge.pdf (source-range-83ecb080-02615))_
