---
page_id: javascriptallonge-bonus
page_kind: source
summary: bonus from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.175-176
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the bonus chapter from JavaScript Allongé, focusing on lazy evaluation and collection operations in JavaScript.

## Key supported claims

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. (raw/javascriptallonge.pdf p.175-176)
- In Smalltalk, for example, they are known as collect , select , and detect . (raw/javascriptallonge.pdf p.175-176)
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. (raw/javascriptallonge.pdf p.175-176)

## Technical details

### `technical-atom-06627249e05d277a` code

Citation: (raw/javascriptallonge.pdf p.175-176)

```javascript
const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
```

### `technical-atom-88e9bb41a37459ac` code

Citation: (raw/javascriptallonge.pdf p.175-176)

```javascript
const firstInArray = (fn, array) => array.filter(fn)[0];
```

### `technical-atom-071065f77ad2e28e` worked-example

Citation: (raw/javascriptallonge.pdf p.175-176)

In Smalltalk, for example, they are known as collect , select , and detect .

## Related technical details

### From [[javascriptallonge-functional-iterators]]: `technical-atom-66284ad4815503e0` code

Relation: nearby source page; matched terms `doesn`, `javascript`, `method`, `other`

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-5b37e3daf21d3949` worked-example

Relation: nearby source page; matched terms `detect`, `example`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.
