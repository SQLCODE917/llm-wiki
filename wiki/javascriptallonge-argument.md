---
page_id: javascriptallonge-argument
page_kind: concept
summary: Argument: 13 statement(s) and 21 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-argument@21568237b6f284945170e1de9793162d
---

# Argument

What [[javascriptallonge]] covers about argument:

## Statements

- This works just fine, because arguments[0] refers to the 3 we passed to the function row. _(javascriptallonge.pdf (source-range-83ecb080-00890))_
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- How arguments are used in a body’s expression is probably perfectly obvious to you from the examples, especially if you’ve used any programming language (except for the dialect of BASIC–which I recall from my secondary school–that didn’t allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- Well for arguments, that is very simple. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-01074))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01298))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-83ecb080-01491))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00397))_

> I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00398))_

> (diameter) => diameter * 3.14159265

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00400))_

> Remember that to apply a function with no arguments, we wrote (() => {})(). To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00401))_

> ((diameter) => diameter * 3.14159265)(2)

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00429))_

> Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we’re going to work our way up from (diameter) => diameter * 3.14159265 to functions like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00430))_

> - (x) => (y) => x

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00438))_

> How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00439))_

> ((x) => x)(2) _//=> 2_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00461))_

> Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00459))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00462))_

> And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00464))_

> - ((ref1, ref2) => ref1 === ref2)(value, value)

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00840, source-range-83ecb080-00843))_

> Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00841))_

> _.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00843))_

> This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00844))_

> **const** squareAll = (array) => map(array, (n) => n * n);

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00846))_

> **const** mapWith = (fn) => (array) => map(array, fn);

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00847))_

> **const** squareAll = mapWith((n) => n * n);

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00848))_

> squareAll([1, 2, 3]) _//=> [1, 4, 9]_

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00866))_

> The first magic name is this, and it is bound to something called the function’s context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00867))_

> **const** plus = **function** (a, b) { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00868, source-range-83ecb080-00870))_

> Although arguments looks like an array, it isn’t an array: It’s more like an object[43] that happens to bind some values to properties with names that look like integers starting with zero: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00869))_

> **const** args = **function** (a, b) { **return** arguments; } args(2,3) _//=> { '0': 2, '1': 3 }_

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00876))_

> When discussing objects, we’ll discuss properties in more depth. Here’s something interesting about arguments:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00877))_

> **const** howMany = **function** () { **return** arguments['length']; } howMany() _//=> 0_ howMany('hello') _//=> 1_ howMany('sharks', 'are', 'apex', 'predators') _//=> 4_

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00885))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. And thus arguments[0] will refer to "outer", not to "inner":

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00886))_

> ( **function** () { **return** (() => arguments[0])('inner'); })('outer') _//=> "outer"_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01074))_

> Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01075))_

> **const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01074))_

> Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01076))_

> first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_

### Technical atom 18

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00019))_

| **Composing and Decomposing Data** . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | **77** |
| --- | --- | --- |
| Arrays and Destructuring Arguments<br>. . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects<br>. . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment<br>. . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| **Recipes with Data** . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | **168** |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| **A Warm Cup: Basic Strings and Quasi-Literals** | . . . . . . . . . . . . . . . . . . . . . . . . | **179** |
| **Served by the Pot: Collections** . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | **182** |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| **The Golden Crema: Appendices and Afterwords** | . . . . . . . . . . . . . . . . . . . . . . . | **265** |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |

<details>
<summary>Raw table text</summary>

```
|**Composing and Decomposing Data** . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**77**|
|---|---|---|
|Arrays and Destructuring Arguments<br>. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|78|
|Self-Similarity . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|86|
|Tail Calls (and Default Arguments) . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|94|
|Garbage, Garbage Everywhere . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|103|
|Plain Old JavaScript Objects<br>. . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|109|
|Mutation . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|118|
|Reassignment<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|125|
|Copy on Write . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|135|
|Tortoises, Hares, and Teleporting Turtles . . .|. . . . . . . . . . . . . . . . . . . . . . . .|141|
|Functional Iterators . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|144|
|Making Data Out Of Functions . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|154|
|**Recipes with Data** . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**168**|
|mapWith . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|170|
|Flip . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|172|
|Object.assign . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|175|
|Why? . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|178|
|**A Warm Cup: Basic Strings and Quasi-Literals**|. . . . . . . . . . . . . . . . . . . . . . . .|**179**|
|**Served by the Pot: Collections** . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**182**|
|Iteration and Iterables . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|183|
|Generating Iterables . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|201|
|Lazy and Eager Collections . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|223|
|Interlude: The Carpenter Interviews for a Job|. . . . . . . . . . . . . . . . . . . . . . . .|238|
|Interactive Generators . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|250|
|Basic Operations on Iterables . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|261|
|**The Golden Crema: Appendices and Afterwords**|. . . . . . . . . . . . . . . . . . . . . . .|**265**|
|How to run the examples . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|266|
|Thanks! . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|268|
|Copyright Notice . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|270|
|About The Author . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|274|
```

</details>

### Technical atom 19

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00020))_

| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |

<details>
<summary>Raw table text</summary>

```
| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |
```

</details>

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01453))_

> We can use it with ridiculously large arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01455))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
|0,|1,|2,|3,|4,|5,|6,|7,|8,|9,|
|---|---|---|---|---|---|---|---|---|---|
|10,|11,|12,|13,|14,|15,|16,|17,|18,|19,|
|20,|21,|22,|23,|24,|25,|26,|27,|28,|29,|
|30,|31,|32,|33,|34,|35,|36,|37,|38,|39,|
|40,|41,|42,|43,|44,|45,|46,|47,|48,|49,|
|50,|51,|52,|53,|54,|55,|56,|57,|58,|59,|
|60,|61,|62,|63,|64,|65,|66,|67,|68,|69,|
|70,|71,|72,|73,|74,|75,|76,|77,|78,|79,|
|80,|81,|82,|83,|84,|85,|86,|87,|88,|89,|
|90,|91,|92,|93,|94,|95,|96,|97,|98,|99,|
```

</details>

### Technical atom 21

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01462))_

> In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01463))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (5 shared statement(s), 14 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms (1 shared atom(s))

## Source

- [[javascriptallonge]]
