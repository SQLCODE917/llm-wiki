---
page_id: javascriptallonge-section-why-const-and-let-were-invented-32b697a4
page_kind: source
summary: **why const and let were invented**: 22 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-why-const-and-let-were-invented-32b697a4@cf183268b4f1aa15046125f052fcc440
---

# **why const and let were invented**

From [[javascriptallonge]].

## Statements

- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). _(javascriptallonge.pdf (source-range-83ecb080-01820))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-83ecb080-01820))_
- We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. _(javascriptallonge.pdf (source-range-83ecb080-01821))_
- Hopefully, you can think of a faster way to calculate this sum.[72] And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. _(javascriptallonge.pdf (source-range-83ecb080-01823))_
- > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- The other kids were adding the numbers like this: 1 + 2 + 3 + . _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- There are 50 pairs of numbers, so the answer is 50*101 = 5050. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- If you notice every pair of numbers adds up to 101. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- The answer is that pesky var i. _(javascriptallonge.pdf (source-range-83ecb080-01833))_
- But at the time we _call_ one of the functions, i has the value 3, which is why the loop terminated. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- Now, at the time we created each function, i had a sensible value, like 0, 1, or 2. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let, programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-83ecb080-01840))_
- This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-83ecb080-01844))_
- The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-83ecb080-01845))_
- The purpose of your own code is to get things done. _(javascriptallonge.pdf (source-range-83ecb080-01845))_
- That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. _(javascriptallonge.pdf (source-range-83ecb080-01845))_

## Technical atoms

> Context: We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var: > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . 
_(context: javascriptallonge.pdf (source-range-83ecb080-01821, source-range-83ecb080-01824))_

> **var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050
_(source: javascriptallonge.pdf (source-range-83ecb080-01822))_

> Context: Again, so far, so good. Let’s try one of our functions: What went wrong? Why didn’t it give us ‘Hello, Raganwald, my name is Friedrich’? The answer is that pesky var i. Remember that i is bound in the surrounding environment, so it’s as if we wrote:
_(context: javascriptallonge.pdf (source-range-83ecb080-01831, source-range-83ecb080-01833))_

> introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is undefined'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01832))_
