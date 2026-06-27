---
page_id: javascriptallonge-section-destructuring-arrays-df8a9943
page_kind: source
summary: **destructuring arrays**: 14 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-arrays-df8a9943@ca201b5b0df2b20367fbdc13116f369a
---

# **destructuring arrays**

From [[javascriptallonge]].

## Statements

- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- The line const wrapped = [something]; is interesting. _(javascriptallonge.pdf (source-range-83ecb080-01227))_
- In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-83ecb080-01228))_
- The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. _(javascriptallonge.pdf (source-range-83ecb080-01232))_
- We could do the same thing with (name) => name[1], but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-83ecb080-01237))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01221))_

> There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01222))_

> **const** wrap = (something) => [something];

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01223))_

> Let’s expand it to use a block and an extra name:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01224))_

> **const** wrap = (something) => { **const** wrapped = [something];

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01223))_

> Let’s expand it to use a block and an extra name:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01226))_

> wrap("package") _//=> ["package"]_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01228))_

> In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01229))_

> **const** unwrap = (wrapped) => { **const** [something] = wrapped;

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01228))_

> In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01231))_

> unwrap(["present"]) _//=> "present"_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01232))_

> The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01235))_

> **const** surname = (name) => { **const** [first, last] = name; **return** last; }

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01236))_

> surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01238))_

> Destructuring can nest:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01239))_

> **const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation;
