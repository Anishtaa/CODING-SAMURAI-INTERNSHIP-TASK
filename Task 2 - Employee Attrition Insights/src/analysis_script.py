import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/hr_employee_data.csv')
total = len(df)
attrition_yes = df['Attrition'].value_counts().get('Yes',0)
attrition_rate = (attrition_yes/total)*100 if total else 0
avg_age_leavers = df[df['Attrition']=='Yes']['Age'].dropna().mean()

dept_attr = df[df['Attrition']=='Yes']['Department'].value_counts()
dept_attr.plot(kind='bar')
plt.tight_layout()
plt.savefig('../docs/attrition_by_department.png')
