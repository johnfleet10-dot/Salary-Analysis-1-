import pandas as pd

df = pd.read_csv("d:/Salary-Analysis/ds_salaries.csv")
print(df.columns.tolist())
print(df.head())