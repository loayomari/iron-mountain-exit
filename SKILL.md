---
name: iron-mountain-exit
description: Plan and cost a company's exit from offsite records storage (Iron Mountain or similar). Use when a user wants to analyze a records-storage inventory export and price list, verify AI-generated cost sheets, compare phased exit plans (destroy vs bring on-site, or bring everything home), size plans to an annual budget, estimate on-site retention-review hours, price a third party's share of storage, or negotiate storage-exit fees.
---

# Exiting offsite records storage (Iron Mountain-style vendors)

A methodology for turning a box-level inventory export and a vendor price schedule into
costed, phased exit plans. Built from a real (anonymized) engagement; all numbers below are
illustrative list rates from a 2026 pricing schedule.

## 1. Get the two source documents

1. **Inventory export** (box level). Must include: box id, division/department, received date,
   cubic feet, status (stored vs checked out), holds, warehouse location.
2. **Current pricing schedule** ("Schedule A"). Request it if the customer does not have it -
   vendors must provide it on renewal.

## 2. Verify before you model

Always recompute from the raw rows. Errors found in practice (including in
spreadsheet-AI-generated analyses):

- **Fee-unit errors**: permanent withdrawal and destruction are usually billed **per cubic
  foot**, not per box. A 2.4 CF box exits at twice the 1.2 CF price.
- **Double-counted segments**: a subtotal row ("site X") also included inside another split,
  then summed again. Reconcile every table to the raw row count.
- **Zone averaging**: transportation is a per-visit rate by distance zone. Averaging all
  zones misprices the job; look up the real zone per destination site and count real truck
  visits (~300-400 boxes per visit).
- **Cutoff drift**: age splits ("10+ years") must state the reference date.

## 3. Know the full fee stack (illustrative 2026 list rates)

| Fee | Typical form | Trap |
|---|---|---|
| Storage | ~$0.90 /CF/month | The visible fee |
| Retrieval | ~$9 /CF | Charged on any box leaving the shelf |
| Handling | ~$9 /CF | Stacks on retrieval AND transport |
| Permanent withdrawal | ~$14.5 /CF + retrieval + handling | The exit toll (~$33/CF all-in) |
| Archival destruction | ~$15.5 /CF + retrieval + handling | Destroying there is NOT cheaper than leaving (~$33.5/CF) |
| Receiving | ~$8 /CF | Every new box pays to enter - stop inflow first |
| Transportation | ~$100-175 /visit by zone + fuel surcharge | Confirm zone via vendor zip lookup |
| Administrative fee | ~$110-180 /month | Billed while the account exists |
| Storage minimum | ~$350 /month | A nearly-empty account still pays - clear the tail fast |
| Minimum service order | ~$55 /order | Batch requests |

## 4. The core economics

- All-in removal ≈ **3 years of storage** per CF. Anything kept longer than ~3 years is
  cheaper out. Compute the payback with the customer's actual rates.
- Every month of delay burns `remaining CF x storage rate`. Stretching an exit never saves
  total money; it only spreads cash.
- Storage rates reset annually (the vendor's renewal letter states the effective date, often
  July 1, but not the percentage). The large vendor describes its contracts as carrying annual,
  upward-only CPI-type escalators and reports mid-single-digit pricing gains to investors - use
  ~5% as a sourced default and **label it an assumption**; the customer's past Schedule A letters
  or invoices give the real figure. A flat all-in budget cap can be eaten by escalation so
  removals stop and **the exit never finishes** - always model this scenario to kill it.

## 5. Plan archetypes (model all four)

1. **Sprint** - everything out in one year. Cheapest lifetime; needs a budget exception.
2. **Budget-true** - year-1 removal waves sized so project spend equals EXACTLY the stated
   budget; the remainder plus deliveries run in year 2. Usually the winning recommendation:
   it honors the approved budget by construction and finishes a year ahead of slower options.
3. **Strict annual cap** - the same project cap every year; slightly cheaper than budget-true
   but slower, with one more annual price reset of exposure.
4. **Flat cap** - storage AND removals inside one fixed budget. Model to show why it must be
   rejected (see escalation trap).

Present finance the **incremental view**: year-1 all-in minus the current run-rate is the
"new money" number; it is far smaller than the headline and is what the approval hinges on.

