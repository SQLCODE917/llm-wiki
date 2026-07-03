---
page_id: javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-9074fc35
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution: 24 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-9074fc35@1e08732b77857d396c3d85fb746fba5d
---

# We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-196a6679]] - broader source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job

## Statements

- The Carpenter was not surprised at the problem. Bob Plissken was a crafty, almost reptilian recruiter that traded in information and secrets. Whenever Bob sent a candidate to a job interview, he debriefed them afterwards and got them to disclose what questions were asked in the interview. He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- Bob had, in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-7239e085-01830))_
- The Carpenter coughed softly, then began. 'To begin with, I'll transform a game into an iterable that generates arrows, using the 'Starman' notation for generators. I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-7239e085-01831))_
- 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-7239e085-01834))_
- 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.' _(javascriptallonge.pdf (source-range-7239e085-01841))_
- 'There's an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with === , I can show you this function:' _(javascriptallonge.pdf (source-range-7239e085-01844))_
- 'A long time ago,' The Carpenter explained, 'Someone asked me a question in an interview. I have never forgotten the question, or the general form of the solution. The question was, Given a linked list, detect whether it contains a cycle. Use constant space. ' _(javascriptallonge.pdf (source-range-7239e085-01846))_
- He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-7239e085-01831))_
- I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-7239e085-01831))_
- That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-7239e085-01834))_
