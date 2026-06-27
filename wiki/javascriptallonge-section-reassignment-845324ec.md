---
page_id: javascriptallonge-section-reassignment-845324ec
page_kind: source
summary: **Reassignment**: 13 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reassignment-845324ec@d494d0f4565bbfdf7e8257c9b4e1d0ad
---

# **Reassignment**

From [[javascriptallonge]].

## Statements

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-01758))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- What we want is a statement that works like const, but permits us to rebind variables. _(javascriptallonge.pdf (source-range-83ecb080-01766))_
- The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-83ecb080-01769))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- However, if we don’t shadow age with let, reassigning within the block changes the original: _(javascriptallonge.pdf (source-range-83ecb080-01780))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-83ecb080-01782))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01766))_

> Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01767))_

> **let** age = 52;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01766))_

> Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01768))_

> age = 53; age _//=> 53_
