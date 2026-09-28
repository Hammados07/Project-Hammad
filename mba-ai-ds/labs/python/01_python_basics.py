# %% [markdown]
# # Lab 01 · Python from Zero (Module M6)
# 🧒 Python is a very obedient robot. It does exactly what you type, top to bottom.
# Run one "# %%" block at a time (VS Code: "Run Cell"; Colab: paste each block into a cell).
# After each block: CHANGE a number and predict the new output before you run it again.

# %% 1. Variables = labelled boxes
calls_offered = 120          # an int (whole number)
aht_minutes = 5.5            # a float (decimal)
queue_name = "Billing"       # a string (text)
is_peak_hour = True          # a boolean (True/False)

workload_minutes = calls_offered * aht_minutes
print("Queue:", queue_name)
print("Total workload (minutes):", workload_minutes)
print(f"That's {workload_minutes / 60:.1f} agent-hours")   # f-string: text with values inside

# %% 2. Lists = a shelf of items in order
calls_per_hour = [80, 120, 150, 110, 90]
print("First hour:", calls_per_hour[0])      # Python counts from 0!
print("Last hour:", calls_per_hour[-1])
print("Total calls:", sum(calls_per_hour))
print("Busiest hour:", max(calls_per_hour))
calls_per_hour.append(70)                    # add one more item
print("Now:", calls_per_hour, "->", len(calls_per_hour), "hours")

# %% 3. Dictionaries = a phone book (key -> value)
agent = {"name": "Asha", "team": "Billing", "calls_handled": 64, "aht_sec": 312}
print(agent["name"], "handled", agent["calls_handled"], "calls")
agent["aht_sec"] = 298                       # update a value
agent["tenure_months"] = 14                  # add a new key
print(agent)

# %% 4. Conditions = decisions
sla = 76
if sla >= 80:
    status = "Green"
elif sla >= 70:
    status = "Amber"
else:
    status = "Red"
print(f"SLA {sla}% is {status}")

# %% 5. Loops = repeat for each item
sla_by_interval = {"09:00": 91, "09:30": 84, "10:00": 72, "10:30": 65, "11:00": 88}
for interval, value in sla_by_interval.items():
    flag = "⚠️ below target" if value < 80 else "ok"
    print(interval, value, flag)

# %% 6. Functions = a reusable recipe (input -> steps -> output)
def sla_status(sla_pct, target=80):
    """Return a RAG colour for an SLA percentage."""
    if sla_pct >= target:
        return "Green"
    if sla_pct >= target - 10:
        return "Amber"
    return "Red"


def erlangs(calls_per_hour, aht_seconds):
    """Traffic intensity: how many agents' worth of work is arriving (Module M10)."""
    return calls_per_hour * aht_seconds / 3600


print([sla_status(v) for v in sla_by_interval.values()])   # a "list comprehension": a loop in one line
print("Traffic:", erlangs(120, 300), "Erlangs")             # 120 calls × 300 s = 10 agents' work

# %% 7. Errors are friends. Read the LAST line first.
try:
    print(calls_per_hour[10])        # there is no item number 10
except IndexError as e:
    print("Python says:", e)         # "list index out of range" = you asked for something that doesn't exist

# %% 8. Your turn (challenges)
# a) Make a list of 7 daily call volumes and print the average (hint: sum(...) / len(...)).
# b) Write a function occupancy(erlangs, agents) that returns erlangs / agents as a %.
# c) Loop over 3 agents (a list of dictionaries) and print who has the lowest AHT.
