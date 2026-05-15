# ==================================
# File: 10_mini_project_analysis.py
# Author: Dimaz
# Month: 2
# Week: 1
# ==================================
import pandas as pd

# read data from csv
data = pd.read_csv('data.csv')

# Display all product from data
def show_all():
    print(data)

# Filter and display products with stock above
def filter_stock():
    result = data[data['stock']> 20]
    print(result)

# Display basic statistics (count,mean,min,max)
def basic_statistic():
    print(data.describe())

# Add total_value column (price x stock) and display the result
def add_column():
    result = data['total_value'] = data['price'] * data['stock']
    print(result)

show_all()
filter_stock()
basic_statistic()
add_column()

