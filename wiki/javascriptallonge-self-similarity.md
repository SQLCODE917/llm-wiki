---
page_id: javascriptallonge-self-similarity
page_kind: concept
summary: Self-Similarity: 45 statement(s) and 19 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-self-similarity@b5d5a440235e598d41a24e3a413bb6b5
---

# Self-Similarity

What [[javascriptallonge]] covers about self-similarity:

## Statements

- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- > 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. _(javascriptallonge.pdf (source-range-83ecb080-01315))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
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

## Technical atoms

> Context: For the purpose of this exploration, we will presume the following:[61]
_(context: javascriptallonge.pdf (source-range-83ecb080-01311))_

> **const** isEmpty = ([first, ...rest]) => first === **undefined** ;
_(source: javascriptallonge.pdf (source-range-83ecb080-01312))_

> Context: For the purpose of this exploration, we will presume the following:[61]
_(context: javascriptallonge.pdf (source-range-83ecb080-01311))_

> isEmpty([]) _//=> true_ isEmpty([0]) _//=> false_ isEmpty([[]]) _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01313))_

> Context: First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:
_(context: javascriptallonge.pdf (source-range-83ecb080-01319))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_
_(source: javascriptallonge.pdf (source-range-83ecb080-01320))_

> Context: First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:
_(context: javascriptallonge.pdf (source-range-83ecb080-01319))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);
_(source: javascriptallonge.pdf (source-range-83ecb080-01322))_

> Context: Let’s try it! Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.
_(context: javascriptallonge.pdf (source-range-83ecb080-01323, source-range-83ecb080-01325))_

> length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01324))_

> Context: If we want to square each number in a list, we could write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01354))_

> **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01355))_


## Source

- [[javascriptallonge]]
