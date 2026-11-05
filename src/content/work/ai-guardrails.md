---
headline: "Four guardrails that take an AI app to production"
client: "AthEngine"
summary: "A multi-club sports platform, built by our team, where the AI can't run up a bill, can't write data on its own, and can't leak one club's data to another. The guardrails are tests, so breaking one fails the build."
track: production
order: 1
stack: ["Next.js", "TypeScript", "Postgres", "Claude", "Vercel"]
approved: false
---

## The problem

AI features look great in a demo. In production, the same feature can run up a surprise bill, write bad data into the system, or show one customer another customer's records.

AthEngine runs many sports clubs on one platform, so all three risks were real from day one.

## The four guardrails

### 1. One door to the AI model

Exactly one file in the app talks to the AI model, and it pins the model version. Every AI feature goes through that door. That gives us one place to control cost, logging, and which model runs.

### 2. A spend cap per club, checked before every call

Each club has a monthly AI budget. Before any call, the app checks it. A club over its cap gets blocked before the model is ever called, and one club going over never blocks another. Tests cover both.

### 3. AI proposes, a person confirms

Updates that come in from chat or pasted text never write straight to the database. They become proposed changes. For example, an imported tournament schedule creates no games until a club director confirms it.

### 4. Guardrails fail the build

There are at least 13 guardrail test files, covering data isolation between clubs, money routes, AI gating, and more. Every change runs them, plus a live check that one club can't read another club's data. If a guardrail breaks, the change doesn't ship.

## Why it matters for your prototype

None of this is exotic, and it's the difference between a demo and something you can put real customers on.
