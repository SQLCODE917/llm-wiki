---
page_id: javascriptallonge-code
page_kind: concept
summary: Code: 17 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-code@39a8a07422e524d2fa5db3ae1e19969b
---

# Code

What [[javascriptallonge]] covers about code:

## Statements

- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00192))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- This code does _not_ name a function: **const** repeat = (str) => str + str _(javascriptallonge.pdf (source-range-83ecb080-00518))_
- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00554))_
- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). _(javascriptallonge.pdf (source-range-83ecb080-00584))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-83ecb080-00718))_
- The purpose of your own code is to get things done. _(javascriptallonge.pdf (source-range-83ecb080-01211))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01249))_
- All the summing code needs to know is to add eachIteration.value. _(javascriptallonge.pdf (source-range-83ecb080-01288))_
- With this code, we make a POJO that has done and value keys. _(javascriptallonge.pdf (source-range-83ecb080-01288))_
- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-01319))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-83ecb080-01556))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-01719))_
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. _(javascriptallonge.pdf (source-range-83ecb080-01796))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00187, source-range-83ecb080-00192))_

> One of the most oft-repeated examples is this: > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00190))_

> - 1.0 + 1.0 + 1.0 _//=> 3_ However:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00192))_

> > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00195))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_


## Related pages

- [[javascriptallonge-javascript]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-node]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-follow]] - shared statements (3 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements (2 shared statement(s))
- [[javascriptallonge-language]] - shared statements (2 shared statement(s))
- [[javascriptallonge-write]] - shared statements (2 shared statement(s))
- [[javascriptallonge-combinator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements (1 shared statement(s))
- [[javascriptallonge-javascript-allong-and]] - shared statements (1 shared statement(s))
- [[javascriptallonge-partial-application]] - shared statements (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))
- [[javascriptallonge-programmer]] - shared statements (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements (1 shared statement(s))
- [[javascriptallonge-rule]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
