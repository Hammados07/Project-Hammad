# %% [markdown]
# # Lab 04 · Regression: linear & logistic (Module M13)
# 🧒 Linear = the best straight line through the dots. Logistic = that line in an S-shaped costume (yes/no).

# %% Setup
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split

from _paths import DATA

calls = pd.read_csv(DATA / "call_centre_intervals.csv")
cust = pd.read_csv(DATA / "customers.csv")

# %% PART 1: Linear regression: what drives SLA?
calls["workload_per_agent"] = calls.calls_offered * calls.aht_sec / 1800 / calls.agents_staffed
model = smf.ols("sla_pct ~ workload_per_agent + C(queue) + C(day_of_week)", data=calls).fit()
print(model.summary().tables[1])       # the coefficient table
print(f"R² = {model.rsquared:.2f}  → the model explains {model.rsquared:.0%} of SLA variation")

# %% How to READ it
coef = model.params["workload_per_agent"]
print(f"👉 Each +0.1 in workload per agent changes SLA by about {coef * 0.1:.1f} points, holding queue & day constant.")
print("👉 p-value < 0.05 in the P>|t| column = this variable really matters.")

# %% Check the LINE assumptions quickly
resid = model.resid
print(f"Residual mean ≈ {resid.mean():.2f} (should be ~0); residual std = {resid.std():.1f}")
# Plot: plt.scatter(model.fittedvalues, resid) → look for a shapeless cloud (good)

# %% PART 2: Logistic regression: who will churn?
train, test = train_test_split(cust, test_size=0.25, random_state=42, stratify=cust.churned)
logit = smf.logit("churned ~ tenure_months + complaints_6m + monthly_charges + C(contract_type)",
                  data=train).fit(disp=False)
print(logit.summary().tables[1])

# Odds ratios: how the odds of churning multiply for +1 unit
print("Odds ratios:\n", np.exp(logit.params).round(3))
print("👉 e.g. each extra complaint multiplies the odds of churning by "
      f"{np.exp(logit.params['complaints_6m']):.2f}")

# %% Evaluate on UNSEEN data
prob = logit.predict(test)
pred = (prob >= 0.5).astype(int)
tn, fp, fn, tp = confusion_matrix(test.churned, pred).ravel()
print(f"Confusion matrix → TP {tp}, FP {fp}, FN {fn}, TN {tn}")
print(f"Accuracy {(tp + tn) / len(test):.2f} | Precision {tp / (tp + fp):.2f} | "
      f"Recall {tp / (tp + fn):.2f} | ROC-AUC {roc_auc_score(test.churned, prob):.2f}")

# %% Your turn
# a) Add support_calls_6m to the logistic model. Does it help (p-value, AUC)?
# b) Lower the threshold to 0.35. What happens to recall and precision? Why might a business want that?
# c) Predict SLA for workload_per_agent = 0.9 in Billing on Monday: model.predict(pd.DataFrame({...}))
