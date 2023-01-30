import pandas as pd
ra = pd.read_csv(r"H:\automation_scripts\pandasss\data.csv",nrows=3)
ra1 = pd.read_csv(r"H:\automation_scripts\pandasss\data.csv",usecols=[0])
raj=pd.read_csv(r"H:\automation_scripts\pandasss/data.csv",index=False)
raj=pd.read_csv(r"H:\automation_scripts\pandasss/data.csv",skiprows=1)
raj=pd.read_csv(r"H:\automation_scripts\pandasss/data.csv",index_col='name of col.')
raj=pd.read_csv(r"H:\automation_scripts\pandasss/data.csv",header=3)
raj=pd.read_csv(r"H:\automation_scripts\pandasss/data.csv",header=None,prefix='col')
raj=pd.read_csv(r"H:\automation_scripts\pandasss/data.csv",names='col')
raj=pd.read_csv(r"H:\automation_scripts\pandasss/data.csv",dtype={'name of column you want to change type':'type you want to give'})

print(ra)
print(ra1)
print(raj)