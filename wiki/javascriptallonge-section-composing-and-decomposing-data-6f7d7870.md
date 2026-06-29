---
page_id: javascriptallonge-section-composing-and-decomposing-data-6f7d7870
page_kind: source
summary: Composing and Decomposing Data: 416 source-backed entries and 135 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-6f7d7870@6af50c983d5980bed6c67132322b8f0f
---

# Composing and Decomposing Data

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-c1f61fb6]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-f4d3bc3f]] - narrower source section: Composing and Decomposing Data / Self-Similarity
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)
- [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-83116d81]] - narrower source section: Composing and Decomposing Data / Garbage, Garbage Everywhere
- [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-bce9b969]] - narrower source section: Composing and Decomposing Data / Plain Old JavaScript Objects
- [[javascriptallonge-section-composing-and-decomposing-data-mutation-d77e57e8]] - narrower source section: Composing and Decomposing Data / Mutation
- [[javascriptallonge-section-composing-and-decomposing-data-reassignment-5040fcae]] - narrower source section: Composing and Decomposing Data / Reassignment

## Statements

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 55 _(javascriptallonge.pdf (source-range-7239e085-00815))_

## Statements by subsection

### Composing and Decomposing Data / Arrays and Destructuring Arguments

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-7239e085-00818))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-7239e085-00818))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-7239e085-00818))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

- JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: _(javascriptallonge.pdf (source-range-7239e085-00820))_
- We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional: _(javascriptallonge.pdf (source-range-7239e085-00822))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-7239e085-00828))_
- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-7239e085-00831))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-7239e085-00828))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-7239e085-00834))_
- As we can see, JavaScript Arrays are zero-based 56 . _(javascriptallonge.pdf (source-range-7239e085-00836))_
- We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind? _(javascriptallonge.pdf (source-range-7239e085-00837))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [ , expressions, , and ] . Here's an example of an array literal that uses a name: _(javascriptallonge.pdf (source-range-7239e085-00841))_
- The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string. _(javascriptallonge.pdf (source-range-7239e085-00844))_
- In JavaScript, we can actually reverse the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-7239e085-00845))_
- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-7239e085-00847))_
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-7239e085-00849))_
- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-7239e085-00841))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

- Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-7239e085-00853))_
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58 _(javascriptallonge.pdf (source-range-7239e085-00855))_
- Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write _(javascriptallonge.pdf (source-range-7239e085-00856))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

- Some other languages have something called pattern matching , where you can write something like a destructuring assignment, and the language decides whether the 'patterns' matches at all. If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-7239e085-00862))_
- That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: _(javascriptallonge.pdf (source-range-7239e085-00865))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-7239e085-00869))_
- That match would fail because the array doesn't have an element to assign to what . _(javascriptallonge.pdf (source-range-7239e085-00865))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-7239e085-00869))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

- It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that: _(javascriptallonge.pdf (source-range-7239e085-00878))_
- Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59 _(javascriptallonge.pdf (source-range-7239e085-00880))_
- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. We gather the rest of the parameters. _(javascriptallonge.pdf (source-range-7239e085-00881))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-7239e085-00878))_

### Composing and Decomposing Data / Self-Similarity

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 60 _(javascriptallonge.pdf (source-range-7239e085-00883))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-7239e085-00884))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-7239e085-00885))_
- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-7239e085-00886))_
- But we can also define a list by describing a rule for building lists. One of the simplest, and longeststanding in computer science, is to say that a list is: _(javascriptallonge.pdf (source-range-7239e085-00887))_
- Consists of an element concatenated with a list . _(javascriptallonge.pdf (source-range-7239e085-00889))_
- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-7239e085-00890))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-7239e085-00892))_
- Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already? _(javascriptallonge.pdf (source-range-7239e085-00897))_
- 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0 , but we are doing backflips to keep this within a very small and contrived playground. _(javascriptallonge.pdf (source-range-7239e085-00898))_
- We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-7239e085-00901))_
- Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-7239e085-00904))_
- If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-7239e085-00901))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-7239e085-00904))_

