"""
author: Robin Shindelman
date: 2025-05-09

Script for mining information from the Telco IBM dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_dems_fp = "/Users/robinshindelman/school/Spring 25/CS406/churn-analysis-406/data/queries-eda/dems-loc-all-cust.csv"
df_services = "/Users/robinshindelman/school/Spring 25/CS406/churn-analysis-406/data/queries-eda/services.csv"
df_dems = pd.read_csv(df_dems_fp)
df_services = pd.read_csv(df_services)

df_dems["Zip Code"] = df_dems["Zip Code"].astype('object')

plt.figure(figsize=(8,5))
sns.violinplot(data=df_dems, x='Customer Status', y='Age', hue='Gender')
plt.title("Customer Status by Age & Gender")
plt.legend(frameon=False, bbox_to_anchor=(1, 0.5))
plt.show()

plt.figure(figsize=(5,10))
sns.histplot(data=df_services, x='Monthly Charge', hue='Customer Status')
plt.title("Monthly Charges & Churn Counts")
plt.show()

plt.figure(figsize=(5,5))
df_services_churned = df_services[df_services['Customer Status']== "Churned"]
sns.scatterplot(data=df_services_churned, x='Monthly Charge', y='Tenure in Months', hue='Internet Type')
plt.title('Churned Customers by Monthly Bill, Tenure, and Internet Type')
plt.show()