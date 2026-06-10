import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("d:/Salary-Analysis/ds_salaries.csv")

# ---- CHART 1: Average Salary by Experience Level ----
exp_labels = {'EN': 'Entry', 'MI': 'Mid', 'SE': 'Senior', 'EX': 'Executive'}
df['experience_label'] = df['experience_level'].map(exp_labels)

exp_salary = df.groupby('experience_label')['salary_in_usd'].mean().reindex(['Entry', 'Mid', 'Senior', 'Executive'])

plt.figure(figsize=(8, 5))
plt.bar(exp_salary.index, exp_salary.values, color='steelblue')
plt.title('Average Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary (USD)')
plt.tight_layout()
plt.savefig('d:/Salary-Analysis/chart1_experience.png')
plt.show()

# ---- CHART 2: Top 10 Highest Paying Job Titles ----
top_jobs = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_jobs.index[::-1], top_jobs.values[::-1], color='steelblue')
plt.title('Top 10 Highest Paying Data Science Jobs')
plt.xlabel('Average Salary (USD)')
plt.tight_layout()
plt.savefig('d:/Salary-Analysis/chart2_top_jobs.png')
plt.show()

# ---- CHART 3: Salary Growth Over Time ----
yearly_salary = df.groupby('work_year')['salary_in_usd'].median()

plt.figure(figsize=(8, 5))
plt.plot(yearly_salary.index, yearly_salary.values, marker='o', color='steelblue')
plt.title('Median Data Science Salary Over Time')
plt.xlabel('Year')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.savefig('d:/Salary-Analysis/chart3_salary_trend.png')
plt.show()

# ---- CHART 4: Remote Work Distribution ----
remote_labels = {0: 'On-site', 50: 'Hybrid', 100: 'Fully Remote'}
df['remote_label'] = df['remote_ratio'].map(remote_labels)
remote_counts = df['remote_label'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(remote_counts.values, labels=remote_counts.index, autopct='%1.1f%%', colors=['steelblue', 'skyblue', 'lightblue'])
plt.title('Remote Work Distribution')
plt.tight_layout()
plt.savefig('d:/Salary-Analysis/chart4_remote.png')
plt.show()

print("All charts saved!")