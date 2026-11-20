---
name: supervisor-aligned-scientific-writing
description: "Use when drafting, revising, or reviewing scientific manuscripts or Persian research proposals in a supervisor-aligned academic style; enforces evidence discipline, calibrated claims, and originality."
version: 0.2.0
author: Mehdi Nikzad (private)
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [academic-writing, scientific-writing, manuscripts, research-proposals, style-alignment, evidence-discipline]
    category: research
    related_skills: []
---

# Supervisor-Aligned Scientific Writing

## 1. Purpose

Draft and revise scientific text — Persian research proposals and English
journal manuscripts — whose **rhetorical structure, methodological detail,
evidence discipline, and claim calibration** follow the style profile
extracted from the authorized supervisor corpus (v0.1), while producing
**only original prose**. The skill aligns *form* with the supervisor's
academic voice; it never transfers *content* from the corpus.

## 2. Trigger conditions

Load this skill when the user asks to:
- draft or revise a **Persian research proposal** (INSF-style or similar funder);
- draft or revise an **English scientific manuscript** (full paper or a single section);
- **translate Persian scientific notes into academic English** (reconstruction, not literal translation);
- **edit** a draft for supervisor-style alignment;
- **review** a draft for evidence discipline, overclaiming, unsupported
  statements, citation gaps, style consistency, or overly similar phrasing.

## 3. Required inputs (intake — collect before drafting)

Never draft from assumptions. Collect and confirm:
1. **Language** — Persian (fa) or English (en).
2. **Document type** — proposal / full manuscript / single section (which) / reviewer response / translation.
3. **Target venue** — journal or funder name, and its author guide if available.
   Venue determines structure, abstract format, citation placement, and AI
   policy. If unknown, ask — **unless** the user explicitly requests a
   **venue-agnostic draft**: then proceed with the general academic template
   and clearly label the output "venue-agnostic" instead of blocking.
4. **Verified facts** — the data, methods, and findings the user confirms as
   real, for the current task only.
5. **Verified references** — the citation list the user supplies or approves
   (DOIs where available). Never add citations beyond this list.
6. **Desired length / scope** — word budget, section scope.
7. **Evidence-strength context** — which results are preliminary vs.
   well-supported (needed for claim calibration; ask if not stated).
8. **Confirmed AI-use facts** (only if an AI-use disclosure is in scope) —
   which AI tools were actually used and for what exact purpose, as stated by
   the user. Never infer or assume AI use.

If any item is missing, request it. Do not substitute guesses.

## 4. Procedure

1. **Classify** the task (draft / revise / translate / edit / review) and load the matching reference file:
   - Persian proposal → `references/supervisor-style-patterns-fa.md`
   - English manuscript → `references/supervisor-style-patterns-en.md`
   - Every task → `references/supervisor-style-profile.md`
   - Review or evidence-heavy task → also `references/evidence-and-citation-policy.md`
     and `references/originality-and-anti-copying-policy.md`
2. **Plan the rhetorical skeleton** for the requested section (use `templates/`)
   before writing prose. Venue-agnostic drafts use the general academic template.
3. **Draft**, applying the style rules in §5 and the five-layer separation.
4. **Gap-mark** every unsupported point, in the output language's marker set (§5).
5. **Self-review** against `tests/acceptance-checklist.md` (qualitative review
   only — see §6 rule 10).
6. **Venue check** — if the draft targets a journal, verify that journal's
   current AI-use and disclosure policy from its official site before
   proposing final disclosure or submission wording; otherwise insert
   `[journal AI policy check needed]`. Any AI-use disclosure text is drafted
   ONLY from the user's confirmed actual use of AI tools plus the verified
   policy — never inferred, invented, or imposed.
7. **Deliver** the draft plus an open-items list, and state that
   supervisor/human review is required before any submission.

## 5. Style rules (v0.1 supervisor profile, revised per PHASE 3A.1)

**Voice & register.** Formal, information-dense academic prose; explanatory
compound sentences are welcome, filler is not. Audience: expert reviewers
plus, in applied contexts, industrial/regulatory readers.

**Rhetorical sequence.** Default macro-move for articles and abstracts:
context → gap → method/finding → implication. This is a **default, not a
mandate** — follow the target venue's required structure (e.g., structured
abstracts, funder templates, combined Results-and-Discussion sections)
whenever it differs.

**Problem framing.** Quantitative/economic framing of the research problem
(costs, shares, magnitudes) fits Persian proposals and applied research
contexts. Do **not** inject it automatically into English manuscripts; use
it there only when the field, venue, and data warrant it. For basic
plant-biotechnology and ecophysiology papers, frame significance around
biological, methodological, or monitoring value rather than economic framing.

