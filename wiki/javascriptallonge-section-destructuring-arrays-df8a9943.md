---
page_id: javascriptallonge-section-destructuring-arrays-df8a9943
page_kind: source
summary: **destructuring arrays**: 14 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-arrays-df8a9943@c0fe7b19cdfb5859bccafe5703b9d4c6
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

> Context: There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name:
_(context: javascriptallonge.pdf (source-range-83ecb080-01221))_

> **const** wrap = (something) => [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01222))_

> Context: Let’s expand it to use a block and an extra name:
_(context: javascriptallonge.pdf (source-range-83ecb080-01223))_

> **const** wrap = (something) => { **const** wrapped = [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01224))_

> Context: Let’s expand it to use a block and an extra name:
_(context: javascriptallonge.pdf (source-range-83ecb080-01223))_

> wrap("package") _//=> ["package"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01226))_

> Context: In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:
_(context: javascriptallonge.pdf (source-range-83ecb080-01228))_

> **const** unwrap = (wrapped) => { **const** [something] = wrapped;
_(source: javascriptallonge.pdf (source-range-83ecb080-01229))_

> Context: In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:
_(context: javascriptallonge.pdf (source-range-83ecb080-01228))_

> unwrap(["present"]) _//=> "present"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01231))_

> Context: The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element:
_(context: javascriptallonge.pdf (source-range-83ecb080-01232))_

> **const** surname = (name) => { **const** [first, last] = name; **return** last; }
_(source: javascriptallonge.pdf (source-range-83ecb080-01235))_

> surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01236))_

> Context: Destructuring can nest:
_(context: javascriptallonge.pdf (source-range-83ecb080-01238))_

> **const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation;
_(source: javascriptallonge.pdf (source-range-83ecb080-01239))_
