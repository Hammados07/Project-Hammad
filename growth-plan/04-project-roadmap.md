# 🛠️ Project Roadmap for This Repository

Tasks 1–4 (SQL capstone) are done. New projects continue the numbering. Each one:
- matches a block in the upskill timetable,
- uses **synthetic data only** (never company data),
- gets its own README section + screenshots folder (same style as Tasks 1–4),
- becomes **at least one YouTube video** and **one book chapter**.

| # | Project | Skills | Upskill weeks | Status |
|---|---|---|---|---|
| **5** | **Side Hustle Tracker**: SQL database to track time, content, income & expenses for this plan | SQL (DDL, FKs, CHECK, views, aggregations) | Week 1 | ✅ Starter built: `Task5_Side_Hustle_Tracker.sql` |
| 6 | **Contact Centre Interval Database**: 15/30-min interval data for queues & agents; KPI queries (SLA %, AHT, occupancy, abandon rate, adherence) | SQL: CTEs, window functions, date/time | Weeks 4–6 | ⬜ |
| 7 | **Real-Time Ops Dashboard** in Power BI on Task 6 data: intraday SLA, queue heatmap, agent state, drill-through | Power BI, DAX, data modelling | Weeks 7–9 | ⬜ |
| 8 | **Erlang C Staffing Calculator**: required agents for a target SLA, in Python (and an Excel version) | Python, maths, Excel | Weeks 10–11 | ⬜ |
| 9 | **Call Volume Forecasting**: weekly/intraday forecast with seasonality; compare accuracy (MAPE) | Python, pandas, statsmodels | Weeks 15–17 | ⬜ |
| 10 | **Real-Time Adherence Alert Bot**: script that reads a (synthetic) agent-state feed and flags adherence/SLA breaches | Python automation | Weeks 20–21 | ⬜ |
| 11 | **Creator Analytics Dashboard**: YouTube + Instagram exports combined with the Task 5 tracker | Python / Power BI | Weeks 22–23 | ⬜ |

**Where each project fits in the MBA rebuild:** Task 6 → M7 (SQL) · Task 7 → M15 (Power BI) · Task 8 → M10/M20 (starter: `mba-ai-ds/labs/python/08_optimisation_staffing.py`) · Task 9 → M19 (starter: `labs/python/07_time_series_forecast.py`) · Task 10 → M20–M21 · Task 11 → M22 · **Capstone → M28**.

## Suggested folder layout as the repo grows
```
Project-Hammad/
├── Task1..Task4 *.sql          # SQL capstone (done)
├── Task5_Side_Hustle_Tracker.sql
├── task6_contact_centre/       # schema.sql, data.sql, kpi_queries.sql
├── task7_powerbi_dashboard/    # .pbix + screenshots
├── task8_erlang_c/             # erlang_c.py, erlang_c.xlsx, README.md
├── ...
├── screenshots/
└── growth-plan/                # this roadmap
```

## Definition of done (for every project)
1. Runs from scratch using only files in the repo.
2. README section: problem, dataset, what it shows, screenshots.
3. Commit messages that explain *why*, not just *what*.
4. A 1-paragraph LinkedIn post + a video about it.
