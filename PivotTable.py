import numpy as np
import pandas as pd
data={
    'Date':pd.date_range('2025-11-01',periods=20),
    'Product':['A','B','C','D']*5,
    'Region':['East','West','North','South','East','West','North','South',
    'East','West','North','South','East','West','North','South','East','West','North','South'],
    'Sales':np.random.randint(100,1000,20),
    'Units':np.random.randint(10,100,20),
    'Rep':['John','Marie','Bob','Alice','John','Marie','Bob','Alice','John'
    ,'Marie','Bob','Alice','John','Marie','Bob','Alice','John','Marie','Bob','Alice']
}

df=pd.DataFrame(data)
# print(df)
# df['Month']=df['Date'].dt.month_name()
# print(df)
# df=pd.pivot_table(df,values='Sales',index='Region',columns='Product') #isme default mean select rehta h hm change bhi kr skte h
# print(df)

# Cross Tab
df=pd.crosstab(df['Region'],df['Product']) #yeh btata h ki itne counts h
print(df)