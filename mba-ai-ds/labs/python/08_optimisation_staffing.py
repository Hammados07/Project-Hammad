# %% [markdown]
# # Lab 08 · Erlang C staffing + cheapest shift plan (Modules M10, M20)
# 🧒 Part A: how many cooks do we need so hungry customers don't wait too long?
#    Part B: which shifts should cooks work so we cover every hour at the lowest cost?

# %% Setup
import math

import numpy as np
import pandas as pd
from scipy.optimize import linprog

# %% PART A: Erlang C
def erlang_c(traffic, agents):
    """Probability that a caller has to wait (all agents busy)."""
    if agents <= traffic:
        return 1.0
    top = traffic ** agents / math.factorial(agents) * agents / (agents - traffic)
    bottom = sum(traffic ** k / math.factorial(k) for k in range(agents)) + top
    return top / bottom


def service_level(calls_per_hour, aht_sec, agents, target_sec=20):
    """% of calls answered within target_sec seconds."""
    traffic = calls_per_hour * aht_sec / 3600          # Erlangs
    pw = erlang_c(traffic, agents)
    return 1 - pw * math.exp(-(agents - traffic) * target_sec / aht_sec)


def agents_needed(calls_per_hour, aht_sec, sl_target=0.80, target_sec=20, shrinkage=0.30):
    """Smallest number of agents meeting the SLA, grossed up for shrinkage (breaks, training, leave)."""
    traffic = calls_per_hour * aht_sec / 3600
    n = max(1, math.ceil(traffic))
    while service_level(calls_per_hour, aht_sec, n, target_sec) < sl_target:
        n += 1
    return n, math.ceil(n / (1 - shrinkage))


# One example, explained
calls, aht = 120, 300
traffic = calls * aht / 3600
print(f"{calls} calls/hour × {aht}s AHT = {traffic:.1f} Erlangs (agents' worth of pure talk time)")
for n in range(int(traffic) + 1, int(traffic) + 6):
    print(f"  {n} agents → SLA {service_level(calls, aht, n):.1%}, occupancy {traffic / n:.0%}")
net, gross = agents_needed(calls, aht)
print(f"👉 Need {net} agents on the phones → {gross} scheduled after 30% shrinkage")

# %% Requirement for a whole day (hourly forecast)
hours = list(range(8, 22))
forecast = [40, 80, 130, 150, 140, 110, 95, 100, 105, 95, 90, 75, 50, 35]
req = [agents_needed(c, 300, shrinkage=0)[0] for c in forecast]
print(pd.DataFrame({"hour": hours, "calls": forecast, "agents_required": req}).to_string(index=False))

# %% PART B: cheapest shift plan with integer linear programming
# Shifts: full-time 8h (cost ₹800) starting 08:00–14:00; part-time 4h (cost ₹450) starting 08:00–18:00.
shifts = [(start, 8, 800) for start in range(8, 15)] + [(start, 4, 450) for start in range(8, 19)]
# A[h][s] = 1 if shift s covers hour h
A = np.array([[1 if s <= h < s + length else 0 for (s, length, _) in shifts] for h in hours])
cost = np.array([c for (_, _, c) in shifts])

# linprog minimises cost·x subject to A_ub·x ≤ b_ub, so "coverage ≥ requirement" becomes "−A·x ≤ −req"
res = linprog(c=cost, A_ub=-A, b_ub=-np.array(req), bounds=(0, None),
              integrality=np.ones(len(shifts)), method="highs")
x = np.round(res.x).astype(int)
plan = pd.DataFrame([(f"{s:02d}:00", f"{length}h", n) for (s, length, _), n in zip(shifts, x) if n > 0],
                    columns=["start", "length", "agents"])
print(plan.to_string(index=False))
print(f"Total daily cost ₹{cost @ x:,}")
cover = A @ x
print(pd.DataFrame({"hour": hours, "required": req, "scheduled": cover, "surplus": cover - np.array(req)}).to_string(index=False))

# %% Your turn
# a) Change the SLA target to 90/20. How many more agents at peak? What does the daily cost become?
# b) Remove part-time shifts. How much more expensive is the plan? (That's the value of flexibility!)
# c) Why must agents be integers? What happens if you delete the `integrality` argument?