### Composing and Decomposing Data / Self-Similarity / linear recursion

- There is more to recursive solutions that simply functions that invoke themselves. Recursive algorithms follow the 'divide and conquer' strategy for solving a problem: _(javascriptallonge.pdf (source-range-7239e085-00910))_
- When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-7239e085-00914))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- This simpler form of 'divide and conquer' is called linear recursion . It's very useful and simple to understand. Let's take another example. Sometimes we want to flatten an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays. 62 _(javascriptallonge.pdf (source-range-7239e085-00916))_
- We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us: _(javascriptallonge.pdf (source-range-7239e085-00917))_
- The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. _(javascriptallonge.pdf (source-range-7239e085-00919))_
- 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. Unfolds can be thought of a 'path' through a data structure, and flattening a tree is equivalent to a depth-first traverse. _(javascriptallonge.pdf (source-range-7239e085-00921))_
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-7239e085-00923))_
- Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- This simpler form of 'divide and conquer' is called linear recursion . _(javascriptallonge.pdf (source-range-7239e085-00916))_

### Composing and Decomposing Data / Self-Similarity / mapping

- Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let's write our own using linear recursion. _(javascriptallonge.pdf (source-range-7239e085-00925))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-7239e085-00930))_
- Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-7239e085-00933))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-7239e085-00930))_

### Composing and Decomposing Data / Self-Similarity / folding

- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-7239e085-00936))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-7239e085-00943))_
- Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-7239e085-00945))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-7239e085-00949))_

### Composing and Decomposing Data / Self-Similarity / summary

- Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized cases of mapping and folding are especially useful and can be used to build other functions. And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-7239e085-00952))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments)

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-7239e085-00954))_
- Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-7239e085-00957))_
- Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 . _(javascriptallonge.pdf (source-range-7239e085-00960))_
- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-7239e085-00961))_
- This keeps on happening, so that JavaScript collects the values 1 , 2 , 3 , 4 , and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []) . It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-7239e085-00962))_
- That information is saved on a call stack , and it is quite expensive. Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called call frames , and they include the place where the function was called, an environment, and so on). _(javascriptallonge.pdf (source-range-7239e085-00963))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-7239e085-00964))_
- Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we're going to look at here is called tail-call optimization , or 'TCO.' _(javascriptallonge.pdf (source-range-7239e085-00966))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-7239e085-00957))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

- There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. _(javascriptallonge.pdf (source-range-7239e085-00971))_
- That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length : _(javascriptallonge.pdf (source-range-7239e085-00972))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-7239e085-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-7239e085-00975))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-7239e085-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-7239e085-00975))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

- The obvious solution is push the 1 + work into the call to length . Here's our first cut: _(javascriptallonge.pdf (source-range-7239e085-00978))_
- This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that: _(javascriptallonge.pdf (source-range-7239e085-00980))_
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith : _(javascriptallonge.pdf (source-range-7239e085-00983))_
- Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-7239e085-00986))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-7239e085-00980))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

- In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example: _(javascriptallonge.pdf (source-range-7239e085-00989))_
- While this is mathematically elegant, it is computational filigree 63 . _(javascriptallonge.pdf (source-range-7239e085-00993))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done: _(javascriptallonge.pdf (source-range-7239e085-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-7239e085-01004))_
- JavaScript provides this exact syntax, it's called a default argument , and it looks like this: _(javascriptallonge.pdf (source-range-7239e085-01005))_
- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-7239e085-01009))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-7239e085-01011))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-7239e085-01013))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere

- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-7239e085-01017))_
- But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-7239e085-01019))_
- Every time we call mapWith , we're calling [...prepend, fn(first)] . To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith . _(javascriptallonge.pdf (source-range-7239e085-01020))_
- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-7239e085-01023))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-7239e085-01024))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript's built-in arrays work. _(javascriptallonge.pdf (source-range-7239e085-01026))_
- Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-7239e085-01024))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-7239e085-01026))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word. _(javascriptallonge.pdf (source-range-7239e085-01031))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-7239e085-01032))_
- Lists were represented as linked lists of cons cells, with each cell's head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-7239e085-01033))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-7239e085-01034))_
- Here's the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-7239e085-01035))_
- This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it: _(javascriptallonge.pdf (source-range-7239e085-01042))_
- car is very fast, it simply extracts the first element of the cons cell. _(javascriptallonge.pdf (source-range-7239e085-01044))_
- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-7239e085-01047))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-7239e085-01048))_
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car / cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. _(javascriptallonge.pdf (source-range-7239e085-01050))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-7239e085-01031))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-7239e085-01032))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-7239e085-01034))_
- This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . _(javascriptallonge.pdf (source-range-7239e085-01042))_
- In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-7239e085-01047))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-7239e085-01048))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. _(javascriptallonge.pdf (source-range-7239e085-01055))_
- We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-7239e085-01056))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-7239e085-01057))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-7239e085-01058))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / summary

- Although we showed how to use tail calls to map and fold over arrays with [first, ...rest] , in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-7239e085-01060))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-7239e085-01060))_

### Composing and Decomposing Data / Plain Old JavaScript Objects

- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list: _(javascriptallonge.pdf (source-range-7239e085-01062))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-7239e085-01065))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-7239e085-01067))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-7239e085-01068))_
- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-7239e085-01069))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-7239e085-01070))_
- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-7239e085-01062))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-7239e085-01065))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-7239e085-01068))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

- JavaScript has a literal syntax for creating objects. This object maps values to the keys year , month , and day : _(javascriptallonge.pdf (source-range-7239e085-01073))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-7239e085-01077))_
- Names needn't be alphanumeric strings. For anything else, enclose the label in quotes: _(javascriptallonge.pdf (source-range-7239e085-01079))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-7239e085-01081))_
- Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] : _(javascriptallonge.pdf (source-range-7239e085-01083))_
- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-7239e085-01091))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-7239e085-01077))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

- Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: _(javascriptallonge.pdf (source-range-7239e085-01100))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

- In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest } _(javascriptallonge.pdf (source-range-7239e085-01106))_
- What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list: _(javascriptallonge.pdf (source-range-7239e085-01109))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-7239e085-01111))_
- We could follow the strategy of delaying the work. Let's write that naively: _(javascriptallonge.pdf (source-range-7239e085-01112))_
- Well, well, well. We have unwittingly reversed the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. This isn't a bad thing by any stretch of the imagination. Let's call it what it is: _(javascriptallonge.pdf (source-range-7239e085-01114))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-7239e085-01116))_
- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-7239e085-01117))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-7239e085-01111))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-7239e085-01116))_
- Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-7239e085-01117))_

### Composing and Decomposing Data / Mutation

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-7239e085-01121))_
- Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example: _(javascriptallonge.pdf (source-range-7239e085-01127))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: _(javascriptallonge.pdf (source-range-7239e085-01129))_
- There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-7239e085-01131))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment? _(javascriptallonge.pdf (source-range-7239e085-01134))_
- This is different. We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. Now that we've finished with mutation and aliases, let's have a look at it. _(javascriptallonge.pdf (source-range-7239e085-01136))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-7239e085-01138))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction. _(javascriptallonge.pdf (source-range-7239e085-01140))_
- Recall that you can access a value from within an array or an object using [] . _(javascriptallonge.pdf (source-range-7239e085-01121))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-7239e085-01129))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-7239e085-01131))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-7239e085-01134))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-7239e085-01140))_

### Composing and Decomposing Data / Mutation / mutation and data structures

- Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell 70 don't permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-7239e085-01142))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-7239e085-01143))_
- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-7239e085-01150))_
- So back to avoiding mutation. In general, it's easier to reason about data that doesn't change. We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it. We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be 'safe.' _(javascriptallonge.pdf (source-range-7239e085-01151))_

