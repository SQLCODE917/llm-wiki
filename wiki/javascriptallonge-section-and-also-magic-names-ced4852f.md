---
page_id: javascriptallonge-section-and-also-magic-names-ced4852f
page_kind: source
page_family: section-reference
summary: And also: / Magic Names: 33 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-magic-names-ced4852f@729a296670b6af405aa2f5e8d66da509
---

# And also: / Magic Names

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-3f50274e]] - broader source section: And also:
- [[javascriptallonge-section-and-also-magic-names-magic-names-and-fat-arrows-a644f644]] - narrower source section: And also: / Magic Names / magic names and fat arrows
- [[javascriptallonge-section-and-also-magic-names-the-function-keyword-b8eb1a25]] - narrower source section: And also: / Magic Names / the function keyword

## Statements

- When a function is applied to arguments (or 'called'), JavaScript binds the values of arguments to the function's argument names in an environment created for the function's execution. What we haven't discussed so far is that JavaScript also binds values to some 'magic' names in addition to any you put in the argument list. 42 _(javascriptallonge.pdf (source-range-7239e085-00605))_

## Statements by subsection

### And also: / Magic Names / the function keyword

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-7239e085-00607))_
- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-7239e085-00608))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-7239e085-00617))_

### And also: / Magic Names / magic names and fat arrows

- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-7239e085-00620))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-7239e085-00625))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working: _(javascriptallonge.pdf (source-range-7239e085-00627))_
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-00628))_
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code. _(javascriptallonge.pdf (source-range-7239e085-00631))_
- But sometimes, a function is a small-f function. It's a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-7239e085-00632))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith . _(javascriptallonge.pdf (source-range-7239e085-00633))_
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-7239e085-00620))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . _(javascriptallonge.pdf (source-range-7239e085-00627))_
- It has a name, it is called by different pieces of code, it's a first-class entity in the code. _(javascriptallonge.pdf (source-range-7239e085-00631))_

## Technical atoms

### Technical frame 1: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00617))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00609))_

<a id="atom-technical-atom-013351b465690d3d"></a>

```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical atom 2

<a id="atom-technical-atom-40032b1d8caeb152"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00612))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00613))_

```text
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

</details>
