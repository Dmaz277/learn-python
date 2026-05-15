import pandas as pd
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# df.groupby is bult in function in pandas library same like df.sort_value
group = df.groupby('category')['stock'].sum()

print(group)