### Composing and Decomposing Data / Mutation / building with mutation

- As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-7239e085-01153))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-7239e085-01155))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-7239e085-01157))_

### Composing and Decomposing Data / Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-7239e085-01162))_
- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-7239e085-01167))_
- Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const , but permits us to rebind variables. JavaScript has such a thing, it's called let : _(javascriptallonge.pdf (source-range-7239e085-01168))_
- We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-7239e085-01170))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from: _(javascriptallonge.pdf (source-range-7239e085-01173))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-7239e085-01178))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . _(javascriptallonge.pdf (source-range-7239e085-01173))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-7239e085-01178))_

### Composing and Decomposing Data / Reassignment / mixing let and const

- Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. _(javascriptallonge.pdf (source-range-7239e085-01180))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-7239e085-01183))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-7239e085-01185))_

### Composing and Decomposing Data / Reassignment / mixing let and const / var

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-7239e085-01187))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-7239e085-01191))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-7239e085-01193))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-7239e085-01200))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-7239e085-01200))_

### Composing and Decomposing Data / Reassignment / why const and let were invented

- const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-7239e085-01202))_
- We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var : _(javascriptallonge.pdf (source-range-7239e085-01203))_
- Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem? _(javascriptallonge.pdf (source-range-7239e085-01205))_
- 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . . . . + 99 + 100 = ? But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . . . . + (50 + 51) = ? If you notice every pair of numbers adds up to 101. There are 50 pairs of numbers, so the answer is 50*101 = 5050. Of course Gauss came up with the answer about 20 times faster than the other kids. _(javascriptallonge.pdf (source-range-7239e085-01206))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00815))_

> Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 55

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00813))_

> [Figure] (p.100)

### Technical frame 2: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00822))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00821))_

```
[]
//=> []
```

### Technical frame 3: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00823))_

```
[1]
//=> [1]
[2, 3, 4]
//=> [2,3,4]
```

### Technical frame 4: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00825))_

```
[ 2,
3,
2 + 2
]
//=> [2,3,4]
```

### Technical frame 5: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00827))_

```
[[[[[]]]]]
```

### Technical frame 6: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00830))_

```
const wrap = (something) => [something];
wrap("lunch")
//=> ["lunch"]
```

### Technical frame 7: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00832))_

```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```

### Technical frame 8: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00836))_

> As we can see, JavaScript Arrays are zero-based 56 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00835))_

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

### Technical frame 9: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00837))_

> We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00839))_

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```

### Technical frame 10: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00844))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00842))_

```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

### Technical frame 11: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00844))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00843))_

```
const wrap = (something) => {
const wrapped = [something]
return wrapped;
}
wrap("package")
//=> ["package"]
```

### Technical frame 12: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00847))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00846))_

