---
title: "I Have a Vibe-Coded MVP. Now What?"
description: "You built a working demo with Lovable, Bolt, Cursor, or Claude Code. Real users want it. Investors are circling. Here's the honest playbook for taking an AI-generated prototype to a product you can stake your company on."
date: 2026-05-16
author: "Ben McDonald"
tags: ["Vibe Coding", "AI Development", "MVP", "Startups"]
---

You typed a prompt. Something appeared. You typed another prompt. It got better. A week later you had a working app. Real people clicked on it. A few of them paid. An investor asked for a demo. And then, very quietly, the wall arrived.

Every new change breaks something old. You can't tell what's safe to touch. The bug report from yesterday is hard to reproduce because you don't actually know how the code works. Auth feels like it's held together with hope. The database might or might not have backups. You haven't looked.

If any of that sounds familiar, you're not alone. Vibe coding (the practice of building software primarily by prompting AI tools like Lovable, Bolt, v0, Cursor, Replit Agent, or Claude Code) has produced more working software in the last 12 months than the previous 12 years. It is genuinely magical until the moment it isn't.

Here's the honest playbook for what to do next.

## The MVP gap nobody warned you about

A vibe-coded MVP is a working demo, not a working product. The distinction is uncomfortable but worth naming.

A working demo proves the idea is real. It convinces investors. It earns a thumbs up from your friends. It produces a checkout flow that successfully takes a credit card on a sunny afternoon.

A working product survives the rainy afternoon. The one where a user uploads a 50MB file, your background job times out, the retry loop fires forever, and the database fills up. The one where someone's session token gets shared accidentally and now two accounts can see each other's data. The one where you push a "small" change and three unrelated features break because the AI restructured a shared utility you didn't know existed.

The gap between those two states is what we'd call "the production hardening tax." It is real. It is not optional. It is also not nearly as bad as the internet would have you believe, if you tackle it intentionally.

## Step one: stop coding for a week

This is the part founders hate. You have momentum. You have ideas. Stopping feels expensive.

Stop anyway.

Spend a week doing nothing but reading the code, running the app, and writing down what you find. The questions to answer:

- **What is in this repo and what does it do?** Read every file. Yes, every file. AI tools love to leave orphaned helpers, duplicated logic, and abandoned routes. You can't safely change what you can't see.
- **Where is the data?** Database connection strings, secrets, API keys. Are any in the repo? In commit history? In an environment variable file that got committed by accident?
- **What breaks if production goes down right now?** Do you have backups? Do you know when the last one ran? Have you ever tested restoring from one?
- **What does a deploy look like?** Is there a CI pipeline, or do you click a button in Vercel and pray? Both can work; pretending is dangerous.
- **What can a user do that you didn't intend?** Can an unauthenticated request hit your admin endpoint? Can a user fetch someone else's data by guessing an ID? Can SQL be injected through a search box?

You don't need to fix any of this in week one. You need to write it down. The pile of risks is your real backlog. Everything else (the next feature, the next investor demo, the next pricing experiment) is a distraction until you can see this pile clearly.

## Step two: triage by blast radius

You now have a list of 30 to 100 problems. You don't have time or money to fix all of them. You have to choose.

The wrong way: fix the ones that feel scary or annoying. Refactor that file you keep tripping over. Rename that confusing variable.

The right way: rank by blast radius. For each item, ask two questions:

1. If this goes wrong, who finds out? (You alone. One user. All users. Investors. Regulators.)
2. If this goes wrong, can you undo it? (Trivially. With effort. Not at all.)

The combination tells you what to fix first. Anything that's both high-blast-radius and irreversible (data corruption, secret leaks, payment errors, auth bypasses) goes to the top. Everything else can wait.

Most vibe-coded apps have three to seven items at the top of the list. That's tractable. That's a few weeks of focused work, not a rewrite.

## Step three: add the safety nets

Before you fix the scary items, install the safety nets that let you fix them safely. These are the things every production system needs and most vibe-coded MVPs don't have:

- **Source control discipline.** Branches for changes. Commit messages that say what changed and why. A `main` branch that always works.
- **A test suite around the scary parts.** Not every function. Just the ones whose breakage you'd be embarrassed by. Auth, payments, data integrity, anything that touches money or trust.
- **Error tracking.** Sentry, Highlight, Honeybadger, anything. You should know about a production error before your users tell you.
- **Backups, verified.** Automated daily backups. A documented restore procedure. A practice run where you actually restore one. The first restore attempt is always the wrong time to discover the backup is empty.
- **A staging environment.** A second copy of your app that is not production where you can try changes safely.
- **A real deploy pipeline.** Every push to `main` runs tests, then ships. Manual deploys hide what changed and when.

None of this is glamorous. All of it is faster to do once than to skip and pay for later.

## Step four: rewrite only what you must

Founders panic and try to rewrite the whole codebase. Don't.

A full rewrite throws away the only thing you've already proven: that the product works. It restarts the discovery process, costs months, and almost never produces a meaningfully better outcome than incremental hardening.

Pick the two or three highest-risk modules. Rewrite those, with tests, deliberately. Leave the rest alone until it actually needs to change. Refactor opportunistically, not aspirationally.

The version of your codebase that ships your next 100 users probably looks 80% like what AI wrote. That's fine. The 20% that matters is the part you owned on purpose.

## Step five: pick what to keep vibe-coding

Vibe coding is not the enemy. It's a productivity multiplier when used in the right places.

What's safe to keep prompting: UI tweaks. New marketing pages. Internal admin tools nobody but you uses. One-off scripts. Throwaway analyses.

What's not safe to keep prompting (without review): Auth. Payments. Anything that writes to the database. Anything that touches user data. Anything you'd be embarrassed by if it leaked to TechCrunch.

The rule is simple. If the blast radius is small, vibe away. If it's large, slow down. AI tools don't know which is which. You do.

## When to bring in help

Most founders can do steps one and two themselves. Steps three through five benefit from someone who has done this before.

Bring in help when:

- You've stopped touching the code because you don't trust yourself.
- You're about to demo to investors or onboard paying customers and you can't sleep.
- You don't know what "blast radius" even means for half the code in your repo.
- You're hiring engineers and you have no idea how to interview them or what to look for.

That's exactly the gap our [vibe coding rescue](/services/vibe-coding-rescue/) engagements close. We start with a paid audit (about a week), produce a written risk report ranked by blast radius, and hand back a fixed-scope proposal for the rescue work. No mystery, no upsell.

## The bigger picture

Vibe coding broke the old rule that building software was slow. It did not break the rule that running software in production is hard. Both things can be true at once.

The founders winning right now are the ones who use AI to get to a working demo in a week, then have the discipline to spend the next month making it real. The ones losing are the ones who confuse the demo for the product, ship it as-is, and discover the gap the hard way.

You're not behind. You're at the beginning. The next move is the one that matters.