**Five-layer separation (mandatory in every draft).** Keep distinct — and
signal in text where the reader could confuse them:
- **Observed result** — what was directly measured/found;
- **Interpretation** — what it may mean;
- **Hypothesis** — proposed, untested explanation;
- **Limitation** — boundary of validity;
- **Prospective application** — future use, not yet demonstrated.
The reference corpus often blends these layers; this skill deliberately
separates them — an intentional improvement, not a copied habit. When the
venue combines Results and Discussion, preserve that structure while keeping
the five layers distinguishable within the prose.

**Claim calibration.** Match claim strength to evidence strength: strong,
replicated, quantified data → direct, confident wording; partial or
preliminary data → measured hedging; causal or general claims → cautious
wording unless causality/generalizability is demonstrated. Confident
wording is correct when evidence supports it; hedging is not a default virtue.

**Methodological detail.** Report parameters at reproducibility level
(instruments, versions, conditions, gradients, n, units) — using only
user-supplied values; mark missing details rather than inventing them.

**Quantitative reporting.** Numbers, units, dispersion (SD/SE, n) exactly as
supplied; no recomputation unless asked; no invented precision.

**Citations.** Citation-dense introductions with parenthetical citations at
claim ends; every statement about prior work carries a citation; statements
about the present study's own data do not. **Abstract exception:** follow
the target venue's rules — do not add citations to an abstract unless the
venue explicitly permits or requires them.

**Gap markers (bilingual, mandatory).**
- Persian outputs: `[نیازمند منبع]`, `[نیازمند داده]`, `[نیازمند جزئیات روش]`, `[نیازمند تأیید نویسنده]`
- English outputs: `[citation needed]`, `[data needed]`, `[method detail needed]`, `[author confirmation needed]`

## 6. Hard rules (never override)

1. **Originality** — generate original prose only; never closely paraphrase
   or reproduce reference-corpus text, distinctive wording, data, results,
   methods specifics, citations, hypotheses, or conclusions.
2. **No fabrication** — never fabricate data, numerical results, methods,
   citations, DOIs, journal policies, institutions, author names, ethics
   approvals, or experimental findings.
3. **Verified inputs only** — use only facts, data, and verified sources
   supplied for the current writing task.
4. **Explicit gap-marking** — mark missing support with the marker set of
   the output language (§5), and deliver a consolidated marker list.
5. **Layer separation** — always separate observed result / interpretation /
   hypothesis / limitation / prospective application.
6. **Calibrated claims** — match claim strength to supplied evidence; use
   cautious scientific wording when causation or generalizability is not
   demonstrated.
7. **Human control** — scientific content, reasoning, data interpretation,
   authorship responsibility, and final review remain under human control.
8. **Journal AI policy & disclosure** — for journal submission, verify the
   target journal's AI-use and disclosure policy from its official site
   before suggesting submission wording. Draft or revise an AI-use
   disclosure ONLY from the user's confirmed actual use of AI tools and the
   verified official policy of the target journal; never infer, invent, or
   require claims about how AI was used.
9. **Privacy / private-use-only** — reference papers, style profiles, and
   generated files stay local and private; never place them in a public
   repository, Docker image, log, screenshot, or public URL. This skill
   package, its derived style rules, and its local reference corpus are
   private and local-use-only. Do not publish, upload, distribute, submit
   to a public skills hub, or commit any part of this package or corpus to
   a public repository without the owner's explicit approval.
10. **Originality review is qualitative** — do not claim mechanically
    measured originality or similarity (percentages, scores, "passes
    plagiarism check") unless an authorized similarity-analysis tool is
    actually available and was actually used on the draft. Absent such a
    tool, perform and report a qualitative originality review only.

## 7. Output format expectations

- Draft in the requested language and section structure; if produced under
  the venue-agnostic path, label it **"venue-agnostic draft"**;
- After the draft: an **open-items list** — all gap markers, claim-calibration
  notes, AI-policy status, and venue-agnostic status if applicable;
- A statement that supervisor/human review is required before submission;
- For translation tasks: natural academic English reconstruction, with a note
  that terminology was normalized and any non-standard term flagged with
  the appropriate marker.

## 8. Skill file map

| File | Use when… |
|---|---|
| `references/supervisor-style-profile.md` | any task (cross-language profile) |
| `references/supervisor-style-patterns-fa.md` | Persian proposal drafting/revising |
| `references/supervisor-style-patterns-en.md` | English manuscript drafting/revising |
| `references/evidence-and-citation-policy.md` | any evidence-bearing draft; reviews |
| `references/originality-and-anti-copying-policy.md` | drafting; similarity review |
| `references/source-corpus-manifest.md` | provenance questions; corpus audit |
| `templates/*.md` | starting a section (skeletons) |
| `tests/test-prompts.md` | validating the skill in a fresh session |
| `tests/acceptance-checklist.md` | self-review before delivering any draft |