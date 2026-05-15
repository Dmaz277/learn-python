import pandas as pd
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# this is sort from big to small
df_sort = df.sort_values(by='price')

# this is sort from small to big
df_desc = df.sort_values(by='price', ascending=False) 

print(df_sort)
print(df_desc)