---
page_id: javascriptallonge-array
page_kind: concept
summary: Array: 30 statement(s) and 35 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-array@eab78967eb064dd9f54ca993057fa75a
---

# Array

What [[javascriptallonge]] covers about array:

## Statements

### reference types

- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-31a4cf47-00141))_

### As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-31a4cf47-00172))_

### Arrays and Destructuring Arguments

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-31a4cf47-00818))_

### array literals

- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-31a4cf47-00831))_

### element references

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-31a4cf47-00834))_

- We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind? _(javascriptallonge.pdf (source-range-31a4cf47-00837))_

### Self-Similarity

- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-31a4cf47-00884))_

- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-31a4cf47-00885))_

- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-31a4cf47-00892))_

- We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-31a4cf47-00901))_

### linear recursion

- This simpler form of 'divide and conquer' is called linear recursion . It's very useful and simple to understand. Let's take another example. Sometimes we want to flatten an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays. 62 _(javascriptallonge.pdf (source-range-31a4cf47-00916))_

### Tail Calls (and Default Arguments)

- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-31a4cf47-00964))_

### Garbage, Garbage Everywhere

- But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-31a4cf47-01019))_

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-31a4cf47-01022))_

- Here's the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-31a4cf47-01034))_

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-31a4cf47-01046))_

### so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-31a4cf47-01056))_

### revisiting linked lists

- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-31a4cf47-01117))_

### Mutation

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-31a4cf47-01121))_

### Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-31a4cf47-01225))_

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-31a4cf47-01226))_

### Functional Iterators

- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-31a4cf47-01278))_

### iterating

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-31a4cf47-01288))_

- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-31a4cf47-01294))_

### unfolding and laziness

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-31a4cf47-01299))_

### bonus

- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-31a4cf47-01321))_

### iterables out to infinity

- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-31a4cf47-01577))_

### lazy collection operations

- Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-31a4cf47-01787))_

- But it's still illustrative to dissect something important: Array's .map and .filter methods gather their results into new arrays. Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-31a4cf47-01788))_


## Technical atoms

### Technical frame 1: reference types

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00138))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00137))_

```
[2-1, 2, 2+1] [1, 1+1, 1+1+1]
```

### Technical frame 2: reference types

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00140))_

> How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00139))_

```
[2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3]
```

### Technical frame 3: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00174))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00173))_

```
() => 0
```

### Technical frame 4: array literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00822))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00821))_

```
[] //=> []
```

### Technical frame 5: array literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00823))_

```
[1] //=> [1] [2, 3, 4] //=> [2,3,4]
```

### Technical frame 6: array literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00827))_

```
[[[[[]]]]]
```

### Technical frame 7: array literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00832))_

```
[] === [] //=> false [2 + 2] === [2 + 2] //=> false const array_of_one = () => [1]; array_of_one() === array_of_one() //=> false
```

### Technical frame 8: element references

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00836))_

> As we can see, JavaScript Arrays are zero-based 56 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00835))_

```
const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] //=> 'one' oneTwoThree[1] //=> 'two' oneTwoThree[2] //=> 'three'
```

### Technical frame 9: element references

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00837))_

> We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00839))_

```
const x = [], a = [x]; a[0] === x //=> true, arrays store references to the things you put in them.
```

### Technical frame 10: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00891))_

```
[] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"]
```

### Technical frame 11: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00895))_

```
const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar"]; first //=> "foo" rest //=> ["bar"] const [first, ...rest] = ["foo", "bar", "baz"]; first //=> "foo" rest //=> ["bar","baz"] For the purpose of this exploration, we will presume the following: const isEmpty = ([first, ...rest]) => first === undefined ;
```

### Technical frame 12: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00900))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : // ???
```

### Technical frame 13: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00902))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let's try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"])
```

### Technical frame 14: linear recursion

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00919))_

> The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00918))_

```
Array.isArray("foo") //=> false Array.isArray(["foo"]) //=> true
```

### Technical frame 15: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00966))_

> Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we're going to look at here is called tail-call optimization , or 'TCO.'

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00965))_

```
mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 ]) //=> ???
```

### Technical frame 16: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01041))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01035))_

