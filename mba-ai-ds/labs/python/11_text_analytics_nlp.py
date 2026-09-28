# %% [markdown]
# # Lab 11 · Text analytics: what are customers saying? (Module M25)
# 🧒 Turn words into numbers (TF-IDF: rare words shout louder), then learn which words mean happy or angry.
# Note: the reviews are generated from templates, so the model scores unrealistically high.
# Real reviews are messier, and that's exactly what to try next on a Kaggle dataset.

# %% Setup
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from _paths import DATA

df = pd.read_csv(DATA / "reviews.csv")
print(df.sample(5, random_state=1).to_string(index=False))
print(df.sentiment.value_counts())

# %% 1. Words → numbers
vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2, stop_words="english")
X = vec.fit_transform(df.text)
print(f"{X.shape[0]} reviews × {X.shape[1]} word/phrase features")

# %% 2. Train a sentiment model
X_train, X_test, y_train, y_test = train_test_split(X, df.sentiment, test_size=0.25,
                                                    random_state=42, stratify=df.sentiment)
clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
print(classification_report(y_test, clf.predict(X_test), digits=3))

# %% 3. Which words push towards negative / positive?
coef = pd.Series(clf.coef_[0], index=vec.get_feature_names_out()).sort_values()
print("Most NEGATIVE words:", list(coef.head(8).index))
print("Most POSITIVE words:", list(coef.tail(8).index))

# %% 4. Business view: complaints by topic
summary = pd.crosstab(df.topic, df.sentiment, normalize="index").round(2)
print(summary)
worst_topic = summary["negative"].idxmax()
print(f"👉 '{worst_topic}' has the highest share of negative reviews. Start root-cause analysis there.")

# %% 5. Score brand-new reviews
new = ["agent was rude and my bill is wrong", "quick resolution, very helpful agent"]
print(dict(zip(new, clf.predict(vec.transform(new)))))

# %% Your turn
# a) Write 3 reviews of your own and score them. Where does the model fail?
# b) Stretch (M25): paste the 20 most negative reviews into an LLM and ask for 3 themes + 1 action each.
#    (Only ever do this with synthetic/public data, never company data.)
