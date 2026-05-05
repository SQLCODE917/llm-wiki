---
title: Data Structures
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Data Structures

Data structures in programming involve strategies for managing how data is stored, accessed, and modified, particularly when multiple tasks or functions interact with shared data. Copy-on-write (COW) is a specific strategy where copies are made only when writing to shared data structures, preventing interference between modifications.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Copy-on-write is a strategy where copies are made only when writing to shared data structures, preventing interference between modifications. | "This strategy of waiting to copy until you are writing is called copy-on-write, or "COW:"" | normalized:L5299 | [Source](../sources/js-allonge.md) |
| Copy-on-write prevents changes from becoming visible to all tasks by creating separate copies before modification. | "Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks." | normalized:L5308 | [Source](../sources/js-allonge.md) |
| Copy-on-write is more efficient than pessimistic copying when making infrequent small changes to shared data structures. | "It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive." | normalized:L5312 | [Source](../sources/js-allonge.md) |
| When constructing data, ownership allows liberal mutation, but once data is given to others, conservative strategies like copy-on-write should be used. | "Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write." | normalized:L5315 | [Source](../sources/js-allonge.md) |

## Why it matters

Copy-on-write is a memory-efficient technique for handling shared data structures in concurrent environments. By deferring the cost of copying until a write operation occurs, it avoids unnecessary duplication of data when reads are frequent and writes are rare. This approach helps maintain data integrity across multiple tasks or threads, ensuring that modifications made by one task don't inadvertently affect others until those changes are actually committed. Understanding when and how to apply copy-on-write is crucial for optimizing performance in systems where data sharing and mutability intersect.

## Source pages

- [Source](../sources/js-allonge.md)