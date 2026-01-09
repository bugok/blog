---
title: Leveling up my claude code usage
date: 2026-01-07T10:09:26+02:00
summary: A few tips for how I get more of using claude code
description: A few tips for how I get more of using claude code
tags:
- coding
- claudecode
---

In the last few weeks, I've been using Claude Code more extensively. As I read more about it, used more of it, experimented with it, I came up with a few tips which perhaps would be useful for someone who so far has just ran `claude` in the terminal, used a prompt and got reasonable results.

For context, I currently work at Meta, so my experience is somewhat limited to how we use Claude at Meta.

## Skills

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWxoODE4cXRnbGFwdHE3dTJtZHR3aDdrbHZxbXo0YjZscGR6eG1odiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3WvhJ783Le5ieNEZ8z/giphy.gif)

The way I like to think about skills is this scene from the Matrix. Neo gets hooked up, and is loaded with different skills in just a few moments.
[Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview):

> Agent Skills are modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.

Those are markdown files which give instructions on how to generate code, interact with a system, run a CLI, etc. Those markdown files can be personal (in your `~/.claude/skills`) directory. They can also be shared with other people - given the right source control / deployment solution.

Unlike full markdown files which are loaded - **skills don't fill out the context window** just by being there. Skills have a format of a name and a short description. Those are loaded when Claude Code starts. That's about 50-100 tokens. Once loaded, after determining that a skill is needed, it does use the full content in the context window.

### First skill pattern - how to generate code

One common pattern is how to **generate code**. Encapsulating best-practices, organization-specific patterns for coding conventions, testing, file structuring for each programming language - all those can be specified in skills.

To me, this is the evolutions of linters. You're not submitting code and then CI complains that something isn't according to the standards. You're using Claude to generate the code **according** to those standards.

### Second skill pattern - wrapping CLIs

Another common pattern for using skills for me is **wrapping CLIs**. To create such a skill, I instruct claude code to:
1. Run the CLI with `--help` recursively
1. I point it to the CLI's documentation
1. I point it to the CLI's source code (if available)

Then, it creates the skill for that CLI.
That allows me to perform actions using the CLI - in natural language. I don't need to remember how to invoke the CLI.

### Concrete skill example

A concrete example I've experimented with is [Anthropic's code review plugin](https://github.com/anthropics/claude-code/tree/main/plugins%2Fcode-review). Because of how things are structured internally, we translated this plugin to a skill which is part of an internal plugin.
Launching multiple agents to review code from different perspectives was helpful, and provided good feedback about the code. This allowed to standardize the automated code review process, Encapsulating best practices into it.

### When to create a skill?

I usually search for an existing skill or create one after 2-3 times I had to teach claude about how to use a certain system or a workflow.

## Plan mode

Claude code is known for generating code and running commands. For performing multiple, larger, multi-step tasks - using [plan mode](https://code.claude.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis). In plan mode, Claude doesn't perform destructive actions. It doesn't write code. It just builds a plan according to which it'll execute on later.

Move to plan mode (`shift+tab`), describe the task, and let Claude build the plan. You can then iterate on the plan - until you're happy with it. The plan is written as a markdown file under `~/.claude/plans` - so you can edit it with Claude, or manually. After you're happy with the plan, you can instruct Claude to move to execution mode - and execute on the plan.

Usually, I combine plan mode with [`ultrathink`](https://code.claude.com/docs/en/common-workflows#per-request-thinking-with-ultrathink), which means Claude takes more time to think, uses more tokens - but potentially produces a higher-quality response.

In some cases, Claude will prompt and ask clarification questions about the required plan. That allow Claude to build a plan which is tailored to the situation you have at hand.

## Creating custom commands

Similar to not repeating myself - and using skills. I do similar things for more deterministic actions - using commands. In addition to the [built-in commands](https://code.claude.com/docs/en/slash-commands), you can define your own custom commands under `~/.claude/commands`.

For example, it's common for me to want to share a certain response from Claude. One scenario is pasting the markdown response in a commit message, and another, is sharing it as a Google doc. Therefore, I created two commands:

* `export_last_response_as_md` which dumps Claude's last response to a markdown file. (I initially wanted to print the markdown to the terminal, but the markdown formatting got messed up all the time)
* `export_last_response_as_gdoc` which dumps Claude's last response to a Google doc, translating the markdown formatting to Google docs formatting. I can then use Google docs's sharing mechanism to share the nicely formatted response with the needed people.


## Take your environment everywhere

One of the ways I like to scale claude is to run multiple instances of it, sometimes on the same repository. Outside of meta, I've read that people use [git worktrees](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees), but as we use [sapling](https://sapling-scm.com/) at Meta, I haven't used git worktrees yet.

Nevertheless, the concept is what matters. The idea is to take your claude environment and replicate it to another instance of your repository. That way, you could run multiple instances of claude, running different tasks, on the same repository - but without interfering with each other.

The way I do it, is to get another development machine. At Meta, we use an internal system which synchronizes **some** of my dotfiles across multiple servers (including development machines). It's very important **not to sync all files under `~/.claude`** as there are some machine-specific, session-specific and cache files there. Again, the mechanism is less-important. The important bit is to have a way to synchronize the needed files under `~/.claude`. For what I understand, those are:

```
~/.claude/commands/
~/.claude/skills/
~/.claude/plugins/
~/.claude/settings.json
```

One you have that properly setup - the flow is:
1. Get a new dev machine (which has your claude configuration as well as a fresh version of your repository)
2. Launch claude
3. Profit.

Another trick I use is to **differentiate between different development machines**. I have a script which colors the vscode instance connected to a dev machine in a random color based on a hash of the hostname. This allows me a stable color for a given machine, so I can quickly differentiate between different machines. If I disconnect and reconnect to the same dev machine - I would run the coloring script again - and get the same color I got before, which helps me link the work I did with the same color of vscode.

## Use the most out of your single Claude instance

Claude has an internal mechanism to parallelize work. Before looking into it - I was able to trigger it only by chance, once I understood how claude tasks are built - I was able to get better parallelization results.

A claude task has the following attributes:

- **Subagent type**: Explore, Plan, general-purpose (and maybe others)
- **Run in background**: (bool) - non-blocking vs. blocking
- **Model**: (opus / sonnet / haiku)
- **Prompt**: Instructions

Once I understood that - I was able to specify different tasks with claude, instruct it to run those tasks **in parallel** - and then claude would do so.

There's also the concept of batching. Assuming you have a very large number of tasks you'd like to run simultaneously, you could also specify the batch size of the task - so that you won't exhaust the resources of the machine.

Claude is good about creating a task dependency graph (in plan mode, for example), and then executing on that graph. It can run some tasks sequentially, then run a parallelized batch, gather that data, aggregate it - and feed it to the next task.

The important bit here is to be **explicit**. You prompts should say "Run X, Y and Z **in parallel**" or "**in batches of 5**" or something of that sort. Then, claude will follow.

## Final words

The meta-bit about working with Claude is that it's an ongoing process. I continuously learn new things: read online, ask claude itself or come across different things my other claude-curious co-workers have done. I iterate on my `~/.claude` configuration and I'm trying to codify repeated tasks into skills or commands. Most of the time, it's a lot of fun.
