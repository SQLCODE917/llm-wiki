---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-c21c4915
page_kind: source
page_family: section-reference
summary: And also: / That Constant Coffee Craving / rebinding: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-c21c4915@fc4c4fe57d03afe0cc1e0c1ac98406ea
---

# And also: / That Constant Coffee Craving / rebinding

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-7d1b2fd1]] - broader source section: And also: / That Constant Coffee Craving

## Statements

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-7239e085-00496))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-7239e085-00497))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00496))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00495))_

<a id="atom-technical-atom-381b7cb3b61758cd"></a>

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```
