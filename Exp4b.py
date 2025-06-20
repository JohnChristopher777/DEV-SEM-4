import pandas as pd

data2 = {
    'Employee': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'Work_Hours': [40, 45, 38, 42, 48, 50]
}

df2 = pd.DataFrame(data2)

grouped = df2.groupby('Department')['Work_Hours'].agg(['sum', 'mean']).reset_index()
pivot_report = pd.pivot_table(df2, index='Department', values='Work_Hours', aggfunc=['sum', 'mean'])

highest_avg = pivot_report[('mean', 'Work_Hours')].idxmax()

print(pivot_report)
print("Department with highest average hours:", highest_avg)
