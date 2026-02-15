---
title: Adapting to today's AI state as a Senior Engineer
date: 2026-02-12T14:13:57+02:00
summary: Some thoughts on how I think senior engineers should adapt to today's AI state.
description: Some thoughts on how I think senior engineers should adapt to today's AI state.
tags:
- AI
- Claude Code
- Culture
- Senior engineer
images: 
- senior_engineer_ai.png
---

## Setting up guardrails

Similar to the world before AI - if you wanted to keep some behavior in check - you should make sure that behavior is kept using tests which run in CI or as part of the push process. This is still true, and maybe even more so, when more code is flowing from the hands of engineers to the source control repositories.

Lints, static analysis, unit tests, integration tests and load testing - all those can be run to make sure that code structure and expected behavior is kept. Those can help prevent AI slop code to get committed or pushed to production.


## Be opinionated, and teach your team’s AI to work like you

Encode your team’s best practices into the context files. That will allow consistent behavior across the team - even in an unconscious way. It’ll happen because AI agents (mostly) follow that behavior. If all your team members work on the same sub-directory of a repository - and that sub-directory has a context file - AI agents will generate code based on the instructions in that context file.

Continuously maintain those context files when you identify a wrong in the current file or if you identified a better pattern.


## Need to be on top of (AI) things, be open to change

My personal go-to agent is Claude Code. I recently got a tip to refresh [Claude Code’s changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) a few times a day - because claude code publishes a release a few times a day.

It’s extremely hard to follow everything. People are ecstatically sharing AI-related accomplishments, set-ups and recommendations (this post included!) - and it’s hard to find what’s good, what’s relevant - and it’s very likely that in a few weeks - something will reshuffle the current state of things.

We should be able to consume the changes and be open to change how we think - because this area is defining itself, continuously.


## Use the lower barrier of entry to experiment

The needed effort to build initial context on something, or fix a small bug in an unfamiliar area has dropped significantly. With a short prompt, Claude Code can easily come up with a plan - and to (potentially) propose a fix.

I’ve had numerous cases of this - and is some of those cases - the owning team even accepted my change. Not always though.

Doing those small bugfixes has two benefits: First, improve quality of life, by fixing issues which bother me. But second, and more importantly, they act as a test-bed for testing new AI workflows.


## Code review: use AI, but expect human-consumable changes

 Given that code is cheap now - we now spend more time reviewing. You’ve probably seen this many times: you need to review a huge change - like a few hundred lines. Tests are auto-generated - and don’t test the core functionality of the change. Test plan is “CI is happy”. To me, this is not acceptable. Although changes are done by AI agents, I still expect that humans should be able to consume (review) the changes.

So, my suggestion is to push back on this. Although I use [AI to review code](https://github.com/anthropics/claude-code/tree/main/plugins/code-review), I treat that as a suggestion, and build my own review on top of it. Changes are too long? I expect to split it. That type of insisting could help with an easier revert later - if there’s a bug. Unit tests are too verbose? Change it. Core functionality isn’t tested? Change it. Insisting on proper testing ties back to the guardrail setting - it’s making sure that current behavior is kept.


## Clarify requirements, care about the user experience

Code is cheap today - and can be easily replaced, deleted or moved around. It’s harder to change bigger, already running systems. As a senior engineer - you should make sure that your team knows the path they need to take. Code will be written and modified - but if there’s lack of clarity on where we want to go - we might build the wrong thing. As a senior engineer - you should insist on making sure that requirements are crystal clear, and that there are as minimal unknowns as possible.

One that is done - a swarm of AI agents could get you where you want to go. If you have defined the guardrails, best-practices - the ‘how’ part is mostly solved. You should pay attention to the end result - and that the end-product is indeed useful - and easy to use as intended.

You can think about this as: at the beginning, make sure everyone understands where they need to go. The path will be taken alongside AI agents - with the guidance you’ve already set in place. Finally, you should make sure that the resulting product is what you wanted.

And now - look: an AI generated image of a senior engineer working with multiple AI agents:

![AI generated image of an engineer working with AI agents](senior_engineer_ai.png)
