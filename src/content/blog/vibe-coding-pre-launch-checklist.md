---
title: "Vibe Coding to Production: The 7-Point Pre-Launch Checklist"
description: "Before you ship that vibe-coded app to real users, walk this checklist. Seven categories, twenty-one specific checks, no jargon. The difference between a launch and a learning experience."
date: 2026-05-02
author: "Ben McDonald"
tags: ["Vibe Coding", "Production", "Security", "Checklist"]
---

You're about to launch. Real users are about to touch this thing. Investors are about to look. Walk this checklist first.

Twenty-one items across seven categories. Most are short. None are optional. If you can't honestly tick all twenty-one, your launch is going to teach you something expensive.

## 1. Secrets and credentials

**1.1 No secrets in the repo.** Run `git log -p | grep -i 'api[_-]key\|secret\|password'`. If anything matches, you have a problem. Rotate every credential that ever appeared in any commit, even ones you "removed" later. Git remembers.

**1.2 No secrets in client-side code.** Open the deployed JS bundle in your browser dev tools. Search for your API keys. If you find any, they're public, no matter what the AI told you. Move them to server-side only.

**1.3 Production secrets stored somewhere safe.** Vercel/Netlify env vars, AWS Secrets Manager, 1Password, anything but a `.env.production` file on someone's laptop. Document who has access.

## 2. Authentication

**2.1 Auth actually works under attack.** Try logging in with someone else's email + your own password. Try changing the user ID in the URL to fetch another user's data. Try sending an API request without an auth header. If anything succeeds that shouldn't, fix it now.

**2.2 Password reset can't be abused.** Trigger a reset for a known account from an incognito window. Make sure the reset link is single-use, time-limited, and tied to the original session.

**2.3 Sessions expire.** A user who hasn't been active for 30 days should not have a valid session. Persistent "remember me" cookies should still rotate. If your AI generated infinite sessions, fix it.

## 3. Data integrity

**3.1 Database has backups, verified.** Automatic daily backups configured. You have personally restored from one in the last 30 days. Yes, personally. The first time you discover the backup is empty cannot be during the incident.

**3.2 Every destructive operation is reversible.** Soft deletes for anything users care about. Audit logs for admin actions. "Are you sure?" prompts before anything that loses data.

**3.3 Migrations have been tested in staging.** Schema changes have been run against a copy of production data. If you don't have staging, set it up before launch. The first migration that hits production should not be the first time it runs.

## 4. Payments

**4.1 The payment integration is actually tested.** A real card, a successful charge, a successful refund, a webhook delivered, the user's account state updated correctly. End to end. Yes, even though Stripe's docs are good.

**4.2 Failed payments don't trap users in a half-paid state.** What happens when the card declines mid-checkout? Does the user see the error? Does the order land in your DB? Can they retry? Walk it through deliberately.

**4.3 Webhooks are idempotent.** Stripe will deliver the same webhook multiple times. Your code must handle that gracefully. Use the event ID for deduplication, not the order ID.

## 5. Error handling and observability

**5.1 Error tracking is wired up.** Sentry, Highlight, Honeybadger, anything that pages you when production breaks. Confirmed by intentionally throwing a test error and watching the alert fire.

**5.2 Logs exist and are searchable.** When a user reports a bug, you can find the request in the logs in under 60 seconds. If you can't, you don't have logs, you have noise.

**5.3 Health check endpoint.** A `/healthz` or `/api/health` route your hosting provider can poll. Returns 200 if the app is fine, non-200 if not. Used by your provider's uptime monitoring.

## 6. Performance and load

**6.1 Database queries are indexed.** Open the slow query log. Every query over 100ms either has an index, has a reason it can't, or is on a list to be fixed. Vibe-coded apps frequently ship without a single index.

**6.2 Images are optimized.** WebP or AVIF where possible. Width and height attributes set to prevent layout shift. Lazy loading on anything below the fold.

**6.3 The site doesn't fall over with 50 simultaneous users.** Use k6, Artillery, or even just a manual test from 5 different devices. If it dies at 50, what'll happen with 500?

## 7. Legal and trust

**7.1 Privacy policy and terms of service exist.** Real ones, not the placeholder from a template. Whatever country you operate in has rules. Find a lawyer who does startups. Spend the $1500.

**7.2 GDPR / CCPA basics in place.** If you handle EU or California users (you do, even if you don't think so), you need a way for them to request data deletion, a cookie consent banner if you use non-essential cookies, and a clear statement of what you collect.

**7.3 Email deliverability set up.** SPF, DKIM, DMARC records configured. Test sends to Gmail, Outlook, and Yahoo, confirm they land in inbox (not spam). If your transactional emails go to spam, half your auth flow is broken.

## How to use this

Don't try to fix all twenty-one in one day. Score yourself honestly: how many can you tick right now? Anything below 18 means you're not ready to launch publicly. Below 14 means you have a substantial gap.

The good news: this is all tractable work. Most teams can close the gap in two to four weeks of focused effort. Most don't, because it's not glamorous and there's always one more feature to ship.

That's how vibe-coded MVPs become production embarrassments. Not because the AI did anything wrong. Because the founders skipped the unglamorous middle and shipped the demo.

If you're staring at this checklist and wondering where to even start, that's exactly what our [vibe coding rescue](/services/vibe-coding-rescue/) audits do: walk the same twenty-one items (and another forty we don't put in public posts) and hand back a written, prioritized risk report. Usually a week. Sometimes less.

Either way, walk the checklist before you launch. The cost of finding out later is always higher than the cost of fixing it now.
