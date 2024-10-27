---
title: "Rising from failure"
date: 2024-10-24T20:43:29+03:00
summary: A few tips for recovering and rising from failure
description: A few tips for recovering and rising from failure
tags:
- culture
- failure
- motivation
images:
- rising_300x300.png

---

Failures and inevitable when trying to achieve big things. This is true in many aspects in my life. Family, work, maintaining a training routine, and more. The cliche says that 'the road to success isn't a straight line'. When working towards the goal - there will be some detours. The question is - how to navigate through those.

![](rising.png "An image of a person rising from failure, by ChatGPT. Usually, this isn't as dramatic")

## Acknowledge the failure

The first step from rising from failure is to acknowledge that it had happened. You should acknowledge that something sub-optimal has happened. A failure, a mistake, a detour, a bug, a bad decision, something. It might be also beneficial to acknowledge the failure to others as well. It'll help with accountability. Owning a failure can build confidence in others that you'll fix it, and that you'll try to prevent it from happening again.

## Learn from it

At Meta, we have a framework called **DERP** for our post-mortem process. DERP stands for:
* **D**etection: How was the process of detecting the problem? Was there any automation put in place to identify the issue? A common follow-up for a post-mortem is to add automated detection for the issue - so that similar, future incidents could be addressed in a fast manner.
* **E**scalation: How was the process of getting the right people or resources to handle the issue. Were the oncalls responsive?
* **R**emediation: How was the process of 'putting a band-aid' to fix the process. To clarify, this step is about making sure the customers will not experience the outage. Under the hood, things can be ugly, as the main motivation is to 'keep the plane in the air'.
* **P**revention: How to make sure that this incident, and ones similar to it won't happen again. Follow-ups here can be both short and long term. It can be toggling a configuration flag to make the system more resilient to load, or it can re-architecting a component.

## Lower the cost of failures

As failures are bound to happen, it makes sense to build systems in a way so that they'll be fast and easy to recover from failures. An example from production systems is how fast can you push a hotfix. When you trust your push process, you can push new code, configuration or both when there's an issue. Another example is having knobs which are consumed from systems at runtime. When you have those in place, you can change a knob and the effect be applied faster than a full code or configuration push.

Another type of failure (or mis-alignment) is when there's a drift between where you wanted to go and where you actually went. A way to mitigate this issue is to set smaller milestones and check-ups. It doesn't need to be a 'heavy process'. It can be a calendar reminder where you check yourself against some higher level goal, that you still have your eyes on the prize. When doing so, you'll reduce the cost of drift - as it'll be the size of a milestone - compared to the full project.

## Rebuild your confidence with small, easy steps

After experiencing a failure, it may be hard to get back up to the same 'good state', at least its state of mind. Maybe it's me and my self-esteem, maybe it's me berating myself too much - but after taking a few breaths - I'm at a better position to 'rebuild' myself.

For example, a failure to maintain my [Freeletics](https://www.freeletics.com/) training routine. Because of an injury, for example. I found that it helps to get back into the training routine by starting an easier training journey. This puts the emphasis not on the results of the training sessions, but rather on the training routine. Completing the training sessions as instructed rebuilds the confidence that I can get back to the old, steady routine. Then, when I've once again got used to training regularly, I move on to a harder training journey. At that point, I have a regular training routine that acts as foundations for achieving results in my training sessions.

From the tech-side, it can be joining a new team, or starting something completely new - where I don't have enough context on. In that case, I try and find small, easy projects which can get me 'warmed up' to the new area, experience some competence when completing such a small project. Those can open the door to questions about why things are built the way they are, which can then produce harder projects.

## You've already done well. You could do it again.

Taking a step back and looking at facts or ground assumptions helps me to regain my focus. I know for a fact that I've already worked hard to be in 'that good state'. I've been there. I tell myself that if I did that before, I can probably get to that 'good state' again.

If I have failed and regained that 'good state' in the past - that's even a better signal that shows that I'll be able to achieve that yet again.
