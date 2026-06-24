---
page_id: javascriptallonge-making-data-out-of-functions
page_kind: source
summary: Making Data Out Of Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.177-179
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on modeling data using functions, including K, I, and V combinators.

## Key supported claims

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list (raw/javascriptallonge.pdf p.177-179).
- We can model lists just using functions (raw/javascriptallonge.pdf p.177-179).
- We have used arrays and objects to represent the structure of data, and extensively used the ternary operator to write algorithms that terminate when we reach a base case (raw/javascriptallonge.pdf p.177-179).

## Technical details

### `technical-atom-94b1271483ea8499` code

Citation: (raw/javascriptallonge.pdf p.177-179)

```javascript
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 OneTwoThree.rest.rest.first //=> 3 const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### `technical-atom-8dbeecd17e154409` code

Citation: (raw/javascriptallonge.pdf p.177-179)

```javascript
const K = (x) => (y) => x; const I = (x) => (x); const V = (x) => (y) => (z) => z(x)(y);
```

### `technical-atom-f36933c62676c874` formula

Citation: (raw/javascriptallonge.pdf p.177-179)

76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422

### `technical-atom-9c77a5de5c2d57ec` procedure

Citation: (raw/javascriptallonge.pdf p.177-179)

A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations.

### `technical-atom-cf5b15724c23cd8a` procedure

Citation: (raw/javascriptallonge.pdf p.177-179)

To Mock a Mockingbird 76 established the metaphor of songbirds for the combinators, and ever since then logicians have called the K combinator a 'kestrel,' the B combinator a 'bluebird,' and so forth.

### `technical-atom-5b37e3daf21d3949` worked-example

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

### `technical-atom-ac4a59dfcff9d986` worked-example

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list.

## Related technical details

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-1facdd66430f4b84` code

Relation: nearby source page; matched terms `can`, `code`, `data`, `empty`, `functions`, `length`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(rest(aPair), pair(first(aPair), delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); const doubled = mapWith((x) => x * 2, l123); first(doubled) //=> 2 first(rest(doubled)) //=> 4 first(rest(rest(doubled))) //=> 6 Can we do the same with the linked lists we build out of functions? Yes: const first = K, l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### From [[javascriptallonge-functional-iterators]]: `technical-atom-66284ad4815503e0` code

Relation: nearby source page; matched terms `bind`, `code`, `function`, `method`, `our`, `uses`

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-bafff516faf1e5ae` code

Relation: nearby source page; matched terms `code`, `data`, `empty`, `functions`, `length`, `lists`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest)); length(l123) //=> 3 And mapWith ? const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(aPair(rest), pair(aPair(first))(delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed)); const doubled = mapWith((x) => x * 2, l123) doubled(first) //=> 2 doubled(rest)(first) //=> 4 doubled(rest)(rest)(first) //=> 6
```

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-524bbdeeff2aabb1` code

Relation: nearby source page; matched terms `code`, `data`, `empty`, `functions`, `length`, `lists`

Citation: (raw/javascriptallonge.pdf p.183-186)

```
0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ?
```
