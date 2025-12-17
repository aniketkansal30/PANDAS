import numpy as np
import pandas as pd
# Employees=pd.DataFrame({
#     'Employee_ID':[1,2,3,4,5],
#     'Name':['Aniket','Amol','Aman','Harsh','Viraj'],
#     'Department':['HR','IT','Finance','CA','Engineer']
# })
# Salaries=pd.DataFrame({
#     'Employee_ID':[1,2,3,4,5],
#     'Salary':[50000,60000,70000,30000,40000],
#     'Bonus':[5000,6000,7000,3000,4000]
# })
# df=pd.merge(Employees,Salaries)
# print(df)
Employees=pd.DataFrame({
    'Employee_ID':[1,2,3,4,5],
    'Name':['Aniket','Amol','Aman','Harsh','Viraj'],
    'Department':['HR','IT','Finance','CA','Engineer']
})
Salaries=pd.DataFrame({
    'Employee_ID':[1,2,3,6,7],
    'Salary':[50000,60000,70000,30000,40000],
    'Bonus':[5000,6000,7000,3000,4000]
})
# df=pd.merge(Employees,Salaries,on='Employee_ID',how='outer') #on btata h common value s data merge hoga and how btata h ki saara data merge krdo agr value nhi h toh null value(NaN) assign hojayegi
# print(df)
# df=pd.concat([Employees,Salaries],axis=1) #concatenation
# print(df)
df1 = pd.DataFrame({'Name':['Aniket','Amol','Aman']}, index=[1,2,3])
df2 = pd.DataFrame({'City':['Meerut','Delhi','Noida']}, index=[1,2,4])

result = df1.join(df2, how='inner') #join
print(result)
