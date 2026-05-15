import pandas as pd
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
result = df['total_value'] = df['price'] * df['stock']
print(df)