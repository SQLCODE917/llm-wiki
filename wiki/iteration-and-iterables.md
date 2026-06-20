---
page_id: iteration-and-iterables
page_kind: source
summary: Chapter on iteration and iterables in JavaScriptAllonge, covering functional iterators, iterator objects, and the for...of loop.
sources: raw/javascriptallonge.pdf p.206-223
updated: 2026-06-19
---

# Iteration and Iterables

This chapter covers the concept of iteration and iterables in JavaScript. It discusses functional iterators, iterator objects, and how to use the `for...of` loop with iterables. The chapter also explores ordered collections, operations on ordered collections like `mapWith`, `filterWith`, and `untilWith`, and how to create new iterables from existing ones.

## Key Concepts

- **Functional Iterators**: Iterators implemented as functions that return the next element in the sequence.
- **Iterator Objects**: Objects with a `.next()` method that returns the next element in the sequence.
- **Symbol.iterator**: A special symbol that represents the method that objects should use to return an iterator object.
- **for...of loop**: A loop that works directly with any object that is iterable, meaning it works with any object that has a `Symbol.iterator` method that returns an object iterator.
- **Ordered Collections**: Collections that represent a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning.
- **Collection Operations**: Operations that take an ordered collection and return another ordered collection, preserving the collection semantics.

## Summary

The chapter explains how JavaScript provides a standard way to iterate over the contents of collections using the `Symbol.iterator` method. It demonstrates how to implement iterators both as functions and as objects, and how to use the `for...of` loop and the spread operator with iterable objects. The chapter also covers operations on ordered collections such as `mapWith`, `filterWith`, and `untilWith`, and how these operations preserve the semantics of the original collections.

## Examples

### Functional Iterators

The chapter shows how to implement a stack with a functional iterator method:

```javascript
const Stack1 = () => ({
  array: [],
  index: -1,
  push(value) {
    return this.array[this.index += 1] = value;
  },
  pop() {
    const value = this.array[this.index];
    this.array[this.index] = undefined;
    if (this.index >= 0) {
      this.index -= 1
    }
    return value
  },
  isEmpty() {
    return this.index < 0
  },
  iterator() {
    let iterationIndex = this.index;
    return () => {
      if (iterationIndex > this.index) {
        iterationIndex = this.index;
      }
      if (iterationIndex < 0) {
        return {done: true};
      } else {
        return {done: false, value: this.array[iterationIndex--]}
      }
    }
  }
});
```

### Iterator Objects

The chapter also shows how to implement a stack with an iterator object:

```javascript
const Stack2 = () => ({
  array: [],
  index: -1,
  push(value) {
    return this.array[this.index += 1] = value;
  },
  pop() {
    const value = this.array[this.index];
    this.array[this.index] = undefined;
    if (this.index >= 0) {
      this.index -= 1
    }
    return value
  },
  isEmpty() {
    return this.index < 0
  },
  iterator() {
    let iterationIndex = this.index;
    return {
      next() {
        if (iterationIndex > this.index) {
          iterationIndex = this.index;
        }
        if (iterationIndex < 0) {
          return {done: true};
        } else {
          return {done: false, value: this.array[iterationIndex--]}
        }
      }
    }
  }
});
```

### Symbol.iterator

The chapter demonstrates how to use `Symbol.iterator` to make a stack iterable:

```javascript
const Stack3 = () => ({
  array: [],
  index: -1,
  push(value) {
    return this.array[this.index += 1] = value;
  },
  pop() {
    const value = this.array[this.index];
    this.array[this.index] = undefined;
    if (this.index >= 0) {
      this.index -= 1
    }
    return value
  },
  isEmpty() {
    return this.index < 0
  },
  [Symbol.iterator]() {
    let iterationIndex = this.index;
    return {
      next() {
        if (iterationIndex > this.index) {
          iterationIndex = this.index;
        }
        if (iterationIndex < 0) {
          return {done: true};
        } else {
          return {done: false, value: this.array[iterationIndex--]}
        }
      }
    }
  }
});
```

## Operations on Ordered Collections

The chapter introduces several operations on ordered collections:

- `mapWith`: Takes an ordered collection and returns another ordered collection representing a mapping over the original.
- `filterWith`: Takes an ordered collection and returns another ordered collection representing a filter over the original.
- `untilWith`: Takes an ordered collection and returns another ordered collection representing a filter until a condition is met.

## From Function

The chapter also covers how to create a `.from` function that gathers an iterable into a particular collection type:

```javascript
Stack3.from = function(iterable) {
  const stack = this();
  for (let element of iterable) {
    stack.push(element);
  }
  return stack;
}
```
