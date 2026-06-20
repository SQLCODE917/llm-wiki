---
page_id: self-similarity
page_kind: source
summary: Chapter on self-similarity and recursive algorithms in JavaScript.
updated: 2026-06-19
---

## Self-Similarity

Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[60]

In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. 

We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. 

Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. 

But we can also define a list by describing a rule for building lists. One of the simplest, and longeststanding in computer science, is to say that a list is: 

1. Empty, or; 

2. Consists of an element concatenated with a list . 

Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list, [e, ...list] is a list. We can test this manually by building up a list: 

[] _//=> []_ ["baz", ...[]] _//=> ["baz"]_ ["bar", ...["baz"]] _//=> ["bar","baz"]_ ["foo", ...["bar", "baz"]] _//=> ["foo","bar","baz"]_ 

Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: 

60http://www.cs.yale.edu/homes/perlis-alan/quotes.html 

**const** [first, ...rest] = []; first _//=> undefined_ rest _//=> []:_ **const** [first, ...rest] = ["foo"]; first _//=> "foo"_ rest _//=> []_ **const** [first, ...rest] = ["foo", "bar"]; first _//=> "foo"_ rest _//=> ["bar"]_ **const** [first, ...rest] = ["foo", "bar", "baz"]; first _//=> "foo"_ rest _//=> ["bar","baz"]_ 

For the purpose of this exploration, we will presume the following:[61] 

**const** isEmpty = ([first, ...rest]) => first === **undefined** ; 

isEmpty([]) _//=> true_ isEmpty([0]) _//=> false_ isEmpty([[]]) _//=> false_ 

Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using 

> 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0, but we are doing backflips to keep this within a very small and contrived playground. 

Composing and Decomposing Data 

88 

its .length. But as an exercise, how would we write a length function using just what we have already? 

First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let's start our function with the observation that if an array is empty, the length is 0: 

**const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_ 

We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest). Well, the length of first is 1, there's just one element at the front. But we don't know the length of rest. If only there was a function we could call… Like length! 

**const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest); 

Let's try it! 

length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_ 

Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. 

## Linear Recursion 

"Recursion" sometimes seems like an elaborate party trick. There's even a joke about this: 

When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. They find a bunsen burner, a sparker, a tap, an empty beaker, a stand, and a card with the instructions "boil water." 

Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. After a bit the water boils, and they turn off the burner and are lead to a second bench. 

Once again, there is a card that reads, "boil water." But this time, the beaker is on the stand over the burner, as left behind by the previous student. The engineers light the burner immediately. Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. 

There is more to recursive solutions that simply functions that invoke themselves. Recursive algorithms follow the "divide and conquer" strategy for solving a problem: 

1. Divide the problem into smaller problems 

2. If a smaller problem is solvable, solve the small problem 

3. If a smaller problem is not solvable, divide and conquer that problem 

4. When all small problems have been solved, compose the solutions into one big solution 

The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. 

This simpler form of "divide and conquer" is called _linear recursion_ . It's very useful and simple to understand. Let's take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays.[62] 

We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines: 

**const** flatten = (array) => { 
  if (array.length === 0) return []; 
  const [first, ...rest] = array; 
  if (Array.isArray(first)) { 
    return flatten(first).concat(flatten(rest)); 
  } else { 
    return [first].concat(flatten(rest)); 
  } 
}; 

Let's also look at mapping and folding functions, which are special cases of linear recursion.

## Mapping and Folding

Let's look at how we can implement map and fold functions using linear recursion:

**const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; 

**const** foldWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldWith(fn, terminalValue, rest)); 

## Summary 

Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized cases of mapping and folding are especially useful and can be used to build other functions. And finally, while folding is a special case of linear recursion, mapping is a special case of folding.

## Tail Calls (and Default Arguments)

The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not "production-ready" implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. 

In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. 

The solution to this problem is tail-call optimization. In a tail-call, a function's last act is to invoke another function, and then return whatever the other function returns. JavaScript can optimize away the function call overhead and stack space when a function makes a call in tail position.

## Tail-Call Optimization

A tail-recursive version of length would look like:

**const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined** ? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded); 

**const** length = (n) => lengthDelaysWork(n, 0); 

This approach can also be applied to map and fold functions to make them more memory-efficient.

## Factorials

Factorials are another common example of recursion:

**const** factorial = (n) => n === 1 ? n : n * factorial(n - 1); 

A tail-recursive version would be:

**const** factorialWithDelayedWork = (n, work) => n === 1 ? work : factorialWithDelayedWork(n - 1, n * work); 

**const** factorial = (n) => factorialWithDelayedWork(n, 1); 

## Default Arguments

JavaScript provides default arguments to make tail-recursive functions cleaner:

**const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); 

This allows us to call factorial(5) instead of factorial(5, 1).

## Defaults and Destructuring

We can also use default values in destructuring assignments:

**const** [first, second = "two"] = ["one"]; 

This is useful when working with recursive functions that have default parameters.
