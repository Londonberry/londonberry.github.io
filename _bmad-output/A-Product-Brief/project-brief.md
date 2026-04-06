# Project Brief: Conversational AI Lead Qualifier

**Project:** Londonberry Conversational AI Widget
**Date:** 2026-04-06
**Brief Level:** Simplified
**Owner:** Ben McDonald

---

## Project Scope

A conversational AI widget embedded on londonberry.com, triggered by a "Start a conversation" button. The widget acts as Ben — helping visitors articulate their ideas, delivering tangible value, and qualifying leads through natural conversation rather than forms.

The AI adapts its personality and approach based on three visitor archetypes:

- **Nervous First-Timer:** Curious but skeptical. Needs psychological safety, choose-your-own-adventure entry paths, and a tangible takeaway (AI-generated prototype image of their idea).
- **Enterprise PM:** Has budget and authority but no time. Needs direct, predictive engagement, relevant past work surfaced inline, and a frictionless path to booking a call.
- **Tire-Kicker:** Browsing, not committing. Gets the fun, casual, conference-booth version of Ben — plus one memorable insight to take away.

Core value delivery mechanisms:

- AI-generated concept images from conversation context
- Live web research to demonstrate understanding
- Portfolio and case studies surfaced at relevant moments
- Calendly integration for enterprise scheduling

## Challenge / Opportunity

The current londonberry.com is a static Astro site with no interactive engagement mechanism. Visitors arrive, browse, and leave without a meaningful touchpoint. Traditional contact forms create blank-page anxiety, offer no value exchange, and reduce lead qualification to form fields.

Ben's greatest strength is connecting with people — reading their energy, adapting his approach, and delivering value before asking for anything. This widget brings that ability online, 24/7, turning the website from a brochure into a conversation.

## Design Goals

### Experience Goals

- Visitors should feel like they're texting a friend who happens to build software — not interacting with a corporate chatbot.
- Every visitor receives value regardless of buy intent: a prototype image, relevant research, or a memorable insight.
- No visitor should feel "extracted from" — the AI gives more than it asks.

### Business Goals

- Lead qualification happens invisibly through emotional resonance and engagement signals, not explicit qualifying questions.
- Enterprise visitors convert to calendar bookings.
- Explorers receive a wow moment (prototype image) that builds lasting brand impression.
- Tire-kickers leave with a callback — one insight they'll think about later.
- Conversation data feeds a lightweight custom CRM, capturing richer context than any form could.

### Functional Goals

- Adaptive personality engine that shifts tone based on visitor signals.
- Depth gating — information access scales with engagement level.
- "Earn before you ask" rhythm — value delivery precedes any asks.
- Vulnerability-first approach: honesty about building the business acts as a natural qualifier.

## Constraints

### Timeline

- **MVP target:** April 10, 2026
- Prioritize the happy path (nervous first-timer flow) for MVP, expand to other visitor types iteratively.

### Technology

- **Frontend:** Astro static site remains unchanged. Widget implemented as an Astro Island (React/Preact interactive component).
- **Backend:** Lightweight service (Cloudflare Workers or similar) handling AI conversation, storage, and integrations.
- **Database:** Supabase, Turso, or Cloudflare D1 for conversation storage and lead data.
- **CRM:** Custom lightweight CRM built around conversation data — no off-the-shelf CRM. Conversations and extracted metadata (visitor type, idea summary, budget signals, engagement score) are the CRM records.

### APIs and Integrations

- **Claude API** — conversation engine
- **Image generation API** — prototype concept images from conversation summaries
- **Web search API** — real-time research during conversation
- **Calendly** — enterprise visitor scheduling

### Budget

- API and hosting costs are acceptable to get launched; optimize after initial deployment.

### Brand

- Must authentically represent Ben's voice — a dedicated voice guide is a prerequisite before building conversation logic.
- Anti-corporate authenticity: humor, vulnerability, directness.
- Three distinct tonal registers mapped to the three visitor archetypes, sharing a common "soul."

---

## Source Context

- Brainstorming session: `_bmad-output/brainstorming/brainstorming-session-2026-04-06-001.md`
