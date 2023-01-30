import pandas as pd
var=pd.DataFrame({'a':pd.Series([1,2,3,4,5]),'b':pd.Series([6,4,8,9,2]),'c':pd.Series([1,2,3,4,5]),'d':pd.Series([6,4,8,9,2])})
print(var)
raj=var.to_csv(r"H:\automation_scripts\pandasss/raj1.csv",index=False)
raj=var.to_csv(r"H:\automation_scripts\pandasss/raj2.csv")
raj=var.to_csv(r"H:\automation_scripts\pandasss/raj3.csv",index=False,header=[1,2,3,4])
print('done')