import numpy as np
import pandas as pd
df=pd.DataFrame({
    'A' : [1,2,3,4,5],
    'B' : [10,20,30,40,50],
    'C':[100,200,300,400,500]
})
print(df)
# df=df.shape
# print(df)
# df=df.columns
# print(df)
# df=df.info()
# print(df)
# df=df.describe()
# print(df)
def square(x):
    return x**2
df['D']=df['B'].apply(square) #ek col. D bn gya usme B col. k square hogya
print(df)