---
page_id: javascriptallonge-section-and-also-magic-names-the-function-keyword-b8eb1a25
page_kind: source
page_family: section-reference
summary: And also: / Magic Names / the function keyword: 9 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-magic-names-the-function-keyword-b8eb1a25@54fe2f9c066421578c5b24c0c79ca5a1
---

# And also: / Magic Names / the function keyword

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-magic-names-ced4852f]] - broader source section: And also: / Magic Names

### Topics

- [[javascriptallonge-function-keyword]] - topic hub: opens the topic page for Function Keyword

### Other

- [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-5d8f2243]] - same source heading: another source section with the same heading, And also: / Naming Functions / the function keyword

## Statements

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-7239e085-00607))_
- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-7239e085-00608))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-7239e085-00617))_

## Technical atoms

### Technical atom 1

<a id="atom-technical-atom-40032b1d8caeb152"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00612))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00613))_

```text
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

</details>
