"""
Creates the synthetic (made-up) practice datasets used by every lab.
All data is randomly generated with a fixed seed, so it contains no real
company or customer information and is safe to show on YouTube.

Run:  python make_datasets.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(42)


def call_centre_intervals():
    """30-minute interval data for 2 queues over 8 weeks (like an RTA report)."""
    dates = pd.date_range("2026-01-05", periods=56, freq="D")
    intervals = pd.date_range("08:00", "21:30", freq="30min").strftime("%H:%M")
    # Intraday shape: morning peak, lunch dip, evening bump
    hour = np.array([int(t[:2]) + int(t[3:]) / 60 for t in intervals])
    shape = 1 + 0.6 * np.exp(-((hour - 11) ** 2) / 4) + 0.3 * np.exp(-((hour - 18) ** 2) / 3)
    shape /= shape.mean()
    dow_factor = {0: 1.25, 1: 1.1, 2: 1.0, 3: 1.0, 4: 0.95, 5: 0.7, 6: 0.55}
    queues = {"Billing": (60, 330), "Tech Support": (35, 480)}  # (avg calls/interval, AHT seconds)

    rows = []
    for d in dates:
        for q, (base_calls, base_aht) in queues.items():
            for t, s in zip(intervals, shape):
                offered = rng.poisson(base_calls * dow_factor[d.dayofweek] * s)
                aht = max(120, rng.normal(base_aht, 35))
                # Staffing follows a flattened version of the demand shape, so peaks get understaffed
                s_plan = 0.5 + 0.5 * s
                agents = max(3, int(round(base_calls * s_plan * base_aht / 1800 * 1.15 + rng.normal(0, 1.5))))
                load = offered * aht / 1800 / agents  # occupancy-like pressure
                sla = float(np.clip(98 - 60 * max(0, load - 0.75) + rng.normal(0, 3), 20, 100))
                abandoned = int(round(offered * np.clip((100 - sla) / 250, 0, 0.4)))
                answered = offered - abandoned
                rows.append({
                    "date": d.date(), "day_of_week": d.day_name(), "interval_start": t, "queue": q,
                    "calls_offered": offered, "calls_answered": answered,
                    "answered_within_20s": int(round(answered * sla / 100)),
                    "abandoned": abandoned, "aht_sec": round(aht, 1), "agents_staffed": agents,
                })
    df = pd.DataFrame(rows)
    df["sla_pct"] = (100 * df.answered_within_20s / df.calls_offered.where(df.calls_offered > 0)).round(1)
    df.to_csv(OUT / "call_centre_intervals.csv", index=False)
    return df


def daily_calls():
    """Two years of daily call volume with trend + weekly + yearly seasonality + holidays."""
    dates = pd.date_range("2024-01-01", "2025-12-31", freq="D")
    t = np.arange(len(dates))
    weekly = np.array([1.25, 1.1, 1.0, 1.0, 0.95, 0.7, 0.55])[dates.dayofweek]
    yearly = 1 + 0.12 * np.sin(2 * np.pi * (dates.dayofyear - 80) / 365.25)
    trend = 3000 + 1.2 * t
    calls = np.asarray(trend * weekly * yearly * rng.normal(1, 0.04, len(dates)))
    holidays = np.asarray(dates.strftime("%m-%d").isin(["01-26", "08-15", "10-02", "12-25"]))
    calls[holidays] *= 0.5
    df = pd.DataFrame({"date": dates.date, "calls": calls.round().astype(int), "is_holiday": holidays.astype(int)})
    df.to_csv(OUT / "daily_calls.csv", index=False)
    return df


def customers(n=2000):
    """Telecom-style customers with RFM fields and a churn label."""
    region = rng.choice(["North", "South", "East", "West"], n, p=[0.3, 0.3, 0.15, 0.25])
    contract = rng.choice(["Monthly", "Annual", "Two-year"], n, p=[0.55, 0.3, 0.15])
    tenure = rng.integers(1, 72, n)
    monthly = rng.normal(650, 180, n).clip(199, 1499).round(0)
    complaints = rng.poisson(1.0, n)
    support_calls = rng.poisson(2 + complaints)
    recency = rng.exponential(40, n).round().astype(int) + 1
    frequency = rng.poisson(8, n) + 1
    spend = (frequency * monthly * rng.uniform(0.8, 1.3, n)).round(0)
    logit = (-1.3 + 0.55 * complaints - 0.035 * tenure + 0.0012 * (monthly - 650)
             + np.where(contract == "Monthly", 1.0, np.where(contract == "Annual", -0.3, -1.2))
             + 0.01 * recency + rng.normal(0, 0.5, n))
    churned = (rng.uniform(size=n) < 1 / (1 + np.exp(-logit))).astype(int)
    df = pd.DataFrame({
        "customer_id": [f"C{i:05d}" for i in range(1, n + 1)], "region": region,
        "contract_type": contract, "tenure_months": tenure, "monthly_charges": monthly,
        "complaints_6m": complaints, "support_calls_6m": support_calls,
        "recency_days": recency, "frequency_12m": frequency, "spend_12m": spend, "churned": churned,
    })
    df.to_csv(OUT / "customers.csv", index=False)
    return df


def aht_experiment():
    """A/B test: did a new call script reduce handle time? Plus team and complaint data."""
    old = rng.normal(335, 60, 120)
    new = rng.normal(318, 60, 120)
    teams = np.repeat(["Team A", "Team B", "Team C", "Team D"], 60)
    team_aht = rng.normal(320, 55, 240) + np.select(
        [teams == "Team B", teams == "Team D"], [25, -15], 0)
    df = pd.DataFrame({
        "agent_call_id": range(1, 241),
        "script": ["Old"] * 120 + ["New"] * 120,
        "aht_sec": np.concatenate([old, new]).round(1),
        "team": teams,
        "team_aht_sec": team_aht.round(1),
        "region": rng.choice(["North", "South", "East", "West"], 240),
    })
    # complaint type depends a little on region (for chi-square)
    probs = {"North": [0.5, 0.3, 0.2], "South": [0.35, 0.45, 0.2],
             "East": [0.4, 0.3, 0.3], "West": [0.45, 0.35, 0.2]}
    df["complaint_type"] = [rng.choice(["Billing", "Network", "Other"], p=probs[r]) for r in df.region]
    df.to_csv(OUT / "aht_experiment.csv", index=False)
    return df


def reviews(n=600):
    """Short customer reviews with sentiment labels, built from phrase templates."""
    pos = ["quick resolution", "friendly agent", "solved my problem", "very helpful", "fast response",
           "great service", "polite and patient", "clear explanation", "easy refund", "excellent support"]
    neg = ["long wait time", "rude agent", "problem not solved", "call dropped", "wrong bill",
           "no callback", "transferred many times", "slow internet", "hidden charges", "terrible service"]
    neutral = ["called about my plan", "asked about recharge", "updated my address", "checked my balance"]
    topics = {"billing": ["bill", "charges", "refund", "payment"], "network": ["internet", "signal", "network", "speed"],
              "service": ["agent", "call", "wait", "support"]}
    rows = []
    for i in range(n):
        label = rng.choice(["positive", "negative"], p=[0.45, 0.55])
        topic = rng.choice(list(topics))
        words = list(rng.choice(pos if label == "positive" else neg, 2, replace=False))
        words.append(rng.choice(neutral))
        words.append(f"about {rng.choice(topics[topic])}")
        rng.shuffle(words)
        rows.append({"review_id": i + 1, "text": ", ".join(words).capitalize() + ".",
                     "topic": topic, "sentiment": label})
    df = pd.DataFrame(rows)
    df.to_csv(OUT / "reviews.csv", index=False)
    return df


if __name__ == "__main__":
    for fn in [call_centre_intervals, daily_calls, customers, aht_experiment, reviews]:
        d = fn()
        print(f"{fn.__name__:<22} {len(d):>6} rows")
    print(f"Saved to {OUT}")
