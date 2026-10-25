---
name: iron-mountain-exit
description: Plan and cost a company's exit from offsite records storage (Iron Mountain or similar). Use when a user wants to analyze a records-storage inventory export and price list, verify AI-generated cost sheets, compare phased exit plans (destroy vs bring on-site), or negotiate storage-exit fees.
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
- Storage rates escalate annually (customers report high single digits or worse). A flat
  all-in budget cap can be eaten by escalation so removals stop and **the exit never
  finishes** - always model this scenario to kill it.

## 5. Plan archetypes (model all four)

1. **Sprint** - everything out in one year. Cheapest lifetime; needs a budget exception.
2. **Two-phase** - year 1 destroy (no trucks, no space needed, vendor can shred);
   year 2 deliver the keepers on-site. Usually the recommended balance.
3. **Paced** - fixed annual project budget on top of the existing storage line; finishes in
   ~total-removal-cost / annual-budget years. Honest about all-in cash across both lines.
4. **Flat cap** - storage AND removals inside one fixed budget. Model to show why it must be
   rejected (see escalation trap).

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

Destruction only against an approved retention schedule with QA sign-off; certificates of
destruction per batch; legal-hold check per wave; chain of custody manifests per truck; the
inventory export becomes the on-site index.

## 9. Deliverables to produce

- A formula-driven workbook: assumptions/rates tab, verified inventory summary, corrections
  tab, monthly cash-flow grid per plan, native charts.
- A slide deck: inventory picture, fee stack, verification findings, per-CF economics,
  plan comparison with cumulative-cash curves, negotiation playbook, 30/60/90 next steps.
