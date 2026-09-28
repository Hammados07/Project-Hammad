# 🟣 Semester 3: Teaching Computers to Find Patterns
**Weeks 25–36 · Modules M16–M22**

> 🧒 **Semester in one line:** Instead of *us* finding patterns in data, we teach the **computer** to find them, then use those patterns to **predict, group, forecast and optimise** real business decisions.
> *(This is the "IIT Kharagpur semester" of the PGDBA model: machine learning, time series, algorithms, operations modelling, big data.)*

---

## M16 · Data Wrangling & Exploratory Data Analysis (EDA) · *Week 25*

### 🧒 Like I'm 5
Real data is like a **messy room**: toys everywhere, some broken, some in the wrong box. **Wrangling** is tidying the room. **EDA** is walking around the tidy room and noticing things: *"Hmm, most of the broken toys are from the same shelf…"* Data scientists spend **most of their time here**, not building fancy models.

### 🎯 Key concepts
1. **Tidy data:** each column = one variable, each row = one observation, each table = one kind of thing.
2. **Missing values:** drop, fill (mean/median/mode), or flag. *Ask WHY it's missing first.*
3. **Duplicates, wrong types** (dates stored as text), **inconsistent labels** ("Mumbai", "mumbai", "Bombay").
4. **Outliers:** detect with IQR rule or z-score; investigate before deleting (they may be the story!).
5. **Feature engineering:** creating useful columns (day-of-week from date, "calls per agent", tenure buckets).
6. **Reshaping:** wide ↔ long (`melt`, `pivot`), merging/joining tables.
7. **EDA checklist:** shape, types, missing, distributions (histograms), relationships (scatter, correlation heatmap), segments (groupby).
8. **Data leakage:** accidentally giving the model information from the future. The #1 silent ML killer.

### 🧠 Remember it
**"Garbage in, garbage out."**
**EDA = "Shape, Holes, Spread, Pairs, Groups"** → size, missing values, distributions, relationships, segments.

### 📐 Pattern
```python
df.shape; df.info(); df.isna().sum()
df.drop_duplicates(inplace=True)
df["date"] = pd.to_datetime(df["date"])
df["city"] = df["city"].str.strip().str.title()
q1, q3 = df.aht.quantile([.25, .75]); iqr = q3 - q1
outliers = df[(df.aht < q1 - 1.5*iqr) | (df.aht > q3 + 1.5*iqr)]
```

### 📺 Free resources
- **Kaggle Learn:** *Pandas*, *Data Cleaning*, *Data Visualization*, *Feature Engineering*
- **Python Data Science Handbook** (Jake VanderPlas, free online), chapter on pandas
- **R4DS (2e)**: "Data tidying" and "Transform" chapters

### 🛠️ Build it
`labs/python/02_pandas_eda.py`, the full EDA section. Then pick **any Kaggle dataset** you find interesting (e.g. a retail or telecom dataset) and write a 1-page "5 things I found" summary.

### 🎥 Teach it
**"80% of data science is cleaning. Here's how (real messy dataset)"**

### ✅ Self-test
1. Give 3 ways to handle missing values and when you'd use each.
2. What is data leakage? Give an example.
3. What's the IQR rule for outliers?

---

## M17 · Machine Learning I: Supervised Learning (Predicting) · *Weeks 26–28*
*(Maps to "Foundations of Machine Learning" at IIT Kharagpur and "ML Techniques" at IIT Madras.)*

