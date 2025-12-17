import numpy as np
import pandas as pd
data={'Name':['Aniket','Amol','Harsh','Aman'],
      'Age':[20,18,21,22],
      'City':['Meerut','Delhi','Noida','Gurgaon'],
      'Salary':[60000,25000,50000,40000]}
df=pd.DataFrame(data)
print(df) #print complete data
print(df[["Name","Salary"]]) #print data which we want
df["Designation"]=["Engineer","Doctor","CA","Student"] #adding column
print(df)
df=df.drop('Designation',axis=1) #yha p drop k mtlb h removing col, axis=1 k mtlb h hm column m baat kr rhe h 0 k mtlb h row
print(df)
# df=df.drop('Designation',axis=1,inplace=False) #yha p inplace k mtlb h ki Designation hmesha k lye delete ho chuka h
# print(df)
df.loc[4]=["Nagar",23,"Nainital",45000] #Adding row using loc(location)
print(df)
# df=df.loc[[0,1]][['Name','Salary']] #when u want to find the particular data from row as well as col.
# print(df)
# df=df.loc[[2,3]][['Name','Age']]
# print(df)
df=df[df["Age"]>20] #voi print honge jinki age 20 s jyada h
print(df)
df=df[(df['Age']>20)&(df['City']=='Noida')] #age>20 and city noida ho voh select krke dedo
print(df)