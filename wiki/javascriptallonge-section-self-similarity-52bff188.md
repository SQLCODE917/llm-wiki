---
page_id: javascriptallonge-section-self-similarity-52bff188
page_kind: source
summary: Self-Similarity: 71 source-backed entries and 19 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-self-similarity-52bff188@cddbad3185df9c0c2d5e12fa73e4abfd
---

# Self-Similarity

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
- There is more to recursive solutions that simply functions that invoke themselves. _(javascriptallonge.pdf (source-range-83ecb080-01333))_
- When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-83ecb080-01337))_
- Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- This simpler form of “divide and conquer” is called _linear recursion_ . _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- This simpler form of “divide and conquer” is called _linear recursion_ . _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- We need a test for the terminal case. _(javascriptallonge.pdf (source-range-83ecb080-01340))_
- The usual “terminal case” will be that flattening an empty array will produce an empty array. _(javascriptallonge.pdf (source-range-83ecb080-01345))_
- The next terminal case is that if an element isn’t an array, we don’t flatten it, and can put it together with the rest of our solution directly. _(javascriptallonge.pdf (source-range-83ecb080-01345))_
- > 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. _(javascriptallonge.pdf (source-range-83ecb080-01347))_
- Unfolds can be thought of a “path” through a data structure, and flattening a tree is equivalent to a depth-first traverse. _(javascriptallonge.pdf (source-range-83ecb080-01347))_
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-83ecb080-01351))_
- JavaScript has a built-in function for this, but let’s write our own using linear recursion. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- Another common problem is applying a function to every element of an array. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- We can write it out using a ternary operator. _(javascriptallonge.pdf (source-range-83ecb080-01365))_
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-83ecb080-01365))_
- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-01369))_
- Let’s rewrite mapWith so that we can use it to sum squares. _(javascriptallonge.pdf (source-range-83ecb080-01378))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-83ecb080-01380))_
- We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-83ecb080-01382))_
- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-83ecb080-01382))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-83ecb080-01389))_
- Linear recursion is a basic building block of algorithms. _(javascriptallonge.pdf (source-range-83ecb080-01393))_
- Its specialized cases of mapping and folding are especially useful and can be used to build other functions. _(javascriptallonge.pdf (source-range-83ecb080-01393))_
- Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. _(javascriptallonge.pdf (source-range-83ecb080-01393))_
- And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-83ecb080-01393))_

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

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01354))_

> If we want to square each number in a list, we could write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01355))_

> **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01356))_

> And if we wanted to “truthify” each element in a list, we could write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01359))_

> **const** truthyAll = ([first, ...rest]) => first === **undefined**

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01361))_

> truthyAll([ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01363))_

> Given the signature:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01364))_

> **const** mapWith = (fn, array) => _// ..._

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01365))_

> We can write it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01367))_

> mapWith((x) => !!x, [ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01369))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01372))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01375))_

> There are two differences between sumSquares and our maps above:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01374))_

> sumSquares([1, 2, 3, 4, 5]) _//=> 55_

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01378))_

> Let’s rewrite mapWith so that we can use it to sum squares.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01379))_

> **const** foldWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldWith(fn, terminalValue, rest));

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01380))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01381))_

> foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) _//=> 55_

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01382))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01383))_

> **const** squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01384))_

> And if we like, we can write mapWith using foldWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01387))_

> **const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array);

### Technical atom 17

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01388))_

> squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01389))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01390))_

> **const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array);

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01389))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01391))_

> length([1, 2, 3, 4, 5]) _//=> 5_
