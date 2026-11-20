# court — دادگاه ایده (Artemis adaptation)

Puts an idea on trial: prosecutor vs defense, rebuttals, blind independent
juror votes, a judge, and a `VERDICT.md` with the changes that would flip
the losing votes.

- Upstream: https://github.com/alexyc9381/court-skill by Alex Chen
  (@nocodealex), MIT — see `LICENSE`. Original design, juror lenses and the
  bookkeeping approach are his.
- Artemis adaptation (2026-11-09, at Mehdi Nikzad's order): 6-juror default,
  14-seat pool with The Iran Regulator + The Iranian Customer, optional Jev
  advisory rendered with the verdict (never a vote), Persian verdict
  headings, `subagent.spawn` orchestration, unclosed-file cleanup in
  `court.py`.

Files: `SKILL.md` (the playbook), `court.py` (bookkeeping only — no model
calls, no network, writes only inside `.court/`), `jurors.json` (the pool),
`tests/test_court.py` (run: `python3 -m unittest discover -s tests`).
