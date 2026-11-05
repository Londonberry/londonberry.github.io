---
title: "What Agent-Built Code Actually Costs"
description: "Two 30-line fixes cost 5.5M and 6.9M tokens when an AI agent built them unattended. Here's where the tokens went, and how we changed the way we route work."
date: 2026-11-05
author: "Ben McDonald"
tags: ["AI", "Engineering", "Cost"]
---

We run a lot of our build work through AI agents. In September we stopped guessing what that costs and measured it.

## The number

Two small fixes on a client project. One changed 31 lines of code, the other 29. Each ran through our full unattended agent workflow: plan, build, review, test.

They cost **5.46 million and 6.90 million weighted tokens.**

For about 30 lines of code each.

## Where it went

Nearly all of it was the build session. A separate review session was about a fifth of one story, and didn't run at all on the other.

Inside the build session, the agent did what it was told to do:

1. **It wrote a plan.** 260 to 283 lines of spec per story. That's roughly ten times the size of the code it described.
2. **It reviewed its own plan four ways**, and logged a note for every finding.
3. **It re-read everything, every turn.** About 90% of the tokens were cache reads. Each turn reloads the spec, the project context, and the instructions. So cost grows with turns times context, not with lines changed.

For a fix whose shape we already knew, we were paying the agent to rediscover and re-document it.

## What we changed

We didn't drop the planning. Planning is cheap, and it's what makes the next task clear enough to act on. We changed who does the work:

- **Known fix, under about 50 lines: do it in the session you're already in.** No cold, unattended run.
- **Real design work, or a part of the system nobody has settled: use the full agent loop**, one task at a time, so the price shows up per task.
- **Batch neighbors.** Per-session overhead dominates. Three small stories in one night cost 10.5M tokens. Two stories the next night, run separately, cost 12.4M.
- **Report the price.** Every run ends with tokens per task next to what changed, so the next routing call is based on evidence.

## Why this matters for you

If you're building with AI agents, the expensive part isn't the code. It's the context the agent drags through every turn. Measure one or two tasks end to end before you scale it up. The answer will change how you work.
