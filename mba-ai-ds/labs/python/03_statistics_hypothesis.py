# %% [markdown]
# # Lab 03 · Statistics: describing data & testing ideas (Modules M4, M12)
# 🧒 Part A: describe a big pile of numbers. Part B: the "courtroom". Is a difference real or just luck?

# %% Setup
import numpy as np
import pandas as pd
from scipy import stats

from _paths import DATA

calls = pd.read_csv(DATA / "call_centre_intervals.csv")
exp = pd.read_csv(DATA / "aht_experiment.csv")

# %% PART A1: centre and spread
aht = calls.aht_sec
print(f"Mean   {aht.mean():.1f} s")
print(f"Median {aht.median():.1f} s")
print(f"Std    {aht.std():.1f} s   (typical distance from the mean)")
print(f"IQR    {aht.quantile(.75) - aht.quantile(.25):.1f} s   (spread of the middle 50%)")

# Mean vs median with an outlier (salaries)
salaries = pd.Series([20, 22, 25, 27, 300])       # in thousands
print("Salaries mean:", salaries.mean(), "median:", salaries.median(), "← median is the honest one")

# %% PART A2: z-scores (how unusual is a value?)
calls["aht_z"] = (aht - aht.mean()) / aht.std()
print("Intervals more than 2 SD above average AHT:", (calls.aht_z > 2).sum())

# %% PART A3: Poisson: calls arriving per interval
# If on average 12 calls arrive per 30 minutes, how likely is a quiet (≤ 6) or crazy (≥ 20) interval?
lam = 12
print(f"P(exactly 12) = {stats.poisson.pmf(12, lam):.3f}")
print(f"P(≤ 6)        = {stats.poisson.cdf(6, lam):.3f}")
print(f"P(≥ 20)       = {1 - stats.poisson.cdf(19, lam):.3f}")

# %% PART A4: Central Limit Theorem in 5 lines
# AHT is skewed, but averages of samples of 30 calls form a bell curve.
sample_means = [aht.sample(30, random_state=i).mean() for i in range(1000)]
print(f"Sample means: mean {np.mean(sample_means):.1f}, std {np.std(sample_means):.1f} "
      f"(≈ population std / √30 = {aht.std() / np.sqrt(30):.1f})")

# %% PART B1: Confidence interval for average AHT
new = exp.loc[exp.script == "New", "aht_sec"]
ci = stats.t.interval(0.95, df=len(new) - 1, loc=new.mean(), scale=stats.sem(new))
print(f"New-script AHT: {new.mean():.1f} s, 95% CI {ci[0]:.1f} – {ci[1]:.1f} s")

# %% PART B2: t-test: did the NEW call script reduce AHT?
# H0 (innocent): no difference.  H1: the new script changes AHT.
old = exp.loc[exp.script == "Old", "aht_sec"]
t, p = stats.ttest_ind(new, old, equal_var=False)       # Welch's t-test
print(f"Old {old.mean():.1f}s vs New {new.mean():.1f}s → t = {t:.2f}, p = {p:.4f}")
print("Verdict:", "Reject H0: the difference is real" if p < 0.05 else "Can't reject H0: could be luck")
print(f"Practical check: saving {old.mean() - new.mean():.0f} s per call × 10,000 calls/month "
      f"= {(old.mean() - new.mean()) * 10000 / 3600:.0f} agent-hours/month")

# %% PART B3: ANOVA: do 4 teams have different AHT?
groups = [g.team_aht_sec.values for _, g in exp.groupby("team")]
f, p = stats.f_oneway(*groups)
print(exp.groupby("team").team_aht_sec.mean().round(1))
print(f"ANOVA F = {f:.2f}, p = {p:.4f} → {'at least one team differs' if p < 0.05 else 'no evidence of difference'}")

# %% PART B4: Chi-square: is complaint type related to region?
table = pd.crosstab(exp.region, exp.complaint_type)
chi2, p, dof, expected = stats.chi2_contingency(table)
print(table)
print(f"Chi-square = {chi2:.2f}, p = {p:.4f} → {'related' if p < 0.05 else 'no evidence of a relationship'}")

# %% PART B5: Correlation ≠ causation
r, p = stats.pearsonr(calls.calls_offered, calls.abandoned)
print(f"Correlation calls vs abandoned: r = {r:.2f} (p = {p:.3g}). Related, but WHY? (understaffing is the cause)")

# %% Your turn
# a) Is Billing AHT different from Tech Support AHT? (t-test on calls.aht_sec by queue)
# b) Change the Poisson λ to 20. How does P(≥ 20) change?
# c) Explain p-value from B2 in one sentence to a 12-year-old.
