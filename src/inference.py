"""
author: Robin Shindelman
date: 2025-05-24

A 2-sample proportion test for a statistically significant difference between
customers who had DSL vs Fiber Optic and whether or not they churned.
"""

import pandas as pd
import statsmodels.api as sm

fp = '/Users/robinshindelman/school/Spring 25/CS406/churn-analysis-406/data/queries-eda/services.csv'
df = pd.read_csv(fp, usecols=['Customer Status', 'Monthly Charge', 'Internet Type'])

# Drop Cable
df = df[df['Internet Type'] != 'Cable']

# print(df[(df['Internet Type'] == 'DSL') & (df['Customer Status'] == 'Churned')].count())
# print(df[(df['Internet Type'] == 'Fiber Optic') & (df['Customer Status'] == 'Churned')].count())

CHURN_DSL = 307
CHURN_FO = 1236
TOTAL_DSL = 1652
TOTAL_FO = 3035

successes = [CHURN_FO, CHURN_DSL]
totals = [TOTAL_FO, TOTAL_DSL]

z, p = sm.stats.proportions_ztest(successes, totals, alternative='larger')
print(f"Z = {z:.3f}\np value = {p:.6f}")
