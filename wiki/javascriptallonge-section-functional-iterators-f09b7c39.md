---
page_id: javascriptallonge-section-functional-iterators-f09b7c39
page_kind: source
page_family: section-reference
summary: Functional Iterators: 38 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functional-iterators-f09b7c39@8e4a2a08c5dbe0e0ce1723bdb5c4098b
---

# Functional Iterators

From [[javascriptallonge]].

## Statements

- Composing and Decomposing Data 

144 

## **Functional Iterators** 

Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this: 

**const** arraySum = ([first, ...rest], accumulator = 0) => first === **undefined** ? accumulator : arraySum(rest, first + accumulator) 

arraySum([1, 4, 9, 16, 25]) _//=> 55_ 

As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. So we can separate them using fold: 

**const** callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); 

**const** arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) _//=> 55_ 

The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith, so it can only sum arrays. 

What happens when we want to sum a tree of numbers? Or a linked list of numbers? 

Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let’s rearrange our code a bit: _(javascriptallonge.pdf (source-range-af806fb1-00190))_
- 145 

Composing and Decomposing Data 

**const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); 

**const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); 

**const** foldArray = (array) => callRight(foldArrayWith, array); 

**const** sumFoldable = (folder) => folder((a, b) => a + b, 0); 

sumFoldable(foldArray([1, 4, 9, 16, 25])) _//=> 55_ 

What we’ve done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array);. The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable. 

Here it is summing a tree of numbers: 

**const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); 

**const** foldTreeWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : Array.isArray(first) ? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); 

**const** foldTree = (tree) => callRight(foldTreeWith, tree); 

**const** sumFoldable = (folder) => folder((a, b) => a + b, 0); 

sumFoldable(foldTree([1, [4, [9, 16]], 25])) _//=> 55_ 

We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-af806fb1-00191))_
- Composing and Decomposing Data 

146 

## **iterating** 

Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. 

JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: 

**const** arraySum = (array) => { **let** sum = 0; **for** ( **let** i = 0; i < array.length; ++i) { sum += array[i]; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_ 

Once again, we’re mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0. 

We can write this a slightly different way, using a while loop: 

**const** arraySum = (array) => { **let** done, sum = 0, i = 0; **while** ((done = i == array.length, !done)) { **const** value = array[i++]; sum += value; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_ 

Notice that buried inside our loop, we have bound the names done and value. We can put those into a POJO (a Plain Old JavaScript Object). It’ll be a little awkward, but we’ll be patient: _(javascriptallonge.pdf (source-range-af806fb1-00192))_
- 147 

Composing and Decomposing Data 

**const** arraySum = (array) => { **let** iter, sum = 0, index = 0; **while** ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : **undefined** }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } **return** sum; } arraySum([1, 4, 9, 16, 25]) _//=> 55_ 

With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value. Now we can extract the ickiness into a separate function: 

**const** arrayIterator = (array) => { **let** i = 0; **return** () => { **const** done = i === array.length; **return** { done, value: done ? **undefined** : array[i++] } } } **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { _(javascriptallonge.pdf (source-range-af806fb1-00193))_
- 148 

Composing and Decomposing Data 

sum += eachIteration.value; } **return** sum; } 

iteratorSum(arrayIterator([1, 4, 9, 16, 25])) _//=> 55_ 

Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true }. 

We can write a different iterator for a different data structure. Here’s one for linked lists: 

**const** EMPTY = **null** ; **const** isEmpty = (node) => node === EMPTY; **const** pair = (first, rest = EMPTY) => ({first, rest}); **const** list = (...elements) => { **const** [first, ...rest] = elements; **return** elements.length === 0 ? EMPTY : pair(first, list(...rest)) } **const** print = (aPair) => isEmpty(aPair) ? "" : ` **${** aPair.first **} ${** print(aPair.rest) **}** ` **const** listIterator = (aPair) => () => { **const** done = isEmpty(aPair); **if** (done) { **return** {done}; } **else** { **const** {first, rest} = aPair; aPair = aPair.rest; _(javascriptallonge.pdf (source-range-af806fb1-00194))_
- Composing and Decomposing Data 

149 

**return** { done, value: first } } } **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;; 