```
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### Technical frame 17: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01041))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01040))_

```
const node5 = [5, null ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1;
```

### Technical frame 18: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01046))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01045))_

```
cdr(oneToFive) //=> [2,[3,[4,[5,null]]]]
```

### Technical frame 19: so why arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01055))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01054))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical frame 20: so why arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01056))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01055))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical frame 21: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01106))_

> In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest }

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01105))_

```
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### Technical frame 22: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01107))_

```
In that case, a linked list of the numbers 1 , 2 , and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } } . We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Technical frame 23: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01108))_

```
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest //=> {"first":2,"rest":{"first":3,"rest":{}}} OneTwoThree.rest.rest.first //=> 3 Taking the length of a linked list is easy: const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### Technical frame 24: Mutation

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01122))_

```
const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ]
```

### Technical frame 25: Mutation

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01131))_

> There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01130))_

```
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { // ... })(allHallowsEve);
```

### Technical frame 26: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01273))_

```
const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 27: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01275))_

```
const callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 28: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01280))_

> What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01279))_

```
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const foldArray = (array) => callRight(foldArrayWith, array); const sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldArray([1, 4, 9, 16, 25])) //=> 55
```

### Technical frame 29: iterating

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01288))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01287))_

```
const arraySum = (array) => { let sum = 0; for ( let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 30: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01300))_

```
const NumberIterator = (number = 0) => () => ({ done: false , value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne().value; //=> 3 fromOne().value; //=> 4 fromOne().value; //=> 5
```

### Technical frame 31: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01787))_

> Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01786))_

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0)
```

### Technical frame 32: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01792))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01789))_

> When working with very large collections and many operations, this can be important.

### Technical frame 33: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01792))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01790))_

> The effect is even more pronounced when we use methods like first , until , or take :

### Technical frame 34: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01801))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01797))_

```
[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29] .reverse() .map((x) => { console.log(`squaring ${ x } `); return x * x }) .filter((x) => { console.log(`filtering ${ x } `); return x % 2 == 0 })[0] //=> squaring 0 squaring 1 squaring 2 squaring 3 ... squaring 28 squaring 29 filtering 0 filtering 1 filtering 4 ... filtering 784 filtering 841 784
```

### Technical atom 35

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00614))_

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

<details>
<summary>Raw table text</summary>

```
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

</details>


## Related pages

- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Garbage, Garbage Everywhere: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; List shares technical record from Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared statement(s), 10 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from element references: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:; Element shares technical record from element references: const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] //=> 'one' oneTwoThree[1] //=> 'two' oneTwoThree[2] //=> 'three' (6 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Garbage, Garbage Everywhere: Here's the scheme in JavaScript, using two-element arrays to represent cons cells:; Javascript shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated]; Function shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from array literals: Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it co ... [truncated]; Literal shares technical record from array literals: [] //=> [] (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Expression shares technical record from reference types: [2-1, 2, 2+1] [1, 1+1, 1+1+1] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-copy]] - shared statements and technical atoms: Copy shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated]; Copy shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Functional Iterators: Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit:; Functional Iterators shares technical record from Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Value shares technical record from reference types: [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Self-Similarity: Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:; Rest shares technical record from Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Mutation: In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall t ... [truncated]; Object shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Reference shares technical record from Garbage, Garbage Everywhere: const node5 = [5, null ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from Tail Calls (and Default Arguments): In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.; Method shares technical record from Tail Calls (and Default Arguments): mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-problem]] - shared statements and technical atoms: Problem shares source evidence from so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Problem shares technical record from linear recursion: Array.isArray("foo") //=> false Array.isArray(["foo"]) //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-string]] - shared statements and technical atoms: String shares source evidence from As Little As Possible About Functions, But No Less: In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represen ... [truncated]; String shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : // ??? (2 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared technical atoms: the function keyword shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false , value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recall]] - shared technical atoms: Recall shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms: Type shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from revisiting linked lists: Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous value ... [truncated] (1 shared statement(s))
- [[javascriptallonge-argument]] - shared statements: Argument shares source evidence from Self-Similarity: In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of ta ... [truncated] (1 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated] (1 shared statement(s))
- [[javascriptallonge-idea]] - shared statements: Idea shares source evidence from Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated] (1 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))
- [[javascriptallonge-section-so-why-arrays-aa693f44]] - source section: so why arrays shares source evidence from so why arrays: Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointe ... [truncated]; so why arrays shares technical record from so why arrays: And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. (5 shared statement(s), 2 shared atom(s))

## Source

- [[javascriptallonge]]
