---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-a8dcb708
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-a8dcb708@fcae3df48a01f9d161f83b8aa75d615a
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-c1f61fb6]] - broader source section: Composing and Decomposing Data / Arrays and Destructuring Arguments

## Statements

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-7239e085-00834))_
- As we can see, JavaScript Arrays are zero-based 56 . _(javascriptallonge.pdf (source-range-7239e085-00836))_
- We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind? _(javascriptallonge.pdf (source-range-7239e085-00837))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00836))_

> As we can see, JavaScript Arrays are zero-based 56 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00835))_

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

### Technical frame 2: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00837))_

> We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00839))_

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```
