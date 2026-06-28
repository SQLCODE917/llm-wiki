---
page_id: javascriptallonge-length
page_kind: concept
summary: Length: 7 statement(s) and 20 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-length@45a06a2a6d744bf90d2955654f256dd7
---

# Length

What [[javascriptallonge]] covers about length:

## Statements

- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-83ecb080-01444))_
- Well, the length of first is 1, there’s just one element at the front. _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- Our length function is _recursive_ , it calls itself. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-83ecb080-01389))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01319))_

> First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01320))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01319))_

> First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01322))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01323, source-range-83ecb080-01325))_

> Let’s try it! Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01324))_

> length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01369))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01372))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01389))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01390))_

> **const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array);

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01389))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01391))_

> length([1, 2, 3, 4, 5]) _//=> 5_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01422, source-range-83ecb080-01424))_

> That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01423))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01430))_

> The obvious solution is push the 1 + work into the call to length. Here’s our first cut:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01431))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01437))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01439))_

> **const** length = (n) => lengthDelaysWork(n, 0);

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01444))_

> This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01447))_

> **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) =>

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01655))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01656))_

> length(OneTwoThree) _//=> 3_

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02033))_

> For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02036))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02119))_

> We can write length and mapWith functions over it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02122))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair));

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02140))_

> We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here’s length again:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02141))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02142))_

> Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. Instead of writing length(list) and examining a list, we’ll write something like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02143))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02185))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02186))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02191))_

> **const** length = (node, delayed = 0) =>

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02192))_

> node === EMPTY


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (3 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms (1 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms (1 shared atom(s))

## Source

- [[javascriptallonge]]
