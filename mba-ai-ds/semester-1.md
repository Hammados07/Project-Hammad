# 🟢 Semester 1: How Business Works + Speaking the Language of Data
**Weeks 1–12 · Modules M1–M7**

> 🧒 **Semester in one line:** First we learn **what a business is and how it keeps score**, then we learn **how to count, describe and store data** so we can talk about it.

*(Resources: "NPTEL" = free IIT/IISc lecture videos at nptel.ac.in / onlinecourses.nptel.ac.in. Search the course title there. Courses run in cycles, but the recorded videos are always free on the NPTEL site and YouTube.)*

---

## M1 · How a Business Works (Principles of Management) · *Week 1*

### 🧒 Like I'm 5
A business is a **lemonade stand that grew up**. You buy lemons and sugar (**costs**), make lemonade (**operations**), tell people about it (**marketing**), sell cups (**revenue**), pay your little brother to help (**HR**), and keep what's left (**profit**). A **manager** is the person who makes sure all of these work together without the stand falling over.

### 🎯 Key concepts
1. **The 4 functions of management:** **P**lanning, **O**rganising, **L**eading, **C**ontrolling (**POLC**).
2. **Departments = the organs of a company:** Marketing (brings customers), Operations (makes/delivers), Finance (manages money), HR (manages people), IT/Data (manages information), Strategy (decides where to go).
3. **Business model:** who the customer is, what they get (value proposition), how the company earns (revenue model), and what it costs to deliver.
4. **Stakeholders:** everyone who cares about the company: customers, employees, shareholders, suppliers, government, society.
5. **Types of organisations:** sole proprietor, partnership, private/public limited company (Pvt Ltd / Ltd), LLP.
6. **Organisation structure:** functional, divisional, matrix. *(Your call centre: agents → team leader → operations manager → site head is a functional hierarchy.)*
7. **Efficiency vs effectiveness:** doing things *right* vs doing the *right things*.

### 🧠 Remember it
**"POLC is the manager's clock":** **P**lan in the morning, **O**rganise the team, **L**ead through the day, **C**ontrol (check results) in the evening.

### 📐 Pattern: the Business Model Canvas (9 boxes)
Customer Segments · Value Proposition · Channels · Customer Relationships · Revenue Streams · Key Resources · Key Activities · Key Partners · Cost Structure.

