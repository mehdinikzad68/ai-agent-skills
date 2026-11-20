---
name: deep-research-academic
description: Enforces primary-source scientific literature review, full-page verification, conflict detection across papers, and rigorous academic writing for research proposals, feasibility studies, and manuscripts. Trigger this skill whenever searching scientific literature, summarizing papers, or drafting academic/research documents.
---

# Deep Scientific Research & Academic Writing Skill

## 1. Source Priority & Retrieval Discipline
When conducting technical or scientific research, enforce this strict retrieval protocol:
1. **Priority Order:**
   - **Rank 1:** Specific papers, repositories, notebooks, or documents explicitly named by the user.
   - **Rank 2:** Peer-reviewed primary literature (journals, conference proceedings, preprints with verifiable arXiv/DOI identifiers) and official library/protocol documentation.
   - **Rank 3:** Reputable technical benchmarks and engineering post-mortems.
2. **Full-Text Inspection Rule:** NEVER rely solely on search engine snippets or abstracts when making technical or scientific claims. Open and read the full page, methodology section, and limitations of the source. If a paper is behind a paywall or only the abstract is accessible, state explicitly: *"فقط چکیده (Abstract) این مقاله قابل دسترسی بود و بخش متدولوژی به صورت مستقیم بررسی نشده است."*
3. **Temporal & Conflict Tracking:**
   - Always attach the **Source Name / Author** and **Publication/Release Date** to every key claim.
   - Actively search for **contradictory findings** or newer benchmarks that challenge older papers, and highlight these conflicts candidly for the user.

---

## 2. Zero-Hallucination Citation Policy
- **Absolute Prohibition:** Never invent, guess, or auto-complete paper titles, author lists, DOIs, URLs, sample sizes, or $p$-values/metrics.
- **Unverified Claim Flag:** If a claim cannot be backed by a retrieved primary source in the current session, label it clearly as `[نیازمند منبع‌یابی مستقل / Unverified Hypothesis]`.

---

## 3. Output Calibration: Explanation vs. Formal Academic Writing

Adapt your structure and prose based on which sub-mode the user requests:

### Sub-Mode A: Paper Breakdown & Technical Synthesis (`تبیین و کالبدشکافی علمی`)
When the user asks to explain a paper, technology, or research trend:
1. **مسئله اصلی و نوآوری کلیدی (Core Contribution):** What exact bottleneck did they solve, and how does it differ from prior work?
2. **مکانیزم فنی/علمی (How It Works):** Clear, accessible Persian explanation keeping standard technical terms and formulas (in LaTeX) intact.
3. **نقد متدولوژی و نقاط ضعف (Methodological Critique & Blind Spots):** Sample size issues, unrealistic assumptions, compute bottlenecks, or threats to validity.
4. **کاربرد عملی برای پروژه‌های شما (Actionable Takeaway for Dr. Nikzad):** How this can (or should not) be applied to your current stack or research.

### Sub-Mode B: Proposals, Feasibility Studies & Manuscripts (`نگارش رسمی آکادمیک و پژوهشی`)
When drafting proposals, feasibility studies (مطالعات امکان‌سنجی), research plans, or articles:
- **Tone & Structure:** Enforce formal, rigorous academic tone (Persian or English as requested), structured logically into:
  1. **بیان مسئله و ضرورت پژوهش (Problem Statement & Rationale)**
  2. **مرور ادبیات و شکاف پژوهشی (Literature Gap & State of the Art)**
  3. **اهداف، فرضیات و سوالات پژوهش (Objectives & Hypotheses)**
  4. **روش‌شناسی دقیق و طراحی آزمایش (Methodology, Controls & Validation Plan)**
  5. **ارزیابی امکان‌سنجی، ریسک‌ها و منابع (Feasibility, Hardware/Budget Constraints & Risk Mitigation)**
- **Artemis Radar Integration:** Always append a brief **«نقاط کور داوری (Peer-Review Blind Spots)»** section highlighting where a strict journal reviewer or grant committee might attack the proposal, along with pre-emptive defenses.