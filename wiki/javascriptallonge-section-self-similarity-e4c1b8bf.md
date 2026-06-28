---
page_id: javascriptallonge-section-self-similarity-e4c1b8bf
page_kind: source
summary: Self-Similarity: 27 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-self-similarity-e4c1b8bf@d2290c49142ead22a411da80d172ea65
---

# Self-Similarity

From [[javascriptallonge]].

## Statements

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 60 _(javascriptallonge.pdf (source-range-31a4cf47-00883))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-31a4cf47-00884))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-31a4cf47-00885))_
- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-31a4cf47-00886))_
- But we can also define a list by describing a rule for building lists. One of the simplest, and longeststanding in computer science, is to say that a list is: _(javascriptallonge.pdf (source-range-31a4cf47-00887))_
- Consists of an element concatenated with a list . _(javascriptallonge.pdf (source-range-31a4cf47-00889))_
- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-31a4cf47-00890))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-31a4cf47-00892))_
- Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already? _(javascriptallonge.pdf (source-range-31a4cf47-00897))_
- 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0 , but we are doing backflips to keep this within a very small and contrived playground. _(javascriptallonge.pdf (source-range-31a4cf47-00898))_
- We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-31a4cf47-00901))_
- Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-31a4cf47-00904))_
- If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-31a4cf47-00901))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

## Technical atoms

### Technical frame 1: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00891))_

```
[] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"]
```

### Technical frame 2: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00895))_

```
const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar"]; first //=> "foo" rest //=> ["bar"] const [first, ...rest] = ["foo", "bar", "baz"]; first //=> "foo" rest //=> ["bar","baz"] For the purpose of this exploration, we will presume the following: const isEmpty = ([first, ...rest]) => first === undefined ;
```

### Technical frame 3: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00896))_

```
isEmpty([]) //=> true isEmpty([0]) //=> false isEmpty([[]]) //=> false
```

### Technical frame 4: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00900))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : // ???
```

### Technical frame 5: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00902))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let's try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"])
```

### Technical frame 6: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00903))_

```
//=> 3
```
