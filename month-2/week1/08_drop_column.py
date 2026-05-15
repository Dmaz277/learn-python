import pandas as pd
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

drop = df.drop(columns=['category'])
print(drop)