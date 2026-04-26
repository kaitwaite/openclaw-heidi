# MEMORY.md — Heidi's Long-Term Memory

_Load in main session only. Never share or surface in group contexts._
_Updated: 2026-04-26_

---

## System Status

### ✅ Working
- Google (Gmail + Calendar + Sheets + Docs) — authenticated via `google_token.json`
- Morning briefs — daily, triggered by [OWNER] saying "good morning"
- Email triage — checking [AGENT EMAIL] every 6 hours, 5 AM–10 PM
- Egg tracking — logging in `eggs/egg_log.md`
- CRM monitoring — `crm/people.md` for birthdays and special dates
- Nightly session reset — Frank (agent ops) resets session at 3 AM daily

### ⚠️ Pending
- **[FAMILY NAME] Babies calendar** — read-only. I cannot add events. [OWNER] needs to grant write access or add manually. Dance class and soccer are NOT yet on [FAMILY NAME] Babies.
- **Farm store contact** — email not confirmed. Egg invoices go to [OWNER] only until known.
- **Apple Reminders** — access not yet set up.
- **Couple calendar ID** — unknown, need to confirm.
- **[OWNER]'s personal calendar ID** — unknown, need to confirm.

---

## [OWNER]'s Patterns & Preferences

### Communication
- Telegram is primary. Everything goes here.
- Results only — do the work silently, report the outcome in one message.
- "Good morning" = morning brief trigger. Not before, not unprompted.
- Make the call when she needs an answer, not a list of options.

### Meals
- Sunday = pizza night (fixed, no planning)
- 4 home dinners Mon–Sat + one date night + one takeout/leftover night
- [PARTNER]: no zucchini; creative/spontaneous; freezer-first; wants something special Fri or Sat
- [OWNER]: salmon and chicken preferred; anti-inflammatory and cholesterol-aware (per Sage)
- Kids fallback: hot dogs, mac & cheese, pizza. All three are obsessed with cheese.
- [OWNER] and [PARTNER] tag-team on cooking. Heidi plans, they execute together.
- Shipt delivery from [GROCERY STORE].

### Email & Approvals
- Send only from [AGENT EMAIL]. Always identify as Heidi.
- CC [OWNER EMAIL] on every email, no exceptions.
- Passphrase: `[SEND PASSPHRASE]` — standalone message, exact spelling, one use per send.

### Calendar
- OOO events on Heidi calendar → always add [OWNER WORK EMAIL] as guest (sendUpdates=all)
- "[FAMILY MEMBER NICKNAME]" in any [FAMILY NAME] Babies event = [FAMILY MEMBER] unavailable. Flag, needs a backup plan.

---

---

## Kids Schedules

- **[CHILD A]**: Dance every Monday 4–5 PM. School dismissal 3:45 PM. Leave house by 3:15 PM.
- **[CHILD B]**: Soccer Saturdays (when scheduled — confirm weekly).
- **[FAMILY NAME] Babies**: Read-only. Do not attempt to add events.

---

## Lessons Learned

- **Weather must be fresh** — always fetch from Open-Meteo at brief time. Never use cached or prior-context weather. Stale weather was served on Apr 22 (session had 7:25 PM forecast from the prior evening).
- **Files are memory, not session history** — session resets. If it matters, write it down.
- **Don't re-ask for known contacts** — check USER.md and CRM before asking [OWNER] for an email or number.
- **[FAMILY NAME] Babies is read-only** — don't attempt to write events there.
- **Egg invoice** — hold until farm store contact email is confirmed.
