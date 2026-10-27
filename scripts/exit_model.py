#!/usr/bin/env python3
"""Generic monthly cash-flow simulator for exiting offsite records storage.

Usage:
  python3 exit_model.py --cf 7500 --destroy-cf 3700 --storage 0.898 \
      --retrieval 9.02 --handling 9.09 --withdrawal 14.52 --visit 122.68

All rates are illustrative; replace with the customer's Schedule A.
"""
import argparse, json

def simulate(a, schedule, months=240, esc=0.0):
    out_cf = a.withdrawal + a.retrieval + a.handling + a.visit*(1+a.fuel)/a.cf_per_visit
    rem = a.cf
    rows, cum, spent_y = [], 0.0, 0.0
    for m in range(months):
        if rem <= 1: break
        yr = m//12
        if m % 12 == 0: spent_y = 0.0
        stor_rate = a.storage*((1+esc)**yr)
        storage = max(rem*stor_rate, a.storage_min) + a.admin
        if schedule == 'sprint':      cf = a.cf/12
        elif schedule == 'twophase':  cf = (a.destroy_cf/12) if m < 12 else ((a.cf-a.destroy_cf)/12)
        elif schedule == 'paced':     cf = max(0, min((a.budget-spent_y)/out_cf, rem))
        elif schedule == 'steady':    cf = a.budget/12/out_cf   # same CF every month, move cost = budget/yr
        else:  # flat: storage+removal inside budget
            mleft = 12-(m % 12)
            head = a.budget - spent_y - storage - (rem*stor_rate+a.admin)*(mleft-1)
            denom = out_cf - stor_rate*(mleft-1)
            cf = 0 if denom <= 0 else max(0.0, head/denom)
        cf = min(cf, rem)
        removal = cf*out_cf
        spent_y += removal + (storage if schedule == 'flat' else 0)
        rem -= cf
        cum += storage + removal
        rows.append(dict(month=m, storage=round(storage), removal=round(removal),
                         remaining=round(rem), cumulative=round(cum)))
    return dict(plan=schedule, months=len(rows), total=round(cum),
                finished=rem <= 1, by_year=_by_year(rows))

def _by_year(rows):
    y = {}
    for r in rows:
        y.setdefault(r['month']//12, 0)
        y[r['month']//12] += r['storage']+r['removal']
    return {k: round(v) for k, v in y.items()}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--cf', type=float, required=True, help='total in-scope cubic feet')
    p.add_argument('--destroy-cf', dest='destroy_cf', type=float, default=0)
    p.add_argument('--storage', type=float, default=0.898)
    p.add_argument('--retrieval', type=float, default=9.02)
    p.add_argument('--handling', type=float, default=9.09)
    p.add_argument('--withdrawal', type=float, default=14.52)
    p.add_argument('--visit', type=float, default=122.68)
    p.add_argument('--fuel', type=float, default=0.10)
    p.add_argument('--cf-per-visit', dest='cf_per_visit', type=float, default=400)
    p.add_argument('--admin', type=float, default=109.95)
    p.add_argument('--storage-min', dest='storage_min', type=float, default=350)
    p.add_argument('--budget', type=float, default=90000)
    p.add_argument('--escalation', type=float, default=0.0, help='annual rate rise; ~0.05 is a sourced default')
    p.add_argument('--box-cf', dest='box_cf', type=float, default=1.2, help='standard box size')
    p.add_argument('--review-min', dest='review_min', type=float, default=45, help='minutes to review one standard box')
    p.add_argument('--review-buffer', dest='review_buffer', type=float, default=0.33)
    p.add_argument('--review-qa', dest='review_qa', type=float, default=0.10)
    a = p.parse_args()
    p_cf = a.withdrawal + a.retrieval + a.handling + a.visit*(1+a.fuel)/a.cf_per_visit
    res = {s: simulate(a, s, esc=a.escalation)
           for s in ('sprint', 'twophase', 'paced', 'steady', 'flat')}
    res['steady']['cf_per_month'] = round(a.budget/12/p_cf, 1)
    res['steady']['std_boxes_per_month'] = round(a.budget/12/p_cf/a.box_cf)
    hrs = a.cf/a.box_cf*a.review_min*(1+a.review_buffer)/60*(1+a.review_qa)
    res['review'] = dict(hours=round(hrs), reviewer_years=round(hrs/140/11, 1))
    print(json.dumps(res, indent=1))
