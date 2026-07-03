---
page_id: javascriptallonge-functional-iterator
page_kind: concept
page_family: topic-concept
summary: Functional Iterators: 38 statement(s) and 26 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-functional-iterator@bf70d1c3f9c2155d4e3d7d44f85295d9
---

# Functional Iterators

What [[javascriptallonge]] covers about functional iterators:

## Statements

### Yes. Consider this variation: / Functional Iterators

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-7239e085-01276))_

- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-7239e085-01278))_

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-7239e085-01280))_

### Yes. Consider this variation: / Functional Iterators / iterating

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-7239e085-01285))_

- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-7239e085-01286))_

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-7239e085-01288))_

- Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient: _(javascriptallonge.pdf (source-range-7239e085-01291))_

- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-7239e085-01294))_

- We can write a different iterator for a different data structure. Here's one for linked lists: _(javascriptallonge.pdf (source-range-7239e085-01295))_

### Yes. Consider this variation: / Functional Iterators / unfolding and laziness

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-7239e085-01299))_

- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-7239e085-01303))_

- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_

- How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-7239e085-01309))_

- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-7239e085-01312))_

- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-7239e085-01314))_

### Yes. Consider this variation: / Functional Iterators / bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-7239e085-01316))_

- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-7239e085-01319))_

- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-7239e085-01321))_

### Yes. Consider this variation: / Functional Iterators / caveat

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-7239e085-01323))_

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-7239e085-01324))_

### Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

- When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-7239e085-01532))_

- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-7239e085-01541))_

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-7239e085-01543))_

### Like this:

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-7239e085-01552))_

### Like this: / iterables

- People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-7239e085-01554))_

### Like this: / Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-7239e085-01626))_

### Like this: / Generating Iterables / state machines

- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_


## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01273))_

<a id="atom-technical-atom-6b5572164194eb73"></a>

```
const arraySum = ([first, ...rest], accumulator = 0) =>
first === undefined
? accumulator
: arraySum(rest, first + accumulator)
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 2: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01275))_

<a id="atom-technical-atom-c168c344c79ca03d"></a>

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0);
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 3: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01280))_

> What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01279))_

<a id="atom-technical-atom-28df103afd1f2ca4"></a>

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const foldArray = (array) => callRight(foldArrayWith, array);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldArray([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 4: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01283))_

> We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really).

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01282))_

<a id="atom-technical-atom-fd6c44653946062f"></a>

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldTreeWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: Array.isArray(first)
? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\
e, rest))
: fn(first, foldTreeWith(fn, terminalValue, rest));
const foldTree = (tree) => callRight(foldTreeWith, tree);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldTree([1, [4, [9, 16]], 25]))
//=> 55
```

### Technical frame 5: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01288))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01287))_

<a id="atom-technical-atom-61ae9b6a12610202"></a>

```
const arraySum = (array) => {
let sum = 0;
for (let i = 0; i < array.length; ++i) {
sum += array[i];
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 6: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01291))_

> Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01290))_

<a id="atom-technical-atom-401ac2861a7434af"></a>

```
const arraySum = (array) => {
let done,
sum = 0,
i = 0;
while ((done = i == array.length, !done)) {
const value = array[i++];
sum += value;
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 7: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01294))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01292))_

<a id="atom-technical-atom-36834dd82fed3a39"></a>

```
const arraySum = (array) => {
let iter,
sum = 0,
index = 0;
while (
(eachIteration = {
done: index === array.length,
value: index < array.length ? array[index] : undefined
},
++index,
!eachIteration.done)
) {
sum += eachIteration.value;
}
return sum;
}
arraySum([1, 4, 9, 16, 25])
//=> 55
With this code, we make a POJO that has done and value keys. All the summing code needs to know
is to add eachIteration.value. Now we can extract the ickiness into a separate function:
const arrayIterator = (array) => {
let i = 0;
return () => {
const done = i === array.length;
return {
done,
value: done ? undefined : array[i++]
}
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
```

### Technical frame 8: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01294))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01293))_

<a id="atom-technical-atom-99cc8d8b74f77eb7"></a>

```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 9: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01295))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01296))_

<a id="atom-technical-atom-d751402c7f5049a7"></a>

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const print = (aPair) =>
isEmpty(aPair)
? ""
: `${aPair.first} ${print(aPair.rest)}`
const listIterator = (aPair) =>
() => {
const done = isEmpty(aPair);
if (done) {
return {done};
}
else {
const {first, rest} = aPair;
aPair = aPair.rest;
```

### Technical frame 10: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01295))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01297))_

<a id="atom-technical-atom-cfd0ca71b216e058"></a>

```
return { done, value: first }
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
const aListIterator = listIterator(list(1, 4, 9, 16, 25));
iteratorSum(aListIterator)
//=> 55
```

### Technical frame 11: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01300))_

<a id="atom-technical-atom-0ec5247e8a0095b9"></a>

```
const NumberIterator = (number = 0) =>
() => ({ done: false, value: number++ })
fromOne = NumberIterator(1);
fromOne().value;
//=> 1
fromOne().value;
//=> 2
fromOne().value;
//=> 3
fromOne().value;
//=> 4
fromOne().value;
//=> 5
```

### Technical frame 12: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01302))_

<a id="atom-technical-atom-cde01aacf9e50dde"></a>

