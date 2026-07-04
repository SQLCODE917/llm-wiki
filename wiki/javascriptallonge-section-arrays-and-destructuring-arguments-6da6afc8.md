---
page_id: javascriptallonge-section-arrays-and-destructuring-arguments-6da6afc8
page_kind: source
page_family: section-reference
summary: Arrays and Destructuring Arguments: 29 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-arrays-and-destructuring-arguments-6da6afc8@6ecfc53ca2bbca95e51b0f41b13345ee
---

# Arrays and Destructuring Arguments

From [[javascriptallonge]].

## Statements

- Composing and Decomposing Data 

78 

## **Arrays and Destructuring Arguments** 

While we have mentioned arrays briefly, we haven’t had a close look at them. Arrays are JavaScript’s “native” representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. 

## **array literals** 

JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: 

[] 

_//=> []_ 

We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. Whitespace is optional: 

[1] _//=> [1]_ [2, 3, 4] _//=> [2,3,4]_ 

Any expression will work: 

[ 2, 3, 2 + 2 ] _//=> [2,3,4]_ 

Including an expression denoting another array: 

[[[[[]]]]] 

This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. 

Any expression will do, including names: _(javascriptallonge.pdf (source-range-af806fb1-00121))_
- Composing and Decomposing Data 

79 

**const** wrap = (something) => [something]; 

wrap("lunch") _//=> ["lunch"]_ 

Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: 

[] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_ 

**const** array_of_one = () => [1]; 

array_of_one() === array_of_one() _//=> false_ 

## **element references** 

Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: 

**const** oneTwoThree = ["one", "two", "three"]; 

oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_ 

As we can see, JavaScript Arrays are zero-based[56] . 

We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind? 

56https://en.wikipedia.org/wiki/Zero-based_numbering _(javascriptallonge.pdf (source-range-af806fb1-00122))_
- Composing and Decomposing Data 

80 

**const** x = [], a = [x]; 

a[0] === x 

_//=> true, arrays store references to the things you put in them._ 

## **destructuring arrays** 

There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name: 

**const** wrap = (something) => [something]; 

Let’s expand it to use a block and an extra name: 

**const** wrap = (something) => { **const** wrapped = [something]; 

**return** wrapped; } 

wrap("package") _//=> ["package"]_ 

The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string. 

In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: 

**const** unwrap = (wrapped) => { **const** [something] = wrapped; 

**return** something; } 

unwrap(["present"]) _//=> "present"_ 

The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-af806fb1-00123))_
- Composing and Decomposing Data 

81 

**const** surname = (name) => { **const** [first, last] = name; **return** last; } 

surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_ 

We could do the same thing with (name) => name[1], but destructuring is code that resembles the data it consumes, a valuable coding style. 

Destructuring can nest: 

**const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation; 

**return** ` **${** first **}** is a **${** occupation **}** `; } description([["Reginald", "Braithwaite"], "programmer"]) _//=> "Reginald is a programmer"_ 

## **gathering** 

Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: 

**const** [car, ...cdr] = [1, 2, 3, 4, 5]; 

car _//=> 1_ cdr _//=> [2, 3, 4, 5]_ 

car and cdr[57] are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst, or head and tail. We will use a common convention and call variables we gather rest, but refer to the ... operation as a “gather,” following Kyle Simpson’s example.[58] 

Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write 

> 57https://en.wikipedia.org/wiki/CAR_and_CDR 

> 58Kyle Simpson is the author of You Don’t Know JS, available here _(javascriptallonge.pdf (source-range-af806fb1-00124))_
- 82 

Composing and Decomposing Data 

**const** [...butLast, last] = [1, 2, 3, 4, 5]; _//=> ERROR_ **const** [first, ..., last] = [1, 2, 3, 4, 5]; _//=> ERROR_ 

Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. So if 

**const** wrapped = [something]; 

Then: 

**const** [unwrapped] = something; 

What is the reverse of gathering? We know that: 

**const** [car, ...cdr] = [1, 2, 3, 4, 5]; 

What is the reverse? It would be: 

**const** cons = [car, ...cdr]; 

Let’s try it: 

**const** oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] _//=> ["zero","one","two","three"]_ 

It works! We can use ... to place the elements of an array inside another array. We say that using ... to destructure is gathering, and using it in a literal to insert elements is called “spreading.” 

## **destructuring is not pattern matching** 

Some other languages have something called _pattern matching_ , where you can write something like a destructuring assignment, and the language decides whether the “patterns” matches at all. If it does, assignments are made where appropriate. 

In such a language, if you wrote something like: _(javascriptallonge.pdf (source-range-af806fb1-00125))_
- Composing and Decomposing Data 

83 

**const** [what] = []; 

That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore: 

**const** [what] = []; 

what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_ 

And if there aren’t any items to assign with ..., JavaScript assigns an empty array: 

**const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_ 

From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. 

## **destructuring and return values** 

Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring: _(javascriptallonge.pdf (source-range-af806fb1-00126))_
- 84 

Composing and Decomposing Data 

**const** description = (nameAndOccupation) => { **if** (nameAndOccupation.length < 2) { **return** ["", "occupation missing"] } **else** { **const** [[first, last], occupation] = nameAndOccupation; **return** [` **${** first **}** is a **${** occupation **}** `, "ok"]; } } 

**const** [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); 

reg _//=> "Reginald is a programmer"_ status _//=> "ok"_ 

## **destructuring parameters** 

Consider the way we pass arguments to parameters: 

foo() bar("smaug") baz(1, 2, 3) 

It is very much like an array literal. And consider how we bind values to parameter names: 

**const** foo = () => ... **const** bar = (name) => ... **const** baz = (a, b, c) => ... 

It _looks_ like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let’s do that: _(javascriptallonge.pdf (source-range-af806fb1-00127))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-af806fb1-00121))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-af806fb1-00121))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-af806fb1-00121))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-af806fb1-00123))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-af806fb1-00126))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-af806fb1-00127))_

## Technical atoms

### Technical frame 1: Arrays and Destructuring Arguments

**Context:** _(javascriptallonge.pdf (source-range-af806fb1-00123))_

> Composing and Decomposing Data 

80 

**const** x = [], a = [x]; 

a[0] === x 

_//=> true, arrays store references to the things you put in them._ 

## **destructuring arrays** 

There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name: 

**const** wrap = (something) => [something]; 

Let’s expand it to 

**Atom:** _(javascriptallonge.pdf (source-range-af806fb1-00122))_

<a id="atom-technical-atom-aa535d9e48793a76"></a>

> **const** wrap = (something) => [something];
