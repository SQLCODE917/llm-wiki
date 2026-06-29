---
page_id: javascriptallonge-section-array-literals-83ae8bb8
page_kind: source
summary: array literals: 13 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-array-literals-83ae8bb8@02e34847a87287b4937e272c930cafc7
---

# array literals

From [[javascriptallonge]].

## Statements

- JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: _(javascriptallonge.pdf (source-range-8eb13d6b-00820))_
- We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional: _(javascriptallonge.pdf (source-range-8eb13d6b-00822))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-8eb13d6b-00828))_
- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-8eb13d6b-00831))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-8eb13d6b-00828))_

## Technical atoms

### Technical frame 1: array literals

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00822))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00821))_

```
[] //=> []
```

### Technical frame 2: array literals

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00823))_

```
[1] //=> [1] [2, 3, 4] //=> [2,3,4]
```

### Technical frame 3: array literals

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00825))_

```
[ 2, 3, 2 + 2 ] //=> [2,3,4]
```

### Technical frame 4: array literals

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00827))_

```
[[[[[]]]]]
```

### Technical frame 5: array literals

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00830))_

```
const wrap = (something) => [something]; wrap("lunch") //=> ["lunch"]
```

### Technical frame 6: array literals

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00832))_

```
[] === [] //=> false [2 + 2] === [2 + 2] //=> false const array_of_one = () => [1]; array_of_one() === array_of_one() //=> false
```
