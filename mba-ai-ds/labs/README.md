# 🛠️ Labs: How to Run Them

All data is **synthetic** (made up with a fixed random seed), so it's safe to use in YouTube videos.

## Option A: Google Colab (no install, recommended to start)
In a new Colab notebook cell:
```
!git clone -b claude/dreamy-curie-sn7l15 https://github.com/Hammados07/Project-Hammad
%cd Project-Hammad/mba-ai-ds/labs/python
%run 01_python_basics.py
```
(Once merged into `main`, drop `-b claude/dreamy-curie-sn7l15`. If the repo is private, upload the `labs` folder to Colab instead, using the 📁 icon on the left.)
Better for learning: copy **one `# %%` block at a time** into its own cell and run it, so you see each step.

## Option B: Your laptop (VS Code)
```
pip install pandas numpy matplotlib scikit-learn statsmodels scipy
cd mba-ai-ds/labs/python
python 02_pandas_eda.py
```
In VS Code, each `# %%` line becomes a **"Run Cell"** button (install the Python + Jupyter extensions).

## R lab
Open `r/01_r_basics_regression.R` in RStudio or Posit Cloud, set the working directory to this `labs` folder, and run line by line (Ctrl+Enter).

## SQL lab
In pgAdmin: create a database `sql_lab`, open `sql/01_sql_business_patterns.sql` in the Query Tool and run it.

## Datasets (`data/`)
| File | Rows | Used in |
|---|---|---|
| `call_centre_intervals.csv` | 3,136 | 30-min interval stats for 2 queues × 8 weeks (Labs 02, 03, 04, R) |
| `daily_calls.csv` | 731 | 2 years of daily call volume (Lab 07) |
| `customers.csv` | 2,000 | Customers with RFM fields + churn label (Labs 04, 05, 06, R) |
| `aht_experiment.csv` | 240 | A/B test of a call script, team AHT, complaints by region (Lab 03) |
| `reviews.csv` | 600 | Short customer reviews with sentiment (Labs 09, 11) |

Re-create them any time with `python data/make_datasets.py`.
Charts are saved to `labs/output/` (not committed to git).

## The golden rule
After running a block, **change one thing** (a number, a column, a threshold), **predict** what will happen, then run it again. That's where the learning happens.
