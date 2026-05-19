import pandas as pd
# library for make graphic bar from data csv
import matplotlib.pyplot as plt

# read csv
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# axes for x and y
x = df['name_product']
y = df['price']

# make line chart
plt.plot(x,y)
plt.show()
