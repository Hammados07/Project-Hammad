# %% [markdown]
# # Lab 06 · Customer segmentation: RFM + K-Means (Modules M18, M22)
# 🧒 Dump a box of buttons on the table with no labels and let the computer sort them into piles.

# %% Setup
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from _paths import DATA

df = pd.read_csv(DATA / "customers.csv")
rfm = df[["recency_days", "frequency_12m", "spend_12m"]]

# %% 1. Classic RFM scores (1–5 each, no ML needed)
df["R"] = pd.qcut(df.recency_days, 5, labels=[5, 4, 3, 2, 1]).astype(int)    # recent = high score
df["F"] = pd.qcut(df.frequency_12m.rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
df["M"] = pd.qcut(df.spend_12m, 5, labels=[1, 2, 3, 4, 5]).astype(int)
df["RFM_score"] = df.R.astype(str) + df.F.astype(str) + df.M.astype(str)
print(df[["customer_id", "recency_days", "frequency_12m", "spend_12m", "RFM_score"]].head())

# %% 2. Scale (so ₹ spend doesn't bully the other columns), then pick k
X = StandardScaler().fit_transform(rfm)
for k in range(2, 8):
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    print(f"k={k}  inertia={km.inertia_:8.0f}  silhouette={silhouette_score(X, km.labels_):.3f}")
# Elbow: where inertia stops dropping fast. Silhouette: higher = cleaner piles.
# Also ask: can marketing act on this many segments?

# %% 3. Fit k = 4 and describe each segment
df["segment"] = KMeans(n_clusters=4, n_init=10, random_state=42).fit_predict(X)
profile = df.groupby("segment").agg(customers=("customer_id", "count"),
                                    recency=("recency_days", "mean"),
                                    frequency=("frequency_12m", "mean"),
                                    spend=("spend_12m", "mean"),
                                    churn_rate=("churned", "mean")).round(1)
print(profile)

# %% 4. Give segments human names (the business step!)
def name(row, prof=profile):
    if row.recency > prof.recency.median() * 1.5:
        return "😴 Sleeping / at risk"
    if row.spend >= prof.spend.max() * 0.9:
        return "🏆 Champions"
    if row.frequency < prof.frequency.median():
        return "🌱 Occasional"
    return "💙 Loyal regulars"

profile["name"] = profile.apply(name, axis=1)
print(profile[["name", "customers", "recency", "frequency", "spend", "churn_rate"]])

# %% 5. PCA: squeeze 3 columns into 2 so we can draw the piles
coords = PCA(n_components=2).fit_transform(X)
df["pc1"], df["pc2"] = coords[:, 0], coords[:, 1]
# import matplotlib.pyplot as plt; plt.scatter(df.pc1, df.pc2, c=df.segment, s=5); plt.show()

# %% 6. Actions per segment (the "so what")
actions = {"🏆 Champions": "Early access, referral rewards. Don't discount!",
           "💙 Loyal regulars": "Upsell bundles, loyalty points",
           "🌱 Occasional": "Reminders, first-repeat-purchase coupon",
           "😴 Sleeping / at risk": "Win-back call or offer within 7 days"}
for seg, row in profile.iterrows():
    print(f"Segment {seg} · {row['name']:<22} → {actions.get(row['name'], 'Investigate')}")

# %% Your turn
# a) Try k = 3 and k = 5. Which is easier to explain to a marketing manager?
# b) Add tenure_months to the clustering. Do the segments change?