### 🧒 Like I'm 5
You show a child **100 photos of fruit with labels** ("apple", "banana"). Then you show a **new photo without a label**, and the child guesses. That's supervised learning: **learn from labelled examples, then predict new ones.**
- Predicting a **number** (tomorrow's calls) = **regression**
- Predicting a **category** (will churn: yes/no) = **classification**

### 🎯 Key concepts
1. **Features (X)** = the clues; **target (y)** = the answer.
2. **Train / validation / test split** and **cross-validation** (k-fold): test fairly.
3. **Bias vs variance:** **underfitting** (too simple, misses the pattern) vs **overfitting** (memorises the training data, fails on new data).
4. **Algorithms (know the intuition for each):**
   - **Linear / logistic regression**: a line or S-curve
   - **k-Nearest Neighbours**: "you are like your closest neighbours"
   - **Decision tree**: a flowchart of yes/no questions
   - **Random forest**: many trees vote (wisdom of the crowd)
   - **Gradient boosting (XGBoost/LightGBM)**: trees that learn from previous trees' mistakes
   - **Support Vector Machine**: the widest possible street between classes
   - **Naive Bayes**: probability-based, great for text
5. **Classification metrics:** confusion matrix, accuracy, **precision** (of those I flagged, how many were right?), **recall** (of all real cases, how many did I catch?), F1, ROC-AUC.
6. **Regression metrics:** MAE, RMSE, MAPE, R².
7. **Class imbalance:** when 95% don't churn, "always predict no" is 95% accurate and useless. Use recall/F1, resampling, class weights.
8. **Scaling & encoding:** standardise numbers; one-hot encode categories.
9. **Pipelines:** bundle preprocessing + model so nothing leaks.

### 🧠 Remember it
**"Underfit = lazy student, Overfit = student who memorised the answer key."**
**Precision = "When I shout FIRE, am I right?" Recall = "Did I catch every fire?"**
**Random forest = a panchayat of trees voting.**

### 📐 Pattern (the scikit-learn recipe, the same 5 lines for every model)
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = RandomForestClassifier(random_state=42).fit(X_train, y_train)
print(model.score(X_test, y_test))
```

### 📺 Free resources
- **NPTEL:** *Introduction to Machine Learning* (IIT Madras, Prof. Balaraman Ravindran). Rigorous, with a free YouTube playlist
- **ISLP** (statlearning.com), chapters 2, 4, 5, 8. Free book + free lecture videos by the authors
- **StatQuest:** *Machine Learning* playlist (decision trees, random forest, gradient boost, ROC-AUC)
- **Google Machine Learning Crash Course** (free)
- **Kaggle Learn:** *Intro to Machine Learning*, *Intermediate Machine Learning*

### 🛠️ Build it
`labs/python/05_ml_churn_classification.py`: predict customer churn with logistic regression, decision tree and random forest; compare with a confusion matrix, precision, recall and ROC-AUC; show feature importance.

### 🎥 Teach it
**"Machine learning explained like you're 5 (then we predict customer churn)"**
**"Precision vs Recall: the fire alarm analogy"**

### ✅ Self-test
1. Is predicting next week's call volume regression or classification?
2. Your model: 99% train accuracy, 70% test accuracy. What's happening?
3. For detecting fraud, is recall or precision more important? Why?

---

## M18 · Machine Learning II: Unsupervised Learning (Grouping) · *Weeks 29–30*

### 🧒 Like I'm 5
You dump a box of **mixed buttons** on the table **with no labels** and ask a child to sort them. They make piles: big red ones, small blue ones… Nobody told them the groups; they **discovered** them. That's unsupervised learning. Businesses use it to find **customer segments** nobody knew existed.

### 🎯 Key concepts
1. **Clustering:** grouping similar items.
   - **K-Means**: pick k centres, assign points to the nearest, move centres, repeat
   - **Hierarchical**: a family tree of clusters (dendrogram)
   - **DBSCAN**: groups by density, finds odd shapes and outliers
2. **Choosing k:** elbow method, silhouette score, and **business sense** (can marketing actually act on 12 segments? Probably not).
3. **Scaling matters:** without it, ₹ amounts dominate "number of visits".
4. **RFM segmentation:** **R**ecency, **F**requency, **M**onetary. The classic marketing analytics technique.
5. **Dimensionality reduction:** **PCA** squeezes many columns into a few "super-columns" that keep most of the information.
6. **Association rules / market-basket analysis:** "people who buy bread also buy butter". Support, confidence, **lift**.
7. **Anomaly detection:** finding the weird ones (fraud, broken sensors, unusual call spikes).

### 🧠 Remember it
**"K-Means = k magnets pulling iron filings, then moving to the middle of their pile."**
**RFM = "How recently? How often? How much?"**
**Lift > 1 = the items like each other.**

### 📐 Pattern
```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
X = StandardScaler().fit_transform(df[["recency", "frequency", "monetary"]])
df["segment"] = KMeans(n_clusters=4, n_init=10, random_state=42).fit_predict(X)
df.groupby("segment")[["recency", "frequency", "monetary"]].mean()
```

### 📺 Free resources
- **StatQuest:** *K-means*, *Hierarchical clustering*, *PCA step-by-step*
- **ISLP**, chapter 12 (unsupervised learning)
- **NPTEL:** *Business Analytics & Data Mining Modeling Using R* (IIT Roorkee): clustering and association rules sections

### 🛠️ Build it
`labs/python/06_clustering_segmentation.py`: RFM + K-Means on synthetic customers, then **name each segment** ("Champions", "At risk", "New", "Sleeping") and suggest one marketing action per segment.

### 🎥 Teach it
**"How Amazon groups its customers: RFM + K-Means explained simply"**

### ✅ Self-test
1. Why must you scale data before K-Means?
2. What does PCA do, in one sentence?
3. Bread → butter has lift 2.5. What does it mean?

---

## M19 · Time Series & Forecasting · *Weeks 31–32*

### 🧒 Like I'm 5
Forecasting is **guessing tomorrow's weather by looking at the pattern of the past days**. Calls go up every Monday morning, dip at lunch, spike after a bill is sent. If you learn the rhythm, you can guess the future and **staff the right number of agents**. This is literally the heart of WFM.

### 🎯 Key concepts
1. **Components:** **Trend** (long-term up/down) + **Seasonality** (repeating pattern: daily, weekly, yearly) + **Noise** (random).
2. **Decomposition:** splitting a series into those parts.
3. **Baseline methods (always start here):** naive (tomorrow = today), seasonal naive (next Monday = last Monday), moving average.
4. **Exponential smoothing:** recent data matters more. **Holt-Winters** handles trend + seasonality.
5. **ARIMA / SARIMA:** uses the series' own past values and past errors. **Stationarity** (stable mean/variance) and differencing.
6. **Regression with time features / ML:** day-of-week, holiday flags, marketing events as features.
7. **Accuracy:** **MAPE** (average % error), MAE, RMSE; always compare against the naive baseline.
8. **Backtesting:** train on the past, test on the most recent weeks. **Never shuffle time series!**
9. **Intraday forecasting & distribution:** daily volume × interval profile = interval forecast (your job!).

### 🧠 Remember it
**"TSN" = Trend, Seasonality, Noise.**
**"If you can't beat naive, go home."**

### 📐 Formula
```
MAPE = (100 / n) × Σ |actual − forecast| / |actual|
Simple exponential smoothing: F(t+1) = α × Actual(t) + (1 − α) × F(t)
```

### 📺 Free resources
- **Forecasting: Principles and Practice (3rd ed.)** by Hyndman & Athanasopoulos: **free online** (otexts.com/fpp3), in R. The best forecasting book there is. A Python edition, *FPP: the Pythonic Way*, is also free on the same site.
- **NPTEL:** search *Time Series Analysis* / *Business Forecasting*
- **statsmodels docs:** Holt-Winters (`ExponentialSmoothing`) examples

### 🛠️ Build it
`labs/python/07_time_series_forecast.py`: forecast daily call volume with naive, seasonal naive, moving average and Holt-Winters; compare MAPE; plot it. **This is Project Task 9.**

### 🎥 Teach it
**"How call centres predict tomorrow's calls (forecasting explained simply)"**

### ✅ Self-test
1. Name the 3 components of a time series.
2. Why can't you randomly shuffle data for time series testing?
3. Your model has MAPE 12%; seasonal naive has 10%. What do you conclude?

---

## M20 · Optimisation & Operations Research · *Week 33*
*(Maps to "Modeling in Operations Management" at IIT Kharagpur.)*

### 🧒 Like I'm 5
You have **₹100 and want the most chocolate**. Big bars cost more but have more chocolate; the shop allows only 5 bars per kind. What's the best combination? Optimisation is **finding the best answer when you have limits** (money, time, people).

### 🎯 Key concepts
1. **The 3 parts of every optimisation problem:** **decision variables** (what you choose), **objective** (what you maximise/minimise), **constraints** (the limits).
2. **Linear Programming (LP):** everything is a straight-line relationship. Solved with the simplex method.
3. **Integer Programming:** decisions must be whole numbers (you can't hire 3.7 agents).
4. **Shadow price:** how much the objective improves if you relax a constraint by 1 unit (what one more hour of agent time is worth).
5. **Classic problems:** product mix, **staff scheduling / shift planning**, transportation, assignment, knapsack.
6. **Tools:** Excel **Solver**, Python `scipy.optimize.linprog`, `PuLP`.
7. **Simulation (Monte Carlo):** when things are random, run thousands of "what if" worlds.
8. **Decision trees (decision analysis):** expected monetary value under uncertainty.

### 🧠 Remember it
**"Choose, Goal, Rules"** = variables, objective, constraints.

### 📐 Pattern
```python
from scipy.optimize import linprog
# minimise cost c·x subject to A_ub·x <= b_ub
res = linprog(c=costs, A_ub=A, b_ub=b, bounds=(0, None), integrality=[1]*len(costs))
```

### 📺 Free resources
- **NPTEL:** search *Operations Research* / *Introduction to Operations Research* (several IITs)
- **YouTube:** search "Excel Solver linear programming tutorial"
- **PuLP documentation**: case studies (includes scheduling examples)

### 🛠️ Build it
`labs/python/08_optimisation_staffing.py`, Part B: find the **cheapest shift plan** that meets the required agents per time block (from Erlang C in Part A). This is real WFM scheduling in miniature.

### 🎥 Teach it
**"How to build the cheapest shift roster with maths (linear programming)"**

### ✅ Self-test
1. Name the 3 parts of an optimisation problem.
2. Why do staffing problems need *integer* programming?
3. What's a shadow price, in plain words?

---

## M21 · Big Data & Cloud (Hadoop, Spark, Data Engineering) · *Weeks 34–35*

### 🧒 Like I'm 5
If you have to count **all the words in one book**, you do it yourself. If you have to count the words in **every book in India**, you give **one book to each of 10,000 kids** (**Map**), then collect everyone's counts and add them up (**Reduce**). Big data tools are the **teacher organising the 10,000 kids**.

### 🎯 Key concepts
1. **The 5 Vs:** Volume, Velocity, Variety, Veracity (trust), Value.
2. **Distributed storage:** HDFS, cloud object storage (Amazon S3, Azure Data Lake, Google Cloud Storage). Split files across many machines.
3. **MapReduce:** map (process pieces in parallel) → shuffle (group by key) → reduce (combine).
4. **Apache Spark:** a faster, in-memory successor to MapReduce. DataFrames and Spark SQL feel like pandas/SQL. **Lazy evaluation** (plans first, runs when you ask for results).
5. **Data warehouse vs data lake vs lakehouse:** structured & cleaned (Snowflake, BigQuery, Redshift) vs raw everything vs a mix of both (Databricks).
6. **ETL vs ELT:** Extract-Transform-Load vs load first, transform in the warehouse (modern).
7. **Batch vs streaming:** daily reports vs real-time events (Kafka). *Your real-time dashboards are streaming-ish!*
8. **File formats:** CSV (simple, slow), **Parquet** (columnar, compressed, fast).
9. **Cloud basics:** IaaS/PaaS/SaaS, pay-as-you-go, the big three (AWS, Azure, GCP).
10. **NoSQL:** document (MongoDB), key-value (Redis), column (Cassandra), graph (Neo4j).

### 🧠 Remember it
**"Map = split the work; Reduce = add it up."**
**Lake = raw water; Warehouse = bottled water; Lakehouse = a filter on the lake.**

### 📐 Pattern (PySpark looks like pandas + SQL)
```python
from pyspark.sql import SparkSession, functions as F
spark = SparkSession.builder.getOrCreate()
df = spark.read.csv("calls.csv", header=True, inferSchema=True)
df.groupBy("queue").agg(F.sum("calls").alias("calls")).orderBy(F.desc("calls")).show()
```

### 📺 Free resources
- **NPTEL:** *Big Data Computing* (IIT Patna, Dr. Rajiv Misra): Hadoop, MapReduce, Spark, and more
- **Databricks Free Edition**: free, browser-based Spark notebooks to practise on
- **Google Colab:** `pip install pyspark` runs Spark on a single machine for learning
- **Kaggle Learn:** *Advanced SQL* (BigQuery-style thinking)

### 🛠️ Build it
`labs/python/09_mapreduce_bigdata.py`: MapReduce word count in plain Python (to *see* the idea), plus the same thing in PySpark (run in Colab or Databricks).

### 🎥 Teach it
**"Big Data explained with 10,000 kids counting words (MapReduce & Spark)"**

### ✅ Self-test
1. What happens in the map step and in the reduce step?
2. Why is Parquet faster than CSV for analytics?
3. Data lake vs data warehouse, in one line each?

---

## M22 · Functional Analytics: Marketing, Finance, HR, Operations · *Week 36*
*(Maps to the IIM Calcutta semester of the PGDBA: analytics applied to business functions.)*

### 🧒 Like I'm 5
You've learned **how to use the tools** (hammer, saw, drill). Now you learn **what to build** in each room of the house: marketing room, money room, people room, kitchen (operations).

### 🎯 The classic analytics use-case in each function
| Function | Question | Technique (module) |
|---|---|---|
| **Marketing** | Who are our customers? | RFM + clustering (M18) |
| | Who will leave? | Churn classification (M17) |
| | What do people buy together? | Market basket / association rules (M18) |
| | Which ad channel works? | A/B testing (M12), marketing-mix regression (M13) |
| | What's a customer worth? | CLV (M8) |
| **Finance** | Will this borrower default? | Credit scoring with logistic regression (M13) |
| | Is this transaction fraud? | Anomaly detection / classification (M17–18) |
| | Is this project worth it? | NPV / IRR / Monte Carlo simulation (M9, M20) |
| | How risky is this portfolio? | Returns, volatility, correlation (M4) |
| **HR** | Who might quit? | Attrition prediction (M17) |
| | Are we paying fairly? | Regression on pay (M13) |
| | What drives engagement? | Survey analysis, correlation (M12) |
| **Operations** | How many calls tomorrow? | Forecasting (M19) |
| | How many agents do we need? | Erlang C + LP scheduling (M10, M20) |
| | Where is quality failing? | Control charts, Pareto (M10) |
| | How much stock to keep? | EOQ + safety stock (M10) |

### 🧠 Remember it
**Every analytics project = "Business question → Data → Technique → Decision → Money impact."** If you can't name the decision and the money, don't start.

### 📺 Free resources
- **NPTEL:** *Business Analytics & Data Mining Modeling Using R* (IIT Roorkee), Parts I & II
- **Kaggle datasets:** search "telco churn", "HR attrition", "credit default", "online retail". Each has public notebooks to learn from
- **IIMBx / SWAYAM:** business analytics courses

### 🛠️ Build it
Pick **one function**. Write a 1-page **analytics project charter**: business question, data needed, technique, success metric, expected ₹ impact. Then build it using one of the labs as a starting point.

### 🎥 Teach it
**"10 ways companies use data science (one for every department)"**

### ✅ Self-test
1. Which technique predicts employee attrition?
2. What's the difference between segmentation and churn prediction?
3. Write the 5-step analytics project chain.

---

## 🎓 Semester 3 Exam (Week 36, Sunday)
1. Draw the ML workflow from raw data to deployed prediction.
2. Explain overfitting with an analogy, and 2 ways to fix it.
3. Explain precision vs recall with a business example.
4. Explain K-Means and RFM to a marketing manager.
5. Explain MapReduce with a drawing.
6. Pick a department and design an analytics project (question → decision → ₹).
