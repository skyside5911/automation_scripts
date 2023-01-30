import pandas as pd
l=[1,2,3,4,5,6]
var = pd.DataFrame(l)
b={"a":[1,2,3,4,5],"b":[6,7,8,9,0]}
print(var)
var1=pd.DataFrame(b)
var2=pd.DataFrame(b,columns=['a'])
print(var1)
print(var2)
#get specific value
print(var1['a'][3])