import numpy as np
import pandas as pd
data={'A':[1,2,np.nan,4,5],
      'B':[np.nan,2,3,4,5],
      'C':[1,2,3,np.nan,np.nan],
      'D':[1,np.nan,np.nan,np.nan,5]}   #yha p nan k mtlb hota h null value 
df=pd.DataFrame(data)
print(df)
# df=df.isna() #isna bta deta h ki null value h ya na
# print(df)
# df=df.isna().sum() #isne bta diya ki 1 row m kitni null value h
# print(df)
# df=df.dropna() #jis bhi row m null values hongi voh remove hojayegi
# print(df)
# df=df.dropna(thresh=3) #thresh k mtlb h ki atleast 3 non-null value honi chayie 
# print(df)
df=df.fillna(0)
print(df)
