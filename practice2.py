import pandas as pd

df = pd.read_csv('sales.csv')
print(df)
print(df['sales'])
print(df[df['sales'] >= 1000])
print(df['sales'].mean())
print(df.groupby('category')['sales'].sum())