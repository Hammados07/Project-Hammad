# 🔵 Semester 2: Running the Business + Proving Things With Data
**Weeks 13–24 · Modules M8–M15**

> 🧒 **Semester in one line:** Now that we know the parts of a business, we learn **how each department makes decisions**, and how to use statistics to **prove** a decision is right instead of guessing.

---

## M8 · Marketing Management · *Weeks 13–14*

### 🧒 Like I'm 5
Marketing is **finding the people who want your lemonade, making lemonade they love, and telling them where to find it**, at a price they're happy to pay. It's not just ads. Ads are one small part.

### 🎯 Key concepts
1. **STP:** **S**egmentation (split customers into groups), **T**argeting (choose which groups), **P**ositioning (what you want them to think of you, e.g. *"Volvo = safety"*).
2. **The 4 Ps (marketing mix):** **P**roduct, **P**rice, **P**lace (distribution), **P**romotion. Services add 3 more: **P**eople, **P**rocess, **P**hysical evidence (7 Ps).
3. **Customer journey / funnel:** Awareness → Consideration → Purchase → Retention → Advocacy (AIDA: Attention, Interest, Desire, Action).
4. **Customer Lifetime Value (CLV)** and **Customer Acquisition Cost (CAC)**. A healthy business has CLV well above CAC (often ~3×).
5. **Brand equity:** why people pay more for a name.
6. **Pricing strategies:** cost-plus, value-based, penetration (enter cheap), skimming (start high), psychological (₹99).
7. **Digital marketing metrics:** CTR, conversion rate, CPC, CPM, ROAS. (You'll see these in YouTube Studio too!)
8. **Consumer behaviour:** needs vs wants, decision process, influencers.
9. **Product life cycle:** Introduction → Growth → Maturity → Decline.

### 🧠 Remember it
**"STP picks WHO, 4Ps decide HOW."**
**CLV > 3 × CAC = healthy.**

### 📐 Formula
```
Simple CLV   = Avg order value × Purchases per year × Years as customer × Margin %
CAC          = Total marketing & sales spend ÷ New customers acquired
Conversion % = Buyers ÷ Visitors × 100
```

### 📺 Free resources
- **NPTEL:** *Marketing Management-I* (IIT Kanpur, Prof. Jayanta Chatterjee & Prof. Shashi Shekhar Mishra)
- **IIMBx:** *Marketing Management* (IIM Bangalore, edX/SWAYAM)
- **Google Skillshop / Digital Garage:** free digital marketing basics

### 🛠️ Build it
Pick **your own YouTube channel** as the product. Write its STP and 4Ps on one page. Then calculate a simple CLV for a freelance client.

### 🎥 Teach it
**"STP and the 4Ps explained using Zomato vs Swiggy"**

### ✅ Self-test
1. What's the difference between segmentation and targeting?
2. Name the 4 Ps and give an example of each for Maggi.
3. CAC = ₹500, customer buys ₹300/month with 40% margin for 2 years. CLV? Is it healthy? *(CLV = 300 × 12 × 2 × 0.4 = ₹2,880 ≈ 5.8× CAC → healthy)*

---

## M9 · Corporate Finance: Money Has a Time Value · *Weeks 15–16*

### 🧒 Like I'm 5
**₹100 today is better than ₹100 next year**, because today you could put it in the bank and have ₹107 next year. So when a business decides *"Should we spend ₹10 lakh today to earn ₹3 lakh a year for 5 years?"*, it has to **shrink future money back to today's value** before comparing. That shrinking is called **discounting**.

### 🎯 Key concepts
1. **Time Value of Money (TVM):** future value and present value.
2. **Discount rate / cost of capital (WACC):** the "interest rate" used to shrink future cash, reflecting risk.
3. **NPV (Net Present Value):** today's value of all future cash − investment. **NPV > 0 → do it.**
4. **IRR:** the discount rate at which NPV = 0. Compare it to the cost of capital.
5. **Payback period:** how long to get your money back (simple but ignores time value).
6. **Risk & return:** higher risk must promise higher return. **Diversification** reduces risk.
7. **CAPM:** `Expected return = Risk-free rate + β × (Market return − Risk-free rate)`.
8. **Capital structure:** debt vs equity funding. Debt is cheaper (tax benefit) but riskier.
9. **Working capital:** the cash needed to run day-to-day (inventory + receivables − payables).
10. **Valuation basics:** DCF (value = present value of future cash flows), multiples (P/E, EV/EBITDA).

### 🧠 Remember it
**"Money today is a seed. Money tomorrow is the tree minus the waiting."**
**"NPV positive? Project's a go. NPV negative? Say no."**

### 📐 Formula
```
FV  = PV × (1 + r)^n
PV  = FV ÷ (1 + r)^n
NPV = Σ [ CF_t ÷ (1 + r)^t ] − Initial investment
EMI = P × r × (1 + r)^n ÷ [ (1 + r)^n − 1 ]      (r = monthly rate)
```

### 📺 Free resources
- **NPTEL:** *Corporate Finance* (IIT Kharagpur) · *Financial Management for Managers* (IIT Roorkee)
- **Aswath Damodaran** (NYU Stern "Dean of Valuation"): full free corporate finance & valuation classes on YouTube and his website
- **Zerodha Varsity:** modules on *Fundamental Analysis* and *Personal Finance*

### 🛠️ Build it
Run `labs/python/12_finance_npv_irr.py`. Then do the same in Excel with `=NPV()`, `=IRR()`, `=PMT()`. **Real life:** calculate the EMI on a ₹5 lakh loan at 10.5% for 3 years, and the future value of your ₹5,000/month SIP at 12% for 10 years.

### 🎥 Teach it
**"NPV explained like you're 5 (and why your SIP makes you rich slowly)"**

### ✅ Self-test
1. Why is ₹100 today worth more than ₹100 in a year?
2. A project has IRR 14% and cost of capital 11%. Accept or reject?
3. What does β = 1.5 mean for a stock?

---

## M10 · Operations & Supply Chain (incl. Queues & Call Centres) · *Week 17*

### 🧒 Like I'm 5
Operations is **the kitchen of the business**: how the lemonade actually gets made and delivered, fast, cheap and without mistakes. A call centre is also a kitchen: calls come in (**orders**), agents handle them (**cooks**), and the queue is the line of hungry customers.

### 🎯 Key concepts
1. **Process thinking:** input → process → output. Find the **bottleneck** (the slowest step limits everything).
2. **Capacity & utilisation:** how much you *can* do vs how much you *are* doing.
3. **Little's Law:** `Items in system = Arrival rate × Time in system`. Works for queues, inventory, everything!
4. **Queueing theory:** arrivals (Poisson), service time, number of servers, **Erlang C** (probability a caller waits) → staffing. *This is your day job's maths!*
5. **Inventory models:** EOQ (economic order quantity), safety stock, reorder point.
6. **Lean:** remove waste (the 8 wastes: **DOWNTIME**: Defects, Overproduction, Waiting, Non-used talent, Transport, Inventory, Motion, Extra processing).
7. **Six Sigma & DMAIC:** Define, Measure, Analyse, Improve, Control.
8. **Supply chain:** supplier → manufacturer → distributor → retailer → customer. The **bullwhip effect** (small demand changes grow upstream).
9. **Quality:** control charts, Pareto (80/20), fishbone diagram.

### 🧠 Remember it
**Little's Law = "L = λW"** → "**L**ine = arrivals × **W**ait".
**DOWNTIME** for the 8 wastes.

### 📐 Formula
```
Little's Law: L = λ × W
Traffic intensity (Erlangs): A = calls per hour × AHT (hours)
Occupancy = A ÷ agents
EOQ = √(2 × annual demand × order cost ÷ holding cost per unit)
```

### 📺 Free resources
- **NPTEL:** search *Operations Management* and *Supply Chain Management* (several IIT courses)
- **YouTube:** search "Little's Law explained", "Erlang C formula explained"
- **Your job!** WFM concepts: forecasting, scheduling, shrinkage, occupancy, adherence

### 🛠️ Build it
Run `labs/python/08_optimisation_staffing.py`, Part A (Erlang C). Compare it with what your WFM tool suggests (using made-up numbers, not company data).

### 🎥 Teach it
**"The maths behind every call centre: Erlang C explained simply"** ← your signature video

### ✅ Self-test
1. 120 calls/hour, AHT 5 min. Traffic in Erlangs? *(120 × 5/60 = 10 Erlangs)*
2. What's a bottleneck and why does it matter?
3. Name 4 of the 8 wastes with office examples.

---

## M11 · Organisational Behaviour & HR · *Week 18*

### 🧒 Like I'm 5
A company is **people working together**, and people have feelings, motivations and bad days. OB is **understanding why people act the way they do at work**. HR is **finding, growing, paying and keeping the right people**.

### 🎯 Key concepts
1. **Motivation theories:** Maslow's hierarchy (needs pyramid), Herzberg's two factors (**hygiene** like salary *prevents* unhappiness; **motivators** like recognition *create* happiness), expectancy theory.
2. **Personality:** Big Five (**OCEAN**: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism).
3. **Leadership styles:** transformational, transactional, servant, situational.
4. **Team development:** Forming → Storming → Norming → Performing (Tuckman).
5. **Organisational culture:** "how things are done here".
6. **Change management:** Kotter's 8 steps; people resist change they don't understand.
7. **HR cycle:** workforce planning → recruit → onboard → train → appraise → reward → retain → exit.
8. **HR analytics:** attrition rate, time-to-hire, cost-per-hire, engagement scores, **attrition prediction** (an ML project in M22!).
9. **Negotiation & conflict:** BATNA (your best alternative if the deal fails).

### 🧠 Remember it
**OCEAN** for personality. **"Salary stops the crying; recognition starts the smiling"** (Herzberg).
**"Form, Storm, Norm, Perform"**: every new team goes through a fight phase. It's normal.

### 📺 Free resources
- **NPTEL:** search *Organizational Behaviour* and *Human Resource Management*
- **IIMBx:** HR/leadership courses on SWAYAM
- **YouTube:** Simon Sinek's *"Start With Why"* talk (leadership & motivation)

### 🛠️ Build it
Think of your own team (anonymised). Which Tuckman stage is it in? What motivates the agents: hygiene or motivator factors? Write one page on how you'd reduce attrition.

### 🎥 Teach it
**"Why good employees quit: Herzberg's theory in 8 minutes"**

### ✅ Self-test
1. What's the difference between a hygiene factor and a motivator?
2. What is BATNA and why does it matter in salary negotiation?
3. Give 3 HR metrics an analyst could track.

---

## M12 · Business Statistics II: Inference & Hypothesis Testing · *Weeks 19–20*
*(Maps to "Inference" at ISI in the PGDBA.)*

### 🧒 Like I'm 5
You can't taste every drop of soup to know if it's salty. You taste **one spoon** (a **sample**) and guess about the **whole pot** (the **population**). Inference is **how confident you can be in that guess**.
A **hypothesis test** is a **courtroom**: the new idea is "guilty" only if the evidence is strong. We start by assuming *"nothing changed"* (innocent) and only reject that if the data would be really surprising otherwise.

### 🎯 Key concepts
1. **Population vs sample; parameter vs statistic.**
2. **Sampling distribution & standard error** (`SE = s/√n`): how much a sample average wobbles.
3. **Confidence interval:** a range that likely contains the true value ("AHT is 5.2 min ± 0.3").
4. **Null (H₀) vs alternative (H₁) hypothesis.**
5. **p-value:** *if nothing had changed*, how surprising is this data? Small p (< 0.05) → reject H₀.
6. **Type I error** (false alarm) vs **Type II error** (missed it). Significance level α.
7. **Tests:**
   - **t-test:** compare 2 means (old script vs new script AHT)
   - **ANOVA:** compare 3+ means (AHT across 4 teams)
   - **Chi-square:** relationship between two categories (city vs complaint type)
   - **Correlation:** do two numbers move together? (**Correlation ≠ causation!**)
8. **A/B testing:** the business version of all of the above (website button A vs B).
9. **Statistical vs practical significance:** a 0.1-second AHT improvement can be "significant" and still useless.

### 🧠 Remember it
**"If p is low, H₀ must go."**
**Courtroom:** H₀ = innocent. p-value = how weird the evidence would be if innocent. Type I = jailing an innocent person; Type II = letting the guilty go.

### 📐 Formula
```
Standard error   SE = s ÷ √n
95% CI           x̄ ± 1.96 × SE     (large samples)
t statistic      t = (x̄₁ − x̄₂) ÷ √(s₁²/n₁ + s₂²/n₂)
```

### 📺 Free resources
- **StatQuest:** *p-values*, *hypothesis testing*, *t-tests*, *ANOVA* videos
- **NPTEL:** *Data Analytics with Python* (IIT Roorkee), weeks 4–6 (sampling, hypothesis testing, ANOVA, chi-square)
- **Khan Academy:** *Significance tests* and *Confidence intervals*
- **OpenIntro Statistics**, chapters 5–7

### 🛠️ Build it
`labs/python/03_statistics_hypothesis.py`, **Part B**: t-test (did a new call script reduce AHT?), ANOVA (teams), chi-square (region vs complaint type).

### 🎥 Teach it
**"p-values explained with a courtroom (finally makes sense)"**
**"How to A/B test anything at work"**

### ✅ Self-test
1. In plain words, what does p = 0.03 mean?
2. Which test compares average AHT across 4 teams?
3. Ice cream sales and drowning deaths are correlated. Why doesn't one cause the other?

---

## M13 · Regression: Linear & Logistic · *Weeks 21–22*
*(Maps to "Regression and Time Series Models" at IIT Kharagpur in the PGDBA.)*

### 🧒 Like I'm 5
**Linear regression** draws **the best straight line through a cloud of dots** so you can predict. *"Every extra ₹1,000 on ads brings about 12 more sales."*
**Logistic regression** predicts a **yes/no**: *"Will this customer leave? 73% chance yes."* It squeezes the line into an S-shape between 0 and 1.

### 🎯 Key concepts
1. **Dependent (y)** vs **independent (x) variables.**
2. **Simple & multiple linear regression:** `y = b₀ + b₁x₁ + b₂x₂ + … + error`
3. **Coefficients:** how much y changes when x goes up by 1, *holding others constant*.
4. **R²:** % of variation in y explained by the model (0 to 1). Adjusted R² penalises useless variables.
5. **p-values of coefficients:** is this variable really helping?
6. **Assumptions (LINE):** **L**inearity, **I**ndependence, **N**ormal residuals, **E**qual variance. Plus watch **multicollinearity** (x's that copy each other, check VIF).
7. **Dummy variables:** turning categories (city) into 0/1 columns.
8. **Logistic regression:** probability of a class; **odds ratio**; threshold (e.g. 0.5).
9. **Evaluation:** RMSE/MAE (linear); confusion matrix, accuracy, precision, recall, **ROC-AUC** (logistic).
10. **Train/test split:** always test on data the model hasn't seen.

### 🧠 Remember it
**LINE** for assumptions.
**"R² is the % of the story the model tells."**
**Logistic = "line in an S-shaped costume"**, squashed between 0 and 1.

### 📐 Pattern
```python
import statsmodels.formula.api as smf
model = smf.ols("sales ~ ad_spend + price + C(region)", data=df).fit()
print(model.summary())          # coefficients, p-values, R²

logit = smf.logit("churned ~ tenure + complaints", data=df).fit()
```

### 📺 Free resources
- **StatQuest:** *Linear Regression*, *Logistic Regression* playlists
- **ISLP**: *An Introduction to Statistical Learning with Applications in Python* (free PDF at statlearning.com), chapters 3–4. **The best ML book for business people.**
- **NPTEL:** *Data Analytics with Python* (IIT Roorkee), weeks 6–9

### 🛠️ Build it
`labs/python/04_regression.py`: predict AHT from call type & agent tenure; predict churn with logistic regression. Read every line of `summary()`.

### 🎥 Teach it
**"Regression explained like you're 5: predict anything with a straight line"**

### ✅ Self-test
1. The coefficient on ad_spend is 0.012. What does it mean in words?
2. R² = 0.65. Good or bad? Depends on what?
3. Why must you test on data the model hasn't seen?

---

## M14 · R Programming · *Week 23*

### 🧒 Like I'm 5
R is **Python's cousin who was raised by statisticians**. It's brilliant at statistics and charts. Many IIT/IIM/ISI courses (and your NPTEL R course) use it, so knowing both makes you bilingual.

### 🎯 Key concepts
1. **RStudio** layout: script, console, environment, plots.
2. **Vectors** (`c(1,2,3)`), **data frames**, **factors** (categories).
3. **The tidyverse:** `dplyr` verbs: `filter`, `select`, `mutate`, `group_by`, `summarise`, `arrange`; the pipe `|>` (or `%>%`).
4. **ggplot2:** grammar of graphics: data + aesthetics + geoms.
5. **Modelling:** `lm()` (linear), `glm(family = binomial)` (logistic), `summary()`.
6. **R Markdown / Quarto:** reports that mix text, code and charts.

### 🧠 Remember it
**dplyr verbs = English:** "take data |> *filter* rows |> *group by* team |> *summarise* average".
**ggplot = layers of a cake:** data → aesthetics → geometry → labels.

### 📐 Python ↔ R translation
| Task | Python (pandas) | R (dplyr) |
|---|---|---|
| filter | `df[df.x > 5]` | `df \|> filter(x > 5)` |
| new column | `df["y"] = df.x * 2` | `df \|> mutate(y = x * 2)` |
| group summary | `df.groupby("g").x.mean()` | `df \|> group_by(g) \|> summarise(mean(x))` |
| regression | `smf.ols("y ~ x", df).fit()` | `lm(y ~ x, data = df)` |

### 📺 Free resources
- **R for Data Science (2e)** by Hadley Wickham et al. (free online at r4ds.hadley.nz)
- **NPTEL:** *Business Analytics & Data Mining Modeling Using R* (IIT Roorkee, Dr. Gaurav Dixit)
- **Posit Cloud** (posit.cloud) to run R in the browser for free

### 🛠️ Build it
`labs/r/01_r_basics_regression.R`: repeat your Python lab 02 and 04 analysis in R. Notice how similar the answers are.

### 🎥 Teach it
**"Python vs R for business analytics: same problem, both languages"**

### ✅ Self-test
1. Rewrite `df.groupby("team").aht.mean()` in dplyr.
2. What are the three essential parts of a ggplot?
3. Which R function fits a logistic regression?

---

## M15 · Data Visualisation & Storytelling (Power BI) · *Week 24*

### 🧒 Like I'm 5
A chart is a **picture that answers one question fast**. A dashboard is a **car's dashboard**: glance at it and know if you're fine or about to run out of fuel. Storytelling is **telling the boss what to DO**, not just showing numbers.

### 🎯 Key concepts
1. **Pick the chart by the question:** compare → bar; trend → line; part-of-whole → stacked bar (avoid pies with >3 slices); relationship → scatter; distribution → histogram/box plot.
2. **Declutter:** remove gridlines, 3D, extra colours. **One highlight colour** for the key point.
3. **Pre-attentive attributes:** colour, size, position grab attention before the brain "reads".
4. **Story structure:** **Situation → Complication → Resolution** (or "What? So what? Now what?").
5. **Power BI pieces:** Power Query (clean) → Data model (star schema: fact + dimension tables) → **DAX** measures → visuals → publish.
6. **Key DAX:** `SUM`, `CALCULATE` (change the filter context), `DIVIDE`, time intelligence (`TOTALYTD`, `SAMEPERIODLASTYEAR`).
7. **KPI design:** each KPI needs a target, a trend and an owner.

### 🧠 Remember it
**"What? So what? Now what?"** for every chart and every slide.
**Star schema = sun and planets:** the fact table (numbers) in the middle, dimension tables (who/what/when/where) around it.

### 📺 Free resources
- **Microsoft Learn:** *PL-300 Power BI Data Analyst* learning path (free)
- **Guy in a Cube** (YouTube): Power BI tips
- **Storytelling with Data** (Cole Nussbaumer Knaflic): free blog + YouTube talks

### 🛠️ Build it
Build a one-page Power BI dashboard on `labs/data/call_centre_intervals.csv`: SLA trend, calls by hour heatmap, AHT by queue, with one clear "Now what?" text box. **This is Project Task 7 in `growth-plan/04-project-roadmap.md`.**

### 🎥 Teach it
**"From boring table to boss-ready dashboard in Power BI"**

### ✅ Self-test
1. Which chart for "how did SLA change over 30 days"?
2. What does `CALCULATE` do in DAX?
3. What is a star schema?

---

## 🎓 Semester 2 Exam (Week 24, Sunday)
1. Explain STP + 4Ps for a brand of your choice.
2. Calculate the NPV of: invest ₹1,00,000, get ₹30,000/yr for 5 years at 10%. *(≈ +₹13,724 → accept)*
3. Explain Little's Law and Erlang traffic with a call-centre example.
4. Explain a p-value to a 12-year-old.
5. Interpret a regression output (coefficients, p-values, R²).
6. Sketch a dashboard with 4 visuals and its "Now what?" message.
