# %% [markdown]
# # Lab 12 · Finance toolkit: ratios, NPV, IRR, EMI, SIP (Modules M2, M9)
# 🧒 ₹100 today is worth more than ₹100 next year, so we shrink future money back to today before comparing.

# %% Setup
from scipy.optimize import brentq

# %% PART 1 (M2): ratios from a made-up company's statements (₹ crore)
pnl = {"revenue": 1200, "cogs": 720, "opex": 250, "depreciation": 40, "interest": 30, "tax": 40}
bs = {"current_assets": 500, "current_liabilities": 320, "total_debt": 400, "equity": 800}
gross_profit = pnl["revenue"] - pnl["cogs"]
ebitda = gross_profit - pnl["opex"]
ebit = ebitda - pnl["depreciation"]
net_profit = ebit - pnl["interest"] - pnl["tax"]
print(f"Gross margin  {gross_profit / pnl['revenue']:.1%}")
print(f"EBITDA margin {ebitda / pnl['revenue']:.1%}")
print(f"Net margin    {net_profit / pnl['revenue']:.1%}")
print(f"ROE           {net_profit / bs['equity']:.1%}")
print(f"Current ratio {bs['current_assets'] / bs['current_liabilities']:.2f}  (>1 = can pay short-term bills)")
print(f"Debt/Equity   {bs['total_debt'] / bs['equity']:.2f}")

# %% Break-even (M2)
fixed, price, var = 50_000, 200, 120
print(f"Break-even: {fixed / (price - var):.0f} units")

# %% PART 2 (M9): NPV and IRR
def npv(rate, cashflows):
    """cashflows[0] is today (usually negative = investment)."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows):
    return brentq(lambda r: npv(r, cashflows), -0.99, 10)


project = [-100_000, 30_000, 30_000, 30_000, 30_000, 30_000]
print(f"NPV @10% = ₹{npv(0.10, project):,.0f}  → {'ACCEPT' if npv(0.10, project) > 0 else 'REJECT'}")
print(f"IRR      = {irr(project):.1%}  (accept if above the cost of capital)")

# %% Loan EMI
def emi(principal, annual_rate, years):
    r, n = annual_rate / 12, years * 12
    return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)


e = emi(500_000, 0.105, 3)
print(f"EMI on ₹5,00,000 at 10.5% for 3 years = ₹{e:,.0f}/month; total interest ₹{e * 36 - 500_000:,.0f}")

# %% SIP future value (monthly investment, contributions at the start of each month)
def sip_fv(monthly, annual_return, years):
    r, n = annual_return / 12, years * 12
    return monthly * ((1 + r) ** n - 1) / r * (1 + r)


for yrs in (5, 10, 20):
    fv = sip_fv(5_000, 0.12, yrs)
    print(f"₹5,000/month for {yrs:2d} yrs @12% ≈ ₹{fv:,.0f} (you put in ₹{5_000 * 12 * yrs:,})")
print("⚠️ 12% is an assumption for illustration, not a promise. Equity returns vary a lot year to year.")

# %% Your turn
# a) At what discount rate does the project's NPV become 0? (That's the IRR. Check it!)
# b) Compare: ₹5,000/month for 20 years vs ₹10,000/month for 10 years. Which ends higher? Why?
