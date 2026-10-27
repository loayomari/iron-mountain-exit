# iron-mountain-exit

A [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) for planning a
company's exit from offsite records storage (Iron Mountain-style vendors): verify the
vendor's fee stack, model phased exit plans month by month, and negotiate the exit toll.

Built from a real engagement, fully anonymized. All rates are illustrative list rates from a
2026 pricing schedule - replace them with your own Schedule A.

## Install

Copy this folder to `~/.claude/skills/iron-mountain-exit/` (or your project's
`.claude/skills/`). Claude Code picks it up automatically.

## What's inside

- `SKILL.md` - the methodology: verification checklist, fee-stack table, plan archetypes,
  monthly simulation recipe, negotiation playbook, compliance guardrails.
- `scripts/exit_model.py` - standalone monthly cash-flow simulator for five plan
  archetypes (sprint / two-phase / paced / steady / flat-cap) plus review-hours sizing.
  No dependencies.

```bash
python3 scripts/exit_model.py --cf 7500 --destroy-cf 3700 --budget 90000 --escalation 0.05
```

## Key lessons encoded

1. Permanent withdrawal is billed **per cubic foot**, not per box.
2. Removal costs about **3 years of storage** - leaving sooner is always cheaper in total.
3. When every box comes home, the exit toll is fixed and only rent varies: **fastest =
   cheapest**. "Cheapest per year" is a different question - answer both.
4. Budget-paced plans: solve the pace in cubic feet, report boxes per month per site per
   year, and state whether the budget covers the move only or rent as well.
5. A flat budget cap that must cover storage AND removals can be eaten by annual rate
   escalation so the exit **never finishes**. Model it to reject it.
6. Escalation is an assumption unless the customer's past rate letters say otherwise -
   label it, source it, and replace it with invoice data.
7. Cap year-1 removal spend at the approved budget ("budget-true" plan) and pitch finance
   the incremental-over-run-rate number, not the all-in headline.
8. Age is only a candidacy test: QA retention schedules, CDMO client consent, legal-hold
   sweeps and statutory HR/legal/tax cohorts gate every destruction wave.
9. Excluded third-party boxes keep the account open at the storage minimum - price the
   endgame tail and the third party's reimbursement, or it eats the savings.
10. Destroying at the vendor costs about the same as withdrawing - decide on labor and
    compliance certificates, not price.
11. Stop inflow first: every new box pays an entry fee and rent forever.
12. Budget the on-site retention review: ~66 min per standard box all-in.