### 📺 Free resources
- **NPTEL:** *Principles of Management*
- **IIMBx (IIM Bangalore) on SWAYAM/edX:** browse the management courses
- Search "Business Model Canvas explained" on YouTube (Strategyzer's own short videos)

### 🛠️ Build it
Fill a Business Model Canvas for **3 companies**: your employer's *type* of business (BPO/contact centre, no confidential details), Zomato, and a local kirana store. One page each.

### 🎥 Teach it
**"MBA in 10 minutes: How every business actually works (lemonade stand to Zomato)"**

### ✅ Self-test
1. What does POLC stand for? Give a call-centre example of each.
2. What's the difference between efficiency and effectiveness?
3. Draw the Business Model Canvas for YouTube (who pays? who uses it for free?).

---

## M2 · Financial Accounting: Reading the Scorecard · *Weeks 2–3*

### 🧒 Like I'm 5
Accounting is a business's **report card**. Three pages tell the whole story:
- **Income Statement (P&L)** = *"Did I make money this year?"* (like your monthly salary minus expenses)
- **Balance Sheet** = *"What do I own and what do I owe, right now?"* (like listing your phone, savings and your loan)
- **Cash Flow Statement** = *"Where did the actual cash come from and go?"* (your bank passbook)

### 🎯 Key concepts
1. **The accounting equation:** `Assets = Liabilities + Equity` (what you own = what you borrowed + what's truly yours). It **always** balances.
2. **Revenue − Expenses = Profit.** Profit ≠ cash! You can be profitable and still run out of cash (customers haven't paid yet).
3. **Double-entry:** every transaction touches two accounts (buy a laptop with cash: laptop ↑, cash ↓).
4. **Accrual vs cash accounting:** record revenue when *earned*, not when cash arrives.
5. **Depreciation:** spreading the cost of a long-life asset (a laptop) over its useful years.
6. **Key P&L lines:** Revenue → Gross Profit → EBITDA → EBIT → PBT → PAT (net profit).
7. **Key ratios:**
   - *Profitability:* gross margin, net margin, ROE (return on equity), ROCE
   - *Liquidity:* current ratio = current assets / current liabilities
   - *Leverage:* debt-to-equity
   - *Efficiency:* inventory turnover, receivable days
8. **Management/cost accounting:** fixed vs variable cost, contribution margin, **break-even point**.

### 🧠 Remember it
**"P&L is a movie, Balance Sheet is a photo, Cash Flow is the bank passbook."**
Profit waterfall: **"Really Good Employees Earn Promotions And Trophies"** → Revenue, Gross profit, EBITDA, EBIT, PBT, After-tax profit.

### 📐 Formula
```
Break-even units = Fixed costs ÷ (Price per unit − Variable cost per unit)
Net margin       = Net profit ÷ Revenue
ROE              = Net profit ÷ Shareholders' equity
```

### 📺 Free resources
- **NPTEL:** *Financial Accounting* (IIT Bombay) and *Management Accounting* (IIT Roorkee)
- **IIMBx:** *Accounting and Finance* (IIM Bangalore, edX/SWAYAM)
- **Zerodha Varsity** (free, Indian examples): module *"Fundamental Analysis"*, the chapters on reading P&L, balance sheet and cash flow
- Khan Academy: *Accounting and financial statements*

### 🛠️ Build it
1. Download the **annual report** of one listed Indian company you understand (e.g. an IT/BPO services company). Find: revenue, net profit, total assets, total debt, cash from operations.
2. Calculate net margin, ROE, current ratio and debt-to-equity in Excel.
3. Run `labs/python/12_finance_npv_irr.py` (ratio section).

### 🎥 Teach it
**"Read ANY company's financial statements in 12 minutes (with a real Indian example)"**

### ✅ Self-test
1. A company has profit but no cash. How is that possible?
2. Write the accounting equation and explain it with your own finances.
3. Fixed cost ₹50,000, price ₹200, variable cost ₹120. Break-even units? *(Answer: 625)*

---

## M3 · Managerial Economics: Micro & Macro · *Week 4*

### 🧒 Like I'm 5
**Micro** = one shop's decisions: *"If I raise my samosa price from ₹15 to ₹20, will I sell fewer? Will I earn more?"*
**Macro** = the whole country's weather: inflation, interest rates, GDP, jobs. It affects every shop at once.

### 🎯 Key concepts
**Micro**
1. **Demand & supply:** price goes up → people want less, sellers want to sell more. Where they meet = market price.
2. **Price elasticity:** how *sensitive* buyers are to price. Petrol = inelastic (you buy anyway). Pizza brand = elastic (you switch).
3. **Opportunity cost:** the value of the next-best thing you gave up. (Studying 1 hour = giving up 1 hour of Netflix or freelancing.)
4. **Marginal thinking:** decide based on the *next* unit (should we hire *one more* agent?).
5. **Market structures:** perfect competition → monopolistic competition → oligopoly (telecom) → monopoly.
6. **Economies of scale:** bigger = cheaper per unit (up to a point).
7. **Sunk cost:** money already spent and gone. Ignore it in decisions.

**Macro**
8. **GDP, inflation (CPI), unemployment**: the country's vital signs.
9. **Monetary policy (RBI):** repo rate ↑ → loans costlier → spending ↓ → inflation ↓.
10. **Fiscal policy (Government):** taxes and spending (the Union Budget).
11. **Exchange rate:** a weaker rupee helps exporters (like Indian IT/BPO firms billing in dollars).

### 🧠 Remember it
**"Elastic = elastic band stretches (buyers react a lot); Inelastic = brick (buyers barely react)."**
**"RBI turns the tap":** repo up = tap tighter = less money flowing.

### 📐 Formula
```
Price elasticity = % change in quantity demanded ÷ % change in price
|E| > 1 → elastic (price cut increases revenue)
|E| < 1 → inelastic (price rise increases revenue)
```

### 📺 Free resources
- **NPTEL:** *Managerial Economics*
- **Khan Academy:** *Microeconomics* and *Macroeconomics*
- **Marginal Revolution University** (mru.org): short, clear videos
- **RBI Monetary Policy statements** (read one summary) + **Finshots** daily newsletter (free, simple Indian business news)

### 🛠️ Build it
In Excel: a demand table (price ₹10→₹30, quantity falling). Add a revenue column. Find the revenue-maximising price. Chart it.

### 🎥 Teach it
**"Why your EMI goes up when RBI raises the repo rate: economics like you're 5"**

### ✅ Self-test
1. Is salt demand elastic or inelastic? Why?
2. What is opportunity cost? Give one from your life this week.
3. Why do Indian IT/BPO companies like a weaker rupee?

---

## M4 · Business Statistics I: Describing Data & Probability · *Weeks 5–6*

### 🧒 Like I'm 5
Statistics is **how to talk about a big pile of numbers without reading every single one**. If 1,000 calls came in today, you don't list them all. You say: *"On average calls took 5 minutes, most were between 3 and 7 minutes, and a few crazy ones took 30."*
**Probability** is how likely something is: *"There's a 70% chance the next call is about billing."*

### 🎯 Key concepts
1. **Types of data:** numerical (continuous: AHT; discrete: calls) vs categorical (nominal: city; ordinal: rating 1–5).
2. **Centre:** mean (average), median (middle value), mode (most common). *Use median when there are outliers (salaries!).*
3. **Spread:** range, variance, **standard deviation** (average distance from the mean), IQR (middle 50%).
4. **Shape:** normal (bell curve), skewed (long tail, like call durations), outliers.
5. **Probability basics:** P(event) between 0 and 1; addition rule, multiplication rule, **conditional probability** P(A|B).
6. **Bayes' theorem:** updating beliefs with new evidence (spam filters, medical tests).
7. **Distributions:** Binomial (yes/no events), **Poisson** (arrivals per interval, i.e. calls per 30 min!), Normal, Exponential (time between calls).
8. **Central Limit Theorem:** averages of many samples look like a bell curve, even when the data doesn't. This is why statistics works at all.
9. **Z-score:** how many standard deviations away from the mean a value is.

### 🧠 Remember it
**"Mean is moody, median is calm"**: one outlier drags the mean but not the median.
**The 68–95–99.7 rule:** in a bell curve, 68% of values fall within 1 SD, 95% within 2, 99.7% within 3.
**"Poisson = phone calls"**: counts of random arrivals in a time window.

### 📐 Formula
```
Mean               x̄ = Σx / n
Standard deviation s = √[ Σ(x − x̄)² / (n − 1) ]
Z-score            z = (x − x̄) / s
Bayes              P(A|B) = P(B|A) × P(A) / P(B)
```

### 📺 Free resources
- **Khan Academy:** *Statistics and Probability* (units 1–7)
- **StatQuest with Josh Starmer** (YouTube): the clearest stats explainer videos anywhere
- **OpenIntro Statistics** (free PDF textbook at openintro.org)
- **NPTEL:** *Data Analytics with Python* (IIT Roorkee), weeks 1–3

### 🛠️ Build it
Run `labs/python/03_statistics_hypothesis.py`, **Part A** (descriptive stats + Poisson on call arrivals). Then do the same in Excel with `AVERAGE`, `MEDIAN`, `STDEV.S`, `POISSON.DIST`.

### 🎥 Teach it
**"Mean vs Median: why your company's 'average salary' is lying to you"**
**"The Poisson distribution explains your call centre queue"** ← a niche only you can make

### ✅ Self-test
1. Salaries: 20k, 22k, 25k, 27k, 3 lakh. Mean or median, and why?
2. What does a standard deviation of 0 mean?
3. On average 12 calls arrive per 30 min. Which distribution models this?

---

## M5 · Excel for Business Decisions · *Week 7*
*(The "Managerial Computing" course at IIMs.)*

### 🧒 Like I'm 5
Excel is a **giant magic notebook** where each box can do maths by looking at other boxes. Change one number and everything updates, like dominoes.

### 🎯 Key concepts
1. **Cell references:** relative (A1), absolute ($A$1), mixed ($A1).
2. **Lookup:** `XLOOKUP` (modern), `INDEX + MATCH` (classic).
3. **Logic:** `IF`, `IFS`, `AND`, `OR`, `IFERROR`.
4. **Summaries:** `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`.
5. **Dynamic arrays:** `FILTER`, `UNIQUE`, `SORT`, `SEQUENCE`, `LET`.
6. **PivotTables + slicers:** summarise 100,000 rows in 10 seconds.
7. **Power Query:** clean and combine data automatically (record the steps once, refresh forever).
8. **What-if analysis:** Goal Seek, Data Tables, Scenario Manager.
9. **Solver:** optimisation (you'll use it again in M20).

### 🧠 Remember it
**"Look up, Add up, Sum up, Clean up"** = XLOOKUP, SUMIFS, Pivot, Power Query. Master these four and you're ahead of 80% of Excel users.

### 📐 Pattern
```
=XLOOKUP(what_to_find, where_to_look, what_to_return, "Not found")
=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)
```

### 📺 Free resources
- **ExcelJet** (exceljet.net): short, precise function guides
- **Chandoo.org** and **Leila Gharani** (YouTube): dashboards & Power Query
- **Microsoft Learn / Support**: Power Query tutorials

### 🛠️ Build it
Open `labs/data/call_centre_intervals.csv` in Excel. Build: (1) a pivot of calls and SLA % by day, (2) a lookup of team leader by agent, (3) a Goal Seek for *"how many agents to hit 80% SLA?"* (compare with Lab 08 later).

### 🎥 Teach it
**"5 Excel formulas every analyst must know (real call-centre data)"**

### ✅ Self-test
1. What's the difference between `$A$1` and `A1` when you copy a formula?
2. Which tool would you use to clean 12 monthly files automatically?
3. When would you use Goal Seek?

---

## M6 · Python from Zero · *Weeks 8–10*

### 🧒 Like I'm 5
Python is **giving instructions to a very obedient but very literal robot**. It does exactly what you say, nothing more. If you say "add 2 and 2" it says 4. If you misspell a word it gets confused and complains (an **error**). Errors aren't failures, just the robot saying *"I didn't understand"*.

### 🎯 Key concepts
1. **Variables:** labelled boxes that hold values (`calls = 120`).
2. **Data types:** int, float, string (text), boolean (True/False).
3. **Collections:** **list** `[ ]` (ordered shelf), **dictionary** `{key: value}` (phone book), tuple, set.
4. **Conditions:** `if / elif / else`: decisions.
5. **Loops:** `for` (repeat for each item), `while` (repeat until).
6. **Functions:** `def`: a reusable recipe. Input → steps → output.
7. **Libraries:** ready-made toolkits: **pandas** (tables), **numpy** (maths), **matplotlib** (charts), **scikit-learn** (ML).
8. **pandas DataFrame:** an Excel sheet inside Python: `read_csv`, `head`, `describe`, filtering, `groupby`, `merge`.
9. **Reading errors:** read the **last line** of the error first. It says what went wrong.

### 🧠 Remember it
**"Boxes, Shelves, Phone books, Decisions, Repeats, Recipes"** = variables, lists, dicts, if, loops, functions. That's all of programming basics.

### 📐 Pattern (you'll write this 1,000 times)
```python
import pandas as pd
df = pd.read_csv("data.csv")                 # load
df.head()                                    # look
df.describe()                                # summarise
df[df["sla_pct"] < 80]                       # filter
df.groupby("day")["calls"].sum()             # group
```

### 📺 Free resources
- **NPTEL:** *Python for Data Science* (IIT Madras, Prof. Ragunathan Rengasamy), a short 4-week course
- **Harvard CS50P** (*CS50's Introduction to Programming with Python*, free at cs50.harvard.edu/python)
- **Kaggle Learn:** *Python* and *Pandas* micro-courses (free, in-browser, with exercises)
- **Python Data Science Handbook** by Jake VanderPlas (free online)

### 🛠️ Build it
1. `labs/python/01_python_basics.py`: run every cell and change every number.
2. `labs/python/02_pandas_eda.py`: the same analysis you did in Excel, now in Python.
3. **Challenge:** write a function `sla_status(sla)` that returns "Green" (≥80), "Amber" (70–79) or "Red" (<70).

### 🎥 Teach it
**"Python for Excel users: do your daily report in 10 lines"**

### ✅ Self-test
1. What's the difference between a list and a dictionary?
2. Write a loop that prints the numbers 1 to 5.
3. How do you get the total calls per day in pandas?

---

## M7 · SQL & Databases · *Weeks 11–12*
*(Maps to "Database Management" at ISI in the PGDBA.)*

### 🧒 Like I'm 5
A database is a **super-organised library**. Each **table** is a shelf of one kind of book (customers, orders). Each row is one book; each column is a detail (title, author). **SQL** is how you **ask the librarian** for exactly what you want: *"Give me all orders from Mumbai last month, biggest first."*

### 🎯 Key concepts
1. **Tables, rows, columns; primary key** (unique ID) and **foreign key** (a link to another table).
2. **Relational design & normalisation:** don't repeat data. Split it into linked tables (1NF → 3NF).
3. **The query order you write:** `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT`
4. **The order SQL actually runs:** `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`
5. **JOINs:** INNER (only matches), LEFT (everything from left + matches), FULL, SELF.
6. **Aggregates:** COUNT, SUM, AVG, MIN, MAX.
7. **Subqueries & CTEs** (`WITH ...`): break big questions into small steps.
8. **Window functions:** `ROW_NUMBER`, `RANK`, `LAG/LEAD`, running totals. Rank without losing rows.
9. **CASE WHEN:** if-else inside SQL.
10. **OLTP vs OLAP:** transaction databases vs analysis warehouses (you did OLAP in Task 4!).

### 🧠 Remember it
Execution order: **"Friendly Wizards Give Helpful Spells Only Lately"** → FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT.
**WHERE filters rows, HAVING filters groups.**

### 📐 Pattern
```sql
WITH daily AS (
  SELECT call_date, SUM(calls) AS calls
  FROM intervals
  GROUP BY call_date
)
SELECT call_date, calls,
       calls - LAG(calls) OVER (ORDER BY call_date) AS change_vs_yesterday
FROM daily;
```

### 📺 Free resources
- **SQLBolt** (sqlbolt.com): interactive lessons, perfect for a refresh
- **Kaggle Learn:** *Intro to SQL* and *Advanced SQL*
- **Mode SQL Tutorial** (mode.com/sql-tutorial)
- **NPTEL:** *Database Management System* (IIT Kharagpur) for theory depth
- **Your own repo:** Tasks 1–5!

### 🛠️ Build it
`labs/sql/01_sql_business_patterns.sql`: the 12 patterns every analyst uses (top-N, running total, month-over-month, cohort, de-duplication…).

### 🎥 Teach it
**"SQL window functions explained with a call-centre example"**

### ✅ Self-test
1. What's the difference between WHERE and HAVING?
2. LEFT JOIN customers to orders: what happens to customers with no orders?
3. Write a query for the top 3 agents by calls handled each day (hint: `ROW_NUMBER() OVER (PARTITION BY ...)`).

---

## 🎓 Semester 1 Exam (Week 12, Sunday)
Without notes, on paper, 60 minutes:
1. Draw the three financial statements and how they connect.
2. Explain elasticity with a real Indian product.
3. Explain mean, median and standard deviation to a 12-year-old.
4. Write a pandas groupby and an SQL GROUP BY that answer the same question.
5. Fill a Business Model Canvas for a company of your choice.

Score yourself: any question you struggled with → redo that module's Anki cards next week.
