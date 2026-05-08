---
title: Data Types
type: concept
tags: [javascript, data-types, primitives, reference-types]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1229-L1229
  - js-allonge:normalized:L355-L356
  - js-allonge:normalized:L373-L373
  - js-allonge:normalized:L373-L374
  - js-allonge:normalized:L389-L389
  - js-allonge:normalized:L397-L397
  - js-allonge:normalized:L397-L398
  - js-allonge:normalized:L401-L405
  - js-allonge:normalized:L407-L408
  - js-allonge:normalized:L425-L425
  - js-allonge:normalized:L449-L450
  - js-allonge:normalized:L539-L540
  - js-allonge:normalized:L569-L569
---

# Data Types

## Summary

Data types in JavaScript categorize values into distinct groups that determine their behavior and capabilities. Primitive types include strings, numbers, booleans, null, undefined, and symbols, while reference types encompass objects, arrays, and functions. Understanding these distinctions is key to working effectively with JavaScript's value system.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Every value in JavaScript can be considered an expression, as demonstrated by the analogy of handing a café Cubano to a barista who returns it unchanged. | "All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, "I want one of these." The..." | `normalized:L355-L356` | [Source](../sources/js-allonge.md) |
| An espresso produced by combining boiling water and ground coffee illustrates how certain operations create expressions rather than values. | "Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value.[11]..." | `normalized:L373-L374` | [Source](../sources/js-allonge.md) |
| Strings function as values that can be used directly in expressions, but concatenating strings with operators creates new expressions. | "Now we see that "strings" are values, and you can make an expression out of strings and an operator +. Since strings are values, they are also expressions by themselves. But strings with operators..." | `normalized:L389-L389` | [Source](../sources/js-allonge.md) |
| String concatenation with the '+' operator results in expressions rather than values, since the operation combines two values into a new expression. | "Now we see that "strings" are values, and you can make an expression out of strings and an operator +. Since strings are values, they are also expressions by themselves. But strings with operators..." | `normalized:L389-L389` | [Source](../sources/js-allonge.md) |
| JavaScript uses the strict equality operator (===) to determine if two values are identical. | "In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:" | `normalized:L397-L398` | [Source](../sources/js-allonge.md) |
| The === operator compares values based on their type and content, distinguishing between different types like strings and numbers. | "How does === work, exactly? Imagine that you're shown a cup of coffee. And then you're shown another cup of coffee. Are the two cups "identical?" In JavaScript, there are four possibilities:..." | `normalized:L401-L405` | [Source](../sources/js-allonge.md) |
| When comparing values of the same type but different content, the === operator returns false, as seen with numeric values 5 and 2. | "Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values..." | `normalized:L407-L408` | [Source](../sources/js-allonge.md) |
| An espresso created from boiling water and ground coffee demonstrates that the combination forms an expression rather than a value. | "Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value.[11]..." | `normalized:L373-L373` | [Source](../sources/js-allonge.md) |
| JavaScript determines value identity using the === operator, which checks both type and content for equality. | "In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:" | `normalized:L397-L397` | [Source](../sources/js-allonge.md) |
| Values of primitive types such as strings, numbers, and booleans are identical to others with the same type and content. | "Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with..." | `normalized:L425-L425` | [Source](../sources/js-allonge.md) |
| Arrays and other reference types are unique instances that differ from each other even when visually identical. | "How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other..." | `normalized:L449-L450` | [Source](../sources/js-allonge.md) |
| Functions are treated as values in JavaScript and can be assigned to variables, passed as arguments, and returned from other functions. | "Amazing how such an important idea-naming functions-can be explained _en passant_ in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as "first..." | `normalized:L1229-L1229` | [Source](../sources/js-allonge.md) |
| The phrase 'As Little As Possible About Functions, But No Less' indicates a concise yet complete overview of JavaScript functions. | "## **As Little As Possible About Functions, But No Less**" | `normalized:L539-L540` | [Source](../sources/js-allonge.md) |
| Each evaluation of a function-producing expression yields a new, distinct function instance, unlike arrays which also generate unique instances. | "Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it...." | `normalized:L569-L569` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
