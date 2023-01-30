import pandas as pd
var=pd.DataFrame({'a':pd.Series([1,2,3,4]),'b':pd.Series([5,6,7,8])})
var['c']=var['a']+var['b']
var['d']=var['a']-var['b']
var['e']=var['a']*var['b']
var['f']=var['a']/var['b']
var['g']=var['a']%var['b']
print(var)