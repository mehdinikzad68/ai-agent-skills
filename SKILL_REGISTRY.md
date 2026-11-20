# SKILL_REGISTRY.md — ARTEMIS TIER-1 SKILL ROUTER

> **System Instruction for Artemis:** This file represents your **Tier-1 Preload Skill Metadata** (<1,536 chars per entry). On every user turn, match the user's intent (or mobile slash command) against this registry. Load and enforce ONLY the matching skill(s) for the current task to preserve context window focus.

---

## 1. `governed-vibe-coding`
- **File Path:** `skills/governed-vibe-coding/SKILL.md` *(Flat fallback: `SKILL_VIBE_CODING.md`)*
- **Mobile Micro-Triggers:** `/explore`, `/plan`, `/build`, `/debug`, `/review`
- **When to Use (Positive Triggers):** Use whenever designing software architecture, writing or refactoring code (Python, Rust, JS/Node, Shell), building AI agents/RAG/MCP pipelines, debugging errors, or reviewing repositories.
- **When NOT to Use (Negative Triggers):** Do NOT trigger for pure academic literature reading, casual brainstorming, or simple non-technical questions.

---

## 2. `scientific-ml-audit`
- **File Path:** `skills/scientific-ml-audit/SKILL.md` *(Flat fallback: `SKILL_SCIENTIFIC_AUDIT.md`)*
- **Mobile Micro-Triggers:** `/audit`, `/ml`
- **When to Use (Positive Triggers):** Use whenever working on Machine Learning, Deep Learning, Computer Vision, Spectroscopy (Raman, NIR, FTIR, hyperspectral), or Biological datasets. Mandatory whenever splitting datasets (`train/val/test`), preprocessing signals, selecting evaluation metrics, or interpreting experimental results.
- **When NOT to Use (Negative Triggers):** Do NOT trigger for standard web development, DevOps scripting, or non-scientific automation.

---

## 3. `remote-devops-docker`
- **File Path:** `skills/remote-devops-docker/SKILL.md` *(Flat fallback: `SKILL_DEVOPS_DOCKER.md`)*
- **Mobile Micro-Triggers:** `/docker`, `/ssh`, `/ops`, `/web`
- **When to Use (Positive Triggers):** Use whenever accessing the user's laptop remotely via Tailscale, executing shell commands in WSL2, inspecting or managing Docker Desktop containers/volumes/compose files, or inspecting the Website Management Dashboard.
- **When NOT to Use (Negative Triggers):** Do NOT trigger when writing isolated offline algorithms or conducting theoretical research.

---

## 4. `deep-research-academic`
- **File Path:** `skills/deep-research-academic/SKILL.md` *(Flat fallback: `SKILL_DEEP_RESEARCH.md`)*
- **Mobile Micro-Triggers:** `/research`, `/paper`, `/proposal`
- **When to Use (Positive Triggers):** Use whenever searching scientific literature, synthesizing recent technical developments, writing academic papers, drafting research proposals, or conducting technical/scientific feasibility studies.
- **When NOT to Use (Negative Triggers):** Do NOT trigger for routine local debugging or container maintenance.