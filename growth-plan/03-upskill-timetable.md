# 📚 Upskill Timetable (24 weeks)

**Goal:** Go from Real-Time Analyst → **WFM Analyst / MIS Analyst / Data Analyst**, with skills that also make the content and freelancing work better.

**Time:** 3 deep-work sessions (Mon, Tue, Thu mornings, 60 min) + 2 project sessions (Wed, Fri) per week ≈ **5 hrs/week**.

**Every session follows the same pattern:** 20 min learn → 30 min practise → 10 min write notes (notes become video scripts and book chapters).

---

## Phase 1: Core Analyst Stack (Weeks 1–12)

### Block A: Advanced Excel (Weeks 1–3)
| Week | Mon (Learn) | Tue (Practise) | Thu (Apply) |
|---|---|---|---|
| 1 | Power Query: import, clean, merge | Clean a messy interval report | Automate a daily report refresh |
| 2 | XLOOKUP, FILTER, UNIQUE, SORT, LET | Rewrite old VLOOKUP sheets | Build a dynamic agent lookup sheet |
| 3 | PivotTables, slicers, charts | Build an interval SLA pivot | One-page Excel dashboard |

✅ **Checkpoint:** A refreshable Excel dashboard using synthetic data.

### Block B: SQL, intermediate to advanced (Weeks 4–6)
*(Basics already covered in Tasks 1–4 of this repo.)*
| Week | Mon | Tue | Thu |
|---|---|---|---|
| 4 | JOIN types, subqueries, CTEs | 15 practice problems (e.g. HackerRank / LeetCode SQL) | Rewrite a Task 1–3 query with CTEs |
| 5 | Window functions: ROW_NUMBER, RANK, LAG/LEAD, running totals | 15 practice problems | Interval-over-interval change in call volume |
| 6 | Date/time functions, CASE, aggregations for KPIs | SLA %, AHT, occupancy, abandon-rate queries | Finish **Task 6** |

✅ **Checkpoint:** Task 6 contact-centre database with a KPI query pack.

### Block C: Power BI (Weeks 7–9)
| Week | Mon | Tue | Thu |
|---|---|---|---|
| 7 | Power Query in Power BI, star schema, relationships | Model Task 6 data | Date table + relationships |
| 8 | DAX: CALCULATE, filters, time intelligence | Write 10 KPI measures | Drill-through & tooltips |
| 9 | Dashboard design (layout, colour, storytelling) | Rebuild one page 2 ways | Publish **Task 7** screenshots |

✅ **Checkpoint:** Power BI real-time ops dashboard in the portfolio.

### Block D: Python for Analysts (Weeks 10–12)
| Week | Mon | Tue | Thu |
|---|---|---|---|
| 10 | Python basics: variables, loops, functions (Jupyter/VS Code) | 20 small exercises | Erlang C formula in Python |
| 11 | pandas: read, clean, groupby, merge | Analyse Task 6 CSV exports | Finish **Task 8** |
| 12 | matplotlib/seaborn charts | Recreate Excel dashboard charts in Python | Revision + portfolio cleanup |

✅ **Checkpoint:** Erlang C staffing calculator (Task 8).

---

## Phase 2: Specialise in WFM & Analytics (Weeks 13–24)

| Weeks | Topic | Resources (free first) | Output |
|---|---|---|---|
| 13–14 | **Statistics for analysts:** mean/median, std dev, distributions, correlation | Khan Academy statistics, StatQuest (YouTube) | Notes → 2 videos |
| 15–17 | **Forecasting:** moving averages, seasonality, Holt-Winters, intro to Prophet/ARIMA | *Forecasting: Principles and Practice* (free online book), statsmodels docs | **Task 9:** call-volume forecast |
| 18–19 | **PL-300 exam prep** (Power BI Data Analyst) | Microsoft Learn (free learning path) + practice tests | Take the exam (check current fee) |
| 20–21 | **Automation:** Python scheduling, reading Excel/CSV, email/Teams alerts | Automate the Boring Stuff (free online) | **Task 10:** real-time adherence alert script |
| 22–23 | **Content analytics:** YouTube/IG exported CSVs | My own channel data | **Task 11:** creator analytics dashboard |
| 24 | **Job-readiness:** resume, LinkedIn, mock interviews | Portfolio = this repo | Apply to 10 roles / ask for promotion |

---

## Optional add-ons (after week 24, pick one)
- **Advanced WFM:** capacity planning, shrinkage modelling, scheduling optimisation (NICE / Verint / Genesys concepts). Consider a recognised WFM certification.
- **Cloud data:** Azure Data Fundamentals (DP-900) or Google BigQuery basics.
- **AI tools for analysts:** use LLMs to write/explain SQL, summarise reports, automate commentary (also great content topics).

## Tracking progress
Log every session in the Task 5 tracker (`time_log` table, category `Upskill`). The Sunday review query shows hours per week, so I can see whether I'm on track.