```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

### Technical frame 13: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00848))_

```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```

### Technical frame 14: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00851))_

```
const description = (nameAndOccupation) => {
const [[first, last], occupation] = nameAndOccupation;
return `${first} is a ${occupation}`;
}
description([["Reginald", "Braithwaite"], "programmer"])
//=> "Reginald is a programmer"
```

### Technical frame 15: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00855))_

> car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00854))_

```
const [car, ...cdr] = [1, 2, 3, 4, 5];
car
//=> 1
cdr
//=> [2, 3, 4, 5]
```

### Technical frame 16: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00858))_

```
const [...butLast, last] = [1, 2, 3, 4, 5];
//=> ERROR
const [first, ..., last] = [1, 2, 3, 4, 5];
//=> ERROR
Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals.
So if
const wrapped = [something];
Then:
const [unwrapped] = something;
What is the reverse of gathering? We know that:
const [car, ...cdr] = [1, 2, 3, 4, 5];
What is the reverse? It would be:
const cons = [car, ...cdr];
Let’s try it:
const oneTwoThree = ["one", "two", "three"];
```

### Technical frame 17: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00859))_

```
Let’s try it:
const oneTwoThree = ["one", "two", "
["zero", ...oneTwoThree]
//=> ["zero","one","two","three"]
```

### Technical frame 18: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00865))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00864))_

```
const [what] = [];
```

### Technical frame 19: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00866))_

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

### Technical frame 20: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00867))_

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

### Technical frame 21: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00872))_

```
const description = (nameAndOccupation) => {
if (nameAndOccupation.length < 2) {
return ["", "occupation missing"]
}
else {
const [[first, last], occupation] = nameAndOccupation;
return [`${first} is a ${occupation}`, "ok"];
}
}
const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]);
reg
//=> "Reginald is a programmer"
status
//=> "ok"
```

### Technical frame 22: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00875))_

```
foo()
bar("smaug")
baz(1, 2, 3)
```

### Technical frame 23: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00877))_

```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```

### Technical frame 24: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00880))_

> Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00879))_

```
const numbers = (...nums) => nums;
numbers(1, 2, 3, 4, 5)
//=> [1,2,3,4,5]
const headAndTail = (head, ...tail) => [head, tail];
headAndTail(1, 2, 3, 4, 5)
//=> [1,[2,3,4,5]]
```

### Technical frame 25: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00891))_

```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

### Technical frame 26: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00895))_

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

### Technical frame 27: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00896))_

```
isEmpty([])
//=> true
isEmpty([0])
//=> false
isEmpty([[]])
//=> false
```

### Technical frame 28: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00900))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: // ???
```

### Technical frame 29: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00902))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
Let’s try it!
length([])
//=> 0
length(["foo"])
//=> 1
length(["foo", "bar", "baz"])
```

### Technical frame 30: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00903))_

```
//=> 3
```

### Technical frame 31: Composing and Decomposing Data / Self-Similarity / linear recursion

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00919))_

> The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00918))_

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

### Technical frame 32: Composing and Decomposing Data / Self-Similarity / linear recursion

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00923))_

> Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00922))_

```
const flatten = ([first, ...rest]) => {
if (first === undefined) {
return [];
}
else if (!Array.isArray(first)) {
return [first, ...flatten(rest)];
}
else {
return [...flatten(first), ...flatten(rest)];
}
}
flatten(["foo", [3, 4, []]])
//=> ["foo",3,4]
```

### Technical frame 33: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00927))_

```
const squareAll = ([first, ...rest]) => first === undefined
? []
: [first * first, ...squareAll(rest)\
];
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 34: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00929))_

```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 35: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00932))_

```
const mapWith = (fn, array) => // ...
```

### Technical frame 36: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00934))_

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
mapWith((x) => !!x, [null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 37: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00937))_

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 38: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00942))_

```
const foldWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldWith(fn, terminalValue, rest));
```

### Technical frame 39: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00944))_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 40: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00946))_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 41: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00948))_

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\
], array),
squareAll = (array) => mapWith((x) => x * x, array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 42: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00950))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```

### Technical frame 43: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00957))_

> Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00956))_

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 44: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00960))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00959))_

```
const mapWith = function (fn, [first, ...rest]) {
if (first === undefined) {
return [];
}
else {
const _temp1 = fn(first),
_temp2 = mapWith(fn, rest),
_temp3 = [_temp1, ..._temp2];
return _temp3;
}
}
```

### Technical frame 45: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00961))_

> Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00960))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.

### Technical frame 46: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00966))_

> Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we're going to look at here is called tail-call optimization , or 'TCO.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00965))_

```
mapWith((x) => x * x, [
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99
])
//=> ???
```

### Technical frame 47: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00970))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00969))_

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return;
}
else {
for (let arg of args) {
if (arg == null) return;
}
return fn.apply(this, args);
}
}
```

### Technical frame 48: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00974))_

> The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00973))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```

### Technical frame 49: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00980))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00979))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? 0 + numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
lengthDelaysWork(["foo", "bar", "baz"], 0)
//=> 3
```