```
const FibonacciIterator
= () => {
let previous = 0,
current = 1;
return () => {
const value = current;
[previous, current] = [current, current + previous];
return {done: false, value};
};
};
const fib = FibonacciIterator()
fib().value
//=> 1
fib().value
//=> 1
fib().value
//=> 2
fib().value
//=> 3
fib().value
//=> 5
```

### Technical frame 13: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01307))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01305))_

<a id="atom-technical-atom-341fb48fed0de0da"></a>

```
const mapIteratorWith = (fn, iterator) =>
() => {
const {done, value} = iterator();
return ({done, value: done ? undefined : fn(value)});
}
const squares = mapIteratorWith((x) => x * x, NumberIterator(1));
squares().value
//=> 1
squares().value
```

### Technical frame 14: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01307))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01306))_

<a id="atom-technical-atom-977030f55e7c3609"></a>

```
//=> 4
squares().value
//=> 9
```

### Technical frame 15: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01309))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01308))_

<a id="atom-technical-atom-b6c7b5f8c2b10650"></a>

```
const take = (iterator, numberToTake) => {
let count = 0;
return () => {
if (++count <= numberToTake) {
return iterator();
} else {
return {done: true};
}
};
};
const toArray = (iterator) => {
let eachIteration,
array = [];
while ((eachIteration = iterator(), !eachIteration.done)) {
array.push(eachIteration.value);
}
return array;
}
toArray(take(FibonacciIterator(), 5))
//=> [1, 1, 2, 3, 5]
toArray(take(squares, 5))
//=> [1, 4, 9, 16, 25]
```

### Technical frame 16: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01312))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01310))_

<a id="atom-technical-atom-94d949bc4f3d92c7"></a>

```
const odds = () => {
```

### Technical frame 17: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01312))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01311))_

<a id="atom-technical-atom-3f2274499b4e19f1"></a>

```
let number = 1;
return () => {
const value = number;
number += 2;
return {done: false, value};
}
}
const squareOf = callLeft(mapIteratorWith, (x) => x * x)
toArray(take(squareOf(odds()), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 18: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01314))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01313))_

<a id="atom-technical-atom-4efea8fa4b4f428a"></a>

```
const filterIteratorWith = (fn, iterator) =>
() => {
do {
const {done, value} = iterator();
} while (!done && !fn(value));
return {done, value};
}
const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
toArray(take(squareOf(oddsOf(NumberIterator(1))), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 19: Yes. Consider this variation: / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01319))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01318))_

<a id="atom-technical-atom-c5cd3037853933e3"></a>

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 20: Yes. Consider this variation: / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01321))_

> JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01320))_

<a id="atom-technical-atom-b4aa8c9f995e888a"></a>

```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```

### Technical frame 21: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01533))_

<a id="atom-technical-atom-0494f9669763f688"></a>

```
const Stack1 = () =>
({
array:[],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
iterator () {
let iterationIndex = this.index;
return () => {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
});
const stack = Stack1();
stack.push("Greetings");
stack.push("to");
stack.push("you!")
```

### Technical frame 22: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01534))_

<a id="atom-technical-atom-977c2f6172e80243"></a>

```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

### Technical frame 23: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01536))_

<a id="atom-technical-atom-637c40b765d4fca9"></a>

```
The .iterator() method is defined with shorthand equivalent to iterator: function iterator()
{ ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(),
JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is
defined with a fat arrow () => { ... }. What is the value of this within that function?
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable
scoping as any other variable name: We check in the environment enclosing the function. Although
the .iterator() method has returned, its environment is the one that encloses our () => { ...
} function, and that’s where this is bound to the value of stack.
Therefore, the iterator function returned by the .iterator() method has this bound to the stack
object, even though we call it with iter().
```

### Technical frame 24: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01538))_

<a id="atom-technical-atom-ef867f51aa5d4e3b"></a>

```
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
```

### Technical frame 25: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01540))_

<a id="atom-technical-atom-59a4e3c6819adddb"></a>

```
const stack = Stack1();
stack.push(1);
stack.push(2);
stack.push(3);
iteratorSum(stack.iterator())
//=> 6
```

### Technical frame 26: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01543))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01542))_

<a id="atom-technical-atom-bc96f54b184676fd"></a>

```
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 6
```


## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b]] - source section: Yes. Consider this variation: / Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators: The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still re ... [truncated]; Yes. Consider this variation: / Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (30 shared statement(s), 20 shared atom(s))
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-4c177971]] - source section: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators shares source evidence from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functiona ... [truncated]; Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (4 shared statement(s), 6 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Function shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (5 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-iteration]] - shared statements and technical atoms: Iteration shares source evidence from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated]; Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Yes. Consider this variation: / Functional Iterators / iterating: JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with:; Javascript shares technical record from Yes. Consider this variation: / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-data]] - shared statements and technical atoms: Data shares source evidence from Yes. Consider this variation: / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Data shares technical record from Yes. Consider this variation: / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Like this: / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Object shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Yes. Consider this variation: / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Structure shares technical record from Yes. Consider this variation: / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Yes. Consider this variation: / Functional Iterators / iterating: Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like ... [truncated]; Element shares technical record from Yes. Consider this variation: / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from Yes. Consider this variation: / Functional Iterators / bonus: Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smallta ... [truncated]; Language shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Like this: / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated] (1 shared statement(s))
- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from Yes. Consider this variation: / Functional Iterators / caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Yes. Consider this variation: / Functional Iterators / iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-iterator]] - broader topic: Iterator shares source evidence from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.; Iterator shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (4 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-functional]] - broader topic: Functional shares source evidence from Like this: / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
