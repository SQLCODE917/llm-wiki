---
page_id: javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4c0b6367
page_kind: source
summary: Composing and Decomposing Data / Self-Similarity / linear recursion: 17 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4c0b6367@ffeb491e6e80d0249f12c44a7b8eeb57
---

# Composing and Decomposing Data / Self-Similarity / linear recursion

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-f4d3bc3f]] - broader source section: Composing and Decomposing Data / Self-Similarity

## Statements

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

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Self-Similarity / linear recursion

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00919))_

> The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00918))_

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

### Technical frame 2: Composing and Decomposing Data / Self-Similarity / linear recursion

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
