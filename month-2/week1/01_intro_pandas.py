import pandas as pd

data = {
    'nama': ['dimz','ayu','minu'],
    'usia': [12,30,13],
    'kota': ['jambi','jakarta','bandung']
}
df = pd.DataFrame(data)
print(df)