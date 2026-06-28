---
page_id: javascriptallonge-section-basic-operations-on-iterables-8c9fdc37
page_kind: source
summary: Basic Operations on Iterables: 1 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-basic-operations-on-iterables-8c9fdc37@61788a3a60f907c34c6975caf33a0460
---

# Basic Operations on Iterables

From [[javascriptallonge]].

## Statements

- Served by the Pot: Collections

261

## **Basic Operations on Iterables**

Here are the operations we’ve defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given:

## **operations that transform one iterable into another**

**function** * mapWith(fn, iterable) { **for** ( **const** element **of** iterable) { **yield** fn(element); } } **function** * mapAllWith (fn, iterable) { **for** ( **const** element **of** iterable) { **yield** * fn(element); } } **function** * filterWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (!!fn(element)) **yield** element; } } **function** * compact (iterable) { **for** ( **const** element **of** iterable) { **if** (element != **null** ) **yield** element; } } **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield** fn(element); } } **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator](); iterator.next(); _(javascriptallonge.pdf (source-range-83ecb080-00328))_
