---
page_id: javascriptallonge-section-from-18741ea9
page_kind: source
summary: **from**: 12 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-from-18741ea9@28610a982198a573a183c38385f96bcd
---

# **from**

From [[javascriptallonge]].

## Statements

- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-02505))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-83ecb080-02508))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- We can do the same with our own collections. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- And if we assign a function to a property, we’ve created a method. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-83ecb080-02516))_

## Technical atoms

> Context: One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:
_(context: javascriptallonge.pdf (source-range-83ecb080-02508))_

> Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02509))_

> Stack3.from = **function** (iterable) { **const** stack = **this** ();
_(source: javascriptallonge.pdf (source-range-83ecb080-02512))_

> Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next();
_(source: javascriptallonge.pdf (source-range-83ecb080-02514))_

> Context: Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:
_(context: javascriptallonge.pdf (source-range-83ecb080-02516))_

> **const** numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
_(source: javascriptallonge.pdf (source-range-83ecb080-02517))_

> Context: Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:
_(context: javascriptallonge.pdf (source-range-83ecb080-02516))_

> Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ...
_(source: javascriptallonge.pdf (source-range-83ecb080-02518))_
