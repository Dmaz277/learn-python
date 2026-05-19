import pandas as pd 
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
df.to_excel('data.xlsx',index=False)