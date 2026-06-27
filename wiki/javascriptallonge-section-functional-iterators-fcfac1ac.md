---
page_id: javascriptallonge-section-functional-iterators-fcfac1ac
page_kind: source
summary: Functional Iterators: 65 source-backed entries and 25 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functional-iterators-fcfac1ac@8384e0b665294a572ef1703b46530f8a
---

# Functional Iterators

From [[javascriptallonge]].

## Statements

- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- Perhaps we could extract both of those things. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable. _(javascriptallonge.pdf (source-range-83ecb080-01949))_
- We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-83ecb080-01956))_
- Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-83ecb080-01960))_
- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. _(javascriptallonge.pdf (source-range-83ecb080-01960))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-83ecb080-01961))_
- And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0. _(javascriptallonge.pdf (source-range-83ecb080-01963))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- We can put those into a POJO (a Plain Old JavaScript Object). _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- All the summing code needs to know is to add eachIteration.value. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- With this code, we make a POJO that has done and value keys. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- Now this is something else. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- We can write a different iterator for a different data structure. _(javascriptallonge.pdf (source-range-83ecb080-01977))_
- When they iterate over an array or linked list, they are traversing something that is already there. _(javascriptallonge.pdf (source-range-83ecb080-01987))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- This business of going on forever has some drawbacks. _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We’ll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-83ecb080-02003))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-83ecb080-02009))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-83ecb080-02013))_
- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-02020))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-02020))_
- And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- There are some important implications of stateful functions. _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-02025))_

## Technical atoms

> Context: Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01933))_

> **const** arraySum = ([first, ...rest], accumulator = 0) => first === **undefined** ? accumulator : arraySum(rest, first + accumulator)
_(source: javascriptallonge.pdf (source-range-83ecb080-01934))_

> Context: Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01933))_

> arraySum([1, 4, 9, 16, 25]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01935))_

> Context: As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. So we can separate them using fold:
_(context: javascriptallonge.pdf (source-range-83ecb080-01936))_

> **const** arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01938))_

> Context: Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let’s rearrange our code a bit:
_(context: javascriptallonge.pdf (source-range-83ecb080-01941))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01944))_

> **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest));
_(source: javascriptallonge.pdf (source-range-83ecb080-01945))_

> **const** foldArray = (array) => callRight(foldArrayWith, array);
_(source: javascriptallonge.pdf (source-range-83ecb080-01946))_

> **const** sumFoldable = (folder) => folder((a, b) => a + b, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01947))_

> sumFoldable(foldArray([1, 4, 9, 16, 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01948))_

> Context: Here it is summing a tree of numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-01950))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01951))_

> Context: Here it is summing a tree of numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-01950))_

> **const** foldTree = (tree) => callRight(foldTreeWith, tree);
_(source: javascriptallonge.pdf (source-range-83ecb080-01953))_

> **const** sumFoldable = (folder) => folder((a, b) => a + b, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01954))_

> sumFoldable(foldTree([1, [4, [9, 16]], 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01955))_

> sum += eachIteration.value; } **return** sum; }
_(source: javascriptallonge.pdf (source-range-83ecb080-01974))_

> iteratorSum(arrayIterator([1, 4, 9, 16, 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01975))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-01982))_

> **const** aListIterator = listIterator(list(1, 4, 9, 16, 25));
_(source: javascriptallonge.pdf (source-range-83ecb080-01983))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> **const** NumberIterator = (number = 0) => () => ({ done: **false** , value: number++ })
_(source: javascriptallonge.pdf (source-range-83ecb080-01988))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> fromOne = NumberIterator(1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01989))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> fromOne().value; _//=> 1_ fromOne().value; _//=> 2_ fromOne().value; _//=> 3_ fromOne().value; _//=> 4_ fromOne().value; _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-01990))_

> **const** squareOf = callLeft(mapIteratorWith, (x) => x * x)
_(source: javascriptallonge.pdf (source-range-83ecb080-02007))_

> toArray(take(squareOf(odds()), 5)) _//=> [1, 9, 25, 49, 81]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02008))_

> Context: We could also write a filter for iterators to accompany our mapping function:
_(context: javascriptallonge.pdf (source-range-83ecb080-02009))_

> **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02011))_

> Context: We could also write a filter for iterators to accompany our mapping function:
_(context: javascriptallonge.pdf (source-range-83ecb080-02009))_

> toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02012))_

> Context: This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02020))_

> **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02019))_

> Context: This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02020))_

> **const** firstInArray = (fn, array) => array.filter(fn)[0];
_(source: javascriptallonge.pdf (source-range-83ecb080-02021))_
