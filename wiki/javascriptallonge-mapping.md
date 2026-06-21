---
page_id: javascriptallonge-mapping
page_kind: source
summary: Chapter on mapping in JavaScript Allongé
sources: raw/javascriptallonge.pdf p.113-114
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers the concept of mapping in JavaScript, demonstrating how to apply a function to every element of an array using linear recursion.

## Key supported claims

- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again (raw/javascriptallonge.pdf p.113-114).
- Wecanwrite it out using a ternary operator (raw/javascriptallonge.pdf p.113-114).
- [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] mapWith((x) => !!x, [ null , true , 25, false , "foo"]) //=> [false,true,true,false,true] (raw/javascriptallonge.pdf p.113-114).
