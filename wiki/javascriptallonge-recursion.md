---
page_id: javascriptallonge-recursion
page_kind: concept
summary: Recursion: 3 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-recursion@f3525b93d181d061b6fdac056f57e86b
---

# Recursion

What [[javascriptallonge]] covers about recursion:

## Statements

- Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[55] > 55http://www.cs.yale.edu/homes/perlis-alan/quotes.html _(javascriptallonge.pdf (source-range-83ecb080-00827))_
- Linear recursion is a basic building block of algorithms. _(javascriptallonge.pdf (source-range-83ecb080-00947))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-01025))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00916))_

> This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00917))_

> Array.isArray("foo") - _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00916))_

> This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00918))_

> Array.isArray(["foo"]) - _//=> true_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00929))_

> ? [] : [!!first, ...truthyAll(rest)]; truthyAll([ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_ This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00930))_

> Given the signature: **const** mapWith = (fn, array) => _// ..._


## Related pages

- [[javascriptallonge-element]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-problem]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-rest]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
