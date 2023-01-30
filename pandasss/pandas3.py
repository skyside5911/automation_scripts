import pandas as pd
var = pd.DataFrame({'a':[1,2,3,4],'b':[6,7,8,9]})
print(var)
var['c']=var['a']+var['b']
print(var['c'])
print(var)
var['python']=var['a']<3
print(var)