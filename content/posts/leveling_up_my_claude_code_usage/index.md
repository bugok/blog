---
title: Leveling up my claude code usage
date: 2026-01-07T10:09:26+02:00
summary: A few tips for how I get more of using claude code
description: A few tips for how I get more of using claude code
draft: true
tags:
- coding
- claudecode
---

In the last few weeks, I've been using Claude Code more extensively. As I read more about it, used more of it, experimented with it, I came up with a few tips which perhaps would be useful for someone who ran `claude` in the terminal, used a prompt and got reasonable results.

For context, I currently work at Meta, and we're lucky enough to try Claude Code. With all my experimentation, I didn't get a warning about going over a token limit. Maybe some day :)

## Skills

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWxoODE4cXRnbGFwdHE3dTJtZHR3aDdrbHZxbXo0YjZscGR6eG1odiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3WvhJ783Le5ieNEZ8z/giphy.gif)

The way I like to think about skills is this scene from the Matrix. Neo gets hooked up, and is loaded with different skills in just a few moments.
[Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview):

> Agent Skills are modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.

Those are markdown files which give instructions on how to generate code, interact with a system, run a CLI, etc. Those markdown files can be personal (in your `~/.claude/skills`) directory. They can also be shared with other people - given the right source control / deployment solution.

Unlike full markdown files which are loaded - skills don't fill out the context window just by being there. Skills have a format of a name and a short description. Those are loaded when Claude Code starts. That's about 50-100 tokens. Once loaded, after determining that a skill is needed, loading it does use the full content in the context.

### First skill pattern - how to generate code

One common pattern is how to generate code. Encapsulating  best-practices, organization-specific patterns for coding conventions, testing, file structuring for each programming language - all those can be specified in skills.

To me, this is the evolutions of linters. You're not submitting code and then CI complains that something isn't according to the standards. You're using claude to generate the code **according** to those standards.

### Second skill pattern - wrapping CLIs

Another common pattern for using skills for me is **wrapping CLIs**. To create such a skill, I instruct claude code to:
1. Run the CLI with `--help` recursively
1. I point it to the CLI's documentation
1. I point it to the CLI's source code (if available)

Then, it creates the skill for that CLI.
That allows me to perform actions using the CLI - in natural language. I don't need to remember how to invoke the CLI.

### Concrete skill example

A concrete example I've experimented with is [Anthropic's code review plugin](https://github.com/anthropics/claude-code/tree/main/plugins%2Fcode-review). Because of how things are structured internally, we translated this plugin to a skill which is part of an internal plugin.
Launching multiple agents to review code from different perspectives was helpful, and provided good feedback about the code.

### When to create a skill?

I usually search for an existing skill or create one after 2-3 times I had to teach claude about how to use a certain system.

## Plan mode

By default, Claude executes commands. But, for performing larger, more complex tasks - using [plan mode](https://code.claude.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis) is useful. In plan mode, claude doesn't perform destructive actions. It doesn't write code. It just builds a plan according to which it'll execute on later.

Move to plan mode (`shift+tab`), describe the task, and let Claude build the plan. You can then iterate on the plan - until you're happy with it. The plan is written as a markdown file under `~/.claude/plans` - so you can edit it with Claude, or manually. After you're happy with the plan, you can instruct Claude to move to execution mode - and execute on the plan.

Usually, I combine plan mode with [`ultrathink`](https://code.claude.com/docs/en/common-workflows#per-request-thinking-with-ultrathink), which means Claude takes more time to think, using more tokens - but potentially produces a higher-quality response.

In some cases, Claude will prompt and ask clarification questions about the required plan. That allow Claude to build a plan which is tailored to the situation you have at hand.

## Creating custom commands

Similar to not repeating myself - and using skills. I do similar things for more deterministic actions - using commands. In addition to the [built-in commands](https://code.claude.com/docs/en/slash-commands), you can define your own custom commands under `~/.claude/commands`.

For example, it's common for me to want to share a certain response from Claude. One scenario is pasting the markdown response in a commit message, and another, is sharing it as a Google doc. Therefore, I created two commands:

* `export_last_response_as_md` which dumps Claude's last response to a markdown file. (I initially wanted to print the markdown to the terminal, but the markdown formatting got messed up all the time)
* `export_last_response_as_gdoc` which dumps Claude's last response to a Google doc, translating the markdown formatting to Google docs formatting.


## Take your environment everywhere
