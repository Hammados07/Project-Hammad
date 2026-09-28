# 🟠 Semester 4: Advanced AI + Thinking Like a Leader
**Weeks 37–48 · Modules M23–M28**

> 🧒 **Semester in one line:** We learn the **most powerful AI tools** (advanced ML, deep learning, GenAI), then step back and learn **how leaders decide what to build, whether it's ethical, and how it makes the company win**.

---

## M23 · Advanced / Applied Machine Learning (AML) · *Weeks 37–38*

### 🧒 Like I'm 5
In Semester 3 you learned to ride a bicycle. Now you learn to **race**: how to make the model **as accurate as possible**, **explain why** it made a decision, and **keep it working** after you ship it (models "go stale" like bread).

### 🎯 Key concepts
1. **Ensembles:** bagging (random forest: many independent trees), **boosting** (XGBoost, LightGBM, CatBoost: trees fixing each other's mistakes), stacking (a model of models). Boosting usually wins on business tables (tabular data).
2. **Hyperparameter tuning:** the "knobs" (tree depth, learning rate). Grid search, random search, Bayesian search (Optuna) *with cross-validation*.
3. **Regularisation:** L1 (Lasso: removes useless features), L2 (Ridge: shrinks them). Prevents overfitting.
4. **Feature selection & engineering at scale.**
5. **Imbalanced data:** class weights, SMOTE, choosing the **threshold** based on business cost.
6. **Cost-sensitive decisions:** a missed fraud costs ₹50,000; a false alarm costs ₹200 → pick the threshold that minimises *money lost*, not errors.
7. **Explainability (XAI):** feature importance, **permutation importance**, **SHAP values** (how much each feature pushed this one prediction up or down), partial dependence plots.
8. **MLOps:** versioning data + code + model, pipelines, deployment (API), **monitoring for drift** (the world changes, so the model's accuracy decays), retraining.
9. **Model cards & documentation.**

### 🧠 Remember it
**"Bagging = many students answer independently and vote. Boosting = students take turns, each fixing the last one's mistakes."**
**SHAP = "who scored the goals": how much each feature contributed to the final prediction.**
**"Models are milk, not wine"**: they get worse with age unless monitored.

### 📐 Pattern
```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.inspection import permutation_importance
search = RandomizedSearchCV(HistGradientBoostingClassifier(), param_distributions={
    "learning_rate": [0.03, 0.1, 0.3], "max_depth": [3, 5, None]}, n_iter=6, cv=5, scoring="roc_auc")
search.fit(X_train, y_train)
imp = permutation_importance(search.best_estimator_, X_test, y_test, scoring="roc_auc")
```

### 📺 Free resources
- **Kaggle Learn:** *Intermediate Machine Learning* (XGBoost), *Machine Learning Explainability* (permutation importance, SHAP)
- **StatQuest:** *Gradient Boost*, *XGBoost*, *Regularization* series
- **Made With ML** (madewithml.com): free MLOps course
- **Google's "Rules of Machine Learning"** (free guide)

### 🛠️ Build it
Extend `labs/python/05_ml_churn_classification.py`, Part B: tune gradient boosting, compare it to random forest, **choose the threshold by business cost**, and explain the top drivers with permutation importance.

### 🎥 Teach it
**"Why accuracy is the wrong metric: choosing a model by ₹, not %"**

### ✅ Self-test
1. Bagging vs boosting, in one sentence each?
2. What is model drift and how would you detect it?
3. Why would a bank insist on explainable models?

---

## M24 · Deep Learning: Neural Networks · *Weeks 39–40*

### 🧒 Like I'm 5
A neural network is a **huge team of tiny decision-makers (neurons) arranged in rows**. The first row looks at simple things (edges in a photo), the next row combines them (eyes, ears), the last row decides ("it's a cat!"). At first they guess randomly. Each time they're wrong, a teacher tells every neuron **"turn your knob a tiny bit this way"**. After millions of corrections, the team gets very good.
The "turn your knob" process is **backpropagation + gradient descent**.

### 🎯 Key concepts
1. **Neuron:** inputs × weights + bias → **activation function** (ReLU, sigmoid) → output.
2. **Layers:** input → hidden layers → output. "Deep" = many hidden layers.
3. **Loss function:** how wrong the guess is (MSE for numbers, cross-entropy for classes).
4. **Gradient descent:** walk downhill on the error surface. **Learning rate** = step size.
5. **Backpropagation:** the chain rule, passing blame backwards through the layers.
6. **Epochs, batches, overfitting**; fixes: dropout, early stopping, more data.
7. **Architectures:**
   - **CNN** (convolutional): images, looks at small patches
   - **RNN / LSTM**: sequences (older approach for text and time series)
   - **Transformers**: attention, "which words should I focus on?". The basis of ChatGPT/Claude
8. **Transfer learning:** reuse a model trained on huge data and fine-tune it for your problem.
9. **When NOT to use deep learning:** small tabular business data → gradient boosting usually wins and is easier to explain.

### 🧠 Remember it
**"Guess → measure error → blame backwards → adjust knobs → repeat."** That's all training is.
**Gradient descent = walking down a foggy mountain by always stepping downhill.**

### 📐 Formula
```
neuron output = activation( w₁x₁ + w₂x₂ + … + b )
weight update: w_new = w_old − learning_rate × (∂Loss / ∂w)
```

### 📺 Free resources
- **3Blue1Brown:** *Neural Networks* series on YouTube (the most beautiful visual explanation)
- **NPTEL:** *Deep Learning* (IIT Kharagpur) and IIT Madras deep learning courses
- **fast.ai:** *Practical Deep Learning for Coders* (free, top-down, build first)
- **Andrej Karpathy:** *Neural Networks: Zero to Hero* (YouTube). Builds a network from scratch

### 🛠️ Build it
`labs/python/10_neural_network_from_scratch.py`: a tiny neural network written with numpy only, learning a simple pattern. Watch the loss go down epoch by epoch.

### 🎥 Teach it
**"How a neural network learns, explained like you're 5 (with code from scratch)"**

### ✅ Self-test
1. What does an activation function do?
2. What happens if the learning rate is too big? Too small?
3. For 5,000 rows of customer data, deep learning or gradient boosting? Why?

---

## M25 · NLP, Generative AI & Large Language Models · *Weeks 41–42*

### 🧒 Like I'm 5
**NLP** teaches computers to **read**. First we taught them to count words ("*terrible* appears a lot → angry review"). Now **LLMs** (like ChatGPT, Claude, Gemini) have read a huge part of the internet and learned to **predict the next word so well that they can write, summarise, translate and reason**.
**Generative AI** = AI that **makes new things** (text, images, code) instead of just labelling.

### 🎯 Key concepts
1. **Text preprocessing:** tokenisation, lower-casing, stop-words, stemming/lemmatisation.
2. **Bag-of-words & TF-IDF:** turning text into numbers by counting (TF-IDF gives rarer, more meaningful words more weight).
3. **Classic NLP tasks:** sentiment analysis, topic modelling, named-entity recognition, text classification (auto-tagging tickets!).
4. **Embeddings:** words/sentences as points in space, where similar meanings sit close together.
5. **Transformers & attention:** the architecture behind modern LLMs.
6. **How LLMs are made:** pre-training (predict next token) → fine-tuning → human feedback alignment.
7. **Prompt engineering:** role, context, clear task, examples (few-shot), output format, "think step by step".
8. **RAG (Retrieval-Augmented Generation):** give the LLM **your documents** to answer from, which reduces made-up answers (hallucinations).
9. **Agents & tool use:** LLMs that can call tools (search, calculators, databases).
10. **Limits & risks:** hallucination, bias, privacy (never paste confidential company data into public tools), cost, evaluation.

### 🧠 Remember it
**"TF-IDF = rare words shout louder."**
**"RAG = open-book exam for the AI."**
**Good prompt = "Role, Context, Task, Format, Example" (RCTFE).**

### 📐 Pattern
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
X = TfidfVectorizer(ngram_range=(1, 2), min_df=2).fit_transform(reviews)
clf = LogisticRegression(max_iter=1000).fit(X, labels)   # sentiment model
```

### 📺 Free resources
- **Hugging Face LLM Course** (free, hands-on transformers)
- **DeepLearning.AI short courses** (free, 1–2 hrs each: prompt engineering, RAG, agents)
- **Anthropic's prompt engineering interactive tutorial** (free on GitHub) + Anthropic Academy courses
- **3Blue1Brown:** *"But what is a GPT?"* and the attention videos
- **NPTEL:** search *Natural Language Processing* (IIT courses)

### 🛠️ Build it
`labs/python/11_text_analytics_nlp.py`: TF-IDF + logistic regression sentiment model on synthetic customer reviews, plus the top words for each topic. **Stretch:** use an LLM to summarise the 20 most negative reviews into 3 themes.

### 🎥 Teach it
**"How ChatGPT/Claude actually work, explained like you're 5"**
**"5 ways an analyst can use AI at work tomorrow (safely)"**

### ✅ Self-test
1. What does TF-IDF do better than simple word counts?
2. What is RAG and what problem does it solve?
3. Why shouldn't you paste company data into a public chatbot?

---

## M26 · Business Strategy & Digital Transformation · *Week 43*

### 🧒 Like I'm 5
Strategy is **deciding which game to play and how to win it**, and just as importantly, **which games NOT to play**. A lemonade stand next to 10 other stands must decide: be the cheapest? The tastiest? The only one with mango lemonade?

### 🎯 Key concepts
1. **Strategy = choices + trade-offs** (Michael Porter: *"The essence of strategy is choosing what not to do."*).
2. **Analysis tools:**
   - **SWOT**: Strengths, Weaknesses (internal); Opportunities, Threats (external)
   - **PESTEL**: Political, Economic, Social, Technological, Environmental, Legal (the outside world)
   - **Porter's Five Forces**: rivalry, threat of new entrants, threat of substitutes, buyer power, supplier power
   - **Value chain**: where in the chain the company adds value
3. **Generic strategies:** cost leadership, differentiation, focus (niche).
4. **Competitive advantage & moats:** brand, network effects, switching costs, scale, patents, data.
5. **Growth: Ansoff matrix:** market penetration, product development, market development, diversification.
6. **Portfolio: BCG matrix:** stars, cash cows, question marks, dogs.
7. **Blue Ocean strategy:** create uncontested market space instead of fighting in a "red ocean".
8. **Digital transformation & platforms:** network effects (more users → more value), data as a moat, platform business models (Uber, UPI, YouTube).
9. **Business-level vs corporate-level strategy; mergers & acquisitions basics.**

### 🧠 Remember it
**Five Forces = "Rivals, Rookies, Replacements, Buyers, Bosses-of-supply".**
**Ansoff: "Same/New product × Same/New market."**
**Moat = the crocodile-filled ditch around your castle.**

### 📺 Free resources
- **NPTEL:** search *Strategic Management*
- **IIMBx:** *Strategic Management* (IIM Bangalore, SWAYAM)
- **YouTube:** *"The Five Competitive Forces That Shape Strategy"* (Harvard Business Review, with Michael Porter)
- **Business case podcasts:** *Acquired* (deep company histories), *Finshots* (Indian business, daily)

### 🛠️ Build it
Pick one Indian company (e.g. Jio, Zomato, Asian Paints). Do a 1-page **SWOT + Five Forces + moat** analysis. Recommend one strategic move and support it with at least one number.

### 🎥 Teach it
**"Why Jio won: Porter's Five Forces explained with Indian telecom"**

### ✅ Self-test
1. List Porter's five forces.
2. What are "network effects"? Give an Indian example.
3. Cost leadership vs differentiation: give one company for each.

---

## M27 · AI Strategy, Ethics, Governance & Product Management · *Week 44*

### 🧒 Like I'm 5
Having a **super-smart robot** is great, but you must decide **what jobs to give it**, **check it's being fair**, **protect people's secrets**, and **make sure people actually use it**. Many AI projects fail not because the maths is wrong but because they **solved the wrong problem** or **nobody trusted them**.

### 🎯 Key concepts
1. **Where AI creates value:** automation (do cheaper), augmentation (help humans decide), new products.
2. **Choosing AI use-cases:** impact × feasibility matrix; data availability; cost of errors.
3. **Build vs buy vs partner** (use an API, fine-tune, or build from scratch).
4. **AI product management:** problem discovery, user research, MVP, success metrics (business + model metrics), iteration.
5. **AI ethics:** fairness/bias (a model trained on biased history repeats the bias), transparency, accountability, human-in-the-loop.
6. **Privacy & regulation:** India's **Digital Personal Data Protection (DPDP) Act, 2023**; the EU AI Act (risk-based rules); consent, purpose limitation, data minimisation.
7. **Responsible AI frameworks:** NITI Aayog's Responsible AI principles; company AI governance boards; model cards.
8. **ROI of AI:** costs (data, people, compute, maintenance) vs benefits; start small, prove value, scale.
9. **Change management for AI:** training, trust, redesigning jobs rather than just replacing them.

### 🧠 Remember it
**"Start with the pain, not the algorithm."**
**FATE = Fairness, Accountability, Transparency, Ethics.**

### 📺 Free resources
- **Elements of AI** (University of Helsinki, free, non-technical)
- **"AI For Everyone"** by Andrew Ng (DeepLearning.AI / Coursera)
- **NITI Aayog:** *Responsible AI for All* papers (free PDFs)
- **MeitY / official text of the DPDP Act, 2023**: read the summary

### 🛠️ Build it
Write a **1-page AI use-case proposal** for a contact centre (e.g. auto-summarising calls, predicting call spikes, flagging adherence issues): problem, users, data, model type, success metric, risks, ethics check, ₹ ROI estimate.

### 🎥 Teach it
**"How to pick the RIGHT AI project at work (most companies get this wrong)"**

### ✅ Self-test
1. Give 2 reasons AI projects fail that have nothing to do with the model.
2. What does "human-in-the-loop" mean?
3. Name 2 principles of India's DPDP Act.

---

## M28 · Capstone: Consulting Toolkit + End-to-End Project · *Weeks 45–48*

### 🧒 Like I'm 5
This is your **final big LEGO build**, where you use **every piece you've collected** to build one complete thing and **show it to everyone**.

### 🎯 Part A: The consultant's thinking toolkit (Week 45)
1. **MECE:** Mutually Exclusive, Collectively Exhaustive. Break problems into pieces that don't overlap and don't miss anything.
2. **Issue tree / logic tree:** big question → sub-questions → testable hypotheses.
3. **Hypothesis-driven approach:** guess the answer early, then test it with data.
4. **Pyramid principle (Barbara Minto):** **answer first**, then the supporting points, then the data.
5. **Profit tree:** Profit = (Price × Volume) − (Fixed + Variable costs). Every profitability case starts here.
6. **Market sizing (guesstimates):** "How many cups of chai are sold in Mumbai daily?" Population → segments → usage → total.
7. **The 1-page executive summary & the "so what?" test.**

### 🧠 Remember it
**"Answer first, then reasons, then proof."**
**MECE = "no overlaps, no gaps".**

### 📺 Free resources
- **Victor Cheng's free case interview videos** (caseinterview.com)
- **YouTube:** search "Pyramid Principle explained", "MECE issue tree"
- Business school consulting-club casebooks (many IIM/ISB casebooks are shared free online)

### 🛠️ Part B: The Capstone Project (Weeks 46–48)
Build **one end-to-end project** that combines business + data + AI. Recommended (fits your career):

> **"Contact Centre Command Centre"**: forecast volumes (M19) → Erlang C staffing (M10) → optimal shift plan (M20) → Power BI real-time dashboard (M15) → churn/complaint text analysis (M25) → business case with ₹ impact (M9, M26) → AI ethics check (M27).

**Deliverables (this becomes your portfolio centrepiece):**
1. `capstone/` folder in this repo with code, data (synthetic) and README
2. A 10-slide executive deck using the pyramid principle
3. A 15–20 minute **YouTube "final project" video**
4. A LinkedIn post + a book chapter

### 🎥 Teach it
**"I rebuilt my entire MBA in 48 weeks: here's my final project"**

### ✅ Final exam (Week 48)
1. Draw an issue tree for "Why did our SLA drop 10% this month?"
2. Estimate the number of call-centre agents in India (show your logic).
3. Present your capstone in 5 minutes, answer first.

---

## 🎉 Graduation checklist
- [ ] 28 one-page summaries
- [ ] 12+ labs run and modified
- [ ] Capstone in the repo
- [ ] 28+ YouTube episodes
- [ ] 300+ Anki cards reviewed
- [ ] Updated resume + LinkedIn with projects and skills
