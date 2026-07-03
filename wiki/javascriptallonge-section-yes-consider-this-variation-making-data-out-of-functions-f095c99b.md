---
page_id: javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-f095c99b
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation: / Making Data Out Of Functions: 90 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-f095c99b@e9387f723571364750683d97470fbe0c
---

# Yes. Consider this variation: / Making Data Out Of Functions

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-b8b28d41]] - broader source section: Yes. Consider this variation:
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-a-return-to-backward-thinking-b86dc74c]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-backwardness-d9db07eb]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions / backwardness
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-functions-are-not-the-real-point-4469615c]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions / functions are not the real point
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-lists-with-functions-as-data-6f298a2f]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-say-please-4edc5a79]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-kestrel-and-the-idiot-868e3ae2]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot
- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-vireo-6fe9a149]] - narrower source section: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

## Statements

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-7239e085-01328))_
- A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-7239e085-01330))_
- They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions. _(javascriptallonge.pdf (source-range-7239e085-01331))_
- The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-7239e085-01333))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-7239e085-01328))_
- For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-7239e085-01331))_

## Statements by subsection

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

### Technical frame 1: Yes. Consider this variation: / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01330))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01329))_

<a id="atom-technical-atom-8099f5b267d8f12e"></a>

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest.first
//=> 2
OneTwoThree.rest.rest.first
//=> 3
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 2: Yes. Consider this variation: / Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01358))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01355))_

<a id="atom-technical-atom-a507715e23aece58"></a>

```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

### Technical frame 3: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01367))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01366))_

<a id="atom-technical-atom-33d508801ab09389"></a>

```
(first, second) => (selector) => selector(first)(second)
```

### Technical frame 4: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01370))_

<a id="atom-technical-atom-f5a74a636a28bf0f"></a>

```
const first = K,
second = K(I),
pair = (first) => (second) => (selector) => selector(first)(second);
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 5: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01371))_

<a id="atom-technical-atom-efdd17c1e988c898"></a>

> If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) .

### Technical atom 6

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
