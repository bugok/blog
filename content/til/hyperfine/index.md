---
title: Hyperfine - for benchmarking CLIs
date: 2025-06-22T14:44:58+03:00
summary: Hyperfine for benchmarking CLIs
description: Hyperfine for benchmarking CLIs
tags:
- benchmark
- cli
---

[Hyperfine](https://github.com/sharkdp/hyperfine) is a CLI tool for benchmarking
CLI commands.

Example:
```
2|[noamler@noamler-mbp]:~$ hyperfine 'ls -l '
Benchmark 1: ls -l
  Time (mean ± σ):      14.2 ms ±   6.1 ms    [User: 1.0 ms, System: 2.5 ms]
  Range (min … max):     5.2 ms …  39.6 ms    180 runs

```

There are many customizations which can be applied, as well as built-in
intelligence. For example, I've seen the following output when I ran `ls -l` on
a fancy cache-using filesystem:

```
Warning: The first benchmarking run for this command was significantly 
slower than the rest (105.5 ms). This could be caused by (filesystem) 
caches that were not filled until after the first run. You should 
consider using the '--warmup' option to fill those caches before the 
actual benchmark. 
Alternatively, use the '--prepare' option to clear the caches before each 
timing run.
```

So it's nice that hyperfine can tell me about things going on under the hood.
