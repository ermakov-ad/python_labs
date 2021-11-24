import pandas as pd

path = "transactions.csv"

data = pd.read_csv(path, sep=',')

print('The biggest transactions:')
print(data[data['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False).head(3)[['CONTRACTOR', 'SUM']])

print('Sum of transactions to "Umbrella, Inc":')
data_sum = data[data['STATUS'] == 'OK'].groupby('CONTRACTOR').sum()
print(data_sum.loc['Umbrella, Inc', 'SUM'])
