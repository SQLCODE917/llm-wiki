---
page_id: javascriptallonge-code
page_kind: concept
summary: Code: 17 statement(s) and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-code@5f37774d6229b37a17c5b98660a41627
---

# Code

What [[javascriptallonge]] covers about code:

## Statements

- If a particular codebase is written with lots of helper functions that place the subject first, like this: _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-83ecb080-00094))_
- But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). _(javascriptallonge.pdf (source-range-83ecb080-00805))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-83ecb080-00840))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-83ecb080-01021))_
- The purpose of your own code is to get things done. _(javascriptallonge.pdf (source-range-83ecb080-01845))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- All the summing code needs to know is to add eachIteration.value. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- With this code, we make a POJO that has done and value keys. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-02032))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. _(javascriptallonge.pdf (source-range-83ecb080-02788))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00086))_

> Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00087))_

> **const** mapWith = (iterable, fn) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **yield** fn(element); } } });

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00232))_

> > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00235))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00840, source-range-83ecb080-00843))_

> Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00841))_

> _.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00843))_

> This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00844))_

> **const** squareAll = (array) => map(array, (n) => n * n);

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01007))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01008))_

> **var** something = isSomething(value) ? doesntCheckForSomething(value) : value;

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02178))_

> The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02179))_

> **const** first = K, second = K(I), pair = (first) => (second) => { **const** pojo = {first, second};

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02178))_

> The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02180))_

> **return** (selector) => selector(pojo.first)(pojo.second); };

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02178))_

> The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02181))_

> **const** latin = pair("primus")("secundus");

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02185))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02186))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02191))_

> **const** length = (node, delayed = 0) =>

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02192))_

> node === EMPTY


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-language]] - shared statements (2 shared statement(s))
- [[javascriptallonge-write]] - shared statements (2 shared statement(s))
- [[javascriptallonge-combinator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
