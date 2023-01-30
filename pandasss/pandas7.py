import pandas as pd
import numpy as np
ra = pd.read_csv(r"H:\automation_scripts\pandasss\data.csv")
#to get the index of csv file
print(ra.index)
#to get the column of csv file
print(ra.columns)
#to describe of csv file
print(ra.describe)
#to get the first 5 elements of csv file you can also give any number in head
print(ra.head())
#to get the last 5 elements of csv file you can also give any number in tail
print(ra.tail())
#to get any row just use slicing you can also give any number 
print(ra[4:])
#to convert csv into array use filename.index.array
print(type(ra.index.array))
#to convert it into numpy array
print(ra.to_numpy)
aa=np.asarray(ra)
#to do sorting
ra.sort_index(axis=0,ascending=False)
#to change the columns to another data
ra.loc[0,"name of column"]="data what you want to enter"
ra.dropna(how='any')