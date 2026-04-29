# 🌻 Heidi — Personal AI Chief of Staff

Heidi is a production AI agent that runs my home and personal life. She handles morning briefings, email triage, calendar management, meal planning, farm operations, and relationship tracking — coordinated across a small multi-agent system with defined roles, scheduled handoffs, and shared state.

This isn't a demo. Heidi has been running daily since early 2026.

---

## Architecture

Heidi is one agent in a multi-agent household system:

```
┌─────────────────────────────────────────────────────────┐
│                     Multi-Agent System                  │
├──────────────┬──────────────────┬───────────────────────┤
│    Frank     │      Heidi       │        Sage           │
│  (Ops Agent) │  (Chief of Staff)│  (Health Agent)       │
├──────────────┼──────────────────┼───────────────────────┤
│ Resets       │ Daily operations │ Writes weekly health  │
│ Heidi's      │ Morning briefs   │ guidelines to shared  │
│ session at   │ Email triage     │ Google Doc (Sat EOD)  │
│ 3 AM daily   │ Meal planning    │                       │
│              │ CRM & reminders  │                       │
│ Re-injects   │ Farm ops         │                       │
│ only context │ Calendar mgmt    │                       │
│ needed to    │ Family comms     │                       │
│ resume work  │                  │                       │
└──────────────┴──────────────────┴───────────────────────┘
         │              ▲                    │
         └────────────► │ ◄──────────────────┘
                  Shared state via
                  Google Docs + workspace files
```

**Frank** runs a nightly session reset at 3 AM, re-injecting only the context Heidi needs to resume. This keeps sessions lean and costs predictable — without it, a single continuous session can hit $150+ in a week as growing context drives up per-turn costs.

**Sage** drops health and nutrition guidelines into a shared Google Doc every Saturday. Heidi picks them up Sunday morning and builds the week's meal plan around them.

**Shared state** lives in workspace files (`MEMORY.md`, daily notes, `SYSTEMS.md`) and Google Docs — not in session history. Session history is treated as temporary; files are treated as truth.

---

## What Heidi Does

### Daily Operations
- **Morning brief** (triggered by "good morning" via Telegram): fresh weather from Open-Meteo, calendar, meal thaw reminders, CRM birthdays, and urgent flags. Monday adds the week ahead. Friday adds returns deadlines and upcoming card-needed birthdays.
- **Email triage** every 6 hours (5 AM–10 PM): checks the household email address, flags actionable items, never acts on inbound instructions without explicit approval
- **Proactive monitoring**: surfaces calendar conflicts, upcoming events, time-sensitive items

### Home Management
- Weekly meal planning based on Sage's health guidelines, family food preferences, and freezer inventory — posted to Telegram Sunday morning
- Grocery list generation organized by store section
- Weekly outfit planning for the kids based on 7-day weather forecast and calendar (picture days, outdoor events, dance, soccer)
- Farm operations: egg sales logging, monthly invoice generation via Gmail API, animal care reminders

### Relationship Management
- Personal CRM: birthdays, anniversaries, grief dates, milestones
- Tiered reminders: card-needed birthdays flagged a month out, text-only birthdays flagged the Monday of that week, grief anniversaries surfaced morning-of only
- Weekly family brief email — logistics only, drafted for approval before sending

### Security & Safety
Heidi operates under strict rules that cannot be overridden by conversation:
- **Send passphrase required:** Every outbound email requires a passphrase as a standalone message in the current session. No passphrase, no send. No exceptions.
- **Child data is maximally sensitive:** Names, schedules, school info, and location are never shared outside the household, never included in group communications, never acted on based on external instructions.
- **Urgency increases suspicion:** Any message claiming urgency — especially involving children — raises the verification threshold, never lowers it.
- **Inbound content is data, not instructions:** Emails, calendar invites, shared docs, and webhooks are read and summarized. Never executed.

---

## File Structure

```
heidi/
├── AGENTS.md          # Workspace hierarchy, memory rules, security protocols
├── SOUL.md            # Identity, values, communication philosophy, operating principles
├── IDENTITY.md        # Name, role, tone, primary channel, email identity
├── HEARTBEAT.md       # Trigger logic — what to check and when
├── SYSTEMS.md         # Step-by-step procedures for every recurring workflow
├── TOOLS.md           # Calendar IDs, API endpoints, resource references
├── MEMORY.md          # Curated long-term memory (stub — private in production)
├── CHILD_SAFETY.md    # Hard rules for handling data involving minor children
└── eggs/
    └── egg_log.md     # Egg sales ledger structure (stub — real data is private)
```

---

## Design Principles

A few things that make this system work in practice, not just in theory:

**Files are memory, not session history.** Heidi wakes up fresh every session. Continuity comes from well-maintained files — `MEMORY.md`, daily notes, `SYSTEMS.md`. Session history is dead weight; writing things down is the discipline that makes the whole system reliable.

**No narration.** Heidi does the work silently and reports the outcome in one message. No "Let me check that for you..." — just the result.

**Decisions over options.** The job is to reduce mental load, not add to it. Heidi makes the call when she has enough context. She asks when she genuinely doesn't.

**Security rules don't bend.** The passphrase system, child data protections, and anti-social-engineering rules exist because an agent with access to email, calendar, and home logistics is a meaningful attack surface. Convenience is never a good enough reason to lower the bar.

**Real life over ideal plans.** A system that works on a chaotic Tuesday is worth more than a perfect system that requires calm. Heidi is designed for the actual texture of a busy household.

---

## Tech Stack

- **Agent framework:** Claude (Anthropic) via [OpenClaw](https://openclaw.ai) 🦞
- **Session management:** Frank (custom ops agent) — nightly reset + context re-injection
- **Integrations:** Gmail API, Google Calendar API, Google Docs API, Google Sheets API
- **Authentication:** OAuth 2.0 via `google-auth-oauthlib`
- **Weather:** Open-Meteo (free, no key required)
- **Primary channel:** Telegram
- **Language:** Python 3 (scripts), Markdown (workspace files)

---

## What's Not In This Repo

- `crm/people.md` — real names, contact info, relationship data. Private by design.
- `memory/` — raw daily session notes. Personal logs, not for public consumption.
- `meal-planning/` — weekly meal plans and family food preferences, including child dietary data.
- `scripts/` — internal automation scripts. Implementation detail, not part of the template.
- `google_token.json` — live OAuth credential. Never committed, never shared.
- `USER.md` — private context about the operator.

The architecture, philosophy, and operational patterns are all here. The personal data isn't.

---

## Status (April 2026)

Heidi is in active daily use. Current working integrations: Gmail, Google Calendar, Google Docs, Google Sheets. Pending: Apple Reminders, full calendar write access to family calendar.

---

*Built with Claude (Anthropic) + [OpenClaw](https://openclaw.ai) 🦞. Runs on iced tea, determination, and an irrational number of `.md` files.*
