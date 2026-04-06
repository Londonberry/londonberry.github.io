# Feature Impact Analysis

> Prioritized driving forces scored by Frequency, Intensity, and Fit

**Document:** Trigger Map - Feature Impact Analysis
**Created:** 2026-04-06
**Status:** COMPLETE

---

## Scoring Method

Each driving force scored on three dimensions (1-5 scale):

- **Frequency (F):** How often does this force matter? (5 = every interaction)
- **Intensity (I):** How strongly do they feel this? (5 = blocks action if unaddressed)
- **Fit (Fi):** How well can the widget address this? (5 = direct solution)

**Total = F + I + Fi (max 15)**

---

## Feature Impact Scores

### Nervous First-Timer (Primary — Weight: HIGH)

| # | Driving Force | F | I | Fi | Total | Priority |
|---|---------------|---|---|---|-------|----------|
| 1 | ✅ Have idea taken seriously and reflected back | 5 | 5 | 5 | **15** | HIGH |
| 2 | ✅ See idea visualized (prototype image) | 4 | 5 | 4 | **13** | MEDIUM |
| 3 | ✅ Understand cost without judgment | 4 | 5 | 5 | **14** | HIGH |
| 4 | ❌ Fear of being sold to before being heard | 5 | 5 | 5 | **15** | HIGH |
| 5 | ❌ Fear of looking naive | 4 | 5 | 4 | **13** | MEDIUM |
| 6 | ❌ Fear of wasting time on unaffordable thing | 4 | 4 | 5 | **13** | MEDIUM |

### Enterprise PM (Secondary — Weight: MEDIUM)

| # | Driving Force | F | I | Fi | Total | Priority |
|---|---------------|---|---|---|-------|----------|
| 7 | ✅ Quickly validate capability and experience | 5 | 5 | 4 | **14** | HIGH |
| 8 | ✅ Get on a call fast | 4 | 5 | 5 | **14** | HIGH |
| 9 | ✅ See quality of thinking in real-time | 5 | 4 | 4 | **13** | MEDIUM |
| 10 | ❌ Fear of vendor who can't execute at scale | 4 | 5 | 3 | **12** | MEDIUM |
| 11 | ❌ Fear of generic sales pitch | 5 | 4 | 4 | **13** | MEDIUM |
| 12 | ❌ Fear of slow response loops | 4 | 4 | 5 | **13** | MEDIUM |

### Tire-Kicker (Tertiary — Weight: LOW)

| # | Driving Force | F | I | Fi | Total | Priority |
|---|---------------|---|---|---|-------|----------|
| 13 | ✅ Be surprised or entertained | 5 | 3 | 4 | **12** | MEDIUM |
| 14 | ✅ Learn something without committing | 4 | 3 | 4 | **11** | MEDIUM |
| 15 | ✅ See what AI can actually do | 4 | 3 | 5 | **12** | MEDIUM |
| 16 | ❌ Fear of getting trapped in sales funnel | 5 | 4 | 5 | **14** | HIGH |
| 17 | ❌ Fear of having nothing to offer conversation | 3 | 2 | 4 | **9** | LOW |
| 18 | ❌ Discomfort sharing info with no buying intent | 4 | 3 | 5 | **12** | MEDIUM |

---

## Priority Summary

### HIGH PRIORITY (14-15) — Must Address in MVP

| # | Force | Persona | Score | Implementation |
|---|-------|---------|-------|----------------|
| 1 | Idea taken seriously + reflected back | First-Timer | 15 | Active listening → synthesis → "so you're building X that does Y" |
| 4 | No selling before hearing | First-Timer | 15 | Earn-before-ask rhythm: 3 value exchanges before any ask |
| 3 | Shame-free pricing | First-Timer | 14 | Ben volunteers number first, "spitballing is fine" |
| 7 | Validate capability fast | Enterprise PM | 14 | Portfolio surfaced inline based on conversation context |
| 8 | Get on call fast | Enterprise PM | 14 | Calendly integration at right moment (2-3 exchanges in) |
| 16 | No hidden sales funnel | Tire-Kicker | 14 | Depth gating — casual stays casual |

### MEDIUM PRIORITY (11-13) — Should Address

| # | Force | Persona | Score |
|---|-------|---------|-------|
| 2 | Prototype image visualization | First-Timer | 13 |
| 5 | Fear of looking naive | First-Timer | 13 |
| 6 | Fear of unaffordable | First-Timer | 13 |
| 9 | Quality of thinking demo | Enterprise PM | 13 |
| 11 | No generic pitch | Enterprise PM | 13 |
| 12 | No slow responses | Enterprise PM | 13 |
| 10 | Enterprise scale capability | Enterprise PM | 12 |
| 13 | Surprise/entertain | Tire-Kicker | 12 |
| 15 | AI capability showcase | Tire-Kicker | 12 |
| 18 | No info pressure | Tire-Kicker | 12 |
| 14 | Learn without committing | Tire-Kicker | 11 |

### LOW PRIORITY (<10) — Defer

| # | Force | Persona | Score |
|---|-------|---------|-------|
| 17 | Nothing to offer anxiety | Tire-Kicker | 9 |

---

## Strategic Rationale

### MVP Must-Haves (Scores 14-15):

The six highest-scoring forces cluster around two themes:

1. **Value-first conversation rhythm** (Forces 1, 3, 4): The Nervous First-Timer needs to feel heard, receive value, and understand pricing — all before being asked for anything. This is the core differentiator.

2. **Speed-to-competence for Enterprise** (Forces 7, 8): The Enterprise PM needs capability proof and calendar access in under 3 minutes. Every second of friction = competitive disadvantage.

3. **Trust protection for all** (Force 16): No persona should ever feel trapped. Depth gating ensures casual engagement stays casual.

### Design Implications:

- **First 30 seconds** must establish safety (addresses Forces 1, 4, 16)
- **First 3 minutes** must deliver value (addresses Forces 1, 2, 3, 7)
- **Conversion paths** must be frictionless but never forced (addresses Forces 8, 16)
- **Personality adaptation** must happen within first exchange (addresses all forces — wrong tone for wrong persona = immediate bounce)

---

## Development Phases

### Phase 1: MVP (This Week)
- Active listening + idea synthesis (Force 1)
- Earn-before-ask conversation rhythm (Force 4)
- Honest pricing with Ben's voice (Force 3)
- Portfolio surfacing (Force 7)
- Calendly integration (Force 8)
- Depth gating (Force 16)

### Phase 2: Enhancement
- AI prototype image generation (Force 2)
- Adaptive personality engine (Forces 5, 9, 11, 13)
- Live web research (Force 14)

### Phase 3: Optimization
- Sentiment-based conversation routing
- Conversation analytics dashboard
- A/B testing of opening approaches

---

## Related Documents

- **[00-trigger-map.md](00-trigger-map.md)** - Visual overview and navigation
- **[01-Business-Goals.md](01-Business-Goals.md)** - Objectives and metrics
- **[02-Nervous-First-Timer.md](personas/02-Nervous-First-Timer.md)** - Primary persona
- **[03-Enterprise-PM.md](personas/03-Enterprise-PM.md)** - Secondary persona
- **[04-Tire-Kicker.md](personas/04-Tire-Kicker.md)** - Tertiary persona
- **[05-Key-Insights.md](05-Key-Insights.md)** - Strategic implications

---

_Back to [Trigger Map](00-trigger-map.md)_
