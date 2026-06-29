---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-2857d963
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: 13 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-2857d963@ef3ae95a1e63a4c95fa8b0f12e233f43
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-c1f61fb6]] - broader source section: Composing and Decomposing Data / Arrays and Destructuring Arguments

## Statements

- JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: _(javascriptallonge.pdf (source-range-7239e085-00820))_
- We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional: _(javascriptallonge.pdf (source-range-7239e085-00822))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-7239e085-00828))_
- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-7239e085-00831))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-7239e085-00828))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00822))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00821))_

```
[]
//=> []
```

### Technical frame 2: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00823))_

```
[1]
//=> [1]
[2, 3, 4]
//=> [2,3,4]
```

### Technical frame 3: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00825))_

```
[ 2,
3,
2 + 2
]
//=> [2,3,4]
```

### Technical frame 4: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00827))_

```
[[[[[]]]]]
```

### Technical frame 5: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00830))_

```
const wrap = (something) => [something];
wrap("lunch")
//=> ["lunch"]
```

### Technical frame 6: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00832))_

```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```
