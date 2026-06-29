---
page_id: javascriptallonge-section-rebinding-f33b2093
page_kind: source
summary: rebinding: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-rebinding-f33b2093@fc9e9cf230c960aea618e8c108fb651b
---

# rebinding

From [[javascriptallonge]].

## Statements

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-8eb13d6b-00499))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-8eb13d6b-00500))_

## Technical atoms

### Technical frame 1: rebinding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00499))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00496))_

```
const evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { n = n - 2; return evenStevens(n); } } evenStevens(42) //=> true
```

### Technical frame 2: rebinding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00499))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00498))_

```
evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { return evenStevens(n - 2); } } //=> ERROR, evenStevens is read-only
```
