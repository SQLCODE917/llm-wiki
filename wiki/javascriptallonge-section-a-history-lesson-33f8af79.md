---
page_id: javascriptallonge-section-a-history-lesson-33f8af79
page_kind: source
summary: **a history lesson**: 6 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-history-lesson-33f8af79@d541f4f4bd54b879a1a048c422427436
---

# **a history lesson**

From [[javascriptallonge]].

## Statements

- In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-83ecb080-01050))_
- “Ye” in “Ye Olde,” was not actually spelled with a “Y” in days of old, it was spelled with a thorn, and is pronounced “the.” Another word, “Ye” in “Ye of little programming faith,” is pronounced “ye,” but it’s a different word altogether. _(javascriptallonge.pdf (source-range-83ecb080-01053))_
- This is a _right-variadic function_ , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-83ecb080-01060))_

## Technical atoms

> Context: In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory:
_(context: javascriptallonge.pdf (source-range-83ecb080-01050))_

> **var** __slice = Array.prototype.slice;
_(source: javascriptallonge.pdf (source-range-83ecb080-01051))_

> Context: We don’t need rightVariadic any more, because instead of:
_(context: javascriptallonge.pdf (source-range-83ecb080-01056))_

> **var** firstAndButFirst = rightVariadic( **function** test (first, butFirst) { **return** [first, butFirst] });
_(source: javascriptallonge.pdf (source-range-83ecb080-01057))_

> Context: We now simply write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01058))_

> **const** firstAndButFirst = (first, ...butFirst) => [first, butFirst];
_(source: javascriptallonge.pdf (source-range-83ecb080-01059))_
