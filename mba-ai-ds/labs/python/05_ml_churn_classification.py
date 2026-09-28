# %% [markdown]
# # Lab 05 · Machine Learning: predict customer churn (Modules M17, M23)
# 🧒 Show the computer 1,500 customers with the answer (left / stayed), then ask it about 500 new ones.

# %% Setup
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import RandomizedSearchCV, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

from _paths import DATA

df = pd.read_csv(DATA / "customers.csv")
target = "churned"
numeric = ["tenure_months", "monthly_charges", "complaints_6m", "support_calls_6m",
           "recency_days", "frequency_12m", "spend_12m"]
categorical = ["region", "contract_type"]
X, y = df[numeric + categorical], df[target]
print(f"Churn rate: {y.mean():.1%}  ← if we always guessed 'stays', accuracy would be {1 - y.mean():.1%}")

# %% 1. Split (never test on data the model has seen)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# %% 2. Preprocessing pipeline (scale numbers, one-hot categories) → no leakage
prep = ColumnTransformer([("num", StandardScaler(), numeric),
                          ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)])

models = {
    "Logistic regression": LogisticRegression(max_iter=1000),
    "Decision tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random forest": RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=42),
    "Gradient boosting": HistGradientBoostingClassifier(random_state=42),
}

# %% 3. Compare models with 5-fold cross-validation (fair test)
for name, m in models.items():
    pipe = Pipeline([("prep", prep), ("model", m)])
    auc = cross_val_score(pipe, X_train, y_train, cv=5, scoring="roc_auc")
    print(f"{name:<20} ROC-AUC {auc.mean():.3f} ± {auc.std():.3f}")

# %% 4. Fit a model and test ONCE on the hold-out set
# Logistic regression scores about as well as the fancy models here, and it's the easiest to explain,
# so we pick it (simplest model that's good enough wins).
best = Pipeline([("prep", prep), ("model", models["Logistic regression"])]).fit(X_train, y_train)
prob = best.predict_proba(X_test)[:, 1]
print(classification_report(y_test, prob >= 0.5, digits=3))
print("Test ROC-AUC:", round(roc_auc_score(y_test, prob), 3))

# %% PART B (M23): tune gradient boosting
search = RandomizedSearchCV(
    Pipeline([("prep", prep), ("model", HistGradientBoostingClassifier(random_state=42))]),
    param_distributions={"model__learning_rate": [0.03, 0.05, 0.1],
                         "model__max_depth": [2, 3, 4, None],
                         "model__max_iter": [100, 200, 300]},
    n_iter=8, cv=5, scoring="roc_auc", random_state=42)
search.fit(X_train, y_train)
print("Best params:", search.best_params_, "CV AUC:", round(search.best_score_, 3))

# %% PART B: choose the threshold by MONEY, not accuracy
# Assumptions (change them!): a retention offer costs ₹500; a lost customer costs ₹4,000 of future margin;
# the offer saves 30% of the churners who receive it.
# Rule of thumb: offer it when  P(churn) × SAVE_RATE × CHURN_LOSS  >  OFFER_COST
OFFER_COST, CHURN_LOSS, SAVE_RATE = 500, 4000, 0.30
results = []
for thr in np.arange(0.1, 0.9, 0.05):
    flag = prob >= thr
    tp = int(((flag == 1) & (y_test == 1)).sum())
    cost = flag.sum() * OFFER_COST
    saved = tp * SAVE_RATE * CHURN_LOSS
    results.append((round(thr, 2), int(flag.sum()), tp, saved - cost))
res = pd.DataFrame(results, columns=["threshold", "customers_flagged", "true_churners_caught", "net_benefit_inr"])
print(res.to_string(index=False))
print("👉 Best threshold by ₹:", res.loc[res.net_benefit_inr.idxmax(), "threshold"])

# %% PART B: explain the model: what drives churn?
imp = permutation_importance(best, X_test, y_test, scoring="roc_auc", n_repeats=10, random_state=42)
print(pd.Series(imp.importances_mean, index=X_test.columns).sort_values(ascending=False).round(3))

# %% Your turn
# a) Which model won? Is the winner worth the extra complexity vs logistic regression?
# b) Change CHURN_LOSS to ₹2,000. How does the best threshold move? Explain why in one line.
# c) Write the 'boss sentence': "With this model we can ___, worth about ₹___ per month."
