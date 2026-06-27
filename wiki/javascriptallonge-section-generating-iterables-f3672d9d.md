---
page_id: javascriptallonge-section-generating-iterables-f3672d9d
page_kind: source
summary: **Generating Iterables**: 14 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generating-iterables-f3672d9d@afb10eee1745c2e03ba55d063940278a
---

# **Generating Iterables**

From [[javascriptallonge]].

## Statements

- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-02530))_
- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-02530))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- This seems blindingly obvious and simple. _(javascriptallonge.pdf (source-range-83ecb080-02532))_
- The Numbers iterable returns an object that updates a mutable variable, n, to deliver number after number. _(javascriptallonge.pdf (source-range-83ecb080-02536))_
- There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Then it waits for the next request. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- It waits until given a request, and then it returns exactly one item. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. _(javascriptallonge.pdf (source-range-83ecb080-02538))_
- We would _generate_ numbers. _(javascriptallonge.pdf (source-range-83ecb080-02541))_
- And magically, the numbers would pour forth. _(javascriptallonge.pdf (source-range-83ecb080-02541))_
- Well, there are some collections that are much easier to generate than to iterate over. _(javascriptallonge.pdf (source-range-83ecb080-02545))_

## Technical atoms

> Context: Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.
_(context: javascriptallonge.pdf (source-range-83ecb080-02531))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.
_(source: javascriptallonge.pdf (source-range-83ecb080-02532))_

> Context: Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. We usually just write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02538))_

> **let** n = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02539))_
