import numpy as np
import pandas as pd
data={
    'Category':['A','B','A','B','A','B','A','B'],
    'Store':['S1','S1','S2','S2','S1','S2','S2','S1'],
    'Sales':[100,200,150,250,120,180,200,300],
    'Quantity':[10,15,12,18,8,20,15,25],
    'Date':pd.date_range(start='2025-11-01',periods=8)
}
df=pd.DataFrame(data)
print(df)
# cat=df.groupby('Category') #data grouped hogyaa
# for i, v in cat:
#     print(i)
#     print(v)
# df=df.groupby('Category')['Sales'].sum()
# print(df)
# df=df.groupby('Store')['Sales'].sum()
# print(df)
# df=df.groupby(['Category','Store'])['Sales'].sum()
# print(df)

# AGGREGATION
mean_val = df['Sales'].mean()
print("Mean:", mean_val)

median_val = df['Sales'].median()
print("Median:", median_val)

mode_val = df['Sales'].mode()[0]
print("Mode:", mode_val)

count_val = df['Sales'].count()
print("Count:", count_val)

std_val = df['Sales'].std()
print("Standard Deviation:", std_val)

min_val = df['Sales'].min()
print("Minimum:", min_val)

max_val = df['Sales'].max()
print("Maximum:", max_val)

# 1 line m .agg likhke saare operations hoskte h 
df=df['Sales'].agg(['sum','mean','median','count','min','max','std'])
print(df)