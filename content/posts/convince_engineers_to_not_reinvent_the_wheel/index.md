---
title: How to convince engineers to not reinvent the wheel?
date: 2024-06-13T21:27:52+03:00
summary: How to convince an engineer that the right solution to the problem doesn't involve writing code?
description: How to convince an engineer that the right solution to the problem doesn't involve writing code?
tags:
- culture
- mentoring

---

A few weeks ago, I saw a [message in on of Rand's Leadership slack channels](https://rands-leadership.slack.com/archives/CUAAP1A3G/p1717514289990899) asking how to convince a junior engineer not to reinvent the wheel. I commented with some ideas, and then kind of forgot about it.

A few days ago, I had a 1:1 meeting with an engineer from my team. This was a few days after starting the process of our 2024H2 planning. The engineer was so excited only about one specific project - which involved a lot of coding.

After agreeing that it would be a good idea to work on this project, we went over other potential projects for him. Unfortunately, he wasn't excited by any of them. Digging into this, it was because 'they involve very little coding'.

One concrete example was to ramp up a service to an existing integration testing framework - which is tightly integrated at our workplace. He said that he would much rather reimplement the testing framework from scratch.

This made me remember the slack message - so I wanted to circle back and think about it.

# But why do engineers prefer to reinvent the wheel?

Junior engineers, from what I've seen, mostly enjoy writing a lot of code. There's something nice about having a very specific task at hand, quickly iterating by compiling the code (if needed), running it and adding small tests. The short iteration cycle and and full control of that part of the system might get a sense of control of how things work.

I want to assume that when a task becomes more complex and involves a longer iteration cycle - it's harder to enjoy the progress.

But, there are many long-term advantages to reusing existing systems. If you were to convince someone not to write a new system by themselves - but to use an existing one - here's what I would suggest you tell them:

# Counter arguments for not reinventing the wheel

If you'll use an existing system, you:

## Will avoid bugs

If you're going to write code, you're going to have bugs. I have bugs all. the. time. Some are easy to find, some are less. Some don't have a large blast radius, and some can (and did!) took down a production service. If you're going to use a stable, existing system - you probably not going to encounter as many bugs - just because that code has been run multiple times before.

## Won't need to handle corner cases

Similar to having bugs, users of your new shiny code might provide it with input you haven't thought it should handle. Ideally, an existing system has already dealt with weird corner cases - and you won't need to write code in such a protected manner and deal with those corner cases. You'll just be supplying the input and reporting the output. You probably won't need to parse and validate the input yourself.

## Won't need to invest in performance tuning

If you're planning to write a piece of code in a large-scale system, you might eventually get to a point where your code can't handle the load, scale, parallelism, etc. Now you need to yet again, get back to the same task.

However, I can think about two counter examples of this[^1].

[^1]: There are cases of rebuilding something even if there's an existing, mature alternative. Two counter-examples: [`ack`](https://beyondgrep.com/) which is a grep alternative which is much faster. Also [proxygen](https://engineering.fb.com/2014/11/05/production-engineering/introducing-proxygen-facebook-s-c-http-framework/), ~~Facebook~~'s Meta's HTTP load balancer was built after the existing, off-the-shelf HTTP load balancer didn't handle the load. However, in both cases - performance was the key reasoning of rebuilding an existing system. It wasn't because 'someone wanted to write a lot of code'.

## Will have existing integrations with the ecosystem

When working for a company which invests in internal tooling, you have good inter-connections between different components.
Taking the integration testing framework example:
* There's already a base test which can easily be extended.
* You can link an oncall to the test
* A test can easily be run as part of the CI as the code change has been published. If a test fails, it's easy to see that on the code change diff. If you try to push that code - you'll get a warning as there's a test failure.
* A test can easily be run against an RC tier which has just received a version on its way to be pushed to production. If a test run has failed - the push process will automatically stop and the oncall will be notified.

Today, we get all those things automatically. There's so much logic into those few items - and I would really like to avoid rebuilding that logic.

## Will reduce maintenance cost

When you write software - you should also maintain it. Write documentation, fix bugs, upgrade dependencies, etc. All that maintenance takes time - which you won't need to spend if you'll be using an existing system.

# Unfortunately, those arguments aren't always convincing

The arguments I've laid out are **rational**. To me, the desire to rewrite an existing system just because you prefer to code that and not integrate with an existing system is **irrational**. There's a lot of enjoyment in writing code, sure. But when it comes to high scale, production grade code, there should be a very good reason not to use an existing, battle-tested system.

Maybe it's something which comes after experiencing the pain of debugging your own code, in a stressful environment, only to realize that you could have used something better.

But maybe there are ways to penetrate through the wall of irrationality:


## Show them how hard it really is

If you have access to the source code of the existing system, you can go over it with the other engineer - and see if that engineer has under-estimated the complexity of that system.

I've had cases where I thought I can build a replacement over a course of a day - but after looking at the existing implementation - I realized that I can't, and that I've (greatly) underestimated the complexity.

## Find some other thing to code

There might be another project where writing a large amount of code is what's right at this point in time. Perhaps projects can be shuffled around so that the person who wants to write a lot of code will be able to do so.

# Conclusion

I'd like to end this post with a quote a manager of mine said when he talked about software project management:

> We're not here to give engineers an orgasm.

His intent was that the most important thing about a project isn't the enjoyment of the engineers. It's to build the best systems.
