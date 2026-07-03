---
page_id: javascriptallonge-section-yes-consider-this-variation-b8b28d41
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation:: 208 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-b8b28d41@cbc8dadbdd39e387320937f5e384c9bf
---

# Yes. Consider this variation:

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-c844813d]] - narrower source section: Yes. Consider this variation: / Copy on Write
- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b]] - narrower source section: Yes. Consider this variation: / Functional Iterators
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-f095c99b]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions
- [[javascriptallonge-section-yes-consider-this-variation-tortoises-hares-and-teleporting-turtles-091ad917]] - narrower source section: Yes. Consider this variation: / Tortoises, Hares, and Teleporting Turtles

## Statements

- What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote: _(javascriptallonge.pdf (source-range-7239e085-01213))_
- Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . That's not what we want at all. _(javascriptallonge.pdf (source-range-7239e085-01215))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-7239e085-01218))_
- Now we're creating a new inner parameter, i and binding it to the value of the outer i . This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-7239e085-01220))_
- In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-7239e085-01221))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . _(javascriptallonge.pdf (source-range-7239e085-01215))_

## Statements by subsection

### Yes. Consider this variation: / Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-7239e085-01225))_
- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-7239e085-01226))_
- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-7239e085-01227))_
- The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-7239e085-01228))_
- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-7239e085-01232))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-7239e085-01228))_

### Yes. Consider this variation: / Copy on Write / a few utilities

- Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list . _(javascriptallonge.pdf (source-range-7239e085-01237))_

### Yes. Consider this variation: / Copy on Write / copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-7239e085-01242))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- Sometimes we don't need to make a copy because we won't be modifying the list. _(javascriptallonge.pdf (source-range-7239e085-01242))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-7239e085-01252))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-7239e085-01253))_
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-7239e085-01255))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-7239e085-01252))_

### Yes. Consider this variation: / Tortoises, Hares, and Teleporting Turtles

- A good long while ago (The First Age of Internet Startups), someone asked me one of those pet algorithm questions. It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-7239e085-01258))_
- I think I told him that I was trying to figure out if I could adapt a hashing algorithm such as XORing everything together. This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. We moved on from there, and he didn't reveal the 'solution.' _(javascriptallonge.pdf (source-range-7239e085-01260))_
- I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was: _(javascriptallonge.pdf (source-range-7239e085-01261))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-7239e085-01265))_
- Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle 75 . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-7239e085-01268))_
- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. In Functional Iterators, we'll investigate one pattern for separating these concerns. _(javascriptallonge.pdf (source-range-7239e085-01269))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-7239e085-01265))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-7239e085-01265))_

### Yes. Consider this variation: / Functional Iterators

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-7239e085-01276))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-7239e085-01278))_
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-7239e085-01280))_
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-7239e085-01283))_
- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-7239e085-01276))_

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

### Yes. Consider this variation: / Making Data Out Of Functions

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-7239e085-01328))_
- A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-7239e085-01330))_
- They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions. _(javascriptallonge.pdf (source-range-7239e085-01331))_
- The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-7239e085-01333))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-7239e085-01328))_
- For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-7239e085-01331))_

### Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot

- A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K , is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-7239e085-01338))_
- The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. _(javascriptallonge.pdf (source-range-7239e085-01341))_
- This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-7239e085-01344))_
- This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-7239e085-01352))_

### Yes. Consider this variation: / Making Data Out Of Functions / backwardness

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this: _(javascriptallonge.pdf (source-range-7239e085-01354))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-7239e085-01358))_
- But the first and second we built out of K and I don't work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-7239e085-01359))_
- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-7239e085-01362))_

### Yes. Consider this variation: / Making Data Out Of Functions / the vireo

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-7239e085-01364))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-7239e085-01367))_
- As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-7239e085-01374))_

### Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data

- Here's another look at linked lists using POJOs. We use the term rest instead of second , but it's otherwise identical to what we have above: _(javascriptallonge.pdf (source-range-7239e085-01377))_
- Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-7239e085-01385))_
- We used functions to replace arrays and POJOs, but we still use JavaScript's built-in operators to test for equality ( === ) and to branch ?: . _(javascriptallonge.pdf (source-range-7239e085-01387))_

### Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-7239e085-01389))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again: _(javascriptallonge.pdf (source-range-7239e085-01390))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names: _(javascriptallonge.pdf (source-range-7239e085-01394))_
- We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters: _(javascriptallonge.pdf (source-range-7239e085-01397))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-7239e085-01399))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-7239e085-01390))_

### Yes. Consider this variation: / Making Data Out Of Functions / functions are not the real point

- There are lots of similar texts explaining how to construct complex semantics out of functions. You can establish that K and K(I) can represent true and false , model magnitudes with Church Numerals 79 or Surreal Numbers 80 , and build your way up to printing FizzBuzz. _(javascriptallonge.pdf (source-range-7239e085-01401))_
- Functions are a fundamental building block of computation. They are 'axioms' of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-7239e085-01403))_
- However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) _(javascriptallonge.pdf (source-range-7239e085-01404))_

### Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y) . _(javascriptallonge.pdf (source-range-7239e085-01409))_
- But we could have done something completely different. We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-7239e085-01410))_
- The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it: _(javascriptallonge.pdf (source-range-7239e085-01411))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-7239e085-01413))_
- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-7239e085-01416))_
- We won't bother here, but it's easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally not the same thing as this code for the length of a linked list: _(javascriptallonge.pdf (source-range-7239e085-01417))_
- The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-7239e085-01419))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. This is a fundamental principle of good design. It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-7239e085-01420))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-7239e085-01421))_
- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-7239e085-01422))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-7239e085-01416))_

## Technical atoms

### Technical atom 1

<a id="atom-technical-atom-281a1ae07258b1dc"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01335))_

```text
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

</details>
