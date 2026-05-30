---
title: Showing worktree information in the shell prompt
date: 2026-05-30T13:05:19+03:00
summary: How to show your worktree in shell prompt
description: How to show your worktree in shell prompt
tags:
- git
- sapling
- worktree
---

Recently, I've made a [small change](https://github.com/facebook/sapling/commit/cc441b1c1d5b589d209020c5a74a11c83cb14cd6) to Sapling to show export the current worktree in the filesystem.

This allows to make another small test of changes to [scm-prompt.sh](https://github.com/facebook/sapling/blob/b78e23c450e0d004e36192b9cff6ec819789b9a1/eden/scm/contrib/scm-prompt.sh) which shows general information about source control in the shell prompt. That script is compatible with both sapling and git.

Today, I have the following in my `~/.bashrc`:

```bash
if [ -f $HOME/scripts/scm-prompt.sh ]; then
  source $HOME/scripts/scm-prompt.sh
fi
```

Then I have my `PS1` be something like:
```bash
export PS1='$?|[\[\033[36m\]\u\[\033[m\]@\[\033[95m\]\h\[\033[m\]]:\[\033[33;1m\]\w\[\033[m\]$(_scm_prompt)\$ '
```

This means that my shell looks something like this:
```bash
0|[noamler@noamler-mbp]:~/sources/blog (main)$
```

But with this recent change, I can turn on worktree information in the prompt. If I `export SCM_PROMPT_SHOW_WORKTREE=1`, I get something like this:

```bash
0|[noamler@noamler-mbp]:~/worktrees$ cd ~/sources/test_repo/
0|[noamler@noamler-mbp]:~/sources/test_repo (main)$ git worktree add -b my-feature ~/worktrees/worktree1
No possible source branch, inferring '--orphan'
Preparing worktree (new branch 'my-feature')
0|[noamler@noamler-mbp]:~/sources/test_repo (main)$ cd ~/worktrees/worktree1
0|[noamler@noamler-mbp]:~/worktrees/worktree1 (my-feature|worktree1)$ cd subdir/
0|[noamler@noamler-mbp]:~/worktrees/worktree1/subdir (my-feature|worktree1)$
```
