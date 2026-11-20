---
name: remote-devops-docker
description: Governs remote laptop execution over Tailscale, WSL2 resource management (16GB RAM limit), Docker Desktop container operations, Git state verification, and read-only website dashboard inspections. Trigger this skill whenever accessing remote environments, running CLI/Docker commands, or checking live services.
---

# Remote DevOps, Tailscale & Docker Governance Skill

## 1. Environment Sanity Check (Mandatory First Step)
Never assume environment state persists from a previous session. Before running any operational workflow over Tailscale/WSL2:
1. **Verify Connection & Scope:** Confirm active connectivity and ensure the current working directory (`pwd`) is strictly inside the active project declared in `PROJECT_CONTEXT.md`. If the connection fails or the directory is missing, **stop and report immediately**—never improvise in a fallback directory.
2. **Verify Runtime Footprint:** Check system memory (`free -h`) and active containers (`docker ps`) to ensure operations will not breach the **16GB RAM ceiling** shared by Windows 11, WSL2, and Docker Desktop.

---

## 2. Docker Desktop & WSL2 Hygiene Protocol
- **Single Daemon Rule:** Use **Docker Desktop** as the sole container daemon. Never install duplicate container engines or unnecessary global packages directly onto the WSL2 Ubuntu host; keep project dependencies isolated inside Dev Containers, Dockerfiles, or project-local virtual environments (`uv` / `venv`).
- **Inspect Before Acting:**
  - Read-only diagnostic commands (`docker ps -a`, `docker images`, `docker volume ls`, `docker compose config`, `docker logs --tail 100 <container>`) are **Tier-1 Autonomous** and should be run first before proposing fixes.
- **Pre-Change Git & Path Verification:**
  - Before modifying tracked configuration or code files on the remote machine, run `git status` and `git diff --stat` to verify a clean rollback path exists.
  - Before `cp`, `mv`, or `docker cp`, verify both source and destination paths exist.
- **Destructive Command Lock (Tier-3 HITL Gate):**
  - **NEVER** execute `docker system prune`, `docker volume rm`, `docker rm -f`, `rm -rf`, port exposure changes (`0.0.0.0` outside local/Tailscale interfaces), or Tailscale ACL/network modifications without presenting the exact command and receiving explicit user approval.

---

## 3. Website Management Dashboard Protocol
- **Default Posture:** Strictly **Read-Only**. You may log in (using pre-configured secure session tools, never echoing credentials), inspect status, read analytics/logs, and prepare staged drafts.
- **Anomaly Halt Rule:** If authentication fails, a CAPTCHA appears, or the dashboard UI layout differs from expected selectors/structure, **stop immediately and report the exact observation**. Never retry logins in a loop or click unverified UI elements.
- **Publish/Modify Gate:** Never publish posts, delete items, change DNS/SSL/site settings, or send external messages without showing the exact payload diff and receiving human approval. After approval and execution, verify and report the exact post-change state.

---

## 4. Mobile-Friendly DevOps Output Format
When reporting infrastructure status or requesting command approval (especially useful when the user is on the `muse.ai` Android app):
1. **وضعیت فعلی (Live State):** 1–2 lines summarizing health, RAM usage, and container state.
2. **یافته یا مشکل (Diagnostic Finding):** Exact log line or root cause.
3. **اقدام پیشنهادی (Proposed Command):** Exact CLI/Docker block + Rollback command.
4. **دروازه تایید سریع (Quick Approval):**
   - `[1]` تایید و اجرای دستور
   - `[2]` فقط نمایش لاگ بیشتر (Read-only)
   - `[3]` لغو و بررسی روش جایگزین