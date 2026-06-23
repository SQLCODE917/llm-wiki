---
page_id: javascriptallonge-garbage-garbage-everywhere
page_kind: source
summary: Garbage, Garbage Everywhere from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.126-128
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains tail‑call recursion for array mapping, the memory cost of temporary arrays, and contrasts JavaScript arrays with Lisp linked lists, noting possible performance drawbacks.

## Key supported claims

- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using (raw/javascriptallonge.pdf p.126-128).
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another (raw/javascriptallonge.pdf p.126-128).
- Lather, rinse, repeat: Every time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend (raw/javascriptallonge.pdf p.126-128).
- It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made (raw/javascriptallonge.pdf p.126-128).

## Technical details

### `technical-atom-bb88808ab8488fcf` code

Citation: (raw/javascriptallonge.pdf p.126-128)

```javascript
const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined ? prepend : mapWith(fn, rest, [...prepend, fn(first)]); mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-41b060c77014dd3f` procedure

Citation: (raw/javascriptallonge.pdf p.126-128)

To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith .

### `technical-atom-5d1ebb19d843b288` procedure

Citation: (raw/javascriptallonge.pdf p.126-128)

Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend .

### `technical-atom-426a230840ec0066` exception

Citation: (raw/javascriptallonge.pdf p.126-128)

Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

### `technical-atom-ebf22f50d193ae3e` procedure

Citation: (raw/javascriptallonge.pdf p.126-128)

Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

### `technical-atom-ff30dd9aed90995c` exception

Citation: (raw/javascriptallonge.pdf p.126-128)

64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made.