### Technical frame 50: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00981))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
const length = (n) =>
lengthDelaysWork(n, 0);
```

### Technical frame 51: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00982))_

```
Or we could use partial application:
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const length = callLast(lengthDelaysWork, 0);
length(["foo", "bar", "baz"])
//=> 3
```

### Technical frame 52: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00984))_

```
const mapWithDelaysWork = (fn, [first, ...rest], prepend) =>
first === undefined
? prepend
: mapWithDelaysWork(fn, rest, [...prepend, fn(first)]);
const mapWith = callLast(mapWithDelaysWork, []);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
We can use it with ridiculously large arrays:
```

### Technical frame 53: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00985))_

```
mapWith((x) => x * x, [
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79,
80,
81,
82,
83,
84,
85,
86,
87,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
98,
99,
// ...
2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989,
2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ])
//=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ...
```

### Technical frame 54: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00993))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00990))_

```
5! = 5
x
4
x
3
x
2
x
1 = 120.
```

### Technical frame 55: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00993))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00992))_

```
const factorial = (n) =>
n == 1
? n
: n * factorial(n - 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

### Technical frame 56: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00999))_

> Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00995))_

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```

### Technical frame 57: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00999))_

> Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00998))_

```
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const factorial = callLast(factorialWithDelayedWork, 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

### Technical frame 58: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01004))_

> What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01002))_

```
const factorial = (n, work) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1, 1)
//=> 1
factorial(5, 1)
//=> 120
```

### Technical frame 59: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01004))_

> What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01003))_

> But it is hideous to have to always add a 1 parameter, we'd be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.

### Technical frame 60: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01006))_

```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```

### Technical frame 61: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01008))_

```
const length = ([first, ...rest], numberToBeAdded = 0) =>
first === undefined
? numberToBeAdded
: length(rest, 1 + numberToBeAdded)
length(["foo", "bar", "baz"])
//=> 3
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 62: Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01013))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01012))_

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```

### Technical frame 63: Composing and Decomposing Data / Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01017))_

> We have now seen how to use Tail Calls to execute mapWith in constant space:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01015))_

> [Figure] (p.126)

### Technical frame 64: Composing and Decomposing Data / Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01019))_

> But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01018))_

```
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 65: Composing and Decomposing Data / Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01026))_

> 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript's built-in arrays work.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01027))_

> [Figure] (p.128)

### Technical frame 66: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01032))_

> Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01031))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

### Technical frame 67: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01036))_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 68: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01038))_

```
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

### Technical frame 69: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01039))_

```
oneToFive
//=> [1,[2,[3,[4,[5,null]]]]]
```

### Technical frame 70: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01041))_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Technical frame 71: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01044))_

> car is very fast, it simply extracts the first element of the cons cell.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01043))_

```
car(oneToFive)
//=> 1
```

### Technical frame 72: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01047))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01046))_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 73: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01055))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical frame 74: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01057))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical frame 75: Composing and Decomposing Data / Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01065))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01063))_

```
const remember = ["the milk", "the coffee beans", "the biscotti"];
And they can be used to store heterogeneous things in various levels of structure:
```

### Technical frame 76: Composing and Decomposing Data / Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01065))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01064))_

```
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### Technical frame 77: Composing and Decomposing Data / Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01067))_

> Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01066))_

```
const NAME = 0,
FIRST = 0,
LAST = 1,
OCCUPATION = 1,
TITLE = 0,
RESPONSIBILITIES = 1;
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### Technical frame 78: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01077))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01074))_

```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 79: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01077))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01076))_

```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }
//=> false
Objects use [] to access the values by name, using a string:
{ year: 2012, month: 6, day: 14 }['day']
//=> 14
```

### Technical frame 80: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01079))_

> Names needn't be alphanumeric strings. For anything else, enclose the label in quotes:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01078))_

```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

