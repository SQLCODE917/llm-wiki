---
page_id: javascriptallonge-return
page_kind: concept
summary: Return: 11 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return@cf10e9a21162a7c50083980c8eedf5be
---

# Return

What [[javascriptallonge]] covers about return:

## Statements

- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-01612))_
- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00607))_
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01289))_
- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-01363))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-83ecb080-01712))_
- We’ve writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-83ecb080-01741))_
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. _(javascriptallonge.pdf (source-range-83ecb080-01796))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00242))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00245))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00246))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01744))_

> Here’s a first crack at a function that returns an iterable object for iterating over trees:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01747))_

> But if you can write it as a simple generator, write it as a simple generator.


## Related pages

- [[javascriptallonge-function-return-value]] - narrower topic (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (4 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-argument]] - shared statements (3 shared statement(s))
- [[javascriptallonge-alway]] - shared statements (1 shared statement(s))
- [[javascriptallonge-block]] - shared statements (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function-decorator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-iterable]] - shared statements (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements (1 shared statement(s))
- [[javascriptallonge-partial-application]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
