---
headline: "A content pipeline that holds instead of publishing"
client: "North Florida Mortgage"
clientUrl: "https://www.nflmortgage.com"
summary: "Weekly blog and social posts for a mortgage broker, where one bad post is a real problem. Claude drafts, a compliance check runs, and anything that fails is held with an alert. Nothing goes out on its own say-so."
track: production
order: 3
stack: ["Python", "TypeScript", "Claude"]
approved: false
---

## The problem

Mortgage marketing has rules. Loan posts need the license footer. Rate talk has to be careful. Old phone numbers from a previous vendor were still floating around, and one wrong number on one post undoes months of cleanup.

The broker needed steady weekly content without someone checking every line by hand.

## What we built

Every week, Claude writes one blog post and two social posts on a planned topic, using only the facts cited for that topic. Then a script checks them, schedules them, and saves a copy.

## What makes it production

- **A compliance check before anything is scheduled:**
  - Loan posts must carry the license footer.
  - Old phone numbers and banned stock phrases are blocked.
  - Rate language without the right flag gets a warning.
- **Fail means hold.** The post is kept and marked held, we get an alert, and nothing goes out.
- **A daily safety net.** An alert fires if the queue runs empty, the scheduler can't be reached, or an approved post never got scheduled. One post once sat unscheduled for weeks before this check existed. Now it can't.
- **X is skipped on purpose.** The required footer doesn't fit in 280 characters, so we don't post there at all.

## The cleanup behind it

The content sits on top of a cleanup: one real office number on every public profile, with every change logged. It replaced tracking numbers from a prior vendor that had scattered across the web.
