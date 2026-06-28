---
page_id: javascriptallonge-section-plain-old-javascript-objects-00921001
page_kind: source
summary: Plain Old JavaScript Objects: 14 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-00921001@500a8b4e5770f89c83f70cb54a866604
---

# Plain Old JavaScript Objects

From [[javascriptallonge]].

## Statements

- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list: _(javascriptallonge.pdf (source-range-31a4cf47-01061))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-31a4cf47-01064))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-31a4cf47-01066))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-31a4cf47-01067))_
- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-31a4cf47-01068))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-31a4cf47-01069))_
- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-31a4cf47-01061))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-31a4cf47-01064))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-31a4cf47-01067))_

## Technical atoms

### Technical frame 1: Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01064))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01062))_

```
const remember = ["the milk", "the coffee beans", "the biscotti"]; And they can be used to store heterogeneous things in various levels of structure:
```

### Technical frame 2: Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01064))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01063))_

```
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### Technical frame 3: Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01066))_

> Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01065))_

```
const NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1; const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
```