**while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } 

**const** aListIterator = listIterator(list(1, 4, 9, 16, 25)); 

iteratorSum(aListIterator) 

_//=> 55_ 

## **unfolding and laziness** 

Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example: 

**const** NumberIterator = (number = 0) => () => ({ done: **false** , value: number++ }) 

fromOne = NumberIterator(1); 

fromOne().value; _//=> 1_ fromOne().value; _//=> 2_ fromOne().value; _//=> 3_ fromOne().value; _//=> 4_ fromOne().value; _//=> 5_ 

And here’s another one: _(javascriptallonge.pdf (source-range-af806fb1-00195))_
- Composing and Decomposing Data 

150 

**const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, current] = [current, current + previous]; **return** {done: **false** , value}; }; }; **const** fib = FibonacciIterator() fib().value _//=> 1_ fib().value _//=> 1_ fib().value _//=> 2_ fib().value _//=> 3_ fib().value _//=> 5_ 

A function that starts with a seed and expands it into a data structure is called an _unfold_ . It’s the opposite of a fold. It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators. 

For starters, we can map an iterator, just like we map a collection: 

**const** mapIteratorWith = (fn, iterator) => () => { **const** {done, value} = iterator(); **return** ({done, value: done ? **undefined** : fn(value)}); } **const** squares = mapIteratorWith((x) => x * x, NumberIterator(1)); squares().value _//=> 1_ squares().value _(javascriptallonge.pdf (source-range-af806fb1-00196))_
- 151 

Composing and Decomposing Data 

_//=> 4_ squares().value _//=> 9_ 

This business of going on forever has some drawbacks. Let’s introduce an idea: A function that takes an iterator and returns another iterator. We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: 

**const** take = (iterator, numberToTake) => { **let** count = 0; **return** () => { **if** (++count <= numberToTake) { **return** iterator(); } **else** { **return** {done: **true** }; } }; }; **const** toArray = (iterator) => { **let** eachIteration, array = []; **while** ((eachIteration = iterator(), !eachIteration.done)) { array.push(eachIteration.value); } **return** array; } toArray(take(FibonacciIterator(), 5)) _//=> [1, 1, 2, 3, 5]_ toArray(take(squares, 5)) _//=> [1, 4, 9, 16, 25]_ 

How about the squares of the first five odd numbers? We’ll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-af806fb1-00197))_
- Composing and Decomposing Data 

152 

**const** odds = () => { **let** number = 1; **return** () => { **const** value = number; number += 2; **return** {done: **false** , value}; } } 

**const** squareOf = callLeft(mapIteratorWith, (x) => x * x) 

toArray(take(squareOf(odds()), 5)) _//=> [1, 9, 25, 49, 81]_ 

We could also write a filter for iterators to accompany our mapping function: 

**const** filterIteratorWith = (fn, iterator) => () => { **do** { **const** {done, value} = iterator(); } **while** (!done && !fn(value)); **return** {done, value}; } 

**const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1); 

toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_ 

Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. 

## **bonus** 

Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect, select, and detect. 

We haven’t written anything that finds the first element of an iteration that meets a certain criteria. Or have we? _(javascriptallonge.pdf (source-range-af806fb1-00198))_
- Composing and Decomposing Data 

153 

**const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); 

This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: 

**const** firstInArray = (fn, array) => array.filter(fn)[0]; 

JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. 

## **caveat** 

Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you’re changing the state of the original! 

For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-af806fb1-00199))_
- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-af806fb1-00190))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-af806fb1-00192))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-af806fb1-00196))_
- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-af806fb1-00198))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-af806fb1-00199))_

## Technical atoms

### Technical frame 1: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-af806fb1-00192))_

> Composing and Decomposing Data 

146 

## **iterating** 

Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. 

JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: 

**const** ar

**Atom:** _(javascriptallonge.pdf (source-range-af806fb1-00191))_

<a id="atom-technical-atom-72b80f187358ba40"></a>

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
