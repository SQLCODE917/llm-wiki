---
page_id: javascriptallonge-section-overcoming-limitations-6137780f
page_kind: source
summary: overcoming limitations: 6 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-overcoming-limitations-6137780f@b42c4f3c4df27177058261ccc4e349f1
---

# overcoming limitations

From [[javascriptallonge]].

## Statements

- That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function? _(javascriptallonge.pdf (source-range-31a4cf47-00735))_
- We sure can, by using the techniques from rightVariadic . Mind you, we can take advantage of modern JavaScript to simplify the code: _(javascriptallonge.pdf (source-range-31a4cf47-00736))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. _(javascriptallonge.pdf (source-range-31a4cf47-00739))_

## Technical atoms

### Technical frame 1: overcoming limitations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00735))_

> That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00734))_

```
const butLastAndLast = (...butLast, last) => [butLast, last];
```

### Technical frame 2: overcoming limitations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00739))_

> Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00737))_

```
const leftVariadic = (fn) => { if (fn.length < 1) { return fn; } else { return function (...args) { const gathered = args.slice(0, args.length - fn.length + 1), spread = args.slice(args.length - fn.length + 1); return fn.apply( this , [gathered].concat(spread)
```

### Technical frame 3: overcoming limitations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00739))_

> Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00738))_

```
); } } }; const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]); butLastAndLast('why', 'hello', 'there', 'little', 'droid') //=> [["why","hello","there","little"],"droid"]
```
