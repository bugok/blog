---
title: "Tips for performing a successful software migration"
date: 2024-06-09T15:20:48+03:00
summary: Battle tested best practices for performing software migrations
description: Battle tested best practices for performing software migrations
tags:
- migration
- production
- reliability
---


> The only constant in life is change

Heraclitus

## Context

Migrations are part of real-world software engineering. If you don’t migrate, [your code will probably rot](https://en.wikipedia.org/wiki/Software_rot). You probably need to make changes to your software systems in order to adapt it to the changing environment.

Recently, we had a small migration in our team. We wanted to replace our configuration mechanism from one to another. Unfortunately, it didn’t go smoothly. As I was performing the migration, I caused two similar outages. After talking to a few colleagues, I was suggested to take a step back and to think about migrations at a higher level. What makes a good migration? How to perform migrations safely? I’ve gone back to past migrations I was part of, or just seen from the sidelines, and thought about what it was that made them good, safe or maybe even awesome. I also thought about what made some migration a nightmare.

## Examples of migration types

Thinking about what types of migrations I’ve seen, I came up with the following list. Obviously, there are many more:

Migrate from one build system to another.
Update your service’s API from version N to version (N+1).
Migrate your configuration mechanism from one to another.
Migrate your underlying machine type from one to another.
Migrate from using one datastore to another.
Update your service’s runtime from one version to another.

When thinking about suggestions for good migrations, I tested the suggestions against the list. Not all suggestions make sense to all the migrations types, but for every suggestion, there’s at least one migration which has benefitted from that suggestion. It’s for you to pick and choose, depending on your migration.

## Suggestions for your migration

### Have a clear, strong reasoning

You should crystalize why you want to perform this migration. Why do you want to move from the old thing to the new thing? Would your service be otherwise depending on a deprecated technology and therefore unmaintainable? Do you require re-architecture to scale your service to adapt to the increasing demand? By performing the migration you’ll save X amount of money?

You should have that strong and clear reasoning so you could:
* Explain why you’re investing in this (as opposed to building the next shiny thing)
* Easily motivate the team when they are less motivated to work on the migration. Especially if it has been a while since starting to work on it.
* Have a ready elevator pitch for when you need to convince a partner to support this migration at a 5-minute notice for ‘an important meeting’.

### Have milestones, progress gradually, celebrate their completion

When you plan a long migration, you should split it into milestones. It’s hard to imagine finishing a long race if there are no pit-stops. Having those milestones will allow you to be more precise about the design and execution details of each of them, it’ll be easier to communicate to partners the progress of the migration (as opposed to ‘we completed 3 weeks of the migration, we have 7 more left’).

Performing a migration gradually will help you progress safely, monitor the progress, identify issues as they arise and reduce the blast radius of a big change immediately deployed to production.

In addition, in a long migration, celebrating the completion of milestones can help with building confidence that the migration will eventually complete and help with the team’s morale.

### Have the end in mind, have a ‘definition of done’

In some migrations you move from the old thing to the new thing. So when is the migration complete? Obviously, it’s not done when you’ve done a proof-of-concept of the new thing. It’s also probably not done after you’ve moved your workload to use the new thing. The migration is almost done when you’ve absolutely, completely deleted the references to the old thing. The migration is done when you’ve cleaned up all the monitoring you’ve put in place to track the migration and after when you’ve summarized the migration with some learned lessons which you didn’t expect to learn.

### Have your customers in mind

Simplistically put, there are two types of migrations: A migration which shouldn’t affect customers and another, which can affect customers. Customers may be real users, or another engineering team which is using your team’s offering. Eventually, if your team’s offering has any type of customer - then your migration will fall to the second bucket. When you have customers, you should reduce the friction of migration from them as much as possible.

In reality, I believe that every team has customers. Someone is probably using whatever your team offers. Otherwise, you’re probably building software in a void. For the sake of the argument, let’s assume that you do have customers.

Think about removing as much friction as possible from your customers. The best case scenario is that your customers become familiar for the first time with the migration after they read the summary of the migration, presenting all the benefits they can get from you now.

When you test code, think about how your customers will be affected.
When you land code, think about how your customers will be affected.
When you push code, think about how your customers will be affected.

It depends if your customers use your service, your code library, your build system or whatever. Put yourself in their shoes, and think about how your changes will affect them. Personally, I know that I have failed at this in the past, which is why I’m trying to advocate for this now.

### Use shadow traffic

Especially at the beginning of the migration, when you might be unsure of the correctness or performance of the new thing, you might benefit from shadowing the existing usage in the new thing. You could replicate a percentage of your customers’ requests and have them go to the new thing (without taking any effect from the customer’s perspective) in addition to them still being sent to the old thing. This could help you get a first taste of production traffic, without actually causing any side effects.

Whereas shadow traffic works for services, it might not be applicable to other use cases. For example, let’s say you want to move from building against one runtime platform to another. In that case, you could set up a shadow CI build of your service which will try and build your service with the new platform, in addition to existing build jobs of the old platform.

The concept here is to have an initial production-like taste of the migration, without affecting anything running in production, staying out of the critical path.

### Get a beta-tester

It might be useful for you to get a beta tester for the new thing. If the new thing offers something that a specific customer wants - that customer may be willing to endure some friction from the new thing, because they’ll be getting that feature they wanted.
That can work well for you as you’ll get feedback from that customer while getting a little production usage through that customer as well.

### Monitor your KPIs

You should have monitoring specifically for the migration. This is so it’ll be easy for you to see if the migration correlates with a certain type of failure or regressions in your KPIs. Software fails sometimes. When it is for the subject of your migration, it’ll be useful for you to know if the migration could be the cause of that.

A dashboard which clearly shows how the old thing behaves compared to the new thing could help you identify if the migration might be causing issues. Otherwise, you can (hopefully) rest assured that it’s not.

### Have a killswitch

It is possible that a migration could be the cause of a regression. You should assume that a migration will be a cause of some regression, as some migrations can have unexpected side effects. Those issues can probably be resolved, but not while standing in the critical path. If a customer reports a big issue, if your SLIs drop or if there’s an outage related to migration - its might be a good idea to hit the killswitch, stabilize, investigate the issue, resolve it, and turn the knob back on, gradually. In order to do that, you should have the tools to enable this flow.

### Be ready to be surprised, especially in the long-tail

In some migrations, weird things reveal themselves. There are cases where a hack which relied on some quirkiness of the old thing no longer works with the new thing. There are cases where a low-level behavior changes. Things were just ‘supposed to work’, but in reality, they don’t. Often, this happens at the end, when you get close to wrapping up the migration.
Have the extra time buffer, patience and creativity to work through those.

### Update documentation

This somewhat ties to the ‘have a definition of done’ suggestion. Please clean up your documentation after the old thing has been completely deleted. As a customer, it’s so frustrating to go through a documented workflow only to see at the end that the linter is complaining because the workflow is deprecated.
Please help your customers do the right thing by removing deprecated documentation.

### Communicate regularly

I’ve seen only positive feedback when I regularly communicated progress related to migrations. People eventually rely on those updates to know if something goes wrong, if there’s a delay, if there's an expected blocker, etc.
The channel through which you’ll regularly communicate progress should also be the one which has the kickoff and wrap-up communication. You should communicate failures to the same channel (hopefully there won’t be too many of them). You should thank the people who partner with you throughout the various milestones of the migration and also customers who provided good feedback.

## Finally

It’s hard to have a catch-all for all migrations, but I believe that some of those tips can be applied to many of the migrations I’ve seen.
Migrations can be hard, but they can be a learning experience of the darker corners of your team’s offering. Especially when things break.

Eventually, migrations try to improve the software. Make it easier to use, maintain, scale, etc. There are benefits to those. We should also pay attention how migrations are being done - as those may leave good or bad taste to our customers.

Paraphrasing Maya Angelou: Engineers will forget what said about a migration, engineers will forget about what you migrated, but engineers will never forget if they got paged because of your migration.
