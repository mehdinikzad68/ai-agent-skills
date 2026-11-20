---
name: court
description: >-
  Put an idea on trial (دادگاه ایده): a prosecutor sub-agent argues it fails,
  a defense sub-agent argues it works, they rebut each other, independent
  juror sub-agents with different lenses vote blind (no juror sees another's
  vote), and a judge sub-agent reads the verdict and the changes that would
  flip it. Use when Mehdi wants honest pushback instead of agreement, asks
  «این ایده خوبه؟» / "is this a good idea", wants an idea, plan, pitch,
  price or claim stress-tested, or says «دادگاه», «محاکمه کن», "court" or
  "put it on trial". Default trial is 6 jurors (11 sub-agent calls);
  --full is 12 jurors (17 calls).
argument-hint: "[--jury N | --full] [--seed S] <the idea, plan or claim>"
license: MIT
metadata:
  author: "Alex Chen (@nocodealex); Artemis adaptation for Mehdi Nikzad"
  homepage: "https://chen.media"
  source: "https://github.com/alexyc9381/court-skill"
  version: "1.1.0-artemis"
---

# court — دادگاه ایده (Artemis adaptation)

Adapted from the MIT-licensed court skill by Alex Chen. Changes from upstream:
the default jury is **6, not 12** (call/cost discipline — Mehdi pays for every
sub-agent call in quota), the juror pool has **14 seats** including two
Iran-specific seats (The Iran Regulator, The Iranian Customer), the optional
**Jev gate score is rendered as an advisory, never as a vote**, the verdict
file uses Persian headings, and orchestration uses Artemis `subagent.spawn`
instead of the Claude Code Agent tool.

For when a single answer would just agree with Mehdi. Instead, the idea goes
on trial: a prosecutor builds the case against it, a defense builds the case
for it, and jurors who never see each other vote. You (Artemis) are the clerk
of the court. You never argue, never vote, and never soften the verdict.

What Mehdi typed after the trigger: the case text. If it is blank, take the
case from the conversation: the idea, plan or claim he most recently wanted
an opinion on. If this skill fired on its own (he never asked for a trial),
ask once first and offer the 6-juror default.

## The tool

All bookkeeping goes through `court.py` in this skill's folder:

```bash
python3 ~/workspace/custom-skills/court/court.py <command>
```

Below, `COURT` means exactly that command. State lives in `.court/<run>/`
inside a per-trial working folder — create it under
`~/workspace/court-trials/<YYYYMMDD>-<slug>/` so trials stay findable and out
of project repos. Every command after `init` finds the run through
`.court/LATEST` in that folder; run all commands with that folder as cwd.

## Step 1: size it

Read the flags out of the request. Everything that is not a flag is the case.

| flag | meaning |
| --- | --- |
| (none) / `--quick` | 6 jurors, 11 sub-agent calls. The default. |
| `--jury N` | N jurors, 3 to 14 (the pool size). |
| `--full` | 12 jurors, 17 calls. Only when Mehdi asks for the full court or the stakes justify it. |
| `--seed S` | Fixes which jurors sit on a smaller jury. Default: random, and recorded. |

Run `COURT plan` with the same flags and tell Mehdi in one line how big the
trial is (for example «۶ عضو، ۱۱ فراخوانی عامل»), then start.

## Step 2: write the case file

**Sub-agents cannot see this conversation.** Every role knows only what is
in the case file, so write `.court/case.md` to stand on its own:

- First line: the case in one sentence, in Mehdi's own words where you can.
- Then everything he gave that matters: numbers, audience, budget, timeline,
  what he has already tried, constraints — including Iran constraints that
  matter (permits, payment rails, Toman pricing) when they are part of the
  case, so the Iran seats have a record to judge.
- Do not add facts he never gave, and do not write your own opinion into it.
  A case file that leans one way decides the trial before it starts.

## Step 3 (optional): Jev advisory

If the Jev decision gate is configured and reachable, run it on the case
text before the trial and write its result (risk score, route, one-line
reason) into `jev.md` in the run folder after `init`. Jurors never see it —
it is rendered at the end of `VERDICT.md` under «نظر مشورتی Jev (رأی نیست)»
as a cross-check against the jury, not as a vote. If Jev is unreachable,
skip this step silently; the trial does not depend on it.

## Step 4: open the trial

```bash
COURT init --case-file .court/case.md [--jury N | --full] [--seed S]
```

## Step 5: the trial

Always drive it with `COURT next`. Phases in order: `opening`, `rebuttal`,
`jury`, `judge`.

Every phase works the same way:

1. `COURT prompts <phase>` writes one brief per job and lists the jobs still
   to run, in waves of at most 6.
2. Launch **one wave at a time** with `subagent.spawn`: spawn all jobs of
   the wave in parallel in a single turn. Each child's task is exactly:
   `Read <brief path> and follow it exactly. It is your whole brief.`
   Children inherit this conversation's context, so add one line to each
   task: `Ignore the conversation context; the brief file is your only
   record.` Wait for every result of the wave before launching the next.
3. After the last wave, run `COURT next`. If an output is missing it sends
   you back to the same phase, and `prompts` then lists only the missing
   jobs. Re-run those once. If a juror fails twice, write the single line
   `NO VOTE` into its file (`COURT check jury` lists it) and move on.
   Never write a vote, a statement or a judgment yourself.

## Step 6: the verdict

When `COURT next` says the trial is over:

```bash
COURT render
```

It counts the votes, writes `VERDICT.md` into the run folder and prints it.
Present it to Mehdi in Persian: the verdict line, the vote table and the
judge's sections, exactly as written — plus at most two lines of your own:
the single condition for acquittal you would start with, and the path to the
full trial folder. Follow Mehdi's standing gloss rule for technical terms in
your own added lines.

Rules for you, the clerk:

- Never change, soften or re-count the verdict. A guilty verdict is useful
  information, not bad news to cushion.
- Never add praise the jury did not give.
- The jury is one model family wearing 14 lenses; if Mehdi leans on the
  vote count as if it were 14 independent humans, say once, plainly, that
  the votes are correlated — then stop, do not lecture.
- If Mehdi disagrees with the verdict, offer a retrial with the changes
  from "Conditions for acquittal" written into a new case file. Do not
  argue for either side yourself.
- A verdict is a structured second opinion, never legal, financial or
  professional advice, and never a substitute for real market data: when a
  charge turns on a checkable fact (a price, a permit, an eligibility
  rule), name that check as the follow-up instead of treating the vote as
  the answer.
