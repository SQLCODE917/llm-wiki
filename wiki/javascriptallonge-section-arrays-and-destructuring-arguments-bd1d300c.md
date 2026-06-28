---
page_id: javascriptallonge-section-arrays-and-destructuring-arguments-bd1d300c
page_kind: source
summary: Arrays and Destructuring Arguments: 50 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-arrays-and-destructuring-arguments-bd1d300c@96842832adb9495b516d4c9cbbac32fe
---

# Arrays and Destructuring Arguments

From [[javascriptallonge]].

## Statements

- Composing and Decomposing Data

78

## **Arrays and Destructuring Arguments**

While we have mentioned arrays briefly, we haven’t had a close look at them. Arrays are JavaScript’s “native” representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality.

## **array literals**

JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: [] _//=> []_ We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. Whitespace is optional:

[1] _//=> [1]_ [2, 3, 4] _//=> [2,3,4]_ Any expression will work:

[ 2, 3, 2 + 2 ] _//=> [2,3,4]_ Including an expression denoting another array: [[[[[]]]]] This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

Any expression will do, including names: _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Composing and Decomposing Data

79 **const** wrap = (something) => [something]; wrap("lunch") _//=> ["lunch"]_ Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: [] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_ **const** array_of_one = () => [1]; array_of_one() === array_of_one() _//=> false_

## **element references**

Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: **const** oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_ As we can see, JavaScript Arrays are zero-based[56] .

We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

56https://en.wikipedia.org/wiki/Zero-based_numbering _(javascriptallonge.pdf (source-range-83ecb080-00125))_
- Composing and Decomposing Data

80 **const** x = [], a = [x]; a[0] === x

_//=> true, arrays store references to the things you put in them._

## **destructuring arrays**

There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name: **const** wrap = (something) => [something];

Let’s expand it to use a block and an extra name: **const** wrap = (something) => { **const** wrapped = [something]; **return** wrapped; } wrap("package") _//=> ["package"]_ The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: **const** unwrap = (wrapped) => { **const** [something] = wrapped; **return** something; } unwrap(["present"]) _//=> "present"_

The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- Composing and Decomposing Data

81 **const** surname = (name) => { **const** [first, last] = name; **return** last; } surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_

We could do the same thing with (name) => name[1], but destructuring is code that resembles the data it consumes, a valuable coding style.

Destructuring can nest: **const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation; **return** ` **${** first **}** is a **${** occupation **}** `; } description([["Reginald", "Braithwaite"], "programmer"]) _//=> "Reginald is a programmer"_

## **gathering**

Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: **const** [car, ...cdr] = [1, 2, 3, 4, 5]; car _//=> 1_ cdr _//=> [2, 3, 4, 5]_ car and cdr[57] are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst, or head and tail. We will use a common convention and call variables we gather rest, but refer to the ... operation as a “gather,” following Kyle Simpson’s example.[58] Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

> 57https://en.wikipedia.org/wiki/CAR_and_CDR

> 58Kyle Simpson is the author of You Don’t Know JS, available here _(javascriptallonge.pdf (source-range-83ecb080-00127))_
- 82

Composing and Decomposing Data **const** [...butLast, last] = [1, 2, 3, 4, 5]; _//=> ERROR_ **const** [first, ..., last] = [1, 2, 3, 4, 5]; _//=> ERROR_

Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. So if **const** wrapped = [something]; Then: **const** [unwrapped] = something;

What is the reverse of gathering? We know that: **const** [car, ...cdr] = [1, 2, 3, 4, 5];

What is the reverse? It would be: **const** cons = [car, ...cdr];

Let’s try it: **const** oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] _//=> ["zero","one","two","three"]_ It works! We can use ... to place the elements of an array inside another array. We say that using ... to destructure is gathering, and using it in a literal to insert elements is called “spreading.”

## **destructuring is not pattern matching**

Some other languages have something called _pattern matching_ , where you can write something like a destructuring assignment, and the language decides whether the “patterns” matches at all. If it does, assignments are made where appropriate.

In such a language, if you wrote something like: _(javascriptallonge.pdf (source-range-83ecb080-00128))_
- Composing and Decomposing Data

83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore: **const** [what] = []; what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_ And if there aren’t any items to assign with ..., JavaScript assigns an empty array: **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_ From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

## **destructuring and return values**

Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring: _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- 84

Composing and Decomposing Data **const** description = (nameAndOccupation) => { **if** (nameAndOccupation.length < 2) { **return** ["", "occupation missing"] } **else** { **const** [[first, last], occupation] = nameAndOccupation; **return** [` **${** first **}** is a **${** occupation **}** `, "ok"]; } } **const** [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); reg _//=> "Reginald is a programmer"_ status _//=> "ok"_

## **destructuring parameters**

Consider the way we pass arguments to parameters: foo() bar("smaug") baz(1, 2, 3) It is very much like an array literal. And consider how we bind values to parameter names: **const** foo = () => ... **const** bar = (name) => ... **const** baz = (a, b, c) => ...

It _looks_ like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let’s do that: _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- 85

