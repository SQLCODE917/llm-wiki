---
page_id: javascriptallonge-section-self-similarity-8316c798
page_kind: source
summary: **Self-Similarity**: 25 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-self-similarity-8316c798@4e881b415606ff207ae787dff06c1d53
---

# **Self-Similarity**

From [[javascriptallonge]].

## Statements

- Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[60] _(javascriptallonge.pdf (source-range-83ecb080-01297))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01298))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01299))_
- Let’s be more specific. _(javascriptallonge.pdf (source-range-83ecb080-01300))_
- Some data structures, like lists, can obviously be seen as a collection of items. _(javascriptallonge.pdf (source-range-83ecb080-01300))_
- Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-83ecb080-01300))_
- But we can also define a list by describing a rule for building lists. _(javascriptallonge.pdf (source-range-83ecb080-01301))_
- The first rule is simple: [] is a list. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- We can express that using a spread. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- Given an element e and a list list, [e, ...list] is a list. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-83ecb080-01306))_
- > 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. _(javascriptallonge.pdf (source-range-83ecb080-01315))_
- If only there was a function we could call… Like length! _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- We need something for when the array isn’t empty. _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- Well, the length of first is 1, there’s just one element at the front. _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- If only there was a function we could call… Like length! _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- Our length function is _recursive_ , it calls itself. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-01325))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01311))_

> For the purpose of this exploration, we will presume the following:[61]

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01312))_

> **const** isEmpty = ([first, ...rest]) => first === **undefined** ;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01311))_

> For the purpose of this exploration, we will presume the following:[61]

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01313))_

> isEmpty([]) _//=> true_ isEmpty([0]) _//=> false_ isEmpty([[]]) _//=> false_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01319))_

> First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01320))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01319))_

> First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01322))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01323, source-range-83ecb080-01325))_

> Let’s try it! Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01324))_

> length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_
