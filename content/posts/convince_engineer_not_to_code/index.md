---
title: How to convince an engineer not to code?
date: 2024-06-13T21:27:52+03:00
summary: How to convince an engineer that the right solution to the problem doesn't involve writing code?
description: How to convince an engineer that the right solution to the problem doesn't involve writing code?
tags:
- culture
- mentoring
draft: true
---

A few weeks ago, I saw a [message in on of Rand's Leadership slack channels](https://rands-leadership.slack.com/archives/CUAAP1A3G/p1717514289990899) asking how to convince a junior engineer not to reinvent the wheel. I commented with some ideas, and kind of forgot about it.

Today, I had a 1:1 meeting with an engineer from my team. This was a few days after starting the process of our 2024H2 planning. The engineer was so excited only about one project - which involved a lot of coding.

After agreeing that it would be a good idea to work on this project, we went over other potential projects for him. Unfortunately, he wasn't excited by any of them. Digging into this, it was because 'they involve very little coding'.

One concrete example was to ramp up a service to an existing integration testing framework - which is tightly integrated in our workplace. He said that he would much rather reimplement the testing framework from scratch.

This made me remember the slack message - so I wanted to circle back and think about it.

## But why?

Junior engineers, at the beginning of their careers enjoy writing a lot of code. There's something nice about having a very specific task at hand, quickly iterating by compiling the code (if needed), running it, adding small tests. The short iteration cycle and and full control of that part of the system might get a sense of control of how things work.

I want to assume that when the task becomes more complex and involves a longer iteration cycle - it's harder to enjoy the progress.

But, there are many long-term advantages to reusing existing systems. If you were to convince someone not to write a new system by themselves - but to use an existing one - here's what I would suggest you tell them:

## Avoiding bugs

If you're going to write code, you're going to have bugs. I have bugs all. the. time. Some are easy to find, and some will cause outages. If you're going to use a stable, existing system - you probably not going to encounter as many bugs - just because that code has been run multiple times before.

## Handling corner cases

Similar to the having bugs, users of your new shiny code might provide it with input you haven't thought it should handle. Ideally, an existing system has already dealt with weird corner cases - and you won't need to write code in such a protected manner and deal with those corner cases. You'll be supplying the input - not parsing, validating and using it.

## Performance tuning

If you're planning to write a piece of code in a large-scale system, you might eventually get to a point where your code can't handle the load. Now you need to yet again, get back to the same task.

However, I can think about two counter examples of this(*)

## Saving time, in the long run

Depending on how you define the scope of the project, if you think


## Integration with the ecosystem

If



## See how hard it really is

If you have access to the source code of the existing system, you can go over it with the other engineer - and see if that engineer has under-estimated the complexity of that system.

I've had cases where I thought I can build a replacement over a course of a day - but after looking at the existing implementation - I realized that


## Battle-testing in production

## Less code to maintain


(*) for that I can can actually think about two counter-examples: [`ack`](https://beyondgrep.com/) which is a grep alternative which is much faster. Also [proxygen](https://engineering.fb.com/2014/11/05/production-engineering/introducing-proxygen-facebook-s-c-http-framework/), ~~Facebook~~'s Meta's HTTP load balancer was built after the existing, off-the-shelf HTTP load balancer didn't handle the load. However, in both cases - performance was the key reasoning of rebuilding an existing system. It wasn't because 'someone wanted to write a lot of code'.