Composing and Decomposing Data **const** numbers = (...nums) => nums; numbers(1, 2, 3, 4, 5) _//=> [1,2,3,4,5]_ **const** headAndTail = (head, ...tail) => [head, tail]; headAndTail(1, 2, 3, 4, 5) _//=> [1,[2,3,4,5]]_ Gathering works with parameters! This is very useful indeed, and we’ll see more of it in a moment.[59] 59Gathering in parameters has a long history, and the usual terms are to call gathering “pattern matching” and to call a name that is bound to gathered values a “rest parameter.” The term “rest” is perfectly compatible with gather: “Rest” is the noun, and “gather” is the verb. We _gather_ the _rest_ of the parameters. _(javascriptallonge.pdf (source-range-83ecb080-00131))_
- 87

Composing and Decomposing Data **const** [first, ...rest] = []; first _//=> undefined_ rest _//=> []:_ **const** [first, ...rest] = ["foo"]; first _//=> "foo"_ rest _//=> []_ **const** [first, ...rest] = ["foo", "bar"]; first _//=> "foo"_ rest _//=> ["bar"]_ **const** [first, ...rest] = ["foo", "bar", "baz"]; first _//=> "foo"_ rest _//=> ["bar","baz"]_ For the purpose of this exploration, we will presume the following:[61] **const** isEmpty = ([first, ...rest]) => first === **undefined** ; isEmpty([]) _//=> true_ isEmpty([0]) _//=> false_ isEmpty([[]]) _//=> false_

Armed with our definition of an empty list and with what we’ve already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using

> 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0, but we are doing backflips to keep this within a very small and contrived playground. _(javascriptallonge.pdf (source-range-83ecb080-00133))_
- Composing and Decomposing Data

88 its .length. But as an exercise, how would we write a length function using just what we have already?

First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_

We need something for when the array isn’t empty. If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest). Well, the length of first is 1, there’s just one element at the front. But we don’t know the length of rest. If only there was a function we could call… Like length!

**const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

Let’s try it!

length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_

Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

## **linear recursion**

“Recursion” sometimes seems like an elaborate party trick. There’s even a joke about this:

When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. They find a bunsen burner, a sparker, a tap, an empty beaker, a stand, and a card with the instructions “boil water.” _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- 90

Composing and Decomposing Data **const** flatten = ([first, ...rest]) => { **if** (first === **undefined** ) { **return** []; } **else if** (!Array.isArray(first)) { **return** [first, ...flatten(rest)]; } **else** { **return** [...flatten(first), ...flatten(rest)]; } } flatten(["foo", [3, 4, []]]) _//=> ["foo",3,4]_ Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions.

## **mapping**

Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let’s write our own using linear recursion.

If we want to square each number in a list, we could write: **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ And if we wanted to “truthify” each element in a list, we could write: _(javascriptallonge.pdf (source-range-83ecb080-00136))_
- Composing and Decomposing Data

91 **const** truthyAll = ([first, ...rest]) => first === **undefined**

? [] : [!!first, ...truthyAll(rest)]; truthyAll([ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_ This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

Given the signature: **const** mapWith = (fn, array) => _// ..._

We can write it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ mapWith((x) => !!x, [ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_

## **folding**

With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-00137))_
- 93

Composing and Decomposing Data **const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ And to return to our first example, our version of length can be written as a fold: **const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) _//=> 5_

## **summary**

Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized cases of mapping and folding are especially useful and can be used to build other functions. And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-83ecb080-00139))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- 83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- If only there was a function we could call… Like length! _(javascriptallonge.pdf (source-range-83ecb080-00134))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00134))_

> Composing and Decomposing Data 88 its .length. But as an exercise, how would we write a length function using just what we have already? First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_ We need something for when the array isn’t empty. If an array is not empty, and we break it into two

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00135))_

| entry | content |
| --- | --- |
| 1 | Divide the problem into smaller problems |
| 2 | If a smaller problem is solvable, solve the small problem |
| 3 | If a smaller problem is not solvable, divide and conquer that problem |
| 4 | When all small problems have been solved, compose the solutions into one big solution The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us: The usual “terminal case” will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn’t an array, we don’t flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we’ll flatten it and put it together with the rest of our solution. > 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. Unfolds can be thought of a “path” through a data structure, and flattening a tree is equivalent to a depth-first traverse. |

<details>
<summary>Raw table text</summary>

```
Composing and Decomposing Data 

89 

Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. After a bit the water boils, and they turn off the burner and are lead to a second bench. 

Once again, there is a card that reads, “boil water.” But this time, the beaker is on the stand over the burner, as left behind by the previous student. The engineers light the burner immediately. Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. 

There is more to recursive solutions that simply functions that invoke themselves. Recursive algorithms follow the “divide and conquer” strategy for solving a problem: 

1. Divide the problem into smaller problems 

2. If a smaller problem is solvable, solve the small problem 

3. If a smaller problem is not solvable, divide and conquer that problem 

4. When all small problems have been solved, compose the solutions into one big solution 

The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. 

This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] 

We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us: 

Array.isArray("foo") 

- _//=> false_ 

Array.isArray(["foo"]) 

- _//=> true_ 

The usual “terminal case” will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn’t an array, we don’t flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we’ll flatten it and put it together with the rest of our solution. 

So our first cut at a flatten function will look like this: 

> 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. Unfolds can be thought of a “path” through a data structure, and flattening a tree is equivalent to a depth-first traverse.
```

</details>
