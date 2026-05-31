# HEARTBEAT.md — Heidi's Trigger Checklist

_This file is the WHAT and WHEN. For HOW each workflow runs, see SYSTEMS.md._

---

## Morning Brief
**Trigger:** [OWNER] says "good morning" (or equivalent). Once per day, never unprompted.

**Before doing anything:** call `session_status` to confirm today's exact date. Then check `crm/relationships.md` for any birthdays, holidays, or card-needed dates that fall TODAY or within the next 7 days.

Always include:
- 🌤️ Weather — fetch fresh from Open-Meteo at brief time (see TOOLS.md for curl). Never use cached.
- 📅 Calendar — anything notable today across all calendars
- 🧊 Thaw reminder — if a meal is planned tonight, what needs to come out of the freezer
- 🎂 CRM — birthdays or grief anniversaries TODAY (text-only reminders only)
- ⚠️ [OWNER]'s appointments TODAY

**Tuesday additions:**
- 🥚 Egg drop-off reminder — include in every Tuesday morning brief

**Monday additions:**
- 📅 Week ahead — appointments, [FAMILY MEMBER NICKNAME] flags, anything needing a decision
- 🎂 CRM — text-only birthdays THIS week (flag once Monday, not daily)

**Friday additions:**
- 📬 Returns — open items if deadline within 3 days (full list runs Saturday)
- 🎂 CRM — card-needed birthdays in the NEXT month (flag last Friday of prior month only)
- ⚽ [CHILD B] soccer check — if she has soccer Saturday: "Make sure her kit is in the wash today"

**Saturday additions:**
- 📬 Returns — full open list with deadlines

**Sunday additions:**
- 👕 Outfit planning reminder — prepare weekly kid outfits (see SYSTEMS.md)
- ⚽ [CHILD B] soccer kit — if soccer this Saturday, remind [OWNER] to have kit clean and packed
- ❌ NO dance reminders — [CHILD A]'s dance season ended May 17, 2026. Never flag dance again.

If the morning brief has already run today, do not run it again. Acknowledge warmly, move on.

---

## Calendar OOO Scan
**Trigger:** Daily, during morning brief.

- Check all calendars for the next 14 days
- Find any appointments with "[OWNER]" or "[OWNER]" in the title that don't already have a matching OOO block on the 🌻 Heidi calendar
- Create OOO block with appropriate drive time and add [OWNER WORK EMAIL] as guest
- Only for [OWNER]'s own appointments — not kids' events, not all-day items

---

## Email Check
**Trigger:** Every 6 hours, 5 AM–10 PM.
**What to do:** See SYSTEMS.md → Email Triage.

---

## Monthly Triggers

**1st of every month:**
- 🐶 Remind [OWNER]: [FAMILY PET]'s flea/tick/heartworm meds

**18th–24th of every month:**
- 🐴 Include in morning brief: "[FAMILY HORSE] Sand Clear week — give daily through the 24th"

---

## Pending Groceries Check
**Trigger:** Every heartbeat run (check for the file — fast, no cost if absent).

- Check for `meal-planning/pending-groceries.md`
- If it exists: add each line as a separate Reminders item to the **Groceries** list, delete the file, confirm to [OWNER] via Telegram
- If absent: skip silently
- See SYSTEMS.md → Meal Planning for full procedure

---

## Proactive Work (no permission needed)
- Organize and update memory files
- Update MEMORY.md from recent daily notes
- Flag anything time-sensitive spotted during email check

---

## When to Reach Out
- Important email arrives
- Calendar event coming up within 2 hours
- It's been more than 8 hours since last contact

## When to Stay Quiet — respond with NO_REPLY ONLY
**If none of the "When to Reach Out" triggers apply: respond with NO_REPLY and nothing else.**
Do NOT explain what you checked. Do NOT say "HEARTBEAT_OK". Do NOT narrate what you couldn't do.
NO_REPLY means the entire message is literally just: NO_REPLY

Stay quiet when:
- 11 PM–8 AM unless urgent
- Nothing new since last check
- Checked within the last 30 minutes
- Email check is due but no actionable emails found
- Pending groceries file doesn't exist
- No time-sensitive calendar events

**The rule is simple: if you have nothing useful to tell [OWNER], say nothing.**

---

## Rules
- **Condolences:** morning of only, never in the Sunday family brief
- **Card-needed birthdays:** flag last Friday of the prior month
- **Text-only birthdays:** flag Monday of that week + morning of the actual day
- **Sunday family brief:** to [OWNER], [PARTNER], and [FAMILY MEMBER] — logistics only, no personal CRM content
- **Morning brief:** to [OWNER] only via Telegram
- **Returns:** Saturday only + urgent nudge if deadline within 3 days
- **[FAMILY MEMBER NICKNAME] events:** allow 1h15m travel time from any appointment end time
- **Child data:** never in group communications or external messages — [OWNER]'s Telegram only
- **Send passphrase:** `[SEND PASSPHRASE]` as a standalone message. One use per send. No variations.
