---
title: "Security Debt Is the New Technical Debt"
description: "82% of organizations carry security debt. 1 in 3 AI-generated code snippets has a flaw. Speed without review is a time bomb."
date: 2026-03-28
author: "Ben McDonald"
---

Everyone in software knows what technical debt is. You cut a corner to ship faster, you write a TODO comment, and someday you'll come back and fix it. Sometimes you do. Usually you don't. The codebase gets a little worse, and life goes on.

Security debt works the same way, except when it comes due, it doesn't slow down your sprint — it shows up as a breach, a lawsuit, or a headline.

[Veracode's 2026 State of Software Security report](https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/) puts hard numbers on the problem: **82% of organizations carry security debt. 60% carry critical security debt.** Their assessment: "Teams are pushing code to production at record speeds, often fueled by AI-generated code and automated pipelines, but the mechanism for fixing flaws hasn't kept pace with the mechanism for creating them."

That last sentence is the one that keeps me up at night.

## The AI amplifier

AI-generated code has a specific security problem. Veracode's [Spring 2026 GenAI report](https://www.veracode.com/blog/spring-2026-genai-code-security/) found that **security pass rates for AI-generated code are stuck at 55%.** One in three snippets contains a security flaw. Java fails 72% of the time.

This doesn't mean AI writes bad code. It means AI writes code the way a talented junior developer writes code — quickly, correctly in terms of functionality, but without a paranoid security mindset. It doesn't think about: Who might abuse this endpoint? What happens if this input is malicious? Is this dependency trustworthy? Does this logging accidentally expose PII?

When AI generates 10x the code volume and humans review it at the same speed they always have, the math gets ugly fast. More code, same review capacity, lower coverage.

## I've seen what security failures look like

Early in my career, I worked at Symantec building enterprise security software — the products that filtered spam, viruses, and malicious content from organizational email and web traffic. That job rewired how I think about code. When you build security products, you start seeing attack surfaces everywhere. It's a mindset, not a checklist.

Later, at RF-SMART, our mobile data collection software ran inside warehouses for companies where a security breach wouldn't just be embarrassing — it could compromise supply chains that move physical goods across the country. When I introduced test-driven development to the R&D team, security testing wasn't optional. It was baked into how we built everything.

That experience is why I'm genuinely concerned about the current "ship fast with AI" moment. The tools are incredible. The output is impressive. But the security review layer hasn't evolved to match the production speed.

## What responsible rapid development looks like

At Londonberry, rapid prototyping is our core offering. We use AI-assisted development every day. So I'm not arguing against speed — I'm arguing for **speed with guardrails.** Here's what that means in practice:

**Security review is part of the prototype, not an afterthought.** When we build a prototype, it includes auth, input validation, and dependency auditing from day one. Not because the prototype will go straight to production (it might), but because retrofitting security into a codebase that wasn't designed for it is 10x harder than building it in.

**AI generates the code, humans review the boundaries.** I don't review every line AI writes — that would defeat the purpose. Instead, I focus on the boundaries: API endpoints, authentication flows, data access patterns, third-party integrations. Those are the places where security flaws have consequences.

**Dependencies get scrutinized.** AI loves to pull in packages. It doesn't have opinions about whether those packages are maintained, who maintains them, or whether they've had recent CVEs. That judgment call is still mine.

**The threat model comes first.** Before we write a line of code, we ask: who's going to use this, what data does it touch, and what's the worst thing that could happen? That takes 30 minutes and saves weeks of remediation later.

## The real cost of moving fast

Here's a question for every founder and CTO rushing to ship AI-generated code: what's your security review process? Not your scanning tool — your actual process for ensuring that the code going to production doesn't have a vulnerability that will cost you your company?

If the answer is "we'll deal with that later," congratulations — you're accumulating security debt at a rate that would have been physically impossible two years ago.

Technical debt slows you down. Security debt can shut you down. The tools have changed. The stakes haven't.
