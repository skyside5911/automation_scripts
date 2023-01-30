import pandas as pd
a=[1,2,3,4,5,6]
b=pd.Series(a)
print(b)
c=pd.Series(a,index=['a','b','c','d','e','f'],dtype='float',name='python')
print(c)