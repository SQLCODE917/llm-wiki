---
page_id: javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation: / Functional Iterators: 57 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b@1e621711262ca19f7dc232f6922a01c8
---

# Yes. Consider this variation: / Functional Iterators

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-b8b28d41]] - broader source section: Yes. Consider this variation:
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-bonus-6b4a06d7]] - narrower source section: Yes. Consider this variation: / Functional Iterators / bonus
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-caveat-c90295dd]] - narrower source section: Yes. Consider this variation: / Functional Iterators / caveat
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-iterating-c8ddd51e]] - narrower source section: Yes. Consider this variation: / Functional Iterators / iterating
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-unfolding-and-laziness-bcf7ec6a]] - narrower source section: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

### Topics

- [[javascriptallonge-functional-iterator]] - topic hub: opens the topic page for Functional Iterator

### Other

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-4c177971]] - same source heading: another source section with the same heading, Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

## Statements

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-7239e085-01276))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-7239e085-01278))_
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-7239e085-01280))_
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-7239e085-01283))_
- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-7239e085-01276))_

## Statements by subsection

### Yes. Consider this variation: / Functional Iterators / iterating

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-7239e085-01285))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-7239e085-01286))_
- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-7239e085-01288))_
- Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient: _(javascriptallonge.pdf (source-range-7239e085-01291))_
- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-7239e085-01294))_
- We can write a different iterator for a different data structure. Here's one for linked lists: _(javascriptallonge.pdf (source-range-7239e085-01295))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-7239e085-01291))_

### Yes. Consider this variation: / Functional Iterators / unfolding and laziness

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-7239e085-01299))_
- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-7239e085-01303))_
- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_
- How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-7239e085-01309))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-7239e085-01312))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-7239e085-01314))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-7239e085-01303))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_

### Yes. Consider this variation: / Functional Iterators / bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-7239e085-01316))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-7239e085-01319))_
- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-7239e085-01321))_
- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-7239e085-01316))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-7239e085-01319))_

### Yes. Consider this variation: / Functional Iterators / caveat

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-7239e085-01323))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-7239e085-01324))_
