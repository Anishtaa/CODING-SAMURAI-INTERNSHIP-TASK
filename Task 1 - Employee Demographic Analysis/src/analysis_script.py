import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/hr_employee_data.csv')

# Department distribution
dept_counts = df['Department'].value_counts()
print(dept_counts)

# Gender split
df['Sex'].value_counts().plot(kind='pie', title='Gender Distribution')
plt.tight_layout()
plt.show()

# Age histogram
df['Age'].plot(kind='hist', bins=10, title='Age Distribution')
plt.tight_layout()
plt.show()

# Average salary by department
print(df.groupby('Department')['Salary'].mean().round(2))
