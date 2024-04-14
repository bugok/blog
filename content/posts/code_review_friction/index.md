---

title: "Reduce friction of getting your code reviewed"
date: 2023-03-11T07:57:30+02:00
summary: Several tips on how to get your code reviewed with less friction
description: Several tips on how to get your code reviewed with less friction
tags: 
- codereview
- productivity

---

There's this saying: 

> Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. Code for readability.

(According to [Stack Overflow](https://stackoverflow.com/a/878436), this first was said by John Woods)

Thinking about this from another angle - what if that same person is the one who needs to approve your code? 

In this post, I'll try and go over some of my suggestions on how to reduce the friction of getting your code approved by your code reviewers. 

## High level

At high level, put yourself in your reviewer's position, and think about what would make them approve your code changes. If you were the reviewer, what would make you approve the code changes? My answer is: make the reviewer understand what you've done, why you've done it and also convince the reviewer that you're verified the correctness of your changes.

## Concrete suggestions

### Explicit ground rules

Ideally, before a single line of code is written, there should be clear contribution rules. This is well-integrated within [GitHub repos](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors). That allows the repo maintainers to clearly communicate to present and future contributors how to add, remove or modify code on the repo. Ideally, those rules should be verified using automation in CI. 

**Benefits**: clarity and automated-verification for all changes in the repository. 

### Format your code according to a well-defined code-style

A few years ago I was working on a project which was going to be open sourced (and it [eventually did](https://github.com/facebook/proxygen)). We discussed the code-formatting options for it. I remember saying: "I don't care which format we use, I just want it to be defined". It doesn't really matter if the curly brackets are in the same line as the `if` statement or in a new line. What matters is that we shouldn't waste time debating on the matter. 

From the author's point of view - make sure that your code answers to the code style. For example, for Python code, I use [black](https://black.readthedocs.io/en/stable/). In Go, there's [gofmt](https://pkg.go.dev/cmd/gofmt) which is built-in the language. The argument holds for any language: pick a code-style, and stick with it. 

**Code review time saving benefit**: Not wasting time and effort discussing code style issues.

### Make sure your code passes static analysis 

If your repository has some static analysis enforced, make sure your code passes those analysis tests. If possible, run those tests locally before submitting the code changes. As a reviewer, I always request for changes when some automation fails static anlysis. As an author, I make sure that my code passes static analysis before I have someone else look at it. 

**Code review time saving benefit**: Best practices and past-learnings are incorporated into your code ahead of code review time.

### Keep test signal green

Tests are a great way to verify that your code is doing what it's supposed to do. When making changes to code you want to make sure the test signal is kept at a high quality. This means: 

- If the behavior isn't expected to change - make sure that the tests still pass. 
- If the behavior is expected to change - modify the tests to reflect that. This means possibly **removing** existing tests, or **adding** new ones.

Changing the tests based on your changes makes sure that future changes won't break your desired behavior. As an author, I want to be in a place where tests prevent me from breaking the code. Therefore, I want to make sure they evolve the same way the code evolves. 

**Code review time saving benefit**: No additional iteration is needed for breaking desired behavior.

### Clear title and description

Up until now I have shared concepts related to the code itself. Now, let's talk a little about the surroundings: Write a clear title and description to your code changes. 

Concisely explain **what** you are doing in the title. This will allow the reviewer to easily understand what this code-change is going to be about. It also helps when looking at the history of your repository when investigating past changes. 

Explain **why** you're making the code change in the description. Context matters. Whereas a code-change makes sense in terms of functionality - it may not be necessary in the grand scheme of things. What's the high-level goal? What initiative is this change part of? What future changes will come after this code change? 

**Code review time saving benefit**: Reviewer doesn't ask questions about why the code changes are done.

### Solid test plan

As a reviewer, I want to make sure the author made sure that the suggested changes have been properly tested. Having CI pass is table stakes. In most cases, as a reviewer, I'd expect more. For example: 
- Screenshots of before and after the changes
- Canary the changes in a staging tier (or maybe production) with a graph which shows that behavior has been verified. 
- Running the relevant changes locally, supply the output before and after

**Code review time saving benefit**: Reviewer doesn't question the correctness of the changes.

### Small changes and stack commits

This is a very common pattern at Meta. Authors are encouraged to submit changes in small chunks, in a stacked manner. This makes both authoring and reviewing code much easier. It's easier to write and review three code changes of 100 lines each compared to one change of 300 lines. Those smaller changes can be more easily tested, isolated - and if needed - reverted. 

Frankly, I haven't practiced this before working at ~~Facebook~~ Meta, so I'm not sure what tooling allows this outside of Meta. But, [sapling](https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/) was recently released to the public to make this approach available using GitHub. You can see this [reviewstack example](https://reviewstack.dev/bolinfest/monaco-tm/pull/39) to get a glimpse. 

**Code review time saving benefit:** Time author spent when reviewing smaller code changes is shorter. 

## Summary

Mark Twain said:

> “I didn't have time to write a short letter, so I wrote a long one instead.”

My point in this post is kind of reversed to the quote. If you invest time in your code changes, it would make them easier to review. Take the time to write a shorter change. Format the code, explain the rationale, and properly test your change. You'll get a faster, better code review, and you'll keep your repository at a high quality bar.
