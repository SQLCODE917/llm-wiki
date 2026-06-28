---
page_id: javascriptallonge-section-mapping-e23f2810
page_kind: source
summary: mapping: 8 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mapping-e23f2810@d7f8db4287b5d44d2fec91e4b7f036d5
---

# mapping

From [[javascriptallonge]].

## Statements

- Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let's write our own using linear recursion. _(javascriptallonge.pdf (source-range-31a4cf47-00925))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-31a4cf47-00930))_
- Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-31a4cf47-00933))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-31a4cf47-00930))_

## Technical atoms

### Technical frame 1: mapping

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00927))_

```
const squareAll = ([first, ...rest]) => first === undefined ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### Technical frame 2: mapping

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00929))_

```
const truthyAll = ([first, ...rest]) => first === undefined ? [] : [!!first, ...truthyAll(rest)]; truthyAll([ null , true , 25, false , "foo"]) //=> [false,true,true,false,true]
```

### Technical frame 3: mapping

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00932))_

```
const mapWith = (fn, array) => // ...
```

### Technical frame 4: mapping

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00934))_

```
const mapWith = (fn, [first, ...rest]) => first === undefined ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] mapWith((x) => !!x, [ null , true , 25, false , "foo"]) //=> [false,true,true,false,true]
```
