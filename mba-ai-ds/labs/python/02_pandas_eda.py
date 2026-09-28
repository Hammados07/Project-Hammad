# %% [markdown]
# # Lab 02 · pandas & Exploratory Data Analysis (Modules M6, M16)
# 🧒 pandas = Excel inside Python. A DataFrame is a sheet; a column is a Series.
# Dataset: 8 weeks of 30-minute interval data for two queues (synthetic).

# %% Setup
import matplotlib.pyplot as plt
import pandas as pd

from _paths import DATA, OUTPUT

df = pd.read_csv(DATA / "call_centre_intervals.csv", parse_dates=["date"])

# %% 1. LOOK at the data (Shape, Holes, Spread, Pairs, Groups)
print(df.shape)                 # rows, columns
print(df.head())                # first 5 rows
print(df.dtypes)                # column types
print(df.isna().sum())          # missing values per column ("holes")
print(df.describe().round(1))   # spread of every numeric column

# %% 2. FILTER rows (like Excel filter)
bad = df[(df.sla_pct < 70) & (df.queue == "Billing")]
print(f"{len(bad)} Billing intervals below 70% SLA")
print(bad.head())

# %% 3. NEW columns (feature engineering)
df["hour"] = df.interval_start.str[:2].astype(int)
df["abandon_pct"] = (100 * df.abandoned / df.calls_offered).round(1)
df["workload_erlangs"] = df.calls_offered * df.aht_sec / 1800        # 1800 s in a 30-min interval
df["occupancy_pct"] = (100 * df.workload_erlangs / df.agents_staffed).clip(upper=100).round(1)

# %% 4. GROUP and summarise (like a PivotTable)
by_day = (df.groupby(["queue", "day_of_week"])
            .agg(calls=("calls_offered", "sum"),
                 answered_20s=("answered_within_20s", "sum"),
                 avg_aht=("aht_sec", "mean"))
            .assign(sla_pct=lambda t: (100 * t.answered_20s / t.calls).round(1)))
print(by_day)

# Pivot: SLA by hour × queue (a mini heatmap table)
pivot = df.pivot_table(index="hour", columns="queue", values="sla_pct", aggfunc="mean").round(1)
print(pivot)

# %% 5. RELATIONSHIPS: does higher occupancy mean lower SLA?
print(df[["calls_offered", "aht_sec", "agents_staffed", "occupancy_pct", "sla_pct", "abandon_pct"]].corr().round(2))

# %% 6. CHARTS (one question per chart)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
daily = df.groupby(["date", "queue"]).calls_offered.sum().unstack()
daily.plot(ax=axes[0], title="Calls per day (trend)")
pivot.plot(ax=axes[1], marker="o", title="Average SLA % by hour")
axes[1].axhline(80, color="red", linestyle="--", label="Target 80%")
axes[1].legend()
df.plot.scatter(x="occupancy_pct", y="sla_pct", alpha=0.2, ax=axes[2], title="Occupancy vs SLA")
plt.tight_layout()
plt.savefig(OUTPUT / "lab02_eda.png", dpi=120)
plt.show()

# %% 7. The "so what?" (always finish EDA with findings + actions)
worst = pivot.stack().nsmallest(3)
print("Worst hour/queue combinations for SLA:\n", worst)
occ_by_hour = df.groupby("hour").occupancy_pct.mean()
print(f"\n👉 Finding: SLA is lowest around {worst.index[0][0]}:00, where average occupancy is "
      f"{occ_by_hour[worst.index[0][0]]:.0f}% (vs {occ_by_hour.mean():.0f}% overall). Busy agents = long queues."
      "\n👉 Action: move breaks away from those intervals, or add a split shift to cover the peak.")

# %% Your turn
# a) Which day of the week has the highest abandon %?
# b) Make a histogram of aht_sec for each queue (df.hist or plt.hist).
# c) Save `by_day` to Excel: by_day.to_excel(OUTPUT / "by_day.xlsx")  (needs: pip install openpyxl)
