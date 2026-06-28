---
page_id: javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-e932af8c
page_kind: source
summary: values are expressions / Arrays and Destructuring Arguments: 33 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-e932af8c@a9f7242dd3999d26462600606b32e7e4
---

# values are expressions / Arrays and Destructuring Arguments

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-array-literals-1ff63801]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-element-references-e9acc92e]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-destructuring-arrays-a4ceea6e]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-gathering-7ced2d35]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-destructuring-is-not-pattern-matching-072f7058]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-arrays-and-destructuring-arguments-destructuring-parameters-f448aa2d]] - narrower source section

## Statements

- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Arrays are JavaScript’s “native” representation of lists. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- While we have mentioned arrays briefly, we haven’t had a close look at them. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-00832))_

## Statements by subsection

### values are expressions / Arrays and Destructuring Arguments / array literals

- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-00834))_
- We can create an empty array: [] _//=> []_ We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. _(javascriptallonge.pdf (source-range-83ecb080-00834))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-00836))_
- [ 2, 3, 2 + 2 ] _//=> [2,3,4]_ Including an expression denoting another array: [[[[[]]]]] This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-83ecb080-00836))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-00836))_

### values are expressions / Arrays and Destructuring Arguments / element references

- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-00841))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-83ecb080-00842))_

### values are expressions / Arrays and Destructuring Arguments / destructuring arrays

- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-00848))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-00848))_
- The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. _(javascriptallonge.pdf (source-range-83ecb080-00851))_
- We could do the same thing with (name) => name[1], but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-83ecb080-00854))_

### values are expressions / Arrays and Destructuring Arguments / gathering

- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-83ecb080-00857))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-83ecb080-00857))_
- Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. _(javascriptallonge.pdf (source-range-83ecb080-00862))_

### values are expressions / Arrays and Destructuring Arguments / destructuring is not pattern matching

- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-83ecb080-00867))_
- 83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- 83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-00870))_

### values are expressions / Arrays and Destructuring Arguments / destructuring parameters

- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-00877))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-00877))_
- This is very useful indeed, and we’ll see more of it in a moment.[59] 59Gathering in parameters has a long history, and the usual terms are to call gathering “pattern matching” and to call a name that is bound to gathered values a “rest parameter.” The term “rest” is perfectly compatible with gather: “Rest” is the noun, and “gather” is the verb. _(javascriptallonge.pdf (source-range-83ecb080-00879))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> 80 **const** x = [], a = [x]; a[0] === x

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00851))_

> The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00853))_

> 81 **const** surname = (name) => { **const** [first, last] = name; **return** last; } surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_
