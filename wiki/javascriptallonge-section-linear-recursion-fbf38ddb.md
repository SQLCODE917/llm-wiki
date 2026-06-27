---
page_id: javascriptallonge-section-linear-recursion-fbf38ddb
page_kind: source
summary: **linear recursion**: 15 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-linear-recursion-fbf38ddb@ec955758a4149095a91b5f23c11c82da
---

# **linear recursion**

From [[javascriptallonge]].

## Statements

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