### Technical frame 81: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01081))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01080))_

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name']
//=> 'reginald'
```

### Technical frame 82: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01083))_

> Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01082))_

```
const date = { year: 2012, month: 6, day: 14 };
date['day'] === date.day
//=> true
```

### Technical frame 83: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01084))_

```
{
["p" + "i"]: 3.14159265
}
//=> {"pi":3.14159265}
```

### Technical frame 84: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01086))_

```
const Mathematics = {
abs: (a) => a < 0 ? -a : a
};
Mathematics.abs(-5)
//=> 5
```

### Technical frame 85: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01088))_

```
const SecretDecoderRing = {
encode: function (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode: function (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 86: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01090))_

```
const SecretDecoderRing = {
encode: function encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode: function decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 87: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01092))_

```
const SecretDecoderRing = {
encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 88: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01096))_

```
const user = {
name: { first: "Reginald",
last: "Braithwaite"
},
occupation: { title: "Author",
responsibilities: [ "JavaScript Allongé",
"JavaScript Spessore",
"CoffeeScript Ristretto"
]
}
};
user.name.last
//=> "Braithwaite"
user.occupation.title
//=> "Author"
And we can also write:
const {name: { first: given, last: surname}, occupation: { title: title }
er;
surname
//=> "Braithwaite"
title
//=> "Author"
```

### Technical frame 89: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01098))_

```
} = us\
```

### Technical frame 90: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01099))_

```
const description = ({name: { first: given }, occupation: { title: title } }) =>
`${given} is a ${title}`;
description(user)
//=> "Reginald is a Author"
```

### Technical frame 91: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01101))_

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 92: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01102))_

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```

### Technical frame 93: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01106))_

> In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest }

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01105))_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 94: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01107))_

```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Technical frame 95: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01108))_

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest
//=> {"first":2,"rest":{"first":3,"rest":{}}}
OneTwoThree.rest.rest.first
//=> 3
Taking the length of a linked list is easy:
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 96: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01111))_

> The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01110))_

```
const slowcopy = (node) =>
node === EMPTY
? EMPTY
: { first: node.first, rest: slowcopy(node.rest)};
slowcopy(OneTwoThree)
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

### Technical frame 97: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01114))_

> Well, well, well. We have unwittingly reversed the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. This isn't a bad thing by any stretch of the imagination. Let's call it what it is:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01113))_

```
const copy2 = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: copy2(node.rest, { first: node.first, rest: delayed });
copy2(OneTwoThree)
//=> {"first":3,"rest":{"first":2,"rest":{"first":1,"rest":{}}}}
```

### Technical frame 98: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01116))_

> Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01115))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
And now, we can make a reversing map:
const reverseMapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
reverseMapWith((x) => x * x, OneTwoThree)
//=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}}
And a regular mapWith follows:
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
mapWith((x) => x * x, OneTwoThree)
//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

### Technical frame 99: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01121))_

> In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01119))_

> [Figure] (p.141)

### Technical frame 100: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01122))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Technical frame 101: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01124))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[3] = 'four';
oneTwoThree
//=> [ 1, 2, 3, 'four' ]
```

### Technical frame 102: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01126))_

```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'};
name.middleName = 'Austin'
name
//=> { firstName: 'Leonard',
#
lastName: 'Braithwaite',
#
middleName: 'Austin' }
```

### Technical frame 103: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01129))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01128))_

```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

### Technical frame 104: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01131))_

> There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01130))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
// ...
})(allHallowsEve);
```

### Technical frame 105: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01134))_

> The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01133))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween = [2013, 10, 31];
})(allHallowsEve);
allHallowsEve
//=> [2012, 10, 31]
```

### Technical frame 106: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01136))_

> This is different. We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. Now that we've finished with mutation and aliases, let's have a look at it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01135))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween[0] = 2013;
})(allHallowsEve);
allHallowsEve
//=> [2013, 10, 31]
```

### Technical frame 107: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01138))_

> JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01137))_

> [Figure] (p.143)

### Technical frame 108: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01140))_

> Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01139))_

> [Figure] (p.143)

### Technical frame 109: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01144))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

