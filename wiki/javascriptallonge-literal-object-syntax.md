---
page_id: javascriptallonge-literal-object-syntax
page_kind: source
summary: Summary of literal object syntax in JavaScriptAllonge.
sources: raw/javascriptallonge.pdf p.133-136
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day. Two objects created with separate evaluations have differing identities, just like arrays. Values contained within an object work just like values contained within an array, we access them by reference to the original. Names needn't be alphanumeric strings. For anything else, enclose the label in quotes. If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values. Expressions can be used for keys as well. All containers can contain any value, including functions or other containers, like a fat arrow function. Or proper functions. Or named function expressions. It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords.

## Key supported claims

- JavaScript has a literal syntax for creating objects (raw/javascriptallonge.pdf p.133-136).
- Values contained within an object work just like values contained within an array, we access them by reference to the original: (raw/javascriptallonge.pdf p.133-136).
- Two objects created with separate evaluations have differing identities, just like arrays: (raw/javascriptallonge.pdf p.133-136).