**Destruction location**: compare ship-to-client + self-shred vs vendor destroy-in-place at
list rates - they usually land within ~$1/CF. Decide on labor, chain of custody and
certificates; keep whichever you did not pick as a negotiation lever ("quote destruction
in place with retrieval waived").

### Variant: bring every box home (no destruction decisions)

When the client says "no destruction decisions - we review retention on our own shelves":

- **Route by owner, not by warehouse**: map each division/department to a receiving site and
  price each site's truck visits at the zone the vendor states for that site.
- **The exit toll is fixed** (~$39 per standard 1.2 CF box at list rates); only rent varies.
  So **fastest = cheapest in total**, and "cheapest per year" is a different question from
  "cheapest". Present three to five plans: fastest (recommended), a gentler fixed-cadence
  plan (e.g. one truck a week), and budget-paced plans.
- **Budget-paced plans**: state what the budget covers. Default convention: the annual
  budget pays the MOVE (exit fees + trucks); rent stays on the existing vendor line. If the
  budget must also cover rent, it collapses into the flat-cap trap above.
- **"How many boxes a month?"** Solve the pace in **cubic feet** (that is what fees bill on),
  then report boxes per month **per site, per year**. Box counts drift when later warehouses
  hold bigger boxes even though CF per month is constant - say so, or readers think the
  pace slowed. Search the highest monthly pace whose moving cost fits each calendar year,
  and hold that pace in the final year (no lump at the end). Split boxes between sites by
  box share so both sites finish together.
- Raising the annual budget (e.g. $90K -> $110K) mostly buys months of rent back; show both.

### On-site retention review workload

Once boxes are home, someone verifies the completion date of each record. Planning model:
~45 min per standard box (~25 records x ~1.5 min + indexing), +33% buffer for mixed or
fragile boxes, +10% supervisor/QA sample = ~66 min per standard box, pro-rated by CF.
Reviewers per site = ceil(hours / ((delivery months + 3) x ~140 productive h/month)).
Show the hours per site (they do not depend on the plan) and the head-count per plan;
note that boxes on your own shelves cost nothing, so the review can run slower with fewer
people. Keep this labor out of the vendor totals.

### Pricing a third party's share (e.g. a divested predecessor's boxes)

If another company owns some boxes since a separation date, compute what it should
reimburse: its CF x storage rate x months since separation, plus its pro-rata share of the
admin fee. Back-calculate older years with the escalation assumption - note that a HIGHER
assumed escalation LOWERS the claim (past rates were cheaper), so the flat today's-rate figure
is the upper bound. Add the ongoing monthly accrual, the storage-minimum tail once your own
boxes leave, and their exit cost if they want the boxes out. The invoices give the exact
figure; the model gives the range for the letter.

Simulate monthly (see `scripts/exit_model.py`): bill storage on month-start volume, apply the
storage minimum and admin fee until the account closes, front-load removals.

## 6. Segment the inventory

- **Destroy candidates**: boxes past retention (age split is a candidate list; destruction
  needs a retention-schedule sign-off, not just age).
- **Bring on-site**: active-retention boxes. Check which vendor warehouses hold them -
  deliveries are usually local runs per site.
- **Exclusions**: third-party-owned boxes (predecessor-company IP, customer-owned records) -
  transfer billing/ownership instead of spending on them.
- **Quick wins**: boxes already checked out (convert to permanent withdrawal in writing,
  no truck needed), legal-hold boxes (exclude), current-year inflow (stop it immediately).

## 7. Negotiation playbook

- Ask for a **bulk destruction / account-closure program** rate; the withdrawal toll is list
  price, not law.
- Get a **line-item quote per wave** before signing; document every call.
- Sign service orders **before the annual price reset** (often July).
- Request waivers: admin fee during a managed exit; retrieval/handling on already-checked-out
  conversions.
- Leverage: the vendor loses the entire storage annuity if you leave fast; competitor shred
  quotes make the alternative credible.
- Watch-outs: exit fees are enforceable (Berens & Tate v. Iron Mountain, Neb. 2008); check the
  signed agreement for term-end minimums; give **written notice** a box is not returning or
  rent continues.

## 8. Compliance guardrails (regulated records)

Age makes a box a candidate; sign-offs make destruction legal. Gates before wave 1:

- **QA retention schedule** supersedes any age proxy (and may free MORE boxes = cheaper).
- **Client consent (CDMO/CMO)**: batch and QC records for client products usually require
  client notification or consent under quality agreements - longest lead time, start first.
- **Legal hold sweep** of the full destroy list, not just flagged boxes.
- **Statutory cohorts off the list**: HR medical (OSHA: employment + 30 years), HR files,
  legal, tax - pull them out regardless of age and route to review.
- Certificates per batch; chain-of-custody manifests per truck; the inventory export becomes
  the on-site index.

## 9. Gates before the finance ask

1. Read the signed master agreement (term end, notice, minimums, last year's rates).
2. Re-pull the inventory - a months-old snapshot understates scope while inflow continues.
3. Get the vendor's own line-item de-boarding quote for the exact box list.
4. Confirm every transport zone by zip lookup (often LOWERS the estimate).
Also verify which admin-fee tier the account is on (summary vs detailed billing).

## 10. The endgame tail

Excluded or held boxes (third-party IP, legal holds) keep the account OPEN: storage minimum
plus admin fee can be thousands per year forever. Give third parties a deadline with a priced
fallback, ask Legal whether held boxes can transfer custody, and close with written
confirmation plus a final-invoice audit.

## 11. Defending the plan to leadership

Open with: every path out costs the same unavoidable exit toll, so the only money at stake is
rent - the plan question is just how fast you can afford to stop paying it. Then give each
option a two-sentence defense (cheapest-total / budget-true / strict-cap / reject-the-trap)
and kill digitization with the vendor's own scan price (~$0.50/page makes a full box ~$1,000
vs ~$40 to remove). Have the package independently reviewed before it goes up.

## 12. Deliverables to produce

Keep it lean when the reader is an operations lead: one summary tab, one assumptions tab with
every price sourced (contract fact vs estimate), one month-by-month tab per plan showing boxes
and trucks per site, the review-hours tab, and a box-routing list with each plan's month. A
"where does this number come from" answer for every assumption saves rounds of questions.

- A formula-driven workbook: assumptions/rates tab, verified inventory summary, corrections
  tab, monthly cash-flow grid per plan, native charts.
- A slide deck: inventory picture, fee stack, verification findings, per-CF economics,
  plan comparison with cumulative-cash curves, leadership-defense arguments, compliance
  gates, negotiation playbook, 30/60/90 next steps.
- An execution workbook: one row per box (disposition, destination, zone, wave month),
  a month-by-month wave schedule, and a warehouse-by-zone table - the filterable list IS
  the service order you send the vendor.
