import pandas as pd
import matplotlib.pyplot as plt

# read csv
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# axes for x and y
x = df['name_product']
y = df['price']

#make pie chat
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.show()