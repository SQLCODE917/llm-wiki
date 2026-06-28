---
page_id: javascriptallonge-section-values-are-expressions-iteration-and-iterables-a-look-back-at-functional-iterators-436a0f38
page_kind: source
summary: values are expressions / Iteration and Iterables / a look back at functional iterators: 8 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-iteration-and-iterables-a-look-back-at-functional-iterators-436a0f38@2343920a9a0882cfc51454707d6fce3d
---

# values are expressions / Iteration and Iterables / a look back at functional iterators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-iteration-and-iterables-70b2511b]] - broader source section
- [[javascriptallonge-functional-iterator]] - topic hub
- [[javascriptallonge-section-values-are-expressions-functional-iterators-a4bbe212]] - same source heading

## Statements

- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-83ecb080-01532))_
- 184 **const** Stack1 = () => ({ array:[], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty () { **return this** .index < 0 }, iterator () { **let** iterationIndex = **this** .index; **return** () => { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } }); **const** stack = Stack1(); stack.push("Greetings"); stack.push("to"); stack.push("you!") Served by the Pot: Collections _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- } function, and that’s where this is bound to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-01537))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-01538))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-01538))_
- If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-83ecb080-01543))_
- Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-83ecb080-01543))_
