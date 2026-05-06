---
title: Iterators
type: concept
tags: []
status: draft
last_updated: 2026-05-06
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L9655-L9655
  - js-allonge:normalized:L5706-L5706
  - js-allonge:normalized:L7273-L7273
  - js-allonge:normalized:L8180-L8180
  - js-allonge:normalized:L8250-L8250
  - js-allonge:normalized:L8265-L8265
  - js-allonge:normalized:L8283-L8283
  - js-allonge:normalized:L8302-L8302
  - js-allonge:normalized:L8327-L8327
  - js-allonge:normalized:L8348-L8348
---
# Iterators

An iterator is an object that provides a sequence of values, typically through a `next()` method that returns an object with `done` and `value` properties.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| An iterator can be consumed by calling its next() method repeatedly until done is true. | "const { done, value } = iterator.next();" | `normalized:L9655` | [JavaScript Allonge](../sources/js-allonge.md) |
| A function can be defined to map an iterator with a provided function. | "const mapIteratorWith = (fn, iterator) =>" | `normalized:L5706` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterable object's first value can be accessed via its Symbol.iterator method. | "iterable[Symbol.iterator]().next().value;" | `normalized:L7273` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterable object's first value can be accessed via its Symbol.iterator method. | "iterable[Symbol.iterator]().next().value;" | `normalized:L8180` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterator can be obtained from an object by calling its Symbol.iterator method. | "const iterator = this[Symbol.iterator]();" | `normalized:L8250` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterator can be obtained from an object by calling its Symbol.iterator method. | "const iterator = this[Symbol.iterator]();" | `normalized:L8265` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterator can be obtained from an object by calling its Symbol.iterator method. | "const iterator = this[Symbol.iterator]();" | `normalized:L8283` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterator can be obtained from an object by calling its Symbol.iterator method. | "const iterator = this[Symbol.iterator]();" | `normalized:L8302` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterator can be obtained from an object by calling its Symbol.iterator method. | "const iterator = this[Symbol.iterator]();" | `normalized:L8327` | [JavaScript Allonge](../sources/js-allonge.md) |
| An iterator can be obtained from an object by calling its Symbol.iterator method. | "const iterator = this[Symbol.iterator]();" | `normalized:L8348` | [JavaScript Allonge](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allonge](../sources/js-allonge.md)