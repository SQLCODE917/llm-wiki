---
page_id: javascriptallonge-statement
page_kind: concept
summary: Statement: 6 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-statement@a84bdf3b02f653b1a9f7c0e3614b89b7
---

# Statement

What [[javascriptallonge]] covers about statement:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-7239e085-00288))_

### And also: / That Constant Coffee Craving / nested blocks

- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-7239e085-00442))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-7239e085-00465))_

- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-7239e085-00481))_

### And also: / Summary / Functions

- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-7239e085-00649))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-7239e085-00847))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00439))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 2: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00443))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Technical frame 3: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00444))_

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

### Technical frame 4: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00445))_

```
//=> true
```

### Technical frame 5: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00482))_

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 6: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00483))_

```
})(2)
//=> 6.2831853
```

### Technical frame 7: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00486))_

```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

### Technical frame 8: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00488))_

```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

### Technical frame 9: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

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

### Technical frame 10: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

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


## Related pages

- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from And also: / Summary / Functions: Blocks also create scopes if const statements are within them.; Block shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do ... [truncated]; Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: const surname = (name) => { const [first, last] = name; return last; } surname(["Reginald", "Braithwaite"]) //=> "Braithwaite" (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (5 shared atom(s))
- [[javascriptallonge-bound]] - shared technical atoms: Bound shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (4 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else { const odd = (y) => !even(y); return odd(x - 1); } (3 shared atom(s))
- [[javascriptallonge-seen]] - shared technical atoms: Seen shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (3 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms: Environment shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (2 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (2 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: const unwrap = (wrapped) => { const [something] = wrapped; return something; } unwrap(["present"]) //=> "present" (1 shared atom(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies: One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. (1 shared statement(s))

## Source

- [[javascriptallonge]]
