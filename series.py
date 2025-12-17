import numpy as np
import pandas as pd
labels=['a','b','c']
my_list=[10,20,30]
arr=np.array([10,20,30])
d={1:10,2:20,3:30}
print(pd.Series(my_list))
print(pd.Series(arr))
print(pd.Series(d))
print(pd.Series(my_list,index=labels))