import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# df.describe display basic statistics (count, mean, min, max, std)
print(df.describe())