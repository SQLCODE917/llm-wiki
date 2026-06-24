---
page_id: javascriptallonge-combinators
page_kind: source
summary: combinators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.68-69
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on combinators from JavaScript Allongé, covering the mathematical definition of combinators, their implementation in JavaScript, and the practical use of combinators like compose.

## Key supported claims

- If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators, as described in (raw/javascriptallonge.pdf p.68-69).
- We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36, as described in (raw/javascriptallonge.pdf p.68-69).
- In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function, as described in (raw/javascriptallonge.pdf p.68-69).
- We won't be strict about using only previously defined combinators in their construction, as described in (raw/javascriptallonge.pdf p.68-69).

## Technical details

### `technical-atom-5a64ca902d2a5ea5` code

Citation: (raw/javascriptallonge.pdf p.68-69)

```javascript
const compose = (a, b) => (c) => a(b(c)) Let's say we have: const addOne = (number) => number + 1; const doubleOf = (number) => number * 2; With compose , anywhere you would write const doubleOfAddOne = (number) => doubleOf(addOne(number)); You could also write: const doubleOfAddOne = compose(doubleOf, addOne);
```

### `technical-atom-c5b335eb5ded24ba` formula

Citation: (raw/javascriptallonge.pdf p.68-69)

36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20

### `technical-atom-573c28eb9a1b4a43` exception

Citation: (raw/javascriptallonge.pdf p.68-69)

'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35

### `technical-atom-0c6ee2e3b1a2e9c0` exception

Citation: (raw/javascriptallonge.pdf p.68-69)

In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function.

### `technical-atom-1fb1b6b37295dce2` exception

Citation: (raw/javascriptallonge.pdf p.68-69)

We won't be strict about using only previously defined combinators in their construction.

### `technical-atom-5b7054e41352d245` exception

Citation: (raw/javascriptallonge.pdf p.68-69)

While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

### `technical-atom-6fd30e91218f411d` worked-example

Citation: (raw/javascriptallonge.pdf p.68-69)

We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .

### `technical-atom-57ed8734e50b061f` worked-example

Citation: (raw/javascriptallonge.pdf p.68-69)

This is, of course, just one example of many.

## Related technical details

### From [[javascriptallonge-function-declarations]]: `technical-atom-f07b324de3d238c3` code

Relation: nearby source page; matched terms `function`, `javascript`, `return`

Citation: (raw/javascriptallonge.pdf p.65-66)

```javascript
( function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScript behaves as if we'd written: ( function () { {
```

### From [[javascriptallonge-magic-names-and-fat-arrows]]: `technical-atom-fa080dbd9241b746` code

Relation: nearby source page; matched terms `arguments`, `function`, `return`

Citation: (raw/javascriptallonge.pdf p.75-77)

```javascript
( function () { return ( function () { return arguments[0]; })('inner'); })('outer') //=> "inner"
```

### From [[javascriptallonge-function-declaration-caveats-34]]: `technical-atom-f822e3366648ac82` worked-example

Relation: nearby source page; matched terms `example`, `following`, `function`, `javascript`, `some`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.66-67)

Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

### From [[javascriptallonge-the-function-keyword]]: `technical-atom-9b2e7b5be612a8dd` code

Relation: nearby source page; matched terms `function`, `return`

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
function (n) { return (1.618**n - -1.618**-n) / 2.236; }
```
