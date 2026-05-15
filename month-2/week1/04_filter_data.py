import pandas as pd
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
result = df[df['stok']> 20]
print(result)


