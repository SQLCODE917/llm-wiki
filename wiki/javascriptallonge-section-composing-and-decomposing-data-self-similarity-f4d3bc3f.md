---
page_id: javascriptallonge-section-composing-and-decomposing-data-self-similarity-f4d3bc3f
page_kind: source
summary: Composing and Decomposing Data / Self-Similarity: 67 source-backed entries and 18 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-self-similarity-f4d3bc3f@8540ec35ce9b512dfa3e77aa5adc25fc
---

# Composing and Decomposing Data / Self-Similarity

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-6f7d7870]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4c0b6367]] - narrower source section: Composing and Decomposing Data / Self-Similarity / linear recursion
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-mapping-d1acef31]] - narrower source section: Composing and Decomposing Data / Self-Similarity / mapping
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-6afcd1fe]] - narrower source section: Composing and Decomposing Data / Self-Similarity / folding
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-summary-652fb6eb]] - narrower source section: Composing and Decomposing Data / Self-Similarity / summary

## Statements

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 60 _(javascriptallonge.pdf (source-range-7239e085-00883))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-7239e085-00884))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-7239e085-00885))_
- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-7239e085-00886))_
- But we can also define a list by describing a rule for building lists. One of the simplest, and longeststanding in computer science, is to say that a list is: _(javascriptallonge.pdf (source-range-7239e085-00887))_
- Consists of an element concatenated with a list . _(javascriptallonge.pdf (source-range-7239e085-00889))_
- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-7239e085-00890))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-7239e085-00892))_
- Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already? _(javascriptallonge.pdf (source-range-7239e085-00897))_
- 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0 , but we are doing backflips to keep this within a very small and contrived playground. _(javascriptallonge.pdf (source-range-7239e085-00898))_
- We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-7239e085-00901))_
- Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-7239e085-00904))_
- If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-7239e085-00901))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-7239e085-00904))_

## Statements by subsection

### Composing and Decomposing Data / Self-Similarity / linear recursion

- There is more to recursive solutions that simply functions that invoke themselves. Recursive algorithms follow the 'divide and conquer' strategy for solving a problem: _(javascriptallonge.pdf (source-range-7239e085-00910))_
- When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-7239e085-00914))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- This simpler form of 'divide and conquer' is called linear recursion . It's very useful and simple to understand. Let's take another example. Sometimes we want to flatten an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays. 62 _(javascriptallonge.pdf (source-range-7239e085-00916))_
- We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us: _(javascriptallonge.pdf (source-range-7239e085-00917))_
- The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. _(javascriptallonge.pdf (source-range-7239e085-00919))_
- 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. Unfolds can be thought of a 'path' through a data structure, and flattening a tree is equivalent to a depth-first traverse. _(javascriptallonge.pdf (source-range-7239e085-00921))_
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-7239e085-00923))_
- Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- This simpler form of 'divide and conquer' is called linear recursion . _(javascriptallonge.pdf (source-range-7239e085-00916))_

### Composing and Decomposing Data / Self-Similarity / mapping

- Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let's write our own using linear recursion. _(javascriptallonge.pdf (source-range-7239e085-00925))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-7239e085-00930))_
- Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-7239e085-00933))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-7239e085-00930))_

### Composing and Decomposing Data / Self-Similarity / folding

- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-7239e085-00936))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-7239e085-00943))_
- Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-7239e085-00945))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-7239e085-00949))_

### Composing and Decomposing Data / Self-Similarity / summary

- Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized cases of mapping and folding are especially useful and can be used to build other functions. And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-7239e085-00952))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00891))_

```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

### Technical frame 2: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00895))_

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

### Technical frame 3: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00896))_

```
isEmpty([])
//=> true
isEmpty([0])
//=> false
isEmpty([[]])
//=> false
```

### Technical frame 4: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00900))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: // ???
```

### Technical frame 5: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00902))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
Let’s try it!
length([])
//=> 0
length(["foo"])
//=> 1
length(["foo", "bar", "baz"])
```

### Technical frame 6: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00903))_

```
//=> 3
```

### Technical frame 7: Composing and Decomposing Data / Self-Similarity / linear recursion

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00919))_

> The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00918))_

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

### Technical frame 8: Composing and Decomposing Data / Self-Similarity / linear recursion

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00923))_

> Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00922))_

```
const flatten = ([first, ...rest]) => {
if (first === undefined) {
return [];
}
else if (!Array.isArray(first)) {
return [first, ...flatten(rest)];
}
else {
return [...flatten(first), ...flatten(rest)];
}
}
flatten(["foo", [3, 4, []]])
//=> ["foo",3,4]
```

### Technical frame 9: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00927))_

```
const squareAll = ([first, ...rest]) => first === undefined
? []
: [first * first, ...squareAll(rest)\
];
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 10: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00929))_

```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 11: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00932))_

```
const mapWith = (fn, array) => // ...
```

### Technical frame 12: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00934))_

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
mapWith((x) => !!x, [null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 13: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00937))_

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 14: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00942))_

```
const foldWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldWith(fn, terminalValue, rest));
```

### Technical frame 15: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00944))_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 16: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00946))_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 17: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00948))_

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\
], array),
squareAll = (array) => mapWith((x) => x * x, array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 18: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00950))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```
