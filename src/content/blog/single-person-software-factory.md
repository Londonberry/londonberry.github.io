---
title: "The Single-Person Software Factory Is Real. Here's What It Can't Do."
description: "A VC built hundreds of thousands of lines of code in two weeks. But 1 in 3 AI-generated snippets has a security flaw. The future isn't about speed — it's about judgment."
date: 2026-02-05
author: "Ben McDonald"
---

Lee Edwards, a GP at Root Ventures and former engineer, recently told [The SF Standard](https://sfstandard.com/2026/02/19/ai-writes-code-now-s-left-software-engineers/) that he built "hundreds of thousands of lines of code in two weeks" across six projects using Claude Code, reading "almost none of it." He described it as a "single-person software factory."

I believe him. I'm living a version of this reality right now at Londonberry — one person, backed by AI agents, delivering work that would have required a team of five two years ago.

But there's a sentence in that article that deserves more attention than it got: **he read almost none of the code.**

## The Veracode problem

A few weeks after that article ran, [Veracode published their Spring 2026 report](https://www.veracode.com/blog/spring-2026-genai-code-security/) on AI-generated code security. The findings are sobering: **security pass rates for AI-generated code sit at 55%.** Roughly 1 in 3 AI-generated code snippets contains a security flaw. Java is the worst — failure rate exceeds 72%.

Their broader [State of Software Security report](https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/) adds context: 82% of organizations carry security debt, and 60% carry *critical* security debt. Their summary: "Teams are pushing code to production at record speeds, often fueled by AI-generated code and automated pipelines, but the mechanism for fixing flaws hasn't kept pace with the mechanism for creating them."

So when a single person generates hundreds of thousands of lines of code in two weeks without reading it, what are the odds that none of those lines introduce a vulnerability? Statistically, pretty bad.

## What the factory actually needs

I started my career at Symantec, building enterprise security software. Later I spent years as VP of Products at RF-SMART, where our supply chain software ran inside some of the largest warehouses in the world. When your code runs in production environments at that scale, "move fast and break things" isn't a philosophy — it's a firing offense.

The single-person software factory is real. I run one. But here's what it can't do without a human who knows what they're looking at:

**Architecture decisions.** AI will happily build whatever you ask for. It won't tell you that you're building the wrong thing, or that your data model will fall over at 10x scale, or that your auth approach has a fundamental flaw. Those calls come from experience — specifically, experience watching things fail.

**Security review.** Not just scanning for known vulnerabilities, but understanding your threat model. Who's going to attack this? How? What's the blast radius? AI doesn't think adversarially by default.

**Product judgment.** Knowing which features to *not* build is more valuable than building features fast. I'm a Pragmatic Certified Product Manager, and the discipline of saying "no" to plausible feature requests is still a deeply human skill.

**Integration with reality.** Your software doesn't live in a vacuum. It talks to APIs that change, users who behave unexpectedly, and compliance requirements that don't care how fast you shipped.

## The new value proposition

The most interesting question in software right now isn't "can AI write code?" It's settled — yes, incredibly well. The question is: **who do you trust to point the AI in the right direction and catch what it misses?**

That's where 25 years of building, breaking, and fixing software matters more than ever. Not because AI needs a babysitter, but because production systems need an adult in the room.

The single-person software factory isn't a developer writing code. It's a technical leader making thousands of small judgment calls a day, with AI handling the implementation. That's a very different thing.
