
import pandas as pd

data = {
    'City': ['Chennai', 'Chennai', 'Mumbai', 'Mumbai', 'Delhi', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Date': ['2024-04-05', '2024-04-15', '2024-04-22', '2024-05-05', '2024-05-18',
             '2024-06-01', '2024-06-10', '2024-06-15', '2024-06-20'],
    'Temperature': [35, 36, 33, 34, 38, 37, 36, 35, 39]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%B')

monthly_sum = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()
pivot_table = monthly_sum.pivot(index='City', columns='Month', values='Temperature').fillna(0)

summer_months = ['April', 'May', 'June']
pivot_table['Summer_Total'] = pivot_table[summer_months].sum(axis=1)
hottest_city = pivot_table['Summer_Total'].idxmax()

print(pivot_table)
print("City with highest summer temperature:", hottest_city)