### Technical frame 110: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01146))_

```
const EMPTY = {};
const OneToFive = { first: 1,
rest: {
first: 2,
rest: {
first: 3,
rest: {
first: 4,
rest: {
first: 5,
rest: EMPTY } } } } };
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
const ThreeToFive = OneToFive.rest.rest;
ThreeToFive
//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}}
ThreeToFive.first = "three";
ThreeToFive.rest.first = "four";
ThreeToFive.rest.rest.first = "five";
ThreeToFive
//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\
}}
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we
wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of {"first":3,"rest":{"firs
we were getting a reference to the same chain of nodes.
Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

### Technical frame 111: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01148))_

```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

### Technical frame 112: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01149))_

```
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] =
ThreeToFive
//=> [3, 4, 5]
ThreeToFive[0] = "three";
ThreeToFive[1] = "four";
ThreeToFive[2] = "five";
ThreeToFive
//=> ["three","four","five"]
OneToFive
//=> [1,2,3,4,5]
```

### Technical frame 113: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01151))_

> We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.

### Technical frame 114: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01155))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01154))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```

### Technical frame 115: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01156))_

```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
```

### Technical frame 116: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01159))_

```
const mapWith = (fn, node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
return mapWith(fn, rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
tail.rest = newNode;
return mapWith(fn, node.rest, head, newNode);
}
}
mapWith((x) => 1.0 / x, OneToFive)
```

### Technical frame 117: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01160))_

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\
{"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```

### Technical frame 118: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01167))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01164))_

```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```

### Technical frame 119: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01167))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01166))_

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```

### Technical frame 120: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01170))_

> We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01169))_

```
let age = 52;
age = 53;
age
//=> 53
```

### Technical frame 121: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01173))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01172))_

```
(() => {
let age = 49;
if (true) {
let age = 50;
}
return age;
})()
//=> 49
```

### Technical frame 122: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01174))_

```
{age: 49, '..': global-environment}
To:
{age: 50, '..': {age: 49, '..': global-environment}}
Then back to:
```

### Technical frame 123: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01175))_

```
{age: 49, '..': global-environment}
```

### Technical frame 124: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01177))_

```
(() => {
let age = 49;
if (true) {
age = 50;
}
return age;
})()
//=> 50
```

### Technical frame 125: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01181))_

> If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:

### Technical frame 126: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01182))_

```
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```

### Technical frame 127: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01185))_

> Shadowing a const with a let does not permit it to be rebound in its original scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01184))_

```
(() => {
const age = 49;
if (true) {
let age = 50;
}
age = 52;
return age;
})()
//=> ERROR: age is read-only
```

### Technical frame 128: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01191))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01188))_

```
const factorial = (n) => {
let x = n;
if (x === 1) {
return 1;
}
else {
--x;
return n * factorial(x);
}
}
factorial(5)
//=> 120
const factorial2 = (n) => {
var x = n;
if (x === 1) {
return 1;
}
else {
--x;
```

### Technical frame 129: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01191))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01190))_

```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

### Technical frame 130: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01193))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01192))_

```
(() => {
var age = 49;
if (true) {
var age = 50;
}
return age;
})()
//=> 50
```

### Technical frame 131: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01195))_

```
const factorial = (n) => {
return innerFactorial(n, 1);
function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> 24
```

### Technical frame 132: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01197))_

```
const factorial = (n) => {
let innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
return innerFactorial(n, 1);
}
JavaScript hoists the let and the assignment. But not so with var:
const factorial = (n) => {
return innerFactorial(n, 1);
var innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### Technical frame 133: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01199))_

```
const factorial = (n) => {
let innerFactorial = undefined;
return innerFactorial(n, 1);
innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### Technical frame 134: Composing and Decomposing Data / Reassignment / why const and let were invented

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01205))_

> Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01204))_

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```

### Technical atom 135

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00857))_

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

<details>
<summary>Raw table text</summary>

```
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

</details>
