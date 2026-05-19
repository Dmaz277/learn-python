# import pandas library only for read
import pandas as pd

# read excel 
data1 = pd.read_excel('data.xlsx')
data2 = pd.read_excel('data2.xlsx')

# save to list with data as variable
data = [data1,data2]

# merged the data and export to excel with name merged.xlsx',index=False, index= False that it will start index 0
merged = pd.concat(data)
merged.to_excel('merged.xlsx',index=False)


