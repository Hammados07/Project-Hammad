# %% [markdown]
# # Lab 07 · Forecasting daily call volume (Module M19)
# 🧒 Guess tomorrow's weather from the pattern of past days. Rule #1: if you can't beat "naive", go home.

# %% Setup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose

from _paths import DATA, OUTPUT

s = pd.read_csv(DATA / "daily_calls.csv", parse_dates=["date"]).set_index("date")["calls"].asfreq("D")

# %% 1. Look at Trend, Seasonality, Noise
parts = seasonal_decompose(s, model="multiplicative", period=7)
print("Weekly pattern (multiplier by weekday):")
print(parts.seasonal.groupby(parts.seasonal.index.day_name()).mean().round(2).sort_values(ascending=False))

# %% 2. Train/test split BY TIME (never shuffle time series!)
horizon = 56                                   # forecast the last 8 weeks
train, test = s[:-horizon], s[-horizon:]


def mape(actual, forecast):
    return float(np.mean(np.abs((actual - forecast) / actual)) * 100)


forecasts = {}
# a) Naive: tomorrow = today (the last value, repeated)
forecasts["Naive"] = pd.Series(train.iloc[-1], index=test.index)
# b) Seasonal naive: next Monday = last Monday
forecasts["Seasonal naive"] = pd.Series(np.tile(train.iloc[-7:].values, horizon // 7), index=test.index)
# c) 28-day moving average × weekday pattern
weekday_factor = (train / train.rolling(7, center=True).mean()).groupby(train.index.dayofweek).mean()
level = train.iloc[-28:].mean()
forecasts["Moving avg × weekday"] = pd.Series(level * weekday_factor.loc[test.index.dayofweek].values, index=test.index)
# d) Holt-Winters: level + trend + weekly seasonality
hw = ExponentialSmoothing(train, trend="add", seasonal="mul", seasonal_periods=7).fit()
forecasts["Holt-Winters"] = hw.forecast(horizon)

# %% 3. Compare accuracy
scores = pd.Series({name: mape(test, f) for name, f in forecasts.items()}).sort_values()
print("MAPE (lower is better):\n", scores.round(2))
print(f"👉 Best: {scores.index[0]}. Every forecast must beat Seasonal naive ({scores['Seasonal naive']:.1f}%) to be worth it.")
print("👉 Note the holiday in the test window (25 Dec): that one day adds a big chunk of the error. "
      "Real WFM teams add holiday adjustments.")

# %% 4. Plot
ax = s[-150:].plot(figsize=(12, 4), label="Actual", color="black")
for name in ["Seasonal naive", "Holt-Winters"]:
    forecasts[name].plot(ax=ax, label=name)
ax.legend(); ax.set_title("Daily calls: last 150 days and 8-week forecasts")
plt.tight_layout(); plt.savefig(OUTPUT / "lab07_forecast.png", dpi=120); plt.show()

# %% 5. From daily to interval forecast (how WFM actually does it)
tomorrow = hw.forecast(horizon + 1).iloc[-1]
profile = pd.Series([4, 7, 10, 11, 10, 8, 7, 8, 8, 7, 7, 6, 4, 3], index=[f"{h}:00" for h in range(8, 22)])
profile = profile / profile.sum()
print(f"Forecast for the next day: {tomorrow:.0f} calls → by hour:")
print((profile * tomorrow).round().astype(int))

# %% Your turn
# a) Change horizon to 28. Which method wins now?
# b) Try seasonal="add" in Holt-Winters. Better or worse?
# c) Add a holiday rule: multiply the forecast by 0.5 on known holidays. Recompute MAPE.
