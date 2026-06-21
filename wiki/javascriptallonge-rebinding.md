---
page_id: javascriptallonge-rebinding
page_kind: source
summary: Chapter on rebinding in JavaScript Allongé
sources: raw/javascriptallonge.pdf p.60-61
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers rebinding in JavaScript, specifically discussing how names bound with const cannot be rebound, but can be shadowed in new scopes.

## Key supported claims

- By default, JavaScript permits us to rebind new values to names bound with a parameter. (raw/javascriptallonge.pdf p.60-61)
- The line n = n -2; rebinds a new value to the name n. (raw/javascriptallonge.pdf p.60-61)
- JavaScript does not permit us to rebind a name that has been bound with const. (raw/javascriptallonge.pdf p.60-61)
- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. (raw/javascriptallonge.pdf p.60-61)
