---
page_id: javascriptallonge-section-destructuring-arrays-4bb0db7d
page_kind: source
summary: destructuring arrays: 11 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-arrays-4bb0db7d@790340aa48a5b51da7089b72dba4f05b
---

# destructuring arrays

From [[javascriptallonge]].

## Statements

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [ , expressions, , and ] . Here's an example of an array literal that uses a name: _(javascriptallonge.pdf (source-range-31a4cf47-00841))_
- The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string. _(javascriptallonge.pdf (source-range-31a4cf47-00844))_
- In JavaScript, we can actually reverse the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-31a4cf47-00845))_
- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-31a4cf47-00847))_
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-31a4cf47-00849))_
- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-31a4cf47-00841))_

## Technical atoms

### Technical frame 1: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00844))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00842))_

```
const wrap = (something) => [something]; Let's expand it to use a block and an extra name: wrapped = [something];
```

### Technical frame 2: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00844))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00843))_

```
const wrap = (something) => { const return wrapped; } wrap("package") //=> ["package"]
```

### Technical frame 3: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00847))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00846))_

```
const unwrap = (wrapped) => { const [something] = wrapped; return something; } unwrap(["present"]) //=> "present"
```

### Technical frame 4: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00848))_

```
const surname = (name) => { const [first, last] = name; return last; } surname(["Reginald", "Braithwaite"]) //=> "Braithwaite"
```

### Technical frame 5: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00851))_

```
const description = (nameAndOccupation) => { const [[first, last], occupation] = nameAndOccupation; return ` ${ first } is a ${ occupation } `; } description([["Reginald", "Braithwaite"], "programmer"]) //=> "Reginald is a programmer"
```
