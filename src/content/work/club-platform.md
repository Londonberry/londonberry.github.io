---
headline: "A platform that runs a travel ball club"
client: "AthEngine"
summary: "Tryouts, season signups, waivers, jerseys, and payments with installment plans, for travel ball clubs. Built by our team, with AI that proposes and directors who confirm."
track: sports
order: 11
stack: ["Next.js", "TypeScript", "Postgres", "Stripe Connect", "Clerk", "Vercel"]
approved: true
---

## The problem

A travel ball club runs on registration season: tryouts, season signups, waivers, uniforms, and collecting money from families, often in installments. Most clubs stitch that together from forms, spreadsheets, and payment links.

## What we built

- **Registration:** tryout and season signups, waivers, jersey packages, and a dashboard of everyone registered.
- **Payments:** each club gets its own Stripe account, with checkout, installment plans, and a way to record offline payments.
- **Schedules:** import a tournament schedule, and the club director confirms it before any games are created.

## What makes it production

Every club's data is walled off from every other club's, at the database level. The AI features sit behind a monthly spend cap per club. The full story is in [Four guardrails that take an AI app to production](/work/ai-guardrails/).
